import serial.tools.list_ports


def put_choose_list(put_list):
    for i in range(len(put_list)):
        print('[{}] {}'.format(i, put_list[i]))


def choose_port():
    portx = None
    can_used_serial_port = list()
    port_list = list(serial.tools.list_ports.comports())
    for i in range(len(port_list)):
        port = port_list[i]
        if (port.pid == 0x7523
                and port.vid == 0x1A86) or (port.pid == 60000
                                            and port.vid == 0x10C4):
            can_used_serial_port.append(port)

    if len(can_used_serial_port) == 1:
        portx = can_used_serial_port[0].device
    elif len(can_used_serial_port) > 1:
        put_choose_list(can_used_serial_port)
        index = input('请选择串口：')
        portx = can_used_serial_port[int(index)].device
    else:
        Exception('未发现可用串口！')
    return portx


if __name__ == '__main__':
    print(choose_port())
