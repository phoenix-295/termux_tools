from Crypto.Cipher import AES
from Crypto.Util import Padding
from Crypto.Util.Padding import pad, unpad
import base64
import urllib.parse

BLOCKSIZE = 16

def load_key():
	return open("secret.key", "rb").read()

def encrypt_string(message, key):
	key = str(key).encode("utf-8")
	key = key.ljust(32, b'\0')
	cipher = AES.new(key, AES.MODE_ECB)
	message = message.encode("utf-8")
	message = Padding.pad(message, 16)
	return base64.b64encode(cipher.encrypt(message)).decode("utf-8")

def decrypt_string(ciphertext, key):
	key = str(key).encode("utf-8")
	key = key.ljust(32, b'\0')
	cipher = AES.new(key, AES.MODE_ECB)
	ciphertext = base64.b64decode(ciphertext.encode("utf-8"))
	message = cipher.decrypt(ciphertext)
	message = Padding.unpad(message, 16)
	try:
		return message.decode("utf-8")
	except ValueError:
		return None

# def unpad(data):
# 	return data.rstrip(b'{')

# def padkey(key):
# 	while len(key) % 16 != 0:
# 			key += '{'
# 	return key

# def pad(s):
# 	return s + ((16 - len(s) % 16) * '{')

# def encrypt_data(data, key):
# 	key = padkey(key).encode()
# 	# cipher = AES.new(key, AES.MODE_ECB)
# 	# ciphertext = cipher.encrypt(pad(data).encode())
# 	# # print(urllib.parse.quote(base64.b64encode(ciphertext).decode("utf-8")))
# 	# return urllib.parse.quote(base64.b64encode(ciphertext).decode("utf-8"))

# 	cipher = AES.new(key, AES.MODE_ECB)
# 	ciphertext = cipher.encrypt(pad(data).encode())
# 	encoded_ciphertext = base64.b64encode(ciphertext).decode("utf-8")
# 	return urllib.parse.quote(encoded_ciphertext, safe='{')

# def decrypt_data(data, key):
# 	key = padkey(key).encode()
# 	# cipher = AES.new(key, AES.MODE_ECB)
# 	# ciphertext = base64.b64decode(urllib.parse.unquote(data).encode("utf-8"))
# 	# plaintext = cipher.decrypt(ciphertext)
# 	# return plaintext.rstrip(b'{').decode()

# 	encoded_ciphertext = urllib.parse.unquote(data)
# 	ciphertext = base64.b64decode(encoded_ciphertext)
# 	cipher = AES.new(key, AES.MODE_ECB)
# 	data = cipher.decrypt(ciphertext).rstrip(b'{')
# 	return data.decode("utf-8")

def encrypt_data(data, key):
	key = pad(key, BLOCKSIZE)
	data = bytes(data, 'utf-8')
	cipher = AES.new(key, AES.MODE_ECB)
	ciphertext = cipher.encrypt(pad(data, BLOCKSIZE))
	return ciphertext

def decrypt_data(data, key):
	key = pad(key, BLOCKSIZE)
	decipher = AES.new(key, AES.MODE_ECB)
	msg_dec = decipher.decrypt(data)
	return unpad(msg_dec, BLOCKSIZE).decode("utf-8")