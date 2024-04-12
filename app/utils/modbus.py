from pymodbus.client.sync import ModbusTcpClient


def send_command(host, port, command, speed=None, slave=1):
    client = ModbusTcpClient(host, int(port))
    if not client.connect():
        return False, "Нет соединения с устройством"

    res = None
    if speed is not None:
        speed = speed * 50
        print(f"Set speed is {speed}")
        res = client.write_registers(12288, [speed], unit=slave)
    if res and res.isError():
        print("Ошибка записи частоты")
        #client.close()
        #raise HTTPException(status_code=404)

    if command == "forward":
        res = client.write_registers(8192, [1], unit=slave)
    elif command == "stop":
        res = client.write_registers(8192, [5], unit=slave)

    if res and res.isError():
        print("Ошибка записи команды")
        #client.close()
        #raise HTTPException(status_code=404)

    client.close()
    return True, ""


def get_status(host, port, slave=1):
    client = ModbusTcpClient(host, int(port))
    if not client.connect():
        return False, "Нет соединения с устройством"

    res = None
    # чтение состояния и ошибок ЧП
    res = client.read_holding_registers(24576, 3, unit=slave)
    # чтение целевой и текущей частоты частоты
    res = client.read_holding_registers(4352, 2, unit=slave)

    client.close()
    return True, ""
