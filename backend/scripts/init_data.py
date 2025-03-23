#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ruff: noqa: I001
from anyio import run

import sys
import os
# 将项目根目录加入 sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from backend.database.db import create_table


async def init() -> None:
    print('Creating initial data')
    await create_table()
    print('Initial data created')


from backend.database.db import SQLALCHEMY_DATABASE_URL
print(f"Database URL: {SQLALCHEMY_DATABASE_URL}")

# from backend.app.user.model import *  # to excute code for test

from backend.common.model import MappedBase
print(f"Registered tables: {MappedBase.metadata.tables.keys()}")


if __name__ == '__main__':
    run(init)  # type: ignore
