import csv
import datetime as dt
from collections import defaultdict
from pathlib import Path

from pep_parse.settings import RESULTS_DIR

BASE_DIR = Path(__file__).parent.parent
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
PEP_TITLES = ('Статус', 'Количество')
PEP_TOTAL = 'Всего'
FILE_NAME = 'status_summary_{now_formatted}.csv'
DIR_NOT_FOUND = 'Не найдена папка для сохранения результата'


class PepParsePipeline:

    def __init__(self):
        self.results_dir = BASE_DIR / RESULTS_DIR
        self.results_dir.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.statuses = defaultdict(int)

    def process_item(self, item, spider):
        self.statuses[item['status']] += 1
        return item

    def close_spider(self, spider):
        now_formatted = dt.datetime.now().strftime(DATETIME_FORMAT)
        file_name = FILE_NAME.format(now_formatted=now_formatted)
        file_path = self.results_dir / file_name
        with open(file_path, 'w', encoding='utf-8') as f:
            csv.writer(
                f,
                dialect=csv.unix_dialect,
                quoting=csv.QUOTE_NONE
            ).writerows(
                [
                    PEP_TITLES,
                    *self.statuses.items(),
                    (PEP_TOTAL, sum(self.statuses.values()))
                ]
            )
