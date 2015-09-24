from django.utils.importlib import import_module


def import_module_attr(path):
    package, module = path.rsplit('.', 1)
    return getattr(import_module(package), module)


def get_default_item(value):
    return value[0] if isinstance(value, tuple) else value


def get_default_value(value):
    item = get_default_item(value)
    return item[0] if isinstance(item, tuple) else item


def get_default_representation(value):
    item = get_default_item(value)
    return item[1] if isinstance(item, tuple) else item
