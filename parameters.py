import obd
import os
import sys
from colorama import Fore, Back, Style


def para():

    connection = obd.OBD()

    # Check if the connection is established
    if connection.is_connected():
        print(Fore.LIGHTGREEN_EX + "> Connected to the OBD-II Module")
    else:
        print(Fore.LIGHTRED_EX + "> Connection to the OBD-II Module failed. [ ERROR ]")
        exit()

    # Read specific OBD-II parameters
    ## This Scope get oparameters of Car Like Engine RPM and CoolantTemp and Some More
    ## TODO : add More Parameters From Parameters Table
    rpm_response = connection.query(obd.commands.RPM)
    speed_response = connection.query(obd.commands.SPEED)
    coolant_temp_response = connection.query(obd.commands.COOLANT_TEMP)
    
    engine_load_response = connection.query(obd.commands.ENGINE_LOAD)
    fuel_pressure_response = connection.query(obd.commands.FUEL_PRESSURE)
    intake_response = connection.query(obd.commands.INTAKE_PRESSURE)
    timing_advance_response = connection.query(obd.commands.TIMING_ADVANCE)
    intake_temp_response = connection.query(obd.commands.INTAKE_TEMP)
    maf_response = connection.query(obd.commands.MAF)
    throttle_postion_response = connection.query(obd.commands.THROTTLE_POS)
    # Oxygen sensor Parameters
    o2b1s1_response = connection.query(obd.commands.O2_B1S1)
    o2b1s2_response = connection.query(obd.commands.O2_B1S2)
    o2b1s3_response = connection.query(obd.commands.O2_B1S3)
    o2b1s4_response = connection.query(obd.commands.O2_B1S4)
    o2b2s1_response = connection.query(obd.commands.O2_B2S1)
    o2b2s2_response = connection.query(obd.commands.O2_B2S2)
    o2b2s3_response = connection.query(obd.commands.O2_B2S3)
    o2b2s4_response = connection.query(obd.commands.O2_B2S4)
    
    dictance_response = connection.query(obd.commands.DISTANCE_W_MIL)
    fuel_rail_pressure_vac_response = connection.query(obd.commands.FUEL_RAIL_PRESSURE_VAC)
    fuel_rail_pressure_direct_response = connection.query(obd.commands.FUEL_RAIL_PRESSURE_DIRECT)
    
    egr_response = connection.query(obd.commands.COMMANDED_EGR)
    barometric_pressure_response = connection.query(obd.commands.BAROMETRIC_PRESSURE)
    absolute_load_response = connection.query(obd.commands.ABSOLUTE_LOAD)
    
    trottle_actuator_response = connection.query(obd.commands.THROTTLE_ACTUATOR)
    max_maf_response = connection.query(obd.commands.MAX_MAF)
    fuel_inject_timing_response = connection.query(obd.commands.FUEL_INJECT_TIMING)
    fuel_rate_response = connection.query(obd.commands.FUEL_RATE)

    if not rpm_response.is_null():
        print(Fore.LIGHTGREEN_EX + "> RPM:", rpm_response.value)
    if not speed_response.is_null():
        print(Fore.LIGHTGREEN_EX + "> Speed:", speed_response.value)
    if not coolant_temp_response.is_null():
        print(Fore.LIGHTGREEN_EX + "> Coolant Temperature:", coolant_temp_response.value)

    if not fuel_rate_response.is_null():
        print(Fore.LIGHTGREEN_EX + "> Fuel Rate:", fuel_rate_response.value)
    if not fuel_inject_timing_response.is_null():
        print(Fore.LIGHTGREEN_EX + "> Fuel Injection Timing:", fuel_inject_timing_response.value)
    if not max_maf_response.is_null():
        print(Fore.LIGHTGREEN_EX + "> Max Maf:", max_maf_response.value)



    if not trottle_actuator_response.is_null():
        print(Fore.LIGHTGREEN_EX + "> Trottle Actuator Response:", trottle_actuator_response.value)
    if not barometric_pressure_response.is_null():
        print(Fore.LIGHTGREEN_EX + "> Barometric Pressure Response:", barometric_pressure_response.value)
    if not egr_response.is_null():
        print(Fore.LIGHTGREEN_EX + "> EGR Response:", egr_response.value)




    if not absolute_load_response.is_null():
        print(Fore.LIGHTGREEN_EX + "> Absolute Load:", absolute_load_response.value)
    if not fuel_rail_pressure_direct_response.is_null():
        print(Fore.LIGHTGREEN_EX + "> Fuel Rail Pressure Direct:", fuel_rail_pressure_direct_response.value)
    if not fuel_rail_pressure_vac_response.is_null():
        print(Fore.LIGHTGREEN_EX + "> Fuel Rail Pressure Vac:", fuel_rail_pressure_vac_response.value)

    if not dictance_response.is_null():
        print(Fore.LIGHTGREEN_EX + "> Distance :", dictance_response.value)
    if not throttle_postion_response.is_null():
        print(Fore.LIGHTGREEN_EX + "> Throttle Position :", throttle_postion_response.value)
    if not maf_response.is_null():
        print(Fore.LIGHTGREEN_EX + "> Maf Response :", maf_response.value)



    if not o2b1s1_response.is_null():
        print(Fore.LIGHTGREEN_EX + "> O2B1S1:", o2b1s1_response.value)
    if not o2b1s2_response.is_null():
        print(Fore.LIGHTGREEN_EX + "> O2B1S2:", o2b1s2_response.value)
    if not o2b1s3_response.is_null():
        print(Fore.LIGHTGREEN_EX + "> O2B1S3:", o2b1s3_response.value)
    if not o2b1s4_response.is_null():
        print(Fore.LIGHTGREEN_EX + "> O2B1S4:", o2b1s4_response.value)
    if not o2b2s1_response.is_null():
        print(Fore.LIGHTGREEN_EX + "> O2B2S1:", o2b2s1_response.value)
    if not o2b2s2_response.is_null():
        print(Fore.LIGHTGREEN_EX + "> O2B2S2:", o2b2s2_response.value)
    if not o2b2s3_response.is_null():
        print(Fore.LIGHTGREEN_EX + "> O2B2S3:", o2b2s3_response.value)
    if not o2b2s4_response.is_null():
        print(Fore.LIGHTGREEN_EX + "> O2B2S4:", o2b2s4_response.value)



    if not intake_temp_response.is_null():
        print(Fore.LIGHTGREEN_EX + "> Intake Temp:", intake_temp_response.value)
    if not engine_load_response.is_null():
        print(Fore.LIGHTGREEN_EX + "> Engine Load:", engine_load_response.value)
    if not fuel_pressure_response.is_null():
        print(Fore.LIGHTGREEN_EX + "> Fuel Pressure:", fuel_pressure_response.value)
    if not intake_response.is_null():
        print(Fore.LIGHTGREEN_EX + "> Intake Response:", intake_response.value)
    if not timing_advance_response.is_null():
        print(Fore.LIGHTGREEN_EX + "> Timing Advance:", timing_advance_response.value)

    return ( Fore.RESET + "Check Parameters Done")
