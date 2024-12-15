import asyncio
from src.wake_up_detect import wake_up_detect

if __name__ == "__main__":
    try:
        asyncio.run(wake_up_detect())
    except RuntimeError:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(wake_up_detect())