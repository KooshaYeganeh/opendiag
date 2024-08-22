#!/usr/bin/env python

import sys
import time
import numpy as np
import pandas as pd
import obd
import can
import canmatrix
import matplotlib.pyplot as plt
import seaborn as sns
from colorama import Fore
from colorama import init
from pydatalog import pyDatalog
from websocket import create_connection

init(autoreset=True)

class OBD2Tool:
    def __init__(self):
        self.connection = None
        self.setup_connection()
        self.data = pd.DataFrame(columns=['timestamp', 'o2_voltage', 'rpm'])

    def setup_connection(self):
        try:
            self.connection = obd.OBD()
            if not self.connection.is_connected():
                raise Exception("No OBD-II adapters found")
        except Exception as e:
            print(f"Error initializing OBD-II connection: {e}")
            self.connection = None

    def check_dtc(self):
        if not self.connection or not self.connection.is_connected():
            print("OBD-II connection is not established.")
            return

        dtc_response = self.connection.query(obd.commands.GET_DTC)
        if not dtc_response.is_null():
            dtcs = dtc_response.value
            if dtcs:
                print("> Diagnostic Trouble Codes (DTCs):")
                for dtc in dtcs:
                    print(Fore.LIGHTRED_EX + f"{dtc}")
            else:
                print(Fore.LIGHTGREEN_EX + "> No Value Detected For DTCs")
        else:
            print(Fore.LIGHTGREEN_EX + "> No Trouble code Detected [ OK ]")

    def display_parameters(self):
        if not self.connection or not self.connection.is_connected():
            print("OBD-II connection is not established.")
            return

        commands = [
            obd.commands.RPM,
            obd.commands.SPEED,
            obd.commands.COOLANT_TEMP,
            obd.commands.ENGINE_LOAD,
            obd.commands.FUEL_PRESSURE,
            obd.commands.INTAKE_PRESSURE,
            obd.commands.TIMING_ADVANCE,
            obd.commands.INTAKE_TEMP,
            obd.commands.MAF,
            obd.commands.THROTTLE_POS,
            obd.commands.O2_B1S1,
            obd.commands.O2_B1S2,
            obd.commands.O2_B1S3,
            obd.commands.O2_B1S4,
            obd.commands.O2_B2S1,
            obd.commands.O2_B2S2,
            obd.commands.O2_B2S3,
            obd.commands.O2_B2S4,
            obd.commands.DISTANCE_W_MIL,
            obd.commands.FUEL_RAIL_PRESSURE_VAC,
            obd.commands.FUEL_RAIL_PRESSURE_DIRECT,
            obd.commands.COMMANDED_EGR,
            obd.commands.BAROMETRIC_PRESSURE,
            obd.commands.ABSOLUTE_LOAD,
            obd.commands.THROTTLE_ACTUATOR,
            obd.commands.MAX_MAF,
            obd.commands.FUEL_INJECT_TIMING,
            obd.commands.FUEL_RATE
        ]
        
        for command in commands:
            response = self.connection.query(command)
            if not response.is_null():
                print(Fore.LIGHTGREEN_EX + f"{command.name}: {response.value}")

    def start_obd_plotting(self):
        if not self.connection or not self.connection.is_connected():
            print("OBD-II connection is not established.")
            return

        timestamps = []
        o2_values = []
        rev_values = []

        plt.ion()  # Turn on interactive mode for real-time plotting

        try:
            while True:
                # Query OBD2 adapter for Oxygen Sensor data (PID 0x24)
                o2_command = obd.commands.O2_B1S1
                o2_response = self.connection.query(o2_command)
                o2_voltage = o2_response.value.magnitude if o2_response.value else 0

                # Query OBD2 adapter for Engine RPM data (PID 0x0C)
                rev_response = self.connection.query(obd.commands.RPM)
                rpm = rev_response.value.magnitude if rev_response.value else 0

                timestamp = time.time()  # Get current timestamp
                timestamps.append(timestamp)
                o2_values.append(o2_voltage)
                rev_values.append(rpm)

                # Store data in DataFrame
                self.data = pd.DataFrame({
                    'timestamp': timestamps,
                    'o2_voltage': o2_values,
                    'rpm': rev_values
                })

                # Plot the data
                plt.clf()
                plt.subplot(2, 1, 1)
                sns.lineplot(x='timestamp', y='o2_voltage', data=self.data, color='blue')
                plt.xlabel('Time')
                plt.ylabel('O2 Voltage')
                plt.title('Oxygen Sensor Voltage')

                plt.subplot(2, 1, 2)
                sns.lineplot(x='timestamp', y='rpm', data=self.data, color='red')
                plt.xlabel('Time')
                plt.ylabel('RPM')
                plt.title('Engine RPM')

                plt.tight_layout()
                plt.draw()
                plt.pause(0.05)  # Pause to allow time for the plot to update
        except KeyboardInterrupt:
            print("\nStopping oscilloscope plotting.")
        except Exception as e:
            print(f"An error occurred while querying OBD-II data: {e}")
        finally:
            self.connection.close()  # Close the connection when done
            print("OBD-II connection closed.")

    def start_can_sniffer(self):
        try:
            bus = can.interface.Bus(channel='can0', bustype='socketcan')
            print("CAN Sniffer started. Press Ctrl+C to exit.")

            while True:
                message = bus.recv(timeout=1.0)
                if message is not None:
                    print(f"Message received on {message.channel}: {message}")

        except OSError as e:
            print(f"OS error: {e}")
        except KeyboardInterrupt:
            print("\nExiting CAN Sniffer.")
        finally:
            if bus is not None:
                bus.shutdown()

    def websocket_communication(self):
        try:
            ws = create_connection("ws://your-websocket-server-url")
            print("WebSocket connection established.")

            while True:
                result = ws.recv()
                print(f"Received WebSocket message: {result}")

        except Exception as e:
            print(f"WebSocket error: {e}")
        finally:
            ws.close()
            print("WebSocket connection closed.")

def main():
    if len(sys.argv) < 2:
        print("Usage: python opendiag.py <command>")
        sys.exit(1)

    command = sys.argv[1]
    tool = OBD2Tool()

    if command in ["--dtc", "--D"]:
        tool.check_dtc()
    elif command in ["--parameters", "-PR"]:
        tool.display_parameters()
    elif command in ["--can-sniffer", "--CS"]:
        tool.start_can_sniffer()
    elif command in ["--oscilloscope", "--O"]:
        tool.start_obd_plotting()
    elif command in ["--websocket", "--WS"]:
        tool.websocket_communication()
    elif command in ["--help", "H"]:
        print(Fore.LIGHTGREEN_EX + """
Usage:
    --dtc or --D            Check Diagnostic Trouble Codes (DTCs)
    --parameters or -PR     Display OBD-II Parameters
    --can-sniffer or --CS   Start CAN Bus Sniffer
    --oscilloscope or --O   Start OBD-II Oscilloscope Plotting
    --websocket or --WS     Start WebSocket Communication
    --help or H             Display this help message
""")
    else:
        print(Fore.LIGHTRED_EX + "> Invalid command. Please check your command and try again.")
        print(Fore.LIGHTRED_EX + "> For more information, use 'python opendiag.py --help'.")

if __name__ == "__main__":
    main()
