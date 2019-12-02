aliens = 2
password = 'ALIENS'

print('Emergency! Aliens attacked our stars!')
print()
print('Start the Earth Defense System!')
print()
print('I hope you know the startup password...')
print()
print('-------------------------------------------------')
print('＊ Welcom to the "Earth Defense System Network ＊"')
print('-------------------------------------------------')

guess = input('＊ Please enter the password. ＊ : ').upper()

while guess != password:
    print()
    print('＊ Incorrect Password. ＊')
    print()
    aliens = aliens ** 2
    print('＊ Currently,', aliens, 'aliens are invading the earth. ＊')
    print('＊ Please enter the Password again. ＊')

    if aliens > 7000000000:
        break
    print()
    print('Password Hint : "Who is attacking us now?"')
    print()
    guess = input('Harry up! enter the Password! : ').upper()

if aliens > 7000000000:
    print()
    print('Oh!oh wow!! The number of aliens exceeded humanity.')
    print('We are losing...')
else:
    print()
    print('＊ Password... OK. ＊')
    print()
    print('The System has started.')
    print()
    print('All right! We won! The earth was saved!')
