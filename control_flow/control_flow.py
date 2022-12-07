"""
Information about the module
"""

## Match statement

def http_error(status) -> str:
    """return information about a specific http error based on its status

    Args:
        status (int): the status to validate

    Returns:
        str: description about the http error
    """
    match status:
        case 200:
            return "All is fine"
        case 201:
            return "Element was created"
        case 400:
            return "Bad request"
        case 404:
            return "Not Found"
        case 500 | 501 | 502:
            return "Internal Server Error"
        case _:
            return "Something was wrong!"

# positional, default, and kw-values
def start(pos1, pos2, *args, **kwargs):
    """Functions that help us with a explanation

    Args:
        pos1 (any): example
        pos2 (any): example
    """
    print(pos1)
    print(pos2)
    for arg in args:
        print(f"Positional: {arg}")
    for k,v in kwargs.items():
        print(f"{k}: {v}")
        

dict_values ={
    "endpoint": "http://localhost:3306",
    "method": "GET",
    "token" : "biufwebiuoksd",
}


if __name__ == "__main__":
    print(http_error(200))
    print(http_error(400))
    print(http_error(500))
    print(http_error(502))
    print(http_error(300))
    start("name", "last_name", **dict_values)
    start("name", "last_name", "age", "hobbie", "adress", "email", endpoint = "http://localhost:3306", token="biufwebiuoksd")