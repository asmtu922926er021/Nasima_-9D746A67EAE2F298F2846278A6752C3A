class student:

  def __init__
  (self,name,roll_number,cgpa):
    self.name=name
    self.roll_number=roll_number
    self.cgpa=cgpa
    
  def sort_student(student_list):

    sorted_students =
sorted (student_list,key=lamda student: student .cpga, reverse = True)

return sorted_students


students =[
  Student ("Hari","A123",7.8),
  Student ("venu","A124",8.9),
  Student ("meenu","A125",5.1),
  Student ("kaviya","A126",9.9),
]
sorted_student =
sort_student(students)
for student in sorted_student: 
  print ("Name:{} ,Roll number:{},CGPA:{}".format(Student.name, Student.roll_ number, student .cpg a))


  



