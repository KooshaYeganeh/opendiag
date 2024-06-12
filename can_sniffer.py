# can_sniffer.py
import can

def start_can_sniffer():
    bus = None  # Define bus in the outer scope

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

