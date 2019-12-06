# Standard library
import sys

# modules
from bs4 import BeautifulSoup

args = sys.argv
if len(args) > 1:
    try:
        for a_file in args[1:]:
            with open(a_file, 'r') as f:
                soup = BeautifulSoup(f, "html5lib")

            docs = soup.body.text

            doclist = docs.split(sep='\n')

            while '' in doclist:
                doclist.remove('')

            doc = '\n'.join(doclist)

            with open(a_file + ".txt", 'w') as f:
                f.write(doc)
            
    except FileNotFoundError as e:
        print(e)
        sys.exit(1)
else:
    print("args is empty.")
