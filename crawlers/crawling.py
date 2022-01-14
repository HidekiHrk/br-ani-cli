import config

from bs4 import BeautifulSoup

from utils import get_page, parse_search_query


def search_anime(name: str):
    search_query = parse_search_query(name)
    page_response = get_page(
        f'{config.BASE_URL}/{config.SEARCH_URI}/{search_query}')
    html_page = str(page_response.text)
    soup = BeautifulSoup(html_page, 'html.parser')

    anime_container = soup.find('div', 'container')
    anime_container_div = anime_container.find(
        'div', 'row ml-1 mr-1') if anime_container is not None else None
    anime_tags = anime_container_div.find_all(
        'div', 'col-6 col-sm-4 col-md-3 col-lg-2 mb-1 minWDanime divCardUltimosEps') if anime_container_div is not None else []

    anime_list = []
    for tag in anime_tags:
        anime_dict = {
            'title': tag.attrs.get('title')
        }
        url_tag = tag.find('a')
        anime_dict['url'] = url_tag.attrs.get('href')
        anime_list.append(anime_dict)

    return anime_list


def get_anime_episodes(anime_page_uri: str):
    page_response = get_page(anime_page_uri)
    html_page = str(page_response.text)
    soup = BeautifulSoup(html_page, 'html.parser')

    video_list = soup.find('div', 'div_video_list')
    episode_tags = video_list.find_all('a') if video_list is not None else []

    episode_list = [{
        'title': tag.text,
        'url': tag.attrs.get('href')
    } for tag in episode_tags]

    return episode_list


def get_anime_episode_video(anime_episode_page_uri: str):
    page_response = get_page(anime_episode_page_uri)
    html_page = str(page_response.content)
    soup = BeautifulSoup(html_page, 'html.parser')

    video_tag = soup.find(
        'video', 'video-js vjs-16-9 vjs-big-play-centered vjs-show-big-play-button-on-pause')

    video_data_url = video_tag.attrs.get(
        'data-video-src') if video_tag is not None else None

    if(video_data_url):
        data_response = get_page(video_data_url)
        data = data_response.json()
        video_quality_list = data.get('data')
        if video_quality_list:
            return [{'quality': video.get('label'), 'url': video.get('src')} for video in video_quality_list]

    return []
