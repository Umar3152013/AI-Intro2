print("Enter grades in 4 subjects:")
math=int(input("math: "))
english=int(input("english: "))
science=int(input("science: "))
history=int(input("history: "))

sum= math+english+science+history
print("sum of math, english, science and history")

perc = (sum/400)*100

print(end="Percentage Mark = ")
print(perc)