def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def inequalities():
    import math
    print('Enter new inequalities')
    print('Dexrip')
    sample = input('Enter new inequalities')
    s2 = sample.split(' ')
    print(s2)
    for i in range(0, len(s2)):
        if isint(s2[i]):
            s2[i] = int(s2[i])
            print(str(s2[i]) + ' Now is int')
        else:
            print(s2[i] + ' OKEY')
    s2[4] += s2[2]
    print(s2)
