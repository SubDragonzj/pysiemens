import siemens
import S7

client = siemens.S7Client()
client.ConnectTo('10.1.2.69', 0, 2)
Buffer = bytearray(84)
client.DBRead(1, 0, 84, Buffer)
print(Buffer)
print(S7.GetDIntAt(Buffer, 2))
print(S7.GetTODAt(Buffer, 76))
print(S7.GetDateAt(Buffer, 70))
print(S7.GetDateTimeAt(Buffer, 58))
tosend = bytearray(2)
S7.SetIntAt(tosend, 0, 12000)
client.DBWrite(1, 0, len(tosend), tosend)

tosend = bytearray(4)
S7.SetDIntAt(tosend, 0, 12000000)
client.DBWrite(1, 2, len(tosend), tosend)
tosend = bytearray(1)
S7.SetBitAt(tosend, 0, 0, False)
client.DBWrite(1, 30, len(tosend), tosend)
tosend = bytearray(4)
S7.SetFloatAt(tosend, 0, 12342342423421.123)
client.DBWrite(1, 66, 4, tosend)

infos = client.GetAgBlockInfo(BlockType=client.Block_DB, BlockNum=1)
print(infos)

order_code = client.GetOrderCode()
print(order_code)

cpu_info = client.GetCpuInfo()
print(cpu_info)

cp_info = client.GetCpInfo()
print(cp_info)

# client.PlcStop()
# print("Stopped")
# client.PlcColdStart()
# print("HotStart")

print(client.GetPlcStatus())