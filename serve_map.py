#!/usr/bin/env python3

import jinja2
import os
import sqlite3
import traceback
from sanic import Sanic
from sanic.response import html


app = Sanic()
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader('.'))
db_conn = sqlite3.connect('data.db')


def main():
    app.run(host='0.0.0.0', port=8000)


@app.route('/')
async def show_map(request):

    c = db_conn.cursor()
    c.execute("SELECT IP, Latitude, Longitude, Port, Country, Region, City, Timezone, ConnDate, count(IP) FROM Scanners GROUP BY IP")
    result = c.fetchall()

    template = jinja_env.get_template('template.html')
    render = template.render(locations= result)

    return html(render)


if __name__ == "__main__":
    main()
