def get_transactions_for_store_date_range_query(store_id, start_date, end_date):
    """
    Returns a query that returns all transactions between two dates.
    """
    return """
        SELECT
          "transaction_date" as ds
          ,"amount" as y
        FROM transactions
        WHERE store_id = %s
        AND transaction_date >= %s
        AND transaction_date <= %s;
    """, store_id, start_date, end_date


def get_all_transactions_for_store_query(store_id):
    """
    Returns a query that returns all transactions for a store.
    """
    return """
        SELECT
          "transaction_date" as ds
          ,"amount" as y
        FROM transactions
        WHERE store_id = %s;
    """, store_id
