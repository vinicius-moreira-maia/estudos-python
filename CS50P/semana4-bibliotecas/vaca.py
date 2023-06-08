import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.dragon("Oi, " + sys.argv[1])