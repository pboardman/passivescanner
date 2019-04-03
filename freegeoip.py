#!/bin/python3

import json
import os
import urllib.request


class Freegeoip:
    def __init__(self):
        self.info = None
        self.url = "https://freegeoip.app/json/{}"

    def ip_info(self, ip):
        url = self.url.format(ip)
        req = urllib.request.urlopen(url)
        if req.getcode() != 200:
            raise ValueError("Could not get ip info for: {}".format(ip))

        self.info = json.loads(req.read())
        return self.info
