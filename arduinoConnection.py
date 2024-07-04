import serial
import serial.tools.list_ports

def senddata(data, rate=9600):
    ports = serial.tools.list_ports.comports()
    comports = []
    for port in ports:
        comports.append(port.device)

    port = comports[0]

    if (len(comports) == 0):
        print("Please ensure that the Ruckus Controller is connected")

    else:
        port = comports[0]
        try:
            ser = serial.Serial(port, baudrate=rate, timeout=1)
            print(f"Connected to {port}")

            while True:
                ser.write(f"{data}\n".encode('utf-8'))

            ser.write(f"{data}\n".encode('utf-8'))

            #response = ser.readline().decode('utf-8').strip()

        except serial.SerialException as e:
            print(f"Failed to connect to {port}: {e}")
            senddata(data, rate=rate)
        except KeyboardInterrupt:
            print("Stopping communication...")
        finally:
            if ser.is_open:
                ser.close()

if __name__ == "__main__":
    senddata("", 9600)