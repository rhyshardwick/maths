# Questions
# Why is -1 needed, can't we just start with 1?
# Why are we using sets

n=int(input("Input a Number: "))
List=range(-1,n*n+9,2) # make a massive list of odd numbers, with -1 at the start, which is ignored throughout

i=2 #start at 3rd term
while List[i:]: 	# from nth term (i) until end of list
	List=sorted(set(List) - set(List[List[i]::List[i]]))	# create a set of all multiples of i, and then remove it from the list
	i+=1
print(List[1:n+1])

