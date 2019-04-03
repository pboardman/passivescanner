#!/usr/bin/python3

from freegeoip import Freegeoip
import os
import socket
import sys
import sqlite3
import traceback
from datetime import datetime
from threading import Thread


def main():
    db_conn = sqlite3.connect('data.db')
    init_db(db_conn)

    freegeoip = Freegeoip()

    start_server(db_conn, freegeoip)


def start_server(db_conn, freegeoip):
    host = "0.0.0.0"
    port = 22

    print("starting server on port {}".format(port))
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)   # NO IDEA WHAT THIS DOES: SO_REUSEADDR flag tells the kernel to reuse a local socket in TIME_WAIT state, without waiting for its natural timeout to expire
    soc.bind((host, port))

    soc.listen(5) # queue up to 5 requests

    while True:
        # Accept the connection and close it instantly
        connection, address = soc.accept()
        ip = address[0]
        connection.close()
        ip_info = freegeoip.ip_info(ip)
        add_to_db(db_conn, ip_info, port)

    soc.close()


def add_to_db(db_conn, ip_info, port):
    SQL = """
    INSERT INTO Scanners VALUES (?,?,?,?,?,?,?,?,?,?,?)
    """
    db_conn.execute(SQL, (datetime.now(), ip_info['ip'], port, ip_info['country_code'],
                          ip_info['country_name'], ip_info['region_code'],
                          ip_info['region_name'], ip_info['city'], ip_info['time_zone'],
                          ip_info['latitude'], ip_info['longitude']))
    db_conn.commit()


def init_db(conn):
    SQL = """
    CREATE TABLE IF NOT EXISTS Scanners
    (ConnDate text, IP text, Port text, CountryCode text, Country text, RegionCode text, Region text, City Text, TimeZone text, Latitude float, Longitude float)
    """
    conn.execute(SQL)


if __name__ == "__main__":
    main()
