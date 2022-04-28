from ..db.get_db import execute_query

from ..db.transaction_queries import (
    get_transactions_for_store_date_range_query,
    get_all_transactions_for_store_query
)


def get_transactions_for_store_date_range(store_id, start_date, end_date):
    query = get_transactions_for_store_date_range_query(
        store_id, start_date, end_date)
    result = execute_query(query)
    return result


def get_all_transactions_for_store(store_id):
    query = get_all_transactions_for_store_query(store_id)
    result = execute_query(query)
    return result
