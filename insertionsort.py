def insertionSort(nlist):
	   for index in range(1,len(nlist)):
	        currentvalue = nlist[index]
	        position = index
	
	        while position>0 and nlist[position-1]>currentvalue:
	           nlist[position]=nlist[position-1]
	           position = position-1
	        nlist[position]=currentvalue

nlist = [2,46,3,27,17,41,40,21,9,60]
print('Before sorting :',end='')
print(nlist)
insertionSort(nlist)
print('Sorted list: ', end='')
print(nlist)         
	



## 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 ## its token for github


