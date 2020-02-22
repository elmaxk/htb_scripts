from functools import wraps


def preserving_decorator(function):
	@wraps(function)
	def wrapped(*args, **kwargs):
		""" Internally wrapped function document"""
		return function(*args, **kwargs)
	return wrapped


rpc_info = {}


def xmlrpc(in_=(), out=(type(None),)):
	def _xmlrpc(function):

		# registering the signature
		func_name = function.__name__
		rpc_info[func_name] = (in_, out)

		def _check_types(elements, types):
			"""Sub function that checks types."""
			if len(elements) != len(types):
				raise TypeError('Argument count is wrong.')
			typed = enumerate(zip(elements, types))
			for index, couple in typed:
				arg, of_the_right_type = couple
				if isinstance(arg, of_the_right_type):
					continue
				raise TypeError(
					f'arg #{index} should be {of_the_right_type}'
				)

		# wrapped function
		def __xmlrpc(*args):	# No keywords allowed
			# Check what goes in
			checkable_args = args[1:]	# Removing self
			_check_types(checkable_args, in_)
			# Run the function
			res = function(*args)
			# Checking what goes out
			if not type(res) in (tuple, list):
				checkable_res = (res,)
			else:
				checkable_res = res
			_check_types(checkable_res, out)

			# The function and the type
			# checking succeeded
			return res
		return __xmlrpc
	return _xmlrpc


class RPCView:

	@xmlrpc((int, int))
	def accept_integers(self, int1, int2):
		print(f'Received {int1} and {int2}')

	@xmlrpc((str,), (int,))
	def accept_phrase(self, phrase):
		print(f'Received {phrase}')
		return 12