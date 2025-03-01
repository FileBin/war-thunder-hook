#!/usr/bin/env python3

import asyncio
from mouse_manager import MouseManager

mouse_manager = MouseManager()

asyncio.ensure_future(mouse_manager.update_loop())

loop = asyncio.get_event_loop()
loop.run_forever()
