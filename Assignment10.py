a = list(range(1,11))
#print("Original list:                ",a) --------->for alignment
print("Original list:",a)
b = a[0:5]
print("Extracted first five elements:",b)
b.reverse()
#print("Reversed extracted elements:  ",b) --------->for alignment
print("Reversed extracted elements:",b)

#c = b[::-1] ---------> it will start at the end and run till 1st place with step difference of -1
#c=list(reversed(b)) ------------> creates a copy of list reversed order
#for c in reversed(b): --------> for loop to add values in c taking reversed list b
#c = b.sort(reverse=True)-----> Doesn't works,print None. Why ????
#c=b.reverse()-----> reverses the original string. why doesn't works????
