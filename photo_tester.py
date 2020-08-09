import os
import imghdr

def test_imghdr(filename):
 
    try:
        fd = open(filename, 'rb').read()
        return (imghdr.what(None, fd) == 'jpeg')
    except:
        return False

try:
	os.makedirs("valid/")
except FileExistsError:
	pass
try:
	os.makedirs("not_valid/")
except FileExistsError:
	pass


mode=input("Do you want print valid/not valid photos? y/n\n")
save_mode=input("Do you want delete not valid photos? y/n\n")

files=os.listdir()
for i in range(len(files)):
	if not test_imghdr(files[i]):# and i>2:
		try:
			if mode=="y":
				print(files[i]+" not valid")
			if save_mode=="n":
				os.rename("photos/"+files[i],"photos/not_valid/"+files[i])
			else:
				os.remove("photos/"+files[i])
		except:
			pass
	elif test_imghdr(files[i]):# and i>2:
		try:
			if mode=="y":# and i>2:
				print(files[i]+" valid")
			os.rename("photos/"+files[i],"photos/valid/"+files[i])
		except:
			pass