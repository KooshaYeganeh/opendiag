# oscilloscope.py
import obd
import time
import matplotlib.pyplot as plt

class OBD2Oscilloscope:
    def __init__(self):
        try:
            self.connection = obd.OBD()  # Initialize the OBD connection
            if not self.connection.is_connected():
                raise Exception("No OBD-II adapters found")
        except Exception as e:
            print(f"Error initializing OBD-II connection: {e}")
            self.connection = None

    def plot_obd_data(self):
        if not self.connection or not self.connection.is_connected():
            print("OBD-II connection is not established.")
            return

        timestamps = []
        o2_values = []
        rev_values = []

        plt.ion()  # Turn on interactive mode for real-time plotting

        while True:
            try:
                # Query OBD2 adapter for Oxygen Sensor data (PID 0x24)
                # Verify the correct command for oxygen sensor voltage
                o2_command = obd.commands.O2_B1S1  # Example command for Bank 1 Sensor 1
                o2_response = self.connection.query(o2_command)
                o2_voltage = o2_response.value.magnitude if o2_response.value else 0

                # Query OBD2 adapter for Engine RPM data (PID 0x0C)
                rev_response = self.connection.query(obd.commands.RPM)
                rpm = rev_response.value.magnitude if rev_response.value else 0

                timestamp = time.time()  # Get current timestamp
                timestamps.append(timestamp)
                o2_values.append(o2_voltage)
                rev_values.append(rpm)

                # Plot the data
                plt.clf()
                plt.subplot(2, 1, 1)
                plt.plot(timestamps, o2_values, color='blue')
                plt.xlabel('Time')
                plt.ylabel('O2 Voltage')
                plt.title('Oxygen Sensor Voltage')

                plt.subplot(2, 1, 2)
                plt.plot(timestamps, rev_values, color='red')
                plt.xlabel('Time')
                plt.ylabel('RPM')
                plt.title('Engine RPM')

                plt.tight_layout()
                plt.draw()
                plt.pause(0.05)  # Pause to allow time for the plot to update
            except KeyboardInterrupt:
                print("\nStopping oscilloscope plotting.")
                break
            except Exception as e:
                print(f"An error occurred while querying OBD-II data: {e}")
                break

        self.connection.close()  # Close the connection when done
        print("OBD-II connection closed.")

# Create a function to instantiate and start plotting
def start_obd_plotting():
    try:
        plotter = OBD2Oscilloscope()
        plotter.plot_obd_data()
    except Exception as e:
        print(f"An error occurred while starting OBD plotting: {e}")

