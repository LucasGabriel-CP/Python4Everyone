def add_time(start: str, duration: str, *day):
    Ans = ''
    
    Temp1 = start.split()
    Temp = Temp1[0].split(':')
    if Temp1[1] == 'PM' and Temp[0] != '12':
        Ori = 12
    else:
        Ori = 0
    Ori += int(Temp[0])
    Totm = int(Temp[1])
    
    Temp = duration.split(':')
    Add = int(Temp[0])
    Toth = int(Ori + Add)
    Totm = (Totm + int(Temp[1]))
    if Totm >= 60:
        Totm %= 60
        Toth += 1
    ND = ''
    if Toth >= 24:
        if Toth < 48:
            ND = ' (next day)'
        else:
            ND = ' (' + str(int(Toth / 24)) + ' days later)'
    Tip = ''
    Aux = Toth
    Toth = Toth % 24
    if Toth > 11:
        if Toth > 12:
            Toth = Toth - 12
        Tip = ' PM'
    else:
        Tip = ' AM'
    if not Toth:
        Ans = '12'
    else:
        Ans = str(Toth)
    if Totm < 10:
        Ans += ':0' + str(Totm) + Tip
    else:
        Ans += ':' + str(Totm) + Tip

    if day:
        DD = day[0].lower()
        Dic = dict()
        Dic = {'sunday' : 0, 'monday' : 1, 'tuesday' : 2, 'wednesday' : 3, 'thursday' : 4, 'friday' : 5,'saturday' : 6}
        D = Dic[DD]
        Dic = {0 : 'Sunday', 1 : 'Monday', 2 : 'Tuesday', 3 : 'Wednesday', 4 : 'Thursday', 5 : 'Friday', 6 : 'Saturday'}
        D += int(Aux / 24)
        Ans += ', ' + Dic[D % 7]
    return Ans + ND