def arrondir(n) :
	nn = str(n)
	tab = []
	i = 0
	while (i < len(nn)):
		tab.append(nn[i])
		i += 1

	i = 0	
	lt = len(tab)
	while (tab[lt -1 - i] != '.'):
		if (int(tab[lt -1 - i ]) >= 5):
			if (tab[lt -1 - i -1] == '.'):
				tab[lt -1 - i -2] = str(int(tab[lt -1 - i -2]) + 1)	
			else :	
				tab[lt -1 - i -1] = str(int(tab[lt -1 - i -1]) + 1)
							
		i += 1	


	i = 0
	res = ""
	while (i < lt):
		res += tab[i]
		i += 1
	return res	

def enleverPoint(s) :
	i = 0
	res = ""
	while (s[i] != '.'):
		res += s[i]
		i += 1
	return res

def floatString(s) :
	lt = len(s)
	i = 0
	flag = 0
	res = ""
	count = 0
	while (i <lt):
		if (s[i] == '.'):
			flag = 1
			i += 1
		if (flag == 1):
			count += 1

		res += s[i]	
		i += 1

	if (count == 0):
		res += '0'
		count = 1	

	i = 0
	w = 1
	while (i < count):
		w = w*10
		i += 1	
	res = int(res) / w	
	return res



entre = input("Entrez un nombre : ")
entre = floatString(entre)
res = arrondir(entre)
res = enleverPoint(res)
print(res)