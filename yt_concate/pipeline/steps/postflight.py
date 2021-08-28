import logging
import os

from yt_concate.pipeline.steps.step import Step
from yt_concate.setting import CAPTIONS_DIRS
from yt_concate.setting import VIDEOS_DIRS


class Postflight(Step):
    def process(self, data, inputs, utils):
        logger = logging.getLogger('logs')
        if inputs['cleanup']:
            if utils.output_filepath_exist(inputs['channel_id'],inputs['search_word']):
                os.rmdir(CAPTIONS_DIRS)
                os.rmdir(VIDEOS_DIRS)
        logger.debug('in Postflight')
