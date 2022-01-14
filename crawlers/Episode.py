from crawlers.crawling import get_anime_episode_video
from crawlers.EpisodeQuality import EpisodeQuality


class Episode:
    def __init__(self, title: str, url: str):
        self.title = title
        self.url = url
        self.__video_options = None

    @property
    def video_options(self):
        if(self.__video_options is None):
            options = get_anime_episode_video(self.url)
            self.__video_options = [EpisodeQuality(title=option.get(
                'quality'), url=option.get('url')) for option in options]
        return self.__video_options
