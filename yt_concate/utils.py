import os

from yt_concate.setting import DOWNLOADS_DIRS
from yt_concate.setting import CAPTIONS_DIRS
from yt_concate.setting import VIDEOS_DIRS
class Utils:


    def create_dir(self):
        os.makedirs(DOWNLOADS_DIRS)
        os.makedirs(CAPTIONS_DIRS)
        os.makedirs(VIDEOS_DIRS)