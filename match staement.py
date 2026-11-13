<<<<<<< HEAD
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"\
    from enum import Enum
    
    
=======
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"\
    from enum import Enum
    
    
>>>>>>> f4eb38985d009c37b7c0da33d1ec68cfec51e7e7
