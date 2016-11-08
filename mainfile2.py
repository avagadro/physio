print('Enter the Cipher that you want to use:\n')
print('1.ROT13\n2.Substitution\n3.Transposition\n4.Vernam\n5.Double Transposition\n6.Deffie Hellman')
choice=input()

if choice==1:
    import ROT13 as file
if choice==2:
    import substitutiontry as file
if choice==3:
    import transposition as file
if choice==4:
    import vernam as file
if choice==5:
    import doubletransposition as file
if choice==6:
    import deffiehellman as file

file.main()
