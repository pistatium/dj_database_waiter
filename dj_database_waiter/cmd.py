# coding: utf-8

import os
import sys
import argparse
import time

import django

from typing import NamedTuple


class DbStatus(NamedTuple):
    ok: bool
    reason: str = None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--interval', nargs='?', type=int, default=5)
    parser.add_argument('--max_trial', nargs='?', type=int, default=60)
    parser.add_argument('--db_group', nargs='?', type=str, default='default')
    parser.add_argument('setting_module', type=str)

    params = parser.parse_args()

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", params.setting_module)
    django.setup()

    for i in range(params.max_trial):
        status = check_status(params.db_group)
        if status.ok:
            return sys.exit(0)
        print(f'Failed to connect database. :{status.reason}')
        time.sleep(params.interval)
        print(f'Retrying... ({i + 1}/{params.max_trial})')
    print('Error')
    return sys.exit(1)


def check_status(db_group_name: str) -> DbStatus:
    try:
        from django.db import connections
        conn = connections[db_group_name]
        conn.cursor()
    except Exception as e:
        return DbStatus(ok=False, reason=str(e))
    return DbStatus(ok=True)


if __name__ == "__main__":
    main()
