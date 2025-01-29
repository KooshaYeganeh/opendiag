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
from websocket import create_connection


print("""




 ▗▄▖ ▗▄▄▖ ▗▄▄▄▖▗▖  ▗▖▗▄▄▄ ▗▄▄▄▖ ▗▄▖  ▗▄▄▖
▐▌ ▐▌▐▌ ▐▌▐▌   ▐▛▚▖▐▌▐▌  █  █  ▐▌ ▐▌▐▌
▐▌ ▐▌▐▛▀▘ ▐▛▀▀▘▐▌ ▝▜▌▐▌  █  █  ▐▛▀▜▌▐▌▝▜▌
▝▚▄▞▘▐▌   ▐▙▄▄▖▐▌  ▐▌▐▙▄▄▀▗▄█▄▖▐▌ ▐▌▝▚▄▞▘




      """)


init(autoreset=True)

class OBD2Tool:
    def __init__(self):
        self.connection = None
        self.data = pd.DataFrame(columns=['timestamp', 'o2_voltage', 'rpm'])
        self.setup_connection()

    def setup_connection(self):
        """Attempt to establish the OBD-II connection, with enhanced error handling."""
        try:
            self.connection = obd.OBD("/dev/ttyACM0")  # Initialize OBD connection
            if not self.connection.is_connected():
                raise ConnectionError("No OBD-II adapters found. Please check your connection.")
            print(Fore.LIGHTGREEN_EX + "OBD-II connection established successfully.")
        except ConnectionError as e:
            print(Fore.LIGHTRED_EX + f"Connection Error: {e}")
            self.connection = None
        except Exception as e:
            print(Fore.LIGHTRED_EX + f"Unexpected Error: {e}")
            self.connection = None

    def check_dtc(self):
        """Check for diagnostic trouble codes (DTCs) with enhanced error handling."""
        if not self.connection or not self.connection.is_connected():
            print(Fore.LIGHTRED_EX + "OBD-II connection is not established.")
            return

        try:
            dtc_response = self.connection.query(obd.commands.GET_DTC)
            if dtc_response.is_null():
                print(Fore.LIGHTGREEN_EX + "> No Trouble Code Detected [OK]")
            else:
                dtcs = dtc_response.value
                if dtcs:
                    print("> Diagnostic Trouble Codes (DTCs):")
                    for dtc in dtcs:
                        print(Fore.LIGHTRED_EX + f"{dtc}")
                else:
                    print(Fore.LIGHTGREEN_EX + "> No DTCs detected.")
        except obd.OBDException as e:
            print(Fore.LIGHTRED_EX + f"OBD Command Error: {e}")
        except Exception as e:
            print(Fore.LIGHTRED_EX + f"Unexpected Error: {e}")

    def display_parameters(self):
        """Display available OBD-II parameters with enhanced error handling."""
        if not self.connection or not self.connection.is_connected():
            print(Fore.LIGHTRED_EX + "OBD-II connection is not established.")
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

        try:
            for command in commands:
                response = self.connection.query(command)
                if not response.is_null():
                    print(Fore.LIGHTGREEN_EX + f"{command.name}: {response.value}")
                else:
                    print(Fore.LIGHTYELLOW_EX + f"{command.name}: No data")
        except obd.OBDException as e:
            print(Fore.LIGHTRED_EX + f"OBD Command Error: {e}")
        except Exception as e:
            print(Fore.LIGHTRED_EX + f"Unexpected Error: {e}")

    def clear_dtc(self):
        """Send the command to clear Diagnostic Trouble Codes (DTCs)."""
        if not self.connection or not self.connection.is_connected():
            print(Fore.LIGHTRED_EX + "OBD-II connection is not established.")
            return

        try:
            print(Fore.CYAN + "Attempting to clear DTCs...")

            # Send the command to clear the DTCs
            clear_response = self.connection.query(obd.commands.CLEAR_DTC)

            if clear_response.is_null():
                print(Fore.LIGHTRED_EX + "Failed to clear DTCs. The ECU did not respond properly.")
            else:
                print(Fore.LIGHTGREEN_EX + "DTCs cleared successfully.")
        except obd.OBDException as e:
            print(Fore.LIGHTRED_EX + f"OBD Command Error: {e}")
        except Exception as e:
            print(Fore.LIGHTRED_EX + f"Unexpected Error: {e}")

    # Other existing methods like display_parameters, start_obd_plotting, etc.

    def start_obd_plotting(self):
        """Start real-time plotting of OBD-II data with enhanced error handling."""
        if not self.connection or not self.connection.is_connected():
            print(Fore.LIGHTRED_EX + "OBD-II connection is not established.")
            return

        timestamps = []
        o2_values = []
        rev_values = []

        plt.ion()  # Turn on interactive mode for real-time plotting

        try:
            while True:
                # Query OBD-II adapter for Oxygen Sensor data (PID 0x24)
                o2_command = obd.commands.O2_B1S1
                o2_response = self.connection.query(o2_command)
                o2_voltage = o2_response.value.magnitude if o2_response.value else 0

                # Query OBD-II adapter for Engine RPM data (PID 0x0C)
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
            print(Fore.LIGHTYELLOW_EX + "\nStopping oscilloscope plotting.")
        except Exception as e:
            print(Fore.LIGHTRED_EX + f"Error during OBD-II data plotting: {e}")
        finally:
            self.connection.close()  # Close the connection when done
            print(Fore.LIGHTGREEN_EX + "OBD-II connection closed.")

    def start_can_sniffer(self):
        """Start CAN bus sniffer with enhanced error handling."""
        try:
            bus = can.interface.Bus(channel='can0', bustype='socketcan')
            print(Fore.LIGHTGREEN_EX + "CAN Sniffer started. Press Ctrl+C to exit.")

            while True:
                message = bus.recv(timeout=1.0)
                if message is not None:
                    print(f"Message received on {message.channel}: {message}")

        except OSError as e:
            print(Fore.LIGHTRED_EX + f"OS error: {e}")
        except KeyboardInterrupt:
            print(Fore.LIGHTYELLOW_EX + "\nExiting CAN Sniffer.")
        except Exception as e:
            print(Fore.LIGHTRED_EX + f"Unexpected error in CAN Sniffer: {e}")
        finally:
            if bus is not None:
                bus.shutdown()

    def websocket_communication(self):
        """Start WebSocket communication with enhanced error handling."""
        try:
            ws = create_connection("ws://your-websocket-server-url")
            print(Fore.LIGHTGREEN_EX + "WebSocket connection established.")

            while True:
                result = ws.recv()
                print(f"Received WebSocket message: {result}")

        except Exception as e:
            print(Fore.LIGHTRED_EX + f"WebSocket communication error: {e}")
        finally:
            ws.close()
            print(Fore.LIGHTGREEN_EX + "WebSocket connection closed.")

def main():
    if len(sys.argv) < 2:
        print(Fore.LIGHTRED_EX + "Usage: python opendiag.py <command>")
        sys.exit(1)

    command = sys.argv[1]
    tool = OBD2Tool()

    if command in ["--dtc", "--D"]:
        tool.check_dtc()
    elif command in ["--clear-dtc", "--C"]:
        tool.clear_dtc()  # Add this line to handle the clear DTC command
    elif command in ["--parameters", "-PR"]:
        tool.display_parameters()
    elif command in ["--can-sniffer", "--CS"]:
        tool.start_can_sniffer()
    elif command in ["--oscilloscope", "--O"]:
        tool.start_obd_plotting()
    elif command in ["--websocket", "--WS"]:
        tool.websocket_communication()
    elif command in ["--help", "H"]:
        print(Fore.CYAN + """
Usage:
    --dtc or --D            Check Diagnostic Trouble Codes (DTCs)
    --clear-dtc", --C       Remove Diagnostic Trouble Codes (DTCs)
    --parameters or -PR     Display OBD-II Parameters
    --can-sniffer or --CS   Start CAN Bus Sniffer
    --oscilloscope or --O   Start OBD-II Oscilloscope Plotting
    --websocket or --WS     Start WebSocket Communication
    --help or H             Display this help message
""")

    elif command in ["--info", "I"]:
        print(Fore.CYAN + """
INFO :

➜ ARXML (AUTOSAR XML):
    Used for storing data related to AUTOSAR (Automotive Open System Architecture). It's a standard used in the automotive industry for defining software architecture.
--------------------------------------------------------------
➜ LDF (CAN Database File):
    This is a CAN bus database file format used by Vector CANalyzer and other CAN-related tools. It describes the CAN messages, signals, and their properties.
--------------------------------------------------------------
➜ KCD (CANdb++):
    Another format for CAN database files used by tools like CANalyzer, similar to LDF but with different encoding and support for more complex CAN signals and messages.
--------------------------------------------------------------
➜ FIBEX (Field Bus Exchange Format):
    Another format for defining and exchanging fieldbus (e.g., CAN) network descriptions, used in various industrial and automotive networks.
--------------------------------------------------------------
➜ XLS / XLSX (Microsoft Excel files):
    These are standard file formats for spreadsheets. It appears that your application may have attempted to read/write Excel files.
--------------------------------------------------------------
➜ YAML (YAML Ain't Markup Language):
    A human-readable data serialization standard commonly used for configuration files.
--------------------------------------------------------------
➜ ODX (Open Diagnostic Data Exchange):
    Used in the automotive industry for storing diagnostic information about ECUs (Electronic Control Units) and other devices.

""")


    else:
        print(Fore.LIGHTRED_EX + "> Invalid command. Please check your command and try again.")
        print(Fore.LIGHTRED_EX + "> For more information, use 'python opendiag.py --help'.")

if __name__ == "__main__":
    main()
