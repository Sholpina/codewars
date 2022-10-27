def solution(to_cur,values):
    if to_cur == "USD":
        values = list(map (lambda x: x*1.1398734654, values))
        values = ['${:,.2f}'.format(item) for item in values]
        return values
    elif to_cur == "EUR":
        values = list(map (lambda x: x/1.13987124, values))
        values = ['{:,.2f}€'.format(item) for item in values]
        return values
    else:
        return None