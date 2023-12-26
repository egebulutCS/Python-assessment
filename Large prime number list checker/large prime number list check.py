n=32452843
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
k=input("enter")