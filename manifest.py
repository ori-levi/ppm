import json
from jsonschema import validate

with open('manifest.schema') as schema_file:
    MANIFEST_SCHEMA = json.load(schema_file)


def manifest(manifest_path):
    """
    :param manifest_path:
    :return:
    :rtype: Manifest
    """
    with open(manifest_path) as f:
        manifest_obj = json.load(f)
        validate(manifest_obj, MANIFEST_SCHEMA)
        return __Manifest(manifest_obj)


class __Manifest(object):
    def __init__(self, obj):
        super(self.__class__, self).__init__()
        self.__data = obj  # type: dict

    def __getattr__(self, item):
        return self.__data[item]
