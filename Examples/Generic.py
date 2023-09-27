

from mpzinke import Generic
from typing import Any


# As an inheritted class
class A(Generic):
	def __init__(self, a: Any):
		assert(isinstance(a, self.__args__[0])), f"'a' is not of type '{self.__args__[0]}'"
		self.a: Any = a


a = A[int](1)


# As a function decorator
@Generic
def my_function(__args__, a):
	assert(isinstance(a, __args__[0])), f"'a' is not of type '{__args__[0]}'"


my_function[str]("Hello World")
