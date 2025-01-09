import asyncio

# import time
# import sys
# import requests

from loguru import logger
from watchdog.events import FileSystemEvent, FileSystemEventHandler
from watchdog.observers import Observer


class FolderEventHandler(FileSystemEventHandler):

    def _run_created(self, event: FileSystemEvent):
        logger.info(event)

    def _run_modified(self, event: FileSystemEvent):
        logger.info(event)

    def _run_deleted(self, event: FileSystemEvent):
        logger.info(event)

    def _run_moved(self, event: FileSystemEvent):
        logger.info(event)

    def on_created(self, event: FileSystemEvent) -> None:
        self._run_created(event)

    def on_modified(self, event: FileSystemEvent) -> None:
        self._run_modified(event)

    def on_deleted(self, event: FileSystemEvent) -> None:
        self._run_deleted(event)

    def on_moved(self, event: FileSystemEvent) -> None:
        self._run_moved(event)

    # def on_any_event(self, event: FileSystemEvent) -> None:
    #     logger.info("on_any_event:")
    #     logger.info(event)


class WatchFolder:
    def __init__(self, path):
        self.path = path
        self.event_handler = FolderEventHandler()
        self.observer = Observer()
        self.observer.schedule(self.event_handler, path, recursive=True)

    async def start(self):
        self.observer.start()
        logger.info("WatchFolder started")
        # self.observer.join()
        # while True:
        #     await asyncio.sleep(1)
        #     print("Hello")

    def stop(self):
        logger.info("stopping WatchFolder")
        self.observer.stop()
        self.observer.join()
        logger.info("WatchFolder stopped")
