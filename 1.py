#!/usr/bin/env cims_python
import random
import string

def main():
    for _ in range(5):
        print _
    length = random.randrange(5,20)
    print length
    chars = string.ascii_lowercase + string.digits
    print chars
    name = ''.join(random.choice(chars) for x in range(length))
    print name

    a = 'TTCN-LLV+LSV-SSR-SIM'
    #a.replace(',', '+')
    print '1------------------'
    print a.replace(',', '+')
        
if __name__ == "__main__":
    main()

