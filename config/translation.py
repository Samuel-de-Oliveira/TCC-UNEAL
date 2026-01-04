import json
import os

if os.name in ('nt', 'dos'):
    config_dir: str = 'Comming soon...'
else:
    home_dir: str = os.path.expanduser('~')
    config_dir: str = f'{home_dir}/.config/UNEAL'


def get_translation(language: str) -> dict:
    with open(fr'{config_dir}/lang/{language}.json', 'r+') as file:
        translation: dict = json.load(file)

    return translation
