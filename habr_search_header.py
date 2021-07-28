import requests
from bs4 import BeautifulSoup


class Habr_data:

    def __init__(self, keys):
        self.keys = keys

    def get_data_by_template(self):
        ret = requests.get('https://habr.com/ru/all/')
        soup = BeautifulSoup(ret.text, 'html.parser')
        articles = soup.find_all('article')
        result_list = []
        for article in articles:
            if self._get_tags(article) & self.keys:
                self._get_data(article, result_list)
        return result_list

    def _get_data(self, search_article, r_list):
        head_list = search_article.find(class_='tm-article-snippet__title-link')
        time_edition = search_article.find(class_="tm-article-snippet__datetime-published").time.get('title')
        head = head_list.text
        url = 'https://habr.com' + head_list.get('href')
        r_list.append({
            'header': head,
            'link': url,
            'date': time_edition
        })
        return r_list

    def _get_tags(self, search_place):
        found_tags = search_place.find(class_="tm-article-snippet__hubs")
        tags_article = {ft.text.strip().lower() for ft in found_tags}
        return tags_article
