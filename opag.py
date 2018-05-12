import base64
import sys
import io

path = sys.argv[1]
output = sys.argv[2]
conversion = "encode"

def convertToBase64 (inputString):
	return base64.b64encode(inputString)


def openFile (filePath):
	try:
		fileContent = open(filePath)
		stringFileContent = str(fileContent)

		return bytearray(stringFileContent, 'ascii')

		fileContent.close()

	except FileNotFoundError:
		print ("Specified file was not found, please specify it as the first parameter")

if (conversion != "decode"):

	asciiText = openFile(path)
	base64Converted = convertToBase64(asciiText)

	print ("Converted OPAG File: " + str(base64Converted))

	resultContent = open(output, 'w')

	resultContent.write(str(base64Converted))