'''
The print line at end is a decorator that adds the functionality
of appending ====================== at the end of each function
'''
def print_line_atend(func):
	def wrapper(*args,**kwargs):
		func(*args,**kwargs)
		print '======================================================= END Of',func.__name__
	return wrapper


'''
In order to understand decorator, you first need to understand that in 
Python and many other prigramming languages,you can pass a function as
parameter into another function and call it within that function
'''
def foo1():
	print 'Passing foo1 as parameter'

@print_line_atend
def call_function(fun):
	fun()


call_function(foo1)



'''
You also need to undertstand *args and **kwargs in Python

The syntax is the * and **. 
The names *args and **kwargs are only by convention but there's no hard requirement to use them.
'''
def hello():
	print 'This is the hello function'

@print_line_atend
def understand_args(*args):
	print type(args),len(args),args
	for arg in args:
		print arg
	args[5]()

understand_args('hello','world','this','is','Yijie',hello)



@print_line_atend
def understand_kwargs(**kwargs):
	print type(kwargs),len(kwargs),kwargs
	for key in kwargs:
		print 'key is',key,'value is',kwargs[key]

understand_kwargs(name='Yijie',gender='Male',id=12345)



#Example 1 of Decorator
'''
No parameters for the inner functiuon 
No parameters for the decorator

Suppose you have a foo function and you 
later want to add some functionality that
print Starts before executing this foo function


One easy way you can think of is pass the foo function itself 
as a parameter into another wrapper function called decorator 
and add some things in the decorator function

But remember, The original function we want to have is foo!!! not
this decorator function, what we actually want to acheieve is still 
call this foo function but with the added functionalities


'''
def foo():
	print 'This is foo'

@print_line_atend
def decorator(func):
	print 'Starts!'
	func()

decorator(foo)






def betterfoo():
	print 'This is better foo'

def decorator(func):
	def wrapper():
		func()
	return wrapper

betterfoo=decorator(betterfoo)
betterfoo()




