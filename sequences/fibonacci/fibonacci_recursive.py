def recur_fibo(n):
	if n <=1:
		return n
	else:
		return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = int(input("How many terms? "))

answer = recur_fibo(nterms)
print(answer)

