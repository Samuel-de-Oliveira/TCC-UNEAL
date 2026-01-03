import json
import os

if os.system() in ('nt', 'dos')
    config_dir: str = 'Comming soon...'
else:
    config_dir: str = '~/.config/UNEAL'

def get_translation(language: str) -> dict:
    with open(f'{config_dir}/lang/{language}.json', 'r+') as file:
        translation: dict = json.load(file)

    return translation
