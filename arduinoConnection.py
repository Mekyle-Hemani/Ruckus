import serial
import serial.tools.list_ports

def senddata(data, rate=9600, debug=1):
    ports = serial.tools.list_ports.comports()
    comports = []
    for port in ports:
        comports.append(port.device)

    if (len(comports) == 0):
        if (debug == 1):
            print("Please ensure that the Ruckus Controller is connected")
        return False

    else:
        port = comports[0]
        try:
            ser = serial.Serial(port, baudrate=rate, timeout=1)
            if (debug == 1):
                print(f"Connected to {port}")

            ser.write(f"{data}\n".encode('utf-8'))

            if (debug == 1):
                print(f"Sent '{data}' succesfully")

            #response = ser.readline().decode('utf-8').strip()

            return True

        except serial.SerialException as e:
            if (debug == 1):
                print(f"Failed to connect to {port}: {e}")
            return False
        except KeyboardInterrupt:
            if (debug == 1):
                print("Stopping communication...")
            return False
        finally:
            if ser.is_open:
                ser.close()

if __name__ == "__main__":
    print(senddata("hi", 9600))