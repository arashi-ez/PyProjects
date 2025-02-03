weight = int(input('Weight: '))
measure = input('(L)bs or (K)g: ')
measure = measure.lower()

if measure == 'l':
    result = weight/2.20462
    print(f'You are ~{round(result)} kgs')
elif measure == 'k':
    result = weight*2.20462
    print(f'You are ~{round(result)} lbs')
else:
    print('error k or l')