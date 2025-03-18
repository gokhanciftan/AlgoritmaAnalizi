def power(taban, us):
    if us == 0:
        return 1
    elif us % 2 == 0:
        yarim = power(taban, us // 2)
        return yarim * yarim
    else:
        return taban * power(taban, us - 1)

# Test
print(power(2, 10))
