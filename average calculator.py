grades=[]
while True:
    try:
        num=int(input("Enter number of the student :"))
        if num>0:
            break
        else:
            print(" number of the student must be bigger than 0 !! ")
    except:
         print("Enter an integer number ")
    
for i in range(num):
    while True:

        try:
            grd=float(input(f"Enter grade of student {i+1} :"))
            if grd >=0 and grd <=20:
                    break
            else:
                    print("  please Enter a float number [0, 20] ")
        except:
            print("Enter a float  number ")
    grades.append(grd)

sum_s=0
for g in grades:
    
    sum_s=sum_s +g
    
avg = sum_s/len(grades)
print(f"List of Grades is : {grades}")

print(f"your avarages is {avg}")








        


