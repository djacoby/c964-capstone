def get_create_user_query(first_name, last_name, email, password, admin):
    """
    Returns a query that creates a user.
    """
    return """
      INSERT INTO user_data (
        first_name
        ,last_name
        ,email
        ,password
        ,admin
      ) 
      VALUES ( %s, %s, %s, crypt(%s, gen_salt('bf')), %s )
      RETURNING *;
    """, first_name, last_name, email, password, admin


def get_create_manager_query(user_id, store_id):
    """
    Returns a query that creates a manager.
    """
    return """
      INSERT INTO manager (
        user_id
        ,store_id
      )
      VALUES ( %s, %s )
      RETURNING *;
    """, user_id, store_id


def get_create_district_manger_query(user_id, district_id):
    """
    Returns a query that creates a district manager.
    """
    return """
      INSERT INTO district_manager (
        user_id
        ,district_id
      )
      VALUES ( %s, %s )
      RETURNING *;
    """, user_id, district_id


def get_login_query(email, password):
    """
    Returns a query that returns a user by email.
    """
    return """
      SELECT
        id
        ,first_name
        ,last_name
        ,email
        ,admin
      FROM user_data
      WHERE email = %s
      AND password = crypt(%s, password);
    """, email, password


def get_manager_by_user_id_query(user_id):
    """
    Returns a query that returns a manager by user id.
    """
    return """
      SELECT
        user_id
        ,store_id
      FROM manager
      WHERE user_id = %s;
    """, user_id


def get_district_manager_by_user_id_query(user_id):
    """
    Returns a query that returns a manager by user id.
    """
    return """
      SELECT
        user_id
        ,district_id
      FROM district_manager
      WHERE user_id = %s;
    """, user_id
