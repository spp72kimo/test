try:
	num = input('Please input a number: ')
	print('You set number is: ', num)
	result = int(num) + 8
except ValueError:
	print('請輸入數字！')
else:
 	print(num, '+ 8 = ', result)

finally:
 	print('程式結束。')
