
import mpv

from crawlers.Anime import Anime


def cli_interface():
    print('BR Anime CLI by HidekiHrk', '',
          '-------------------------', '', sep='\n')
    anime_for_search = None

    while anime_for_search is None or anime_for_search == '':
        anime_for_search = input('Digite o anime que você procura: ')

    anime_list = Anime.search(anime_for_search)
    anime_quantity = len(anime_list)
    print()
    if(anime_quantity == 0):
        print('Não existem animes com esse nome na host.')
        return 0
    print('Animes Encontrados:', *
          map(lambda anime: f"[{anime[0] + 1}]: {anime[1].title}", enumerate(anime_list)), sep="\n  ")
    print()
    selected_anime_index = None
    while selected_anime_index is None or selected_anime_index > anime_quantity - 1 or selected_anime_index < 0:
        anime_index = input(
            'Selecione o anime desejado [padrão = 1]: ')
        if anime_index.isdigit():
            selected_anime_index = int(anime_index) - 1
        elif anime_index.strip() == '':
            selected_anime_index = 0
    selected_anime = anime_list[selected_anime_index]
    episode_list = selected_anime.episodes
    episode_quantity = len(episode_list)
    print()
    if(episode_quantity == 0):
        print('Esse anime ainda não possui episódios.')
        return 0

    print(f'Episódios disponíveis para {selected_anime.title}:', *
          map(lambda episode: f"[{episode[0] + 1}]: {episode[1].title}", enumerate(episode_list)), sep="\n  ")

    selected_episode_index = None
    while selected_episode_index is None or selected_episode_index > episode_quantity - 1 or selected_episode_index < 0:
        episode_index = input(
            f'Selecione o episódio desejado [padrão = 1; máximo = {episode_quantity}]: ')
        if episode_index.isdigit():
            selected_episode_index = int(episode_index) - 1
        elif episode_index.strip() == '':
            selected_episode_index = 0

    selected_episode = episode_list[selected_episode_index]
    quality_list = selected_episode.video_options
    quality_quantity = len(quality_list)
    print()
    if(quality_quantity == 0):
        print('Parece que esse vídeo ainda não foi lançado :/')
        return 0

    print(f'Qualidades de vídeo disponíveis para {selected_episode.title}:', *
          map(lambda quality: f"[{quality[0] + 1}]: {quality[1].name}", enumerate(quality_list)), sep="\n  ")

    selected_episode_quality_index = None
    while selected_episode_quality_index is None or selected_episode_quality_index > quality_quantity - 1 or selected_episode_quality_index < 0:
        episode_quality_index = input(
            f'Selecione a qualidade desejada [padrão = 1]: ')
        if episode_quality_index.isdigit():
            selected_episode_quality_index = int(episode_quality_index) - 1
        elif episode_quality_index.strip() == '':
            selected_episode_quality_index = 0

    selected_video = quality_list[selected_episode_quality_index]

    print(
        '', f'Assistindo episódio {selected_episode.title} do anime {selected_anime.title}.', 'Aproveite!!', sep='\n')

    player = mpv.MPV(input_default_bindings=True,
                     input_vo_keyboard=True, osc=True)

    player.play(selected_video.url)
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
