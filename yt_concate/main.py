import urllib.request
import json

from yt_concate.pipeline.steps.get_video_list import GetVideoList
from yt_concate.pipeline.steps.downloads_captions import DownloadCaptions
from yt_concate.pipeline.pipeline import Pipeline
from yt_concate.utils import Utils
from yt_concate.pipeline.steps.initialize_yt import InitializeYT
CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'


def main():
    inputs = {
        'channel_id': CHANNEL_ID,
        'search_word': 'incredible',
        'limit': 20,
    }


    steps = [
        #Preflight(),
        GetVideoList(),
        InitializeYT(),
        DownloadCaptions(),
        #ReadCaption(),
        #Search(),
        #DownloadVideos(),
        #EditVideo(),
        #Postflight(),
        ]
    utils=Utils()
    p=Pipeline(steps)
    p.run(inputs,utils)


# video_list=get_all_video_in_channel(CHANNEL_ID)
# print(len(video_list))
