def fact(n):
    if n == 0:
	return 1
    else:
	return n*fac(n-1)
number = 5
res = fac(number)
print(f"the factorial of (number) is (res)")

