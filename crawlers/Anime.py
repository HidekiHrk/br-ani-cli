from typing import List

from crawlers.crawling import get_anime_episodes, search_anime
from crawlers.Episode import Episode


class Anime:
    def __init__(self, title: str, url: str):
        self.title = title
        self.url = url
        self.__episodes: List[Episode] = None

    @property
    def episodes(self):
        if(self.__episodes is None):
            episode_list = get_anime_episodes(self.url)
            new_episode_list = [Episode(title=episode.get(
                'title'), url=episode.get('url')) for episode in episode_list]
            self.__episodes = new_episode_list
        return self.__episodes

    @staticmethod
    def search(anime_title: str):
        anime_list = search_anime(anime_title)
        return [Anime(title=anime.get('title'), url=anime.get('url')) for anime in anime_list]
