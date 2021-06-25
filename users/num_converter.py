def NumConverter(number):
	num = str(number)
	num = num[::-1]
	list_num = []
	spacing = []
	for i in num:
		list_num.append(i)
	for i in range(1, len(list_num)):
		if i % 3 == 0 :
			spacing.append(i)
	for i in range(len(spacing)):
		list_num.insert(spacing[i]+i ,',')
	list_num.reverse()

	for i in range(len(list_num)):
		if list_num[i] == '0':
			list_num[i] = '۰'
		elif list_num[i] == '1':
			list_num[i] = '۱'
		elif list_num[i] == '2':
			list_num[i] = '۲'
		elif list_num[i] == '3':
			list_num[i] = '۳'
		elif list_num[i] == '4':
			list_num[i] = '۴'
		elif list_num[i] == '5':
			list_num[i] = '۵'
		elif list_num[i] == '6':
			list_num[i] = '۶'
		elif list_num[i] == '7':
			list_num[i] = '۷'
		elif list_num[i] == '8':
			list_num[i] = '۸'
		elif list_num[i] == '9':
			list_num[i] = '۹'
	final_res = ""
	for i in list_num:
		final_res+=i
	return final_res


