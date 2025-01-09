import time
import sys
import requests

from loguru import logger
from watchdog.events import FileSystemEvent, FileSystemEventHandler
from watchdog.observers import Observer


# upload sh: https://stackoverflow.com/questions/65102579/send-and-receive-file-using-python-fastapi-and-requests


# def run_deleted(event: FileSystemEvent):
#   logger.debug(event)

# def run_created(event: FileSystemEvent):
#   logger.debug(event)

#   files = {'file_upload': open(event.src_path, 'rb')}
#   headers = {"x-api-key": "123"}

#   res = requests.post(
#       url="http://localhost:8080/file/import",
#       files=files,
#       headers=headers,
#       params={"collection_name": "azure_management"},
#   )
#   logger.info(res.json())


class MyEventHandler(FileSystemEventHandler):
    pot: str = "rag"

    def _run_modified(self, event: FileSystemEvent):
        logger.info(event)

    def _run_deleted(self, event: FileSystemEvent):
        logger.info(event)

    def _run_created(self, event: FileSystemEvent):
        logger.info(f"Starte Import: {event.src_path} -> {self.pot}")

        try:
            files = {"file_upload": open(event.src_path, "rb")}
            headers = {"x-api-key": "123"}

            res = requests.post(
                url="http://localhost:8080/file/import",
                files=files,
                headers=headers,
                params={"collection_name": self.pot},
            )
            logger.info(res.json())
        except Exception as e:
            logger.error(e)

    def on_created(self, event: FileSystemEvent) -> None:
        self._run_created(event)

    def on_deleted(self, event: FileSystemEvent) -> None:
        self._run_deleted(event)

    def on_modified(self, event: FileSystemEvent) -> None:
        self._run_modified(event)


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "."
    logfile_name = sys.argv[2] if len(sys.argv) > 2 else "watch.log"
    pot = sys.argv[3] if len(sys.argv) > 3 else "rag"

    logger.add(
        logfile_name,
        colorize=False,
        enqueue=True,
        level="INFO",
        rotation="1 MB",
    )
    logger.success(
        f"Watchdog started- path: {path}, logfile: {logfile_name}, pot: {pot}"
    )

    event_handler = MyEventHandler()
    event_handler.pot = pot
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    finally:
        observer.stop()
        observer.join()
