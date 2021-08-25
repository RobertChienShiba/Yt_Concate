from yt_concate.pipeline.steps.get_video_list import GetVideoList
from yt_concate.pipeline.steps.downloads_captions import DownloadCaptions
from yt_concate.pipeline.pipeline import Pipeline
from yt_concate.pipeline.steps.initialize_yt import InitializeYT
from yt_concate.pipeline.steps.prefligjt import Preflight
from yt_concate.pipeline.steps.postflight import Postflight
from yt_concate.pipeline.steps.read_captions import ReadCaption
from yt_concate.pipeline.steps.search import Search
from yt_concate.pipeline.steps.downloads_videos import DownloadVideos
from yt_concate.pipeline.steps.edit_videos import EditVideos
from yt_concate.utils import Utils

CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'


def main():
    inputs = {
        'channel_id': CHANNEL_ID,
        'search_word': 'incredible',
        'limit': 20,
    }

    steps = [
        Preflight(),
        GetVideoList(),
        InitializeYT(),
        DownloadCaptions(),
        ReadCaption(),
        Search(),
        DownloadVideos(),
        EditVideos(),
        Postflight(),
    ]
    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils)


if __name__ == '__main__':
    main()
