#Import library
import sys, getopt
def main(argv):
   argument = ''
   usage = 'usage: myscript.py --text <sometext>'
   # parse incoming arguments
   try:
      opts, args = getopt.getopt(argv,"ht:",["text="])
   except getopt.GetoptError:
      print(usage)
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print(usage)
         sys.exit()
      elif opt in ("--text"):
         argument = arg
   print(argument)
if __name__ == "__main__":
    main(sys.argv[1:])