from algorithms.catalog import registry


def get_all_algorithms():
    return registry.list_all()