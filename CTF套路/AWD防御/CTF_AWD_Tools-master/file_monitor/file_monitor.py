import sys
import time
from watchdog.observers import Observer
from watchdog.events import *

watch_path = ''
logging_path = ''


def logging_init():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s  %(message)s',
        datefmt='%Y-%m-%d %A %H:%M:%S',
        filename=logging_path,
        filemode='w')
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s  %(message)s')
    console.setFormatter(formatter)
    logging.getLogger().addHandler(console)


class FileEventHandler(FileSystemEventHandler):
    def __init__(self):
        FileSystemEventHandler.__init__(self)

    def on_moved(self, event):
        if event.is_directory:
            logging.info("MOVE : directory {0} to {1}".format(event.src_path, event.dest_path))
        else:
            logging.info("MOVE : file {0} to {1}".format(event.src_path, event.dest_path))

    def on_created(self, event):
        if event.is_directory:
            logging.info("CREAT : directory {0}".format(event.src_path))
        else:
            logging.info("CREAT : file {0}".format(event.src_path))

    def on_deleted(self, event):
        if event.is_directory:
            logging.info("DELETE : directory {0}".format(event.src_path,))
        else:
            logging.info("DELETE : file {0}".format(event.src_path))

    def on_modified(self, event):
        if event.is_directory:
	    pass
            # logging.info("MODIFY : directory {0}".format(event.src_path))
        else:
            logging.info("MODIFY : file {0}".format(event.src_path))

if __name__ == "__main__":
    if watch_path == '' or logging_path == '':
        if len(sys.argv) != 3:
            print("Usage:")
            print("\t python %s [WATCH_PATH] [LOG_PATH]" % (sys.argv[0]))
            exit(1)
        else:
            watch_path = sys.argv[1]
            logging_path = sys.argv[2]
    logging_init()
    observer = Observer()
    event_handler = FileEventHandler()
    observer.schedule(event_handler, watch_path, True)
    observer.start()
    logging.info("Starting monitor...")
    try:
        while True:
            time.sleep(100)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
