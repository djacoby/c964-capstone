def get_all_stores_query():
    """
    Returns a query that returns all stores.
    """
    return """
        SELECT
          id
          ,city
          ,state
          ,district
        FROM store;
    """, ()


def get_store_by_id_query(store_id):
    """
    Returns a query that returns a single store by id.
    """
    return """
        SELECT
          id
          ,city
          ,state
          ,district
        FROM store
        WHERE id = %s;
    """, store_id


def get_stores_by_district_query(district):
    """
    Returns a query that returns all stores for a district.
    """
    return """
        SELECT
          id
          ,city
          ,state
          ,district
        FROM store
        WHERE district = %s;
    """, district
