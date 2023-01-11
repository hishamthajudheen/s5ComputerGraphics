
limit = int(input("Enter limit: "))
num1 = 0
num2 = 1
count = 0

if limit<=0:
	print("Enter positive integer!")
elif limit == 1:
	print(num1)
else:
	while count<limit:
		print(num1)
		num3 = num1 + num2
		num1 = num2		
		num2 = num3
		count+=1
		
	
