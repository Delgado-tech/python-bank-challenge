def parse_float(value: any, exceptReturn: float = 0.0):
    try:
        return float(value)
    except:
        return exceptReturn