import functools

#Least Recently Used
@functools.lru_cache()
def fib(n):
	if n < 2:
		return n
	return fib(n-2) + fib(n-1)

if __name__=='__main__':
	print(fib(6))
