
# Project_Name = Grade Caluclator

'''
These project invoves in  taking input from the users 
student_name  and marks_obtained fron student
and caluclating Percentage by using total marks and 
assigning Grades based thier percentage
'''


#letter Grade Boot
pointpossible=100  # Maximun Score that student can scored
Total_Marks=625    # Total Marks     
studentname=input("enter the student name  :")                   
Marks_obtained=int(input("enter the marks obtained by student :"))  # Marks obtained by student
score=((Marks_obtained/Total_Marks)*100)                        #Converting Marks to Percentage

"""
A=100-90%    
B=89-80%
C=79-70%
D=69-60%
F=59-0%
    """
# Print the student name and grade they got based on percentage they obtained

if 100 >= score >= 90:
    print(f"{studentname} Obtained {Marks_obtained} Marks and his grade is -A")
elif 89 >= score >= 80:
    print(f"{studentname} Obtained {Marks_obtained} Marks and his grade is -B")
elif 79 >= score >= 70:
    print(f"{studentname} Obtained {Marks_obtained} Marks and his grade is -C")
elif 69 >= score >= 60:
    print(f"{studentname} Obtained {Marks_obtained} Marks and his grade is -D")
else:
    print(f"{studentname} Obtained {Marks_obtained} Marks and his grade is -F")
    
    