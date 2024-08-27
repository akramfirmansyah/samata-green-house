import serial
import serial.tools.list_ports


def scanport():
    portList = list(serial.tools.list_ports.comports())

    for port in portList:
        if (
            "VID:PID=2341:0034" in port[0]
            or "VID:PID=2341:0034" in port[1]
            or "VID:PID=2341:0034" in port[2]
        ):
            return port[0]


portDevice = scanport()

ser = serial.Serial(port=portDevice, baudrate=115200)
