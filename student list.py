#Enter 4 names into a list,
#Enter scores for exam,
#Create report.
#input is always string

print ('List of Student Names\n')
student_names=[]
exam_scores=[]
student_address=[]
#populating data
for i in range(5):
    name=input ("Enter a student name: ")
    student_names.append(name)
    scores=(float (input ("Enter a student grade: ")))
    exam_scores.append(scores)
    address=(input("Enter the student address: "))
    student_address.append(address)
print ('List of students with their grade:\n')
#printing report of data list
for j in range (5):
    print (student_names[j],exam_scores[j],student_address[j])
print ('all done')
