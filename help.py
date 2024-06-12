import os
import sys


def manual():
    print("=================//OpenDiag//==================")
    print("Free and OpenSource Automotive Diag For Linux")
    print("===============================================")

    print("> opendiag --parameters")
    print("or")
    print("> opendiag -PR")
    print("-----------------------------------------")
    print("> opendiag --dtc")
    print("or")
    print("> opendiag -D")
    print("-----------------------------------------")
    print("> opendiag --oscilloscope")
    print("or")
    print("> opendiag -O")
    print("-----------------------------------------")
    print("> opendiag --help")
    print("or")
    print("> opendiag -H")
    print("-----------------------------------------")
    print("> opendiag --can-sniffer")
    print("or")
    print("> opendiag -CS")
    print("--------------- MAIN USAGE --------------")
    print("python opendiag.py --dtc   # Check DTCs ")
    print("python opendiag.py --parameters   # Retrieve parameters")
    print("python opendiag.py --oscilloscope  # Start the oscilloscope")
    print("python opendiag.py --can-sniffer  # Start the can Sniffer")
    print("python opendiag.py --help   # Display help manual")


    return " "
