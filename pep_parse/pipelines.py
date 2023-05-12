import csv
import datetime as dt
from collections import defaultdict
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
RESULTS_DIR_NAME = 'results'
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
PEP_TITLES = ('Статус', 'Количество')
PEP_TOTAL = ('Всего')
FILE_NAME = ('status_summary_{now_formatted}.csv')


class PepParsePipeline:

    def open_spider(self, spider):
        self.statuses = defaultdict(int)

    def process_item(self, item, spider):
        self.statuses[item['status']] += 1
        return item

    def close_spider(self, spider):
        results_dir = BASE_DIR / RESULTS_DIR_NAME
        results_dir.mkdir(exist_ok=True)
        results = [
            PEP_TITLES,
            *self.statuses.items(),
            (PEP_TOTAL, sum(self.statuses.values()))
        ]
        now = dt.datetime.now()
        now_formatted = now.strftime(DATETIME_FORMAT)
        file_name = FILE_NAME.format(now_formatted=now_formatted)
        file_path = results_dir / file_name
        with open(file_path, 'w', encoding='utf-8') as f:
            csv.writer(
                f,
                dialect=csv.unix_dialect
            ).writerows(
                results
            )
