
#UDP checksum
def checksum(data):
    sum = 0
    for i in range(0, len(data), 2):
        if i + 1 < len(data):
            w = (data[i] << 8) + (data[i + 1])
        else:
            w = (data[i] << 8)
        sum = sum + w
    sum = (sum >> 16) + (sum & 0xffff)
    sum = ~sum & 0xffff #取反
    return sum

data = input("Enter data: ").replace("\n", "")
data = bytearray(data, 'utf-8')
print(data)
checksum_result = checksum(data)
print(checksum_result)