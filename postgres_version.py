#!/usr/bin/python
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine

eng = create_engine('postgresql://postgres@localhost:5432/capstone')
con = eng.connect()

rs = con.execute("SELECT VERSION()")
print(rs.fetchone())

con.close()
