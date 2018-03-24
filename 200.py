str=input('Enter your String:')
print(''.join([j for i,j in enumerate(str) if j not in str[:i]]))
