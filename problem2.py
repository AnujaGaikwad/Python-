math = float(input("Enter Percentage of mathematics: "))
eng = float(input("Enter Percentage of english: "))
sci = float(input("Enter Percentage of science: "))

# Check for total percentage
total = (100*(math + eng + sci))/300

if(total>=40 and math>=33 and eng>=33 and sci>=33):
    print("Student is passed in exam", total)

else:
    print("Student is failed in exam", total)