import re

def is_valid_email(email):
    
    pattern = r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*$"
    return bool(re.match(pattern, email))


def is_float_literal(s):
    
    pattern = r'^[-+]?([0-9]*\.[0-9]+|[0-9]+\.?[0-9]*)([eE][-+]?[0-9]+)?[fFlL]?$'
    return bool(re.match(pattern, s))

def is_integer_literal(s):
    try:
        int(s, 0)
        return True
    except ValueError:
        return False