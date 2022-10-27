def solution(to_cur,values):
    if to_cur == "USD":
        values = list(map (lambda x: x*1.1364445, values))
        values = ['${:,.2f}'.format(item) for item in values]
        return values
    elif to_cur == "EUR":
        values = list(map (lambda x: x/1.137874, values))
        values = ['{:,.2f}€'.format(item) for item in values]
        return values
    else:
        return None