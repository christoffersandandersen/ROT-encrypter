encrypt = raw_input("Enter 1 to encrypt and 0 to decrypt: ")
try:
	encrypt = int(encrypt)
except:
	print("Error: Invalid input")
	exit(-1)
data = raw_input("Enter data to process: ")
data = data.lower() # ensuring the string is in all lowercase, in my case this is fine since i do not need excact decryption

def encrypt_rot(rot, data):
	enc_data = list()
	j = 0
	for i in data:
		var = ((ord(i) - 97) + rot) % 26
		char = chr(var + 97)
		enc_data.append(char)
	string = ''.join(enc_data)
	print(string)

def decrypt_rot(rot, data):
	enc_data = list()
	j = 0
	for i in data:
		if i == '/' or i == ' ' or i == ',':
			enc_data.append(i) 
			continue
		var = ((ord(i) - 97) - rot) % 26
		char = chr(var + 97)
		enc_data.append(char)
	string = ''.join(enc_data)
	print(string)


if encrypt == 1:
	encrypt_rot(13, data)
elif encrypt == 0:
	decrypt_rot(13, data)


# in order to generate the invite code, make a post request to /api/invite/generate