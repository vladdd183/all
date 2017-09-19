def quadro():
    import math
    print('Enter new  square sample without  square')
    print('Example, if you want enter 2x²-15x+13, you should enter: 2x-15x+13')
    sample = input('Enter new sample: ')
    s2 = sample.split('x')
    a = int(s2[0])
    b = int(s2[1])
    c = int(s2[2])
    D = (b ** 2) - (4*a*c)
    print('discriminant is ' + str(D))
    if D < 0:
        print('No roots')
    else:
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)
        print('Roots of this pattern is:')
        print('x1 = ' + str(x1))
        print('x2 = ' + str(x2))
