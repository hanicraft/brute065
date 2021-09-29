import PyPDF2
import time
import sys
print("pdf cracker made by hani")
last_time = time.time()
wordlist = open('passwords.txt')
#num_lines = sum(1 for line in open('passwords.txt'))
pdf = PyPDF2.PdfFileReader(open('lock1.pdf','rb'))
if not pdf.isEncrypted:
    print('No password')
else:
    for line in wordlist.readlines():
        if pdf.decrypt(line.rstrip()) :
            print('[+] PASSWORD: ' +line)
            print('Time taken is: ' + str(time.time()-last_time) + ' Second')
            sys.exit()
    print('[-] Password not found')
