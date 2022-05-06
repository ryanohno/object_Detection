def printtime():
	import os
	#cmd = 'lp -o fit-to-page /home/pi/image/Test.png'
	cmd = 'lp -o fit-to-page /home/pi/Desktop/current_time.txt'
	os.system(cmd)

printtime()
