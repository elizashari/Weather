
import requests

def is_cyrrylic(symb):
    if u'\u0400' <= symb <=u'\u04FF' or u'\u0500' <= symb <= u'\u052F':
        return True
    else:
        return False


def show_weather(places):
    for place in places:
        if is_cyrrylic(place):
            payload = {'nqTM': '', 'lang': 'ru'}
        else:
            payload = {'nqTM': '', 'lang': 'en'}
        url = 'http://wttr.in/{}'.format(place)
        response = requests.get(url, params=payload)
        response.raise_for_status()
        print(response.text)


def main():
    places = ['London', 'SVO', 'Череповец']
    show_weather(places)


if __name__ == '__main__':
    main()