import yaml

from django.conf import settings
from django.contrib.sites.models import Site


def ftf_geonode(request):
    """Global values to pass to templates"""

    defaults = {}

    MOCK_FEATURED_DATASETS = None
    with open("ftf_geonode/MOCK_FEATURED_DATASETS.yml", 'r') as f:
        MOCK_FEATURED_DATASETS = yaml.load(f)

    if MOCK_FEATURED_DATASETS:
        defaults['MOCK_FEATURED_DATASETS'] = MOCK_FEATURED_DATASETS.get('datasets', [])


    INDEX_TILES = None
    with open("ftf_geonode/INDEX_TILES.yml", 'r') as f:
        INDEX_TILES = yaml.load(f)

    if INDEX_TILES:
        defaults['INDEX_TILES'] = INDEX_TILES

    return defaults
