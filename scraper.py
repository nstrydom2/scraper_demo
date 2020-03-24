import requests
import lxml

from bs4 import BeautifulSoup


class Scraper:
    def __init__(self):
        pass

    def scrape_imdbtop100(self):
        imdb_url = 'https://www.imdb.com/list/ls055592025/'
        result = {}

        try:
            doc = requests.get(imdb_url)
            soup = BeautifulSoup(doc.text, 'lxml')
            links = soup.find_all('a', href=True)

            count = 0
            for movie in links:
                if 'title' in movie['href'].split('/') and \
                        movie.text.strip() not in ('', 'Best Picture Winners'):
                    count += 1
                    result[count] = movie.text.strip()

            return result
        except Exception as ex:
            print("[*] Error -- Unable to scrape Imdb website: " + str(ex))

    def scrape_billboardtop100(self):
        imdb_url = 'https://www.billboard.com/charts/hot-100'
        result = {}

        try:
            doc = requests.get(imdb_url)
            soup = BeautifulSoup(doc.text, 'lxml')
            song_elements = soup.select('html body.chart-page.chart-page- main#main.page-content div#charts '
                                        'div.charts-container div.chart-list.container ol.chart-list__elements '
                                        'li.chart-list__element.display--flex button.chart-element_'
                                        '_wrapper.display--flex.flex--grow.sort--default span.chart-element'
                                        '__information')

            for idx, song in enumerate(song_elements):
                song_info = song.find_all('span')
                result[idx+1] = song_info[1].text + ' - ' + song_info[0].text

            return result
        except Exception as ex:
            print("[*] Error -- Unable to scrape Billboard website: " + str(ex))


if __name__ == '__main__':
    scraper = Scraper()
    scraper.scrape_billboardtop100()
