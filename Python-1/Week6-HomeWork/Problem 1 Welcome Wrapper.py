
def welcome_Hello(func):
      def wapper():
       print("Hello!")
       func()
      return wapper
def welcome_name(func):
      def wapper():
       print("My name is Saad")
       func()
      return wapper
@welcome_Hello
@welcome_name
def say_hello():
   print ("Goodbye!")

say_hello()
