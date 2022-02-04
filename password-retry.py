password = 'a123456'
i = 0
while i < 3:
	word = input('請輸入密碼:')
	if word == password:
		print('登入成功')
		i = 2
	else:
		print('密碼錯誤，您還有',2 - i ,'次機會')
		if i == 2:
			print('機會用完，您不能再輸入了!')
	i = i + 1

