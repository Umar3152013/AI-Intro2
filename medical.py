medical_cause=input("did you have a medical cause Y or N: ")
atten = int(input("enter the attendence of the student:"))

if medical_cause == 'Y':
    print ("You are sllowed")
else:
    if atten>=75:
        print("allowed")
    else:
        print("Not allowed")
