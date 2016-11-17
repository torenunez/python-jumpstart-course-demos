import requests
import bs4
import collections


WeatherReport = collections.namedtuple('WeatherReport',
                                       'cond, temp, scale, loc')

def main():
    # print the header
    print_the_header()
    # get zipcode from user
    code = input('From which zipcode do you want the weather (e.g. 90210) ? ')
    # get HTML from web
    html = get_url_from_web(code)
    # parse the HTML
    report = get_weather_from_html(html)
    # display for the forecast
    print('The temp in {} is {} {} and {}'.format(
        report.loc,
        report.temp,
        report.scale,
        report.cond
    ))


def print_the_header():
    print('------------------------------------')
    print('         WEATHER APP')
    print('------------------------------------')


def get_url_from_web(zipcode):
    url = 'https://www.wunderground.com/weather-forecast/{}'.format(zipcode)
    response = requests.get(url)
    # print(response.status_code)
    # print(response.text[:250])
    return response.text


def get_weather_from_html(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    # print(soup)
    loc = soup.find(id='location').find('h1').get_text()
    condition = soup.find(id='curCond').find(class_='wx-value').get_text()
    temp = soup.find(id='curTemp').find(class_='wx-value').get_text()
    scale = soup.find(id='curTemp').find(class_='wx-unit').get_text()

    loc = cleanup_text(loc)
    loc = find_city_and_state(loc)
    condition = cleanup_text(condition)
    temp = cleanup_text(temp)
    scale = cleanup_text(scale)

    report = WeatherReport(cond=condition, temp=temp, scale=scale, loc=loc)
    return report

def cleanup_text(text: str):
    if not text:
        return text

    text = text.strip()
    return text


def find_city_and_state(loc: str):
    parts = loc.split('\n')
    return parts[0].strip()


if __name__ == '__main__':
    main()

