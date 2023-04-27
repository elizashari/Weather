
import requests


def show_weather(places):
    for place in places:
        payload = {'nqTM': '', 'lang': 'ru'}
        response = requests.get(url, params=payload)
        response.raise_for_status()
        print(response.text)
        

def main():
    places = ['London', 'SVO', 'Череповец']
    show_weather(places)


if __name__ == '__main__':
    main()
