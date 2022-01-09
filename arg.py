def caculator(n=1, *arg, **kwargs):
	for a in arg:
		n += a
	

	# print(type(kwargs))
	for k,v in kwargs.items():
		print(k,v)

ans = caculator(1, 2, 3, 4, 5, c=5, e=7)
print('答案是：', ans)