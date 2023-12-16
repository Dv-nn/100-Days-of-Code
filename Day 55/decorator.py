# Advanced Python Decorator Functions

class User():
  def __init__(self, name):
    self.name = name
    self.is_logged_in = False

  def is_authentificated_decorator(function):
    def wrapper(*args, **kwarg):
      if args[0].is_loggeed_in = True:
        function(args[0])
    return wrapper

  @is_authentificated_decorator
  def create_blog_post(user):
    print(f"This is {user.name}'s new blog post")

new_user = User("Natalya")
new_user.is_logged_in = True   
