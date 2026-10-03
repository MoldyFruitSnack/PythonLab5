def is_valid_part(part):
    try:
        i_part = int(part)
        if part[0] == '0' and not i_part == 0:return False
        return 0 <= i_part < 256
    except ValueError as ve:
        return False

def is_valid_ip(ip:str):
    parts = ip.split('.')
    if len(parts) !=4: return False
    for part in parts:
        if not is_valid_part(part):return False
    return True

# print(is_valid_part('127'),is_valid_part('AAA'),is_valid_part('257'),is_valid_part('-255'),is_valid_part('01'),is_valid_part('0'), )


print(is_valid_ip('192.168.0.1'))

print(is_valid_ip("192.168.1.1"))  # True
print(is_valid_ip("192.168.256.1"))  # False
print(is_valid_ip("192.168.1"))  # False
print(is_valid_ip("192.168.01.1"))  # False


def decimal_to_binary(n):
    if n == 0: return '0'
    if n == 1: return '1'
    next, digit = divmod(n, 2)
    return (decimal_to_binary(next)) + str(digit)

def binary_to_decimal(b):
    if b == '': return 0
    place = len(b) - 1
    return 2**place * int(b[0]) + binary_to_decimal(b.removeprefix(b[0]))


print(decimal_to_binary(10))

# Test cases
print(decimal_to_binary(10))   # "1010"
print(decimal_to_binary(255))  # "11111111"
print(decimal_to_binary(1))    # "1"

print(binary_to_decimal("1010"))      # 10
print(binary_to_decimal("11111111"))  # 255
print(binary_to_decimal("1"))         # 1
