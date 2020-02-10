#!/usr/bin/python
import sys, getopt

basicTuple = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')

def main(argv):
    inputfile = ''
    outputfile = ''
    try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
      print ('test.py -i <inputfile> -o <outputfile>')
      sys.exit(2)
    for opt, arg in opts:
      if opt == '-h':
         print ('test.py -i <inputfile> -o <outputfile>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg

    f2 = open(outputfile, "w")
    
    with open(inputfile) as f:
        while True:
            c = f.read(1)
            
            if not c:
              break
            
            if c.isalpha():
                c = c.upper()
                f2.write(basicTuple[basicTuple.index(c) - 3])
            else:
                f2.write(c)
                
    f2.close()

if __name__ == "__main__":
   main(sys.argv[1:])
    


    
    

