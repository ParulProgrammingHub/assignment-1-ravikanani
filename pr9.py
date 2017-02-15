a=input("enter maximum marks for a subject: ")
total_marks=a*5.0
sub1=input("enter marks of subject 1: ")
sub2=input("enter marks of subject 2: ")
sub3=input("enter marks of subject 3: ")
sub4=input("enter marks of subject 4: ")
sub5=input("enter marks of subject 5: ")
obtain_marks=sub1+sub2+sub3+sub4+sub5
avg_marks=obtain_marks/5.0
percent=(obtain_marks*100)/total_marks
print "average is :",avg_marks
print "percentage is :",percent
if percent<35:
    print "FAIL"
else:
    print "PASS"
