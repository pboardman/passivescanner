# Passivescanner

Passively check port scanners on a port and add their info to a database.

## How to use

just clone and run passivescanner.py with the port as the first argument (use sudo if port < 1024)

```bash
git clone https://github.com/pboardman/passivescanner
sudo ./passivescanner.py 22 # Or any other port
```

## Info

Info about the port scanners will be added to `./data.db` and can be accessed with the sqlite3 cli tools or something like [sqlitebrowser](https://sqlitebrowser.org/).

Info added to BD includes:
- Country
- Region
- City
- Timezone
- Latitude
- Longitude

IP info is provided by [freegeoip.app](https://freegeoip.app/).
