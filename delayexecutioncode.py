# Delaying Execution Code

def countdown(value):
    import time
    for i in range(value, -1, -1):
        if i != 0:
            print('%d'%i, end='')
            time.sleep(1)
            continue
        print('Go!!!')

print(countdown(10))

'''
sleep(1) will delay 1 second every single execution
'''
