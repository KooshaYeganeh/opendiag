import os
import sys
import obd
import parameters
import dtc
import help
from colorama import Fore, Back, Style



print(Fore.LIGHTGREEN_EX + """

            ██╗  ██╗██╗   ██╗ ██████╗ ███╗   ██╗██╗   ██╗███████╗
            ██║ ██╔╝╚██╗ ██╔╝██╔════╝ ████╗  ██║██║   ██║██╔════╝
            █████╔╝  ╚████╔╝ ██║  ███╗██╔██╗ ██║██║   ██║███████╗
            ██╔═██╗   ╚██╔╝  ██║   ██║██║╚██╗██║██║   ██║╚════██║
            ██║  ██╗   ██║   ╚██████╔╝██║ ╚████║╚██████╔╝███████║
            ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚══════╝

             ██████╗ ██████╗ ███████╗███╗   ██╗██████╗ ██╗ █████╗  ██████╗
            ██╔═══██╗██╔══██╗██╔════╝████╗  ██║██╔══██╗██║██╔══██╗██╔════╝
            ██║   ██║██████╔╝█████╗  ██╔██╗ ██║██║  ██║██║███████║██║  ███╗
            ██║   ██║██╔═══╝ ██╔══╝  ██║╚██╗██║██║  ██║██║██╔══██║██║   ██║
            ╚██████╔╝██║     ███████╗██║ ╚████║██████╔╝██║██║  ██║╚██████╔╝
             ╚═════╝ ╚═╝     ╚══════╝╚═╝  ╚═══╝╚═════╝ ╚═╝╚═╝  ╚═╝ ╚═════╝



      """)




if sys.argv[0] == "opendiag.py":
    if sys.argv[1] == "--dtc" or sys.argv[1] == "--D":
        dtc.check_dtc()
    elif sys.argv[1] == "--parameters" or sys.argv[1] == "-PR":
        parameters.para()
    elif sys.argv[1] == "--help" or sys.argv[1] == "-H":
        help.manual()
    else:
        print(Fore.LIGHTGREEN_EX + "> check command and Try Again" + Fore.RESET)
        print(Fore. LIGHTRED_EX + "> For More Informatin check DTC command info or command opendiag --help" + Fore.RESET)

