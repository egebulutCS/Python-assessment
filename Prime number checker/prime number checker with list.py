N=3

A=2

while(N<=200): #This is to show prime numbers in first 200 numbers to any users.
	if(A<N):

		if((N%A==0)):

			N+=1

			A=2

		else:

			A+=1

	else:

		print(N)

		N+=1

		A=2

print("Are the prime numbers within first 200 numbers.")

#This will keep program running with the given input at the end of the code.
#This features makes it a lot easier to use,so called "user-friendly".
q="y"
while q=="y" or q=="Y":
	#With the input the static part of the code starts here.
	n=int(input("Please enter a number: "))

	a=2

	b=0
	#This code starts below checks the given number list. However on each machine it runs
	#it needs to be located again if the file is not in the given path. In the sample the path 
	#shows my file's location. If the file is not available the program will crash when a number
	#from the list is applied.
	if n>15000000:
		with open(r"C:\Users\EGE\Documents\Python assessment\Large prime number list checker\large prime numbers.txt") as f:
			for line in f:
				numbers_str = line.split()
				numbers_float = [float(x) for x in numbers_str]
				i=0
				while i<=52:
					if n==numbers_float[i]:
						print(n,"is in the large prime numbers list.")
						print("The number's position in the list is",i+1)
						break
					else:
						i+=1
	#As long as "a" is smaller than our number we have to check if it is divisible by it.
	#We have to check if "n" is not a negative number as it will be treated as a positive
	#number and give the result prime number.
	#The prime numbers start from 2 so it is better to seperate special cases from calculations.
	elif n>=2:
		while a<n:
			if n%a==0:

				#if our number is divisible by current a we will save the 
				#information that it is not a prime number by the value b.
				#to get all the values that divides our n number we keep the process live.
				print(n,"is divisible by",a)
				b=1
				a+=1
			else:

				a+=1

		#if the indicator b has not been activated the code will finally print that the
		#number is prime, else it will print that it is not prime.
		if b!=1:

			print(n,"is a prime number.")
		else:
			print(n,"is not a prime number.")
	#0 is considered as not prime and a special case.
	elif n==0:
		print("Zero is considered as a non prime number.")
	#As 0, 1 is also a special case and has to be apart from calculation.
	elif n==1:
		print("Number 1 is by definition can not be a prime number.")
	else:
		print("Please input a positive number.")
	print("You can find a list of large prime numbers at primes.utm.edu/lists/small/millions/")
	q=input("Do you want to try again?[Y/N]:")
k=input("Press enter to exit")