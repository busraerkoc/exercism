def prime(number):
	if number==0:
		raise ValueError("Error")

	list1 = [2]
	for i in range(3, 200000):
        	if i%2!=0:
                        list1.append(i)

	list2 = [2, 3]
	for k in range(2, len(list1)):
                if list1[k]%list1[1]!=0:
                        list2.append(list1[k])
	list3 = [2, 3, 5]
	for l in range(3, len(list2)):
                if list2[l]%list2[2]!=0:
                        list3.append(list2[l])
	list4 = [2, 3, 5, 7]
	for m in range(4, len(list3)):
                if list3[m]%list3[3]!=0:
                        list4.append(list3[m])
	list5 = [2, 3, 5, 7, 11]
	for n in range(5, len(list4)):
		if list4[n]%list4[4]!=0:
			list5.append(list4[n])
	return list5[number-1]


