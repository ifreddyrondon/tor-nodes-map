import os
import re

import pygeoip
import requests
from TorNodesMap.tor.models import Node
from django.conf import settings
from django.core.management.base import BaseCommand


def get_url(url):
    try:
        res = requests.get(url)
    except requests.exceptions.ConnectionError:
        raise requests.exceptions.ConnectionError("DNS lookup failures")
    else:
        if res.status_code != 200:
            raise requests.exceptions.ConnectionError(
                "the {}, answer with {} error".format(url, res.status_code))

        return res


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        file_path = os.path.join(settings.BASE_DIR, 'GeoLiteCity.dat')
        gi = pygeoip.GeoIP(file_path)

        base_url = "https://torstatus.blutmagie.de/query_export.php/Tor_query_EXPORT.csv"
        res = get_url(base_url)

        for line in res.iter_lines():
            line = line.split(",")

            ip = re.findall(r'[0-9]+(?:\.[0-9]+){3}', line[4])
            if len(ip) == 0:
                continue

            ip_address = ip[0]
            geo_data = gi.record_by_addr(ip_address)
            if not geo_data:
                continue

            Node.objects.get_or_create(
                ip=ip_address,
                latitude=geo_data.get('latitude'),
                longitude=geo_data.get('longitude')
            )
