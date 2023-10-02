import logging


class StreamLogFormatter(logging.Formatter):
    grey = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    cyan = "\033[96m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    format = f"%(levelname)-8s [%(asctime)s]: %(message)s  {reset}{grey}%(filename)s:%(lineno)d %(name)s"

    FORMATS = {
        logging.DEBUG: grey + format + reset,
        logging.INFO: cyan + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


class FileLogFormatter(logging.Formatter):
    format_string = f"%(levelname)-8s [%(asctime)s]: %(message)s  %(filename)s:%(lineno)d %(name)s"

    def format(self, record):
        formatter = logging.Formatter(self.format_string)
        return formatter.format(record)
