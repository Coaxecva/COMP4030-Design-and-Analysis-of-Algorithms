from PyPDF2 import PdfFileWriter, PdfFileReader
import sys

fi = sys.argv[1]
n = sys.argv[2]

input1 = PdfFileReader(open(fi,"rb"))
pageNum = input1.getNumPages()
print("Title: %s" % (input1.getDocumentInfo().title))
print("has %s pages." % pageNum)

i = 0
while i < (pageNum):
	output = PdfFileWriter()
	for j in range(int(n)):
		output.addPage(input1.getPage(i+j))		
	i+=int(n)
	newname = str(i) + ".pdf"
	outputStream = open(newname, "wb")
	output.write(outputStream)
	outputStream.close()
	print("%s" %str(i))

print("Done.")