from pytube import YouTube

from yt_concate.pipeline.steps.step import Step
from yt_concate.model.yt import YT


class DownloadCaptions(Step):
    def process(self, data,inputs,utils):
        for yt in data :
            source = YouTube(yt.url)
            en_caption = source.captions.get_by_language_code('a.en')
            en_caption_convert_to_srt = (en_caption.generate_srt_captions())
            print(en_caption_convert_to_srt)
            # save the caption to a file named Output.txt
            text_file = open(f"{yt.id}.txt", "w")
            text_file.write(en_caption_convert_to_srt)
            text_file.close()



