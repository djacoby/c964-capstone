from app.db.get_db import execute_query

from app.db.user_queries import (
    get_create_user_query,
    get_create_manager_query,
    get_create_district_manger_query,
    get_login_query,
    get_manager_by_user_id_query,
    get_district_manager_by_user_id_query,
)


def create_manager(first_name, last_name, email, password, store_id):
    # Create user
    query = get_create_user_query(
        first_name, last_name, email, password, False)
    user_result = execute_query(query)
    # Make user a manager
    query = get_create_manager_query(user_result[0]['id'], store_id)
    manager_result = execute_query(query)
    return user_result[0] | manager_result[0]


def create_district_manager(first_name, last_name, email, password, district_id):
    query = get_create_user_query(
        first_name, last_name, email, password, False)
    # Create user
    user_result = execute_query(query)
    # Make user a district manager
    query = get_create_district_manger_query(user_result[0]['id'], district_id)
    district_manager_result = execute_query(query)
    return user_result[0] | district_manager_result[0]


def create_admin_account(first_name, last_name, email, password):
    query = get_create_user_query(
        first_name, last_name, email, password, True)
    user_result = execute_query(query)
    return user_result[0]


def login_user(email, password):
    # Get user object from database
    query = get_login_query(email, password)
    user = execute_query(query)

    # If there is no user with that email, return None
    if len(user) == 0:
        return None

    # If user is an admin return the user object
    elif user[0]['admin']:
        return user[0]

    else:
        # Check if user is a manager
        query = get_manager_by_user_id_query(user[0]['id'])
        manager = execute_query(query)

        # Check if user is a district manager
        if len(manager) == 0:
            query = get_district_manager_by_user_id_query(user[0]['id'])
            district_manager = execute_query(query)
            return user[0] | district_manager[0]

        return user[0] | manager[0]
