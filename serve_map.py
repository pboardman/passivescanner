#!/usr/bin/env python3

import jinja2
import os
import sqlite3
from flask import Flask
from flask import render_template


app = Flask(__name__)


def main():
    app.run(host='0.0.0.0', port=8000)


@app.route('/')
def show_map():
    db_conn = sqlite3.connect('data.db')
    c = db_conn.cursor()
    c.execute("SELECT IP, Latitude, Longitude, Port, Country, Region, City, Timezone, ConnDate, count(IP) FROM Scanners GROUP BY IP")
    result = c.fetchall()

    return render_template('template.html', locations=result)


if __name__ == "__main__":
    main()
