import sys
import requests
import json


if __name__ == "__main__":

    if len(sys.agrv) < 2:
        print(f'Usage: {sys.agrv[0]} prefix')
        sys.exit()


    prefix = sys.agrv[1]

    print('Download models for prefix: {prefix}')

    response = requests.get('https://data.carnewschina.com/={prefix}')

    if not response.ok:
        print(f'Nastala chyba: {response.status_code}')
        sys.exit()

    data = json.loads(response.text)
    for model in data['models']:
        print(model['name'])
