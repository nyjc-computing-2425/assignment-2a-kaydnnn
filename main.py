num = input('Enter a number (decimal or integer): ')
# type your code here
tmp = num
tmp = tmp.strip(" ")
tmp = tmp.replace(".", "")
tmp = tmp.lstrip("0")

sf = len(tmp)
# do not change any code beyond this point
print('The number', num, 'has', sf, 'significant figures.')
