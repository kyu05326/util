import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file_name")
parser.add_argument("start_line_no")
parser.add_argument("length")
args = parser.parse_args()

#print args
#sys.exit()

row_no = 0

file_name = args.file_name
start_line_no = int(args.start_line_no)
length = int(args.length)

print ("file_name=", file_name)
print ("start_line_no=", start_line_no)
print ("len=", length)

fileobj = open(file_name, "r")
while True:
  line = fileobj.readline()
  if line:
    row_no += 1
    if row_no > start_line_no :
        break

  else:
    break

row_no = 0
while True:
    line = fileobj.readline()
    if line:
        row_no += 1
        if row_no>length :
            break
        print (line.rstrip('\n'))
            
    else:
       break

    