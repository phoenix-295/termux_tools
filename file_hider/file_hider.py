import json
import os
from functions import load_key, encrypt_data, decrypt_data
import binascii

db_file = "new_db.json"

def getTopFiles(folderName):
		files = []
		for item in os.listdir(folderName):
				item_path = os.path.join(folderName, item)
				if os.path.isfile(item_path):
						files.append(item)
		return files

def getAllFiles(folderName):
	files = []
	for root, dirs, filenames in os.walk(folderName):
		for filename in filenames:
			file_path = os.path.join(root, filename)
			files.append(file_path)
	return files

def writeDB(folderName, folderPath):
		with open(db_file, "r") as json_file:
			data = json.load(json_file)
		encryptionLevel = input("Is folder top level encrypted or fully encrypted? F/T/N   ")
		if str.lower(encryptionLevel) == "f":
			data[folderName] = [folderPath, "F"]
		elif str.lower(encryptionLevel) == "t":
			data[folderName] = [folderPath, "T"]
		elif str.lower(encryptionLevel) == "n":
			data[folderName] = [folderPath, "N"]
		else:
			print("Please try again")
			return

		with open(db_file, "w") as json_file:
				json.dump(data, json_file, indent=4)

def readDB():
		with open(db_file, "r") as json_file:
				data = json.load(json_file)
		i = 0
		for key in data:
				i += 1
				print(f"{i}: \t{key} \t\t {data[key][0]} \t {data[key][1]}")
		return data

def removeFolder():
		data = readDB()
		folderName = input("Enter number: ")
		i = 0
		folderToRemove = ""
		for key in data:
				i += 1
				if i == int(folderName):
						folderToRemove = key

		data.pop(folderToRemove, None)

		with open(db_file, "w") as json_file:
				json.dump(data, json_file, indent=4)

def encryptFolder():
	secret_key = load_key()
	data = readDB()
	if len(data) == 0:
		print("Add records in DB")
		return
	folderName = input("Enter number: ")
	i = 0
	fname = "" # key
	folderToHide = "" # Value
	for key in data:
		i += 1
		if i == int(folderName):
			folderToHide = data[key]
			fname = key
	
	if folderToHide[1] != "N":
		if folderToHide[1] == "T":
			txt = "top level"
		elif folderToHide[1] == "F":
			txt = "fully"
		else:
			print("Error")
			return
		print(f"Folder is {txt} encrypted, please decrypt")
		return

	fullFolder = input("Encrypt full folder? (Y/N)")
	fullFolder = str.lower(fullFolder)
	if fullFolder == "y":
		files = getAllFiles(folderName=folderToHide[0])
		for file in files:
			folder, ext = os.path.splitext(file)
			fileName = file.split("\\")[-1]
			# encryptedFileName = encrypt_data(data=fileName, key=key)
			encryptedFileName = binascii.hexlify(encrypt_data(data=fileName, key=secret_key)).decode("utf-8")
			os.rename(file, f"{os.path.dirname(folder)}/{encryptedFileName}")
		data[fname] = [folderToHide[0], "F"]
		with open(db_file, "w") as json_file:
			json.dump(data, json_file, indent=4)

	else:
		files = getTopFiles(folderName=folderToHide[0])
		for file in files:
			fileToHide =  f"{folderToHide[0]}/{file}"
			encryptedFileName =  binascii.hexlify(encrypt_data(data=file, key=secret_key)).decode("utf-8")
			fileToEncrypted = f"{folderToHide[0]}/{encryptedFileName}"
			os.rename(fileToHide, fileToEncrypted)
		data[fname] = [folderToHide[0], "T"]
		with open(db_file, "w") as json_file:
			json.dump(data, json_file, indent=4)

def decryptFolder():
	secret_key = load_key()
	data = readDB()
	folderNumber = input("Enter number: ")
	i = 0
	fname = "" # key
	folderToDecrypt = "" # Value
	for key in data:
			i += 1
			if i == int(folderNumber):
					folderToDecrypt = data[key]
					fname = key

	fullFolder = input("Decrypt full folder? (Y/N) ")
	fullFolder = str.lower(fullFolder)
	if fullFolder == "y":
		if folderToDecrypt[1] != "F":
			if folderToDecrypt[1] == "T":
				txt = "top level"
			elif folderToDecrypt[1] == "N":
				txt = "not"
			else:
				print("Error")
			print(f"Folder is {txt} encrypted, please decrypt")
			return
		files = getAllFiles(folderName=folderToDecrypt[0])
		for file in files:
			folder, ext = os.path.splitext(file)
			fileName = file.split("\\")[-1]
			# decrypt(binascii.unhexlify(str_enc), key)
			# decryptedFileName = decrypt_data(data=fileName, key=secret_key)
			decryptedFileName = decrypt_data(data=binascii.unhexlify(fileName), key=secret_key)
			os.rename(file, f"{os.path.dirname(folder)}/{decryptedFileName}")
		data[fname] = [folderToDecrypt[0], "N"]
		with open(db_file, "w") as json_file:
			json.dump(data, json_file, indent=4)
	elif fullFolder == "n":
		if folderToDecrypt[1] != "T":
			if folderToDecrypt[1] == "F":
				txt = "fully"
			elif folderToDecrypt[1] == "N":
				txt = "not"
			else:
				print("Error")
			print(f"Folder is {txt} encrypted, please decrypt")
			return
		files = getAllFiles(folderName=folderToDecrypt[0])

		files = getTopFiles(folderName=folderToDecrypt[0])
		for file in files:
			fileToDecrypt = f"{folderToDecrypt[0]}/{file}"
			# decrypt(binascii.unhexlify(str_enc), key)
			# decryptedFileName = decrypt_data(data=file, key=secret_key)
			decryptedFileName = decrypt_data(data=binascii.unhexlify(file), key=secret_key)
			fileDecrypted = f"{folderToDecrypt[0]}/{decryptedFileName}"
			os.rename(fileToDecrypt, fileDecrypted)
		data[fname] = [folderToDecrypt[0], "N"]
		with open(db_file, "w") as json_file:
			json.dump(data, json_file, indent=4)

def main():
		startMsg = '''
1: Add folder to DB
2: Show folders from DB
3: Remove folders from DB
4: Encrypt a folder
5: Decrypt Folder   '''
		choice = input(startMsg)
		print()
		if int(choice) == 1:
				folderName = input("Enter folder name: ")
				folderPath = input("Enter folder path: ")
				writeDB(folderName=folderName, folderPath=folderPath)
		elif int(choice) == 2:
				readDB()
		elif int(choice) == 3:
				removeFolder()
		elif int(choice) == 4:
				encryptFolder()
		elif int(choice) == 5:
				decryptFolder()
		else:
				print("Wrong choide, exiting")

if __name__ == "__main__":
	main()