from evdev import InputDevice, categorize, ecodes
from time import sleep
import asyncio
from mouse_manager import MouseManager

mouse_manager = MouseManager()

asyncio.ensure_future(mouse_manager.update_loop())

loop = asyncio.get_event_loop()
loop.run_forever()


# keys = set()
#
# async def human_press(key):
#     if key not in keys:
#         k.press_key(key)
# 
#     keys.add(key)
# 
# 
# 
# async def update_keys():
#     await asyncio.sleep(0.02)
#     for key in keys:
#         k.release_key(key)
# 
#     keys.clear()
#
# async def main():
#     dev = InputDevice('/dev/input/event4') # This can be any other event number. On my Raspi it turned out to be event0
#     while True:
#         await update_keys()
# 
#         select([dev], [], [])
#         for event in dev.read():
#             if event.type == ecodes.EV_KEY:
#                 key_event = categorize(event)
#                 if key_event.keycode == 'BTN_MIDDLE':
#                     await human_press('\\')
# 
# 
#             # The event.code for a scroll wheel event is 8, so I do the following
#             if event.code == 8:
#                 if event.value > 0:
#                     await human_press(k.up_key)
#                 else:
#                     await human_press(k.down_key)
# 
# asyncio.run(main())
