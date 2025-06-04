
print('choose the operation')
print('1. Add')
print('2. Subtract')
print('3. Multiply')
print('4. Division')

choose = input("choose any one from above: ")

num1 = float(input('enter any number:'))
num2 = float(input('enter second number:'))

if choose == '1':
	print('answer:' , num1 + num2)
elif choose == '2':
	print('answer:' , num1 - num2)
elif choose == '3':
	print('answer:' , num1 * num2)
elif choose == '4':
	if num2 >=1:
		print('answer:' , num1 / num2)
	else:
		print('0 cannot divide any number')

else:
	print('invalid syntax')
print("     \n")

print("MADE BY PREM ARYAN,")
print("THANK YOU")
