with open('cv.html', encoding='latin1') as f:
    line = f.read()
    _0x02 = '<div class="css-1dbjc4n r-1wbh5a2 r-dnmrzs r-1ny4l3l"><div class="css-1dbjc4n r-1wbh5a2 r-dnmrzs"><a href="'
    _0x03 = len(_0x02)
    _0x01 = None
    while _0x01 != -1:
        _0x01 = line.find(_0x02)
        line = line[_0x01 + _0x03 : ]
        _0x04 = line.find('"')
        user = line[ : _0x04]
        print(user)