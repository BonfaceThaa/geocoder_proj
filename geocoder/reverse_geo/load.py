from pathlib import Path
from django.contrib.gis.utils import LayerMapping
from .models import Wards

wards_mapping = {
    'gid': 'gid',
    'county': 'county',
    'subcounty': 'subcounty',
    'ward': 'ward',
    'geom': 'MULTIPOLYGON',
}

ward_shp = Path(__file__).resolve().parent / 'data' / 'admin' / 'admin.shp'


def run(verbose=True):
    """
    Function to load Wards data
    """
    lm = LayerMapping(Wards, str(ward_shp), wards_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)
