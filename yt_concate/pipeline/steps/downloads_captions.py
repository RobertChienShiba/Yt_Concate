from youtube_transcript_api import YouTubeTranscriptApi

from yt_concate.pipeline.steps.step import Step


class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        for yt in data:
            if utils.caption_file_exist(yt):
                print('Caption File Has already downloaded')
                continue
            try:
                srt = YouTubeTranscriptApi.get_transcript(yt.id, languages=['en'])
                # print(srt)
            except:
                print('Error when downloading caption for', yt.url)
                continue
            # save the caption to a file named Output.txt
            with open(yt.caption_filepath, "w", encoding='utf-8') as text_file:
                for caption in srt:
                    text_file.write(f"{caption['start']}-->{caption['start'] + caption['duration']:.2f}\n")
                    text_file.write(f"{caption['text']}\n")

        return data
