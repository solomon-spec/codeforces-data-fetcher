array = []
while True:
    try:
        ip,port,user,pas = input().split(':')

        array.append(f'{user}:{pas}@{ip}:{port}')
        # array.append(input())
    except:
        break
print(array)