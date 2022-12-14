from scrapy.utils.project import get_project_settings
from scrapy.exporters import CsvItemExporter


class Exporter(CsvItemExporter):
    def __init__(self, *args, **kwargs):
        settings = get_project_settings()
        delimiter = settings.get("CSV_DELIMITER", ",")
        kwargs["delimiter"] = delimiter
        super(Exporter, self).__init__(*args, **kwargs)