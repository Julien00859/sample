import argparse
import logging

cli = argparse.ArgumentParser()
cli.add_argument('-v', '--verbose', action='count', default=0)
cli.add_argument('-s', '--silent', action='count', default=0)
options = cli.parse_args()()

# Color the [LEVEL] part of messages, need new terminal on Windows
# https://github.com/odoo/odoo/blob/13.0/odoo/netsvc.py#L57-L100
class ColoredFormatter(logging.Formatter):
    colors = {
        10: (34, 49), 20: (32, 49), 21: (37, 49),
        30: (33, 49), 40: (31, 49), 50: (37, 41),
    }
    def format(self, record):
        fg, bg = type(self).colors.get(record.levelno, (32, 49))
        record.levelname = f"\033[1;{fg}m\033[1;{bg}m{record.levelname}\033[0m"
        return super().format(record)

# Reset logging to ONLY log messages on stdout
stdout = logging.StreamHandler()
stdout.formatter = ColoredFormatter(
    "%(asctime)s [%(levelname)s] <%(funcName)s> %(message)s"
)
logging.root.handlers.clear()
logging.root.addHandler(stdout)

# Set the verbosity, enables python level warnings on -vvv
verbosity = 10 * max(0, min(3 - options.verbose + options.silent, 5))
logging.root.setLevel(verbosity)
if verbosity == 0:
    logging.captureWarnings(True)
    warnings.filterwarnings('default')
