import obd
import os
import sys



def para():

    connection = obd.OBD()

    # Check if the connection is established
    if connection.is_connected():
        print("Connected to the OBD-II Module")
    else:
        print("Connection to the OBD-II Module failed.")
        exit()

    # Read specific OBD-II parameters
    ## This Scope get oparameters of Car Like Engine RPM and CoolantTemp and Some More
    ## TODO : add More Parameters From Parameters Table
    rpm_response = connection.query(obd.commands.RPM)
    speed_response = connection.query(obd.commands.SPEED)
    coolant_temp_response = connection.query(obd.commands.COOLANT_TEMP)

    if not rpm_response.is_null():
        print("RPM:", rpm_response.value)
    if not speed_response.is_null():
        print("Speed:", speed_response.value)
    if not coolant_temp_response.is_null():
        print("Coolant Temperature:", coolant_temp_response.value)

    return "check Parameters Done"
