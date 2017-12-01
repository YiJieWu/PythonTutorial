def print_line_atend(func):
	def wrapper(*args,**kwargs):
		func(*args,**kwargs)
		print '======================================================='
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
	print 'hello world'
def understand_args(*args):
	print type(args),len(args),args
	for arg in args:
		print arg
	args[5]()

understand_args('hello','world','this','is','Yijie',hello)









#Example 1
'''
No parameters for the inner functiuon 
No parameters for the decorator

Suppose you have a foo function and you 
later want to add some functionality that
print Starts before executing this foo function

'''
def foo():
	print 'This is foo'

def decorator(func):
	print 'Starts!'
	def wrapper():
		func()
	return wrapper

foo=decorator(foo)
foo()