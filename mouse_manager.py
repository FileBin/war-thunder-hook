from evdev import InputDevice, categorize, ecodes as e
import asyncio
from select import select
from mouse_virtual_gamepad import MouseVirtualGamepad
import subprocess

class MouseManager:
    xinput_id=7
    mouse=InputDevice('/dev/input/event4')
    keyboard=InputDevice('/dev/input/event3')
    virtual_mouse=MouseVirtualGamepad()
    enabled=False

    def __init__(self):
        select([self.mouse, self.keyboard], [], [])
        
    async def keyboard_loop(self):
        async for event in self.keyboard.async_read_loop():
            if event.type == e.EV_KEY:
                key_event = categorize(event)
                match key_event.keycode:
                    case 'KEY_BACKSLASH':
                        if key_event.keystate == 1:
                            await self.switch_state() 
                    case 'KEY_LEFTCTRL':
                        if key_event.keystate == 1:
                            self.virtual_mouse.slow_scroll_speed()
                        elif key_event.keystate == 0:
                            self.virtual_mouse.reset_speed()
    
    async def update_loop(self):
        asyncio.ensure_future(self.keyboard_loop())
        
        async for event in self.mouse.async_read_loop():
            if self.enabled:
                if event.type == e.EV_KEY:
                    key_event = categorize(event)
                    
                    keycode = key_event.keycode
                    if isinstance(keycode, list):
                        keycode = keycode[0]

                    match keycode:
                        case 'BTN_LEFT':
                            await self.virtual_mouse.press_left(key_event.keystate)
                        case 'BTN_RIGHT':
                            await self.virtual_mouse.press_right(key_event.keystate)
                        case 'BTN_MIDDLE':
                            await self.virtual_mouse.press_middle(key_event.keystate)
                        case 'BTN_SIDE':
                            await self.virtual_mouse.press_4th_btn(key_event.keystate)
                        case 'BTN_EXTRA':
                            await self.virtual_mouse.press_5th_btn(key_event.keystate)
    
                elif event.code == 8:
                    await self.virtual_mouse.scroll(event.value)
            
    async def disable_x11_mouse(self):
        subprocess.run(["xinput", "set-button-map", str(self.xinput_id), "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"])

    async def enable_x11_mouse(self):
        subprocess.run(["xinput", "set-button-map", str(self.xinput_id), "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])
        
    async def switch_state(self):
        if self.enabled:
            self.enabled = False
            await self.enable_x11_mouse()
        else:
            self.enabled = True
            await self.disable_x11_mouse()

        self.virtual_mouse.reset()