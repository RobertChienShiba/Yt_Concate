class YT:
    def __init__(self,url):
        self.url = url
        self.id = YT.get_video_id_from_url(self.url)

    @staticmethod
    def get_video_id_from_url(url):
        return url.split('watch?v=')[-1]


