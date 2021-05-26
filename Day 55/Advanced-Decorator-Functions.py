# Decorator with class object passed as an argument
class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        # if user.is_logged_in == True:
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper

@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")

new_user = User("alozie")
new_user.is_logged_in = True
create_blog_post(new_user)

############################################################

# Create the logging_decorator() function 👇
def logging_decorator(function):
    def wrapper(*args):
        print(f"The function name is: {function.__name__}")
        for arg in args:
            print(arg)
        print(function(*args))
    return wrapper


# Use the decorator 👇
@logging_decorator
def add(n1, n2, n3):
    return n1 + n2 + n3

add(3, 4, 5)
