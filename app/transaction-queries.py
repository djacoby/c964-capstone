def get_transactions_for_store_date_range_query(store_id, start_date, end_date):
    """
    Returns a query that returns all transactions between two dates.
    """
    return f"""
        SELECT
          ,"id"
          ,"store_id"
          ,"amount"
          ,"transaction_date"
        FROM transactions
        WHERE store_id = '{store_id}'
        transaction_date >= '{start_date}'
        AND transaction_date <= '{end_date}';
    """
