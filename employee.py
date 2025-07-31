class employee:
    def __init__(self):
        print('Employee created')

    def __init__(self):
        print("Destructor called")
def Create_obj():
    print('Making Object...')
    obj = employee()
    print('function end...')
    return obj

print('Calling Create_obj() function...')
obj = Create_obj
print('Program End...')
