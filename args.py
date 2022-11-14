import argparse
from datetime import datetime


def get_args():
    # TODO: Add --start-date, --end-date and --output arguments
    #       Convert the two dates to datetime objects
    parser = argparse.ArgumentParser()
    parser.add_argument('--start-date', type=datetime, default=datetime.now(), help='initial start-date')
    parser.add_argument('--end-date', type=datetime, default=datetime.now(), help='initial end-date')
    parser.add_argument('--output', type=datetime, default=datetime.now(), help='initial output')
    args = parser.parse_args()
    return args
