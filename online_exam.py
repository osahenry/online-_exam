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
    
 def is_valid_java_identifier(identifier):
    """
    Returns True if the given identifier is a valid Java variable, class, or method name,
    and False otherwise.
    """
    # Java identifiers must start with a letter, underscore, or dollar sign
    # and can be followed by any combination of letters, digits, underscores, or dollar signs
    pattern = r'^[a-zA-Z_$][a-zA-Z0-9_$]*$'
    return bool(re.match(pattern, identifier))   
def is_valid_cpp_multiline_comment(comment):
    """
    Returns True if the given string is a valid C++ multiline comment, and False otherwise.
    """
    # C++ multiline comments start with "/*" and end with "*/"
    pattern = r'^/\*.*\*/$'
    return bool(re.match(pattern, comment, re.DOTALL))
