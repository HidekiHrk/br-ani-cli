
import mpv

from crawlers.Anime import Anime
from utils import prompt_options


def cli_interface():
    print('BR Anime CLI by HidekiHrk', '',
          '-------------------------', '', sep='\n')
    anime_for_search = None

    while anime_for_search is None or anime_for_search == '':
        anime_for_search = input('Digite o anime que você procura: ')

    print()
    anime_list = Anime.search(anime_for_search)
    selected_anime = prompt_options(
        'Animes Encontrados:',
        'Selecione o anime desejado [padrão = 1]: ',
        anime_list, not_exists_message='Não existem animes com esse nome na host.'
    )
    if(selected_anime is None):
        return 0

    print()
    episode_list = selected_anime.episodes
    selected_episode = prompt_options(
        f'Episódios disponíveis para {selected_anime.title}:',
        'Selecione o episódio desejado [padrão = 1; máximo {length}]: ',
        episode_list,
        not_exists_message='Esse anime ainda não possui episódios.'
    )
    if(selected_episode is None):
        return 0

    print()
    quality_list = selected_episode.video_options
    selected_quality = prompt_options(
        f'Qualidades de vídeo disponíveis para {selected_episode.title}:',
        'Selecione a qualidade desejada [padrão = 1]: ',
        quality_list,
        not_exists_message='Parece que esse vídeo ainda não foi lançado :/'
    )
    if(selected_quality is None):
        return 0

    print(
        '', f'Assistindo episódio {selected_episode.title} do anime {selected_anime.title}',
        'Qualidade do vídeo: {selected_quality.title}', 'Aproveite!!', sep='\n')

    player = mpv.MPV(input_default_bindings=True,
                     input_vo_keyboard=True, osc=True)

    player.play(selected_quality.url)
    try:
        player.wait_for_playback()
    except mpv.ShutdownError:
        player.terminate()
        print('Você fechou o vídeo.')
        print()
    return 1


def main():
    prompt = 1
    while prompt == 1:
        prompt = cli_interface()


if __name__ == "__main__":
    main()
