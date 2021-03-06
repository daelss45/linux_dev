#!/usr/bin/env python
# Author: Dael Saint-Surin
# Date: 03-28-2018
# Purpose: To get the memory used for a specific user.
import os
import sys
def script_usage():
    if len(sys.argv) != 2:
        print '\n'
        print '*' * 10
        print 'Script incorrect usage'
        print 'Usage:', sys.argv[0], 'user_name'
        print 'Exmaple:', sys.argv[0], 'wms'
        print '*' * 10
        print '\n'
        exit()

def script_run():
    total = 0
    M = 1024.0
    G = M * 1024.0
    user = sys.argv[1]
    PS = "ps ww -eo user,rssize,cmd | egrep -i ^" + user + " | awk '{print $2}' | egrep -vi [a-z]"
    total = 0
    ALL_PROCESS = os.popen(PS).read()
    ALL_PROCESS = ALL_PROCESS.split()

    for mem in ALL_PROCESS:
      total = total + float(mem)
    print 'Total Memory used in KB:', total
    print 'Total Memroy used in MB:', total / M
    print 'Total Memroy used in GB:', total / G

def main():
    script_usage()
    script_run()

if __name__ == '__main__':
    main()
