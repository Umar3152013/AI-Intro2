print("Enter your grades:")
grade1=int(input())
grade2=int(input())
grade3=int(input())
grade4=int(input())
grade5=int(input())

tot = grade1+grade2+grade3+grade4+grade5
avg = tot/5

if avg>=91 and avg<=100:
    print("Your grade is an A")
elif avg>=81 and avg<91:
    print("Your grade is a B")
elif avg>=71 and avg<81:
    print("Your grade is a C")
elif avg>=61 and avg<71:
    print("Your grade is a D")
elif avg>=51 and avg<61:
    print("Your grade is an F")
elif avg>=41 and avg<51:
    print("Your grade is below an F")
elif avg>=31 and avg<41:
    print("Your grade is below an F (talk with your teacher)")
elif avg>=21 and avg<31:
    print("Your grade is below an F (talk with your teacher)")
elif avg>=0 and avg<21:
    print("Your grade is below an F (let your parents talk with your teacher)")
else:
    print("Valid Input")