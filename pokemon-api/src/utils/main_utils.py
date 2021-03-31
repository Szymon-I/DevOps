from fastapi import Request

# Dependency
def get_db(request: Request) -> Request:
    """ Assign db session for request """
    return request.state.db
