#!/usr/bin/python3
# Hex Ecoding
# R&D ICWR - Afrizal F.A

import sys
from os.path import isfile

class hexa:

    def hex_encode(self, data):

        string = ''

        for x in data:

            string += "\\x" + x.encode().hex()

        return string

    def hex_decode(self, data):

        return data

    def __init__(self):

        if len(sys.argv) > 2:

            if sys.argv[1] == "e" and isfile(sys.argv[2]):

                str_result = self.hex_encode(open(sys.argv[2], "r").read())
                print(str_result)
                f = open(sys.argv[2] + ".hex", "w")
                f.write(str_result)
                f.close()

            elif sys.argv[1] == "e":

                print(self.hex_encode(sys.argv[2]))

            elif sys.argv[1] == "d" and isfile(sys.argv[2]):

                str_result = self.hex_decode(open(sys.argv[2], "r").read())
                print(str_result)
                f = open(sys.argv[2] + ".unhex", "w")
                f.write(str_result)
                f.close()

            elif sys.argv[1] == "d":

                print(self.hex_decode(sys.argv[2]))

if __name__ == "__main__":

    hexa()
