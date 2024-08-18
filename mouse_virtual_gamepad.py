import asyncio
from evdev import AbsInfo, InputDevice, UInput, ecodes as e

class MouseVirtualGamepad:
    scroll_value : float = 0
    scroll_speed : float = 1;
    ui: UInput = None
        
    keys = [e.BTN_A, e.BTN_B, e.BTN_X, e.BTN_Y, e.BTN_SELECT]
    
    def __init__(self):
        cap = {      
            e.EV_KEY : self.keys,

            e.EV_ABS : [

                (e.ABS_X, AbsInfo(value=0, min=0, max=1024,
                                fuzz=0, flat=0, resolution=0))]
        }

        self.ui = UInput(cap, name='mouse-remap', version=0x3)
        
    def reset(self):
        self.reset_speed()
        for key in self.keys:
            self.send_key(key, 0)
            
    def slow_scroll_speed(self):
        self.scroll_speed = 10
        
    def reset_speed(self):
        self.scroll_speed = 200
    
    async def press_left(self, state):
        self.send_key(e.BTN_A, state)
    
    async def press_right(self, state):
        self.send_key(e.BTN_B, state)
    
    async def press_middle(self, state):
        self.send_key(e.BTN_SELECT, state)
    
    async def press_4th_btn(self, state):
        self.send_key(e.BTN_X, state)
    
    async def press_5th_btn(self, state):
        self.send_key(e.BTN_Y, state)
    
    async def scroll(self, value):
        self.scroll_value += value * self.scroll_speed
        
        self.scroll_value = max(0, self.scroll_value)
        self.scroll_value = min(1024, self.scroll_value)
        
        self.ui.write(e.EV_ABS, e.ABS_X, int(self.scroll_value))
        self.ui.syn()
        
        print(self.scroll_value)
        
    def send_key(self, key, state):
        self.ui.write(e.EV_KEY, key, state)
        self.ui.syn()
