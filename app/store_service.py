from db import execute_query

from store_queries import (
    get_all_stores_query,
    get_store_by_id_query,
    get_stores_by_district_query,
)


def get_all_stores():
    query = get_all_stores_query()
    result = execute_query(query)
    return result


def get_store_by_id(store_id):
    query = get_store_by_id_query(store_id)
    result = execute_query(query)
    return result


def get_store_by_district(district):
    query = get_stores_by_district_query(district)
    result = execute_query(query)
    return result
