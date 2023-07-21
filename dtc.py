import obd


def check_dtc():
    dtc_response = connection.query(obd.commands.GET_DTC)
    if not dtc_response.is_null():
        dtcs = dtc_response.value
        if dtcs:
            print("Diagnostic Trouble Codes (DTCs):")
            for dtc in dtcs:
                print(dtc)
                return "Touble Coded Listed [ Done ]"
        else:
            return "No Value Detected For DTCs"
    else:
        return "No Trouble code Detected [ OK ]"
        


