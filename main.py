name=input("enter your name:")
marks=list(map(int,input("enter your marks:").split()))
avg=sum(marks)/len(marks)
if avg>=90:
    grade="A"
elif avg>=80:
    grade="B"
elif avg>=70:
    grade="C"
elif avg>=60:
    grade="D"
elif avg>=50:
    grade="fail"
if avg>=50:
    status="pass"
else:
    status="fail"      
 #final output
print("Name:",name)
print("Avg:",avg)
print("grade:",grade)
print("status:",status)                  
