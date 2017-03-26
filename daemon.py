import pyinotify
from PIL import Image
from zheye import util


wm = pyinotify.WatchManager()


class EventHandler(pyinotify.ProcessEvent):
    def process_IN_CREATE(self, event):
        print("Creating: ", event.pathname)
        if event.pathname[-4:] == '.gif':
	        util.Recognizing(event.pathname)

handler = EventHandler()
notifier = pyinotify.Notifier(wm, handler)

wm.add_watch('./statics', pyinotify.IN_CREATE)
notifier.loop()
