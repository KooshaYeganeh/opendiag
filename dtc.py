import obd
from colorama import Fore, Back, Style

def check_dtc():
    connection = obd.OBD()  # Initialize the OBD connection
    dtc_response = connection.query(obd.commands.GET_DTC)
    if not dtc_response.is_null():
        dtcs = dtc_response.value
        if dtcs:
            print("> Diagnostic Trouble Codes (DTCs):")
            for dtc in dtcs:
                print(Fore.LIGHTRED_EX + f"{dtc}")
                return ( Fore.LIGHTGREEN_EX + "> Touble Coded Listed [ Done ]")
        else:
            return ( Fore.LIGHTGREEN_EX + "> No Value Detected For DTCs")
    else:
        return ( Fore.LIGHTGREEN_EX + "> No Trouble code Detected [ OK ]")
        

 
