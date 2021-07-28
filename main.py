from pprint import pprint
from habr_search_header import Habr_data
if __name__ == '__main__':
    KEYWORDS = {'дизайн', 'фото', 'web', 'python'}
    result = Habr_data(KEYWORDS).get_data_by_template()
    pprint(result)

