# opendiag.py
#!/usr/bin/env python

import sys
import parameters
import help
from colorama import Fore
from dtc import check_dtc  # Import check_dtc from dtc module
from can_sniffer import start_can_sniffer  # Import start_can_sniffer from can_sniffer module
import oscilloscope  # Import oscilloscope module

print(Fore.LIGHTGREEN_EX + """
            ██╗  ██╗██╗   ██╗ ██████╗ ███╗   ██╗██╗   ██╗███████╗
            ██║ ██╔╝╚██╗ ██╔╝██╔════╝ ████╗  ██║██║   ██║██╔════╝
            █████╔╝  ╚████╔╝ ██║  ███╗██╔██╗ ██║██║   ██║███████╗
            ██╔═██╗   ╚██╔╝  ██║   ██║██║╚██╗██║██║   ██║╚════██║
            ██║  ██╗   ██║   ╚██████╔╝██║ ╚████║╚██████╔╝███████║
            ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═══╝╚═════╝ ╚══════╝

             ██████╗ ██████╗ ███████╗███╗   ██╗██████╗ ██╗ █████╗  ██████╗
            ██╔═══██╗██╔══██╗██╔════╝████╗  ██║██╔══██╗██║██╔══██╗██╔════╝
            ██║   ██║██████╔╝█████╗  ██╔██╗ ██║██║  ██║██║███████║██║  ███╗
            ██║   ██║██╔═══╝ ██╔══╝  ██║╚██╗██║██║  ██║██║██╔══██║██║   ██║
            ╚██████╔╝██║     ███████╗██║ ╚████║██████╔╝██║██║  ██║╚██████╔╝
             ╚═════╝ ╚═╝     ╚══════╝╚═╝  ╚═══╝╚═════╝ ╚═╝╚═╝  ╚═╝ ╚═════╝
      """ + Fore.RESET)

def main():
    if len(sys.argv) < 2:
        print("Usage: python opendiag.py <command>")
        sys.exit(1)

    command = sys.argv[1]

    if command == "--dtc" or command == "--D":
        print(check_dtc())
    elif command == "--parameters" or command == "-PR":
        parameters.para()
    elif command == "--can-sniffer" or command == "--CS":
        start_can_sniffer()
    elif command == "--oscilloscope" or command == "--O":
        oscilloscope.start_obd_plotting()
    elif command == "--help" or command == "H":
        help.manual()
    else:
        print(Fore.LIGHTRED_EX + "> Invalid command. Please check your command and try again." + Fore.RESET)
        print(Fore.LIGHTRED_EX + "> For more information, use 'opendiag --help'." + Fore.RESET)

if __name__ == "__main__":
    main()

