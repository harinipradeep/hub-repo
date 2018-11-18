def binarysearch(lst, num):
	first = 0
	last = len(lst) - 1
	found = False
	while first<=last and not found:
		mid = (first+last)/2
		if lst[mid] == num:
			found = True
		else:
			if lst[mid]<num:
				first = mid+1
			else:
				last = mid-1
	return found

lst = [41, 21, 56, 9, 5, 12, 67]
lst.sort()
print(binarysearch(lst, 12))
print(binarysearch(lst, 23))

#$ python binarysearch.py 
#True
#False


