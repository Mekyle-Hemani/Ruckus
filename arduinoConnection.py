import serial
import serial.tools.list_ports
import time

def senddata(data, rate=9600, debug=0):
    ports = serial.tools.list_ports.comports()
    comports = [port.device for port in ports]

    if not comports:
        if debug == 1:
            print("Please ensure that the Arduino is connected")
        return False

    port = comports[0]
    try:
        ser = serial.Serial(port, baudrate=rate, timeout=1)
        time.sleep(2)

        if debug == 1:
            print(f"Connected to {port}")

        ser.write(data.encode('utf-8'))

        if debug == 1:
            print(f"Sent '{data}' successfully")
            #print(ser.readline().decode('utf-8').strip())

        return True

    except serial.SerialException as e:
        if debug == 1:
            print(f"Failed to connect to {port}: {e}")
        return False
    except KeyboardInterrupt:
        if debug == 1:
            print("Stopping communication...")
        return False
    finally:
        if ser.is_open:
            ser.close()

if __name__ == "__main__":
    print(senddata("123456", 9600))