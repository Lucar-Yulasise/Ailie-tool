import Crypto

def testPass(cryptPass):
	salt = cryptPass[0:2]

	dictFile = open('dictionary.txt','r')

	for word in dictFile.readlines():
		word = word.strip('\n')
		crpytWord = crtypt.crypt(word,salt)
		if crpytWord == cryptPass:
			print('[+] Found Passworld: ' + word+"\n")
			return 
	print('[-] Passworld not Found.\n')
	return

def main():
	passFile = open('passwords.txt')
	for line in passFile.readlines():
		if ":" in line:
			user = line.split(':')[0]
			cryptPass = line.split(':')[1].split(' ')
			print('[*] Cracking Password For :' + user)
			testPass(cryptPass)
if __name__ == '__main__':
	main()