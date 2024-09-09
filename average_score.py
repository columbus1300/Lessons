grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
ss = sorted(students)
#ss - sorted students
sas0=('%.1f'%(float(sum(grades[0])/float(len(grades[0])))))
sas1=('%.1f'%(float(sum(grades[1])/float(len(grades[1])))))
sas2=('%.1f'%(float(sum(grades[2])/float(len(grades[2])))))
sas3=('%.1f'%(float(sum(grades[3])/float(len(grades[3])))))
sas4=('%.1f'%(float(sum(grades[4])/float(len(grades[4])))))
#sas0,1,2,3,4 - sorted average score
average_score = {ss[0]:sas0, ss[1]:sas1, ss[2]:sas2, ss[3]:sas3, ss[4]:sas4}
print(average_score)