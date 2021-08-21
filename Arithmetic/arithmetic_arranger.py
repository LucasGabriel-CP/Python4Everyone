def arithmetic_arranger(problems, *arg):
    if len(problems) > 5:
        return 'Error: Too many problems.'
    Ans1 = list()
    Ans2 = list()
    Dashes = list()
    Result = list()
    Maior = None
    for case in problems:
        Conta = case.split()
        if Conta[1] != '-' and Conta[1] != '+':
            return "Error: Operator must be '+' or '-'."
        try:
            First = int(Conta[0])
            Second = int(Conta[2])
        except:
            return 'Error: Numbers must only contain digits.'
        if First > 9999 or Second > 9999:
            return 'Error: Numbers cannot be more than four digits.'
        if First > Second:
            Maior = Conta[0]
            Aux = '  ' + Maior
            Ans1.append(Aux)
            Aux = Conta[1] + ' '
            i = len(Maior) - len(Conta[2])
            Dash = '--'
            while i:
                Aux += ' '
                i -= 1
            Aux += Conta[2]
            Ans2.append(Aux)
        else:
            Maior = Conta[2]
            Aux = Conta[1] + ' ' + Maior
            Ans2.append(Aux)
            Aux = '  '
            i = len(Maior) - len(Conta[0])
            Dash = '--'
            while i > 0:
                Aux += ' '
                i -= 1
            Aux += Conta[0]
            Ans1.append(Aux)
        i = len(Maior)
        while i:
            Dash += '-'
            i -= 1
        Dashes.append(Dash)
        if arg:
            if Conta[1] == '+':
                Aux = str(First + Second)
            else:
                Aux = str(First - Second)
            Space = ''
            if len(Aux) < len(Maior) + 2:
                i = 0
                while i < len(Maior) + 2 - len(Aux):
                    Space += ' '
                    i += 1
            else:
                Space = ' '
            Result.append(Space + Aux)
    Ans = ''
    i = 0
    while i < len(Ans1) - 1:
        Ans += Ans1[i] + '    '
        i += 1
    Ans += Ans1[i] + '\n'
    i = 0
    while i < len(Ans2) - 1:
        Ans += Ans2[i] + '    '
        i += 1
    Ans += Ans2[i] + '\n'
    i = 0
    while i < len(Dashes) - 1:
        Ans += Dashes[i] + '    '
        i += 1
    if arg:
        Ans += Dashes[i] + '\n'
        i = 0
        while i < len(Result) - 1:
            Ans += Result[i] + '    '
            i += 1
        Ans += Result[i]
    else:
        Ans += Dashes[i]
    return Ans