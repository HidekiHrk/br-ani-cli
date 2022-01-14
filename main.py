
from typing import List
import mpv

from crawlers.Anime import Anime
from crawlers.Episode import Episode
from utils import prompt_input, prompt_options


def cli_interface():
    print('BR Anime CLI by HidekiHrk', '',
          '-------------------------', '', sep='\n')

    anime_for_search = prompt_input('Digite o anime que você procura: ')

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
        'Selecione a qualidade desejada [padrão = {length}]: ',
        quality_list,
        not_exists_message='Parece que esse vídeo ainda não foi lançado :/',
        default_option=len(quality_list) - 1
    )
    if(selected_quality is None):
        return 0

    print(
        '', f'Assistindo episódio {selected_episode.title} do anime {selected_anime.title}',
        f'Qualidade do vídeo: {selected_quality.title}', 'Aproveite!!', sep='\n')

    player = mpv.MPV(input_default_bindings=True,
                     input_vo_keyboard=True, osc=True)

    player.play(selected_quality.url)
    try:
        player.wait_for_playback()
    except mpv.ShutdownError:
        print('Você fechou o vídeo.')
        print()

    player.terminate()

    is_reviewing = True
    current_episode = selected_episode
    while is_reviewing:
        episode_pool = [current_episode]
        current_episode_index = episode_list.index(current_episode)

        episode_enum = {
            current_episode: 'Reassistir episódio',
        }

        if(current_episode_index > 0):
            prev_episode = episode_list[current_episode_index - 1]
            episode_pool.insert(0, prev_episode)
            episode_enum[prev_episode] = 'Episódio anterior'
        if(current_episode_index < len(episode_list) - 1):
            next_episode = episode_list[current_episode_index + 1]
            episode_pool.append(next_episode)
            episode_enum[next_episode] = 'Próximo episódio'

        try:

            def option_processor(item_list: List[Episode]):
                return map(lambda item: f"[{item[0] + 1}]: {episode_enum[item[1]]}", enumerate(item_list))

            new_selected_episode = prompt_options(
                f'O que você quer fazer agora? (ctrl + c para voltar ao menu):',
                'Selecione o episódio desejado [padrão = {length}]: ',
                episode_pool,
                custom_options_processor=option_processor,
                default_option=len(episode_pool) - 1
            )

            if(new_selected_episode is None):
                is_reviewing = False
                break

            current_episode = new_selected_episode

            print()
            new_quality_list = new_selected_episode.video_options
            new_selected_quality = prompt_options(
                f'Qualidades de vídeo disponíveis para {new_selected_episode.title}:',
                'Selecione a qualidade desejada [padrão = {length}]: ',
                new_quality_list,
                not_exists_message='Parece que esse vídeo ainda não foi lançado :/',
                default_option=len(new_quality_list) - 1
            )
            if(new_selected_quality is None):
                return 0

            print(
                '', f'Assistindo episódio {new_selected_episode.title} do anime {selected_anime.title}',
                f'Qualidade do vídeo: {new_selected_quality.title}', 'Aproveite!!', sep='\n')

            player = mpv.MPV(input_default_bindings=True,
                             input_vo_keyboard=True, osc=True)
            player.play(new_selected_quality.url)
            try:
                player.wait_for_playback()
            except mpv.ShutdownError:
                print('Você fechou o vídeo.')
                print()
            player.terminate()

        except KeyboardInterrupt:
            is_reviewing = False

    return 1


def main():
    prompt = 1
    while prompt == 1:
        try:
            prompt = cli_interface()
        except KeyboardInterrupt:
            try:
                print('\n')
                response = input(
                    'Você realmente deseja sair? [s/n] (padrão = s): ')
                prompt = 0 if response.strip() == '' or response == 's' else 1
                if prompt == 1:
                    print()
            except KeyboardInterrupt:
                prompt = 0


if __name__ == "__main__":
    main()
