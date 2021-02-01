def card_conv(x,r):
    d = ''
    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUWXYZ'

    while x > 0:
        d += dchar[x % r]
        x //= r
    return d[::-1]