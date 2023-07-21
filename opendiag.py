import os
import sys
import obd
import parameters
import dtc



if sys.argv[0] == "opendiag.py":
    if sys.argv[1] == "--dtc" or sys.argv[1] == "--D":
        dtc.check_dtc()
    elif sys.argv[1] == "--parameters" or sys.argv[1] == "-PR":
        parameters.para()
    else:
        print("check command and Try Again")
        print("For More Informatin check DTC command info or command opendiag --help")

