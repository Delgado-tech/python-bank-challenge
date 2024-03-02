def parse_int(value: any, exceptReturn: int = 0):
    try:
        return int(value)
    except:
        return exceptReturn