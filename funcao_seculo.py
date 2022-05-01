def seculo (periodo):
    if ano >= 1 and ano <= 100:
        return ('I')
    elif ano >= 101 and ano <= 200:
        return ('II')
    elif ano >= 201 and ano <= 300:
        return ('III')
    elif ano >= 301 and ano <= 400:
        return ('IV')
    elif ano >= 401 and ano <= 500:
        return ('V')
    elif ano >= 501 and ano <= 600:
        return ('VI')
    elif ano >= 601 and ano <= 700:
        return ('VII')
    elif ano >= 701 and ano <= 800:
        return ('VIII')
    elif ano >= 801 and ano <= 900:
        return ('IX')
    elif ano >= 901 and ano <= 1000:
        return ('X')
    elif ano >= 1001 and ano <= 1100:
        return ('XI')
    elif ano >= 1101 and ano <= 1200:
        return ('XII')
    elif ano >= 1201 and ano <= 1300:
        return ('XIII')
    elif ano >= 1301 and ano <= 1400:
        return ('XIV')
    elif ano >= 1401 and ano <= 1500:
        return ('XV')
    elif ano >= 1501 and ano <= 1600:
        return ('XVI')
    elif ano >= 1601 and ano <= 1700:
        return ('XVII')
    elif ano >= 1701 and ano <= 1800:
        return ('XVIII')
    elif ano >= 1801 and ano <= 1900:
        return ('IXX')
    elif ano >= 1901 and ano <= 2000:
        return ('XX')
    elif ano >= 2000 and ano <= 2101:
        return ('XXI')
    else:
        print('Ano inválido.')


ano = int(input('Digite o ano: '))
sec = seculo(ano)
print(f'O ano de {ano}, pertence ao século {sec}')

