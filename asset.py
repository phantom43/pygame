import os
lvkekuatan = 0
proses = 0
tenaga = 100
lemak = 40
uang = 5
bgcolor = '\u001b[43m'
fcolor = '\u001b[37m'
def main():
	os.system('clear')
	print('status:')
	print('lv = ', lvkekuatan,'\ntenaga = ', tenaga,'\nlemak = ', lemak)
	print("*"*40)
	print('proses')
	loadp()
	print("*"*40)
	print('apakah anda ingin latihan(y/n/s)')
	pil = input('#>')
	if pil == 'y':
		workout()
	elif pil == 's':
		shop()
def workout():
	global tenaga,proses
	for i in range(1, 11):
		print('workout ke', i)
		os.system('sleep 1')
		os.system('clear')
		if i == 10:
			tenaga -= 20
			proses += 1
			print('result:\n tenaga -20\n proses +10')
			input('enter!')
			main()
	if tenaga <= 40:
		print('Anda terlalu lelah untuk latihan')
		input('Enter!')
		main()
def loadp():
	global proses
	loadb = '#'*proses
	print(loadb)
def shop():
	global uang
	global tenaga
	global buy
	m1 = 15
	m2 = 2
	m3 = 1
	m4 = 2
	m5 = 10
	m6 = 5
	os.system('clear')
	print(' Kasir : Selamat datang di toko panini mau beli apa?')
	input('enter!')
	print("""
+***************************************+
*       barang       *       harga      *
+***************************************+
* [1] Energi Drink   *         15       *
* [2] Jajan          *         2        *
* [3] Somay          *         1        *
* [4] Gorengan       *         2        *
* [5] Nasi Kuning    *         10       *
* [6] Air Mineral    *         5        *
+***************************************+
""")
	print(' $ : ', uang)
	try:
		buy = int(input('buy#> '))
	except Exception as e:
		print('masukan angka saja!!!')
		input('Enter jika anda mengerti')
		main()
	if buy == 1:
		if uang == m1 or uang >=m1:
			uang -= m1
			tenaga += 20
			print('berhasil membeli!!')
			input('enter')
			main()
		else:
			print('uang lu g cukup bambang')
			input('enter')
			shop()
	elif buy == 2: 
		if uang == m2 or uang >=m2:
			uang -= m2
			tenaga += 4
			print('berhasil membeli!!')
			input('enter')
			main()
		else:
			print('uang lu g cukup bambang')
			input('enter')
			shop()
	elif buy == 3:
		if uang == m3 or uang >=m3:
			uang -= m3
			tenaga += 2
			print('berhasil membeli!!')
			input('enter')
			main()
		else:
			print('uang lu g cukup bambang')
			input('enter')
			shop()
	elif buy == 4:
		if uang == m4 or uang >=m4:
			uang -= m4
			tenaga += 4
			print('berhasil membeli!!')
			input('enter')
			main()
		else:
			print('uang lu g cukup bambang')
			input('enter')
			shop()
	elif buy == 5:
		if uang == m5 or uang >=m5:
			uang -= m5
			tenaga += 14
			print('berhasil membeli!!')
			input('enter')
			main()
		else:
			print('uang lu g cukup bambang')
			input('enter')
			shop()
	elif buy == 6:
		if uang == m6 or uang >=m6:
			uang -= m6
			tenaga += 8
			print('berhasil membeli!!')
			input('enter')
			main()
		else:
			print('uang lu g cukup bambang')
			input('enter')
			shop()
	else:
		print('Masukan input dengan benar!!!')
		input('Enter!')
		main()
def kerja():
	print('coming-soon')