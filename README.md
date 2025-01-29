# OBD-II Diagnostic Tool 🚗🔧

Welcome to the **OBD-II Diagnostic Tool**! This powerful Python-based tool allows you to interface with your vehicle's OBD-II system, perform diagnostics, and visualize data. It supports a variety of functionalities including CAN bus sniffing, WebSocket communication, and data plotting.

![OBD-II Diagnostic Tool](https://img.shields.io/badge/OBD--II--Diagnostic--Tool-v1.0-blue)

## Features 🌟

- **Diagnostic Trouble Codes (DTC)**: Retrieve and clear DTCs.
- **OBD-II Parameters**: Display real-time vehicle parameters like RPM, speed, and coolant temperature.
- **CAN Bus Sniffer**: Monitor CAN bus traffic.
- **OBD Oscilloscope**: Plot real-time data for in-depth analysis.
- **WebSocket Communication**: Connect and communicate with WebSocket servers.

## Installation 🛠️

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/obd2-diagnostic-tool.git
   cd obd2-diagnostic-tool
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
### Get Executable File in Linux

```
pyinstaller opendiag.py --onefile -n opendiag && rm opendiag.spec && rm -rvf build && cp dist/opendiag . && rm -rvf dist
```

In Linux Device Name is : /dev/ttyACM0

```
ls /dev/tty* | grep "ACM"
```

```
ls -l /dev/ttyACM0
```

```
sudo usermod -aG dialout $USER
```

```
crw-rw---- 1 root dialout 166, 0 Jan 29 14:12 /dev/ttyACM0
```

**You can USE this Tools to Communicate with ELM327**

obd-II library (Python): Great for programmatically interacting with the ECU.<br/>
can-utils: Useful for low-level CAN bus communication and raw CAN frame handling.<br/>
ELM327 command-line tool: Provides simple command-line interaction with the ELM327 adapter.<br/>
PyOBD: Another Python library alternative.<br/>
miniscan: A minimalistic tool for sending simple OBD-II commands.<br/>
Termite: For manual interaction via a serial terminal.<br/>


## Usage 📋

To use the tool, run the script with the appropriate command. Available commands include:

```sh
python opendiag.py <command>
```

### Commands

- `--dtc` or `--D` 🎛️: Check Diagnostic Trouble Codes (DTCs)
- `--parameters` or `-PR` 📊: Display OBD-II Parameters
- `--can-sniffer` or `--CS` 🕵️: Start CAN Bus Sniffer
- `--oscilloscope` or `--O` 📈: Start OBD-II Oscilloscope Plotting
- `--websocket` or `--WS` 🌐: Start WebSocket Communication
- `--help` or `H` ❓: Display help message

### Example Usage

Retrieve DTCs:
```sh
python opendiag.py --dtc
```

Start CAN bus sniffing:
```sh
python opendiag.py --can-sniffer
```

## Dependencies 📦

- **numpy**: Numerical operations.
- **pandas**: Data manipulation and analysis.
- **matplotlib**: Plotting and visualization.
- **seaborn**: Statistical data visualization.
- **pydatalog**: Logical programming and queries.
- **python-can**: CAN bus interface.
- **canmatrix**: CAN matrix manipulation.
- **websocket-client**: WebSocket communication.
- **colorama**: Terminal color formatting.
- **obd**: OBD-II interface.

## Configuration ⚙️

- **CAN Interface**: Ensure that your CAN interface is correctly configured and connected.
- **WebSocket URL**: Update the WebSocket URL in the `websocket_communication` method.

## Contributing 🤝

We welcome contributions! If you have suggestions, bug fixes, or new features, please fork the repository and create a pull request.

## License 📜

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact 📧

For any questions or support, please reach out to [kooshakooshadv@gmail.com](mailto:your.email@example.com).
[http://kooshateganeh.github.io](website)
