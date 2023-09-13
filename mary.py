name = 'Mary'
passwrod = 'password'
print('Name: ')
name = input ()
if name == 'Mary':
    print('Password: ')
    password = input()
    if password == 'password':
        print('Access Granted')
    else:
        print('Access Denied')
else: print('Hello stranger')
