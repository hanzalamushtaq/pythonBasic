#Question 15: Student Result Privacy
#Ek dictionary banayein (name, roll_no, marks). 
#Result hide karne ke liye .pop() method use kar ke
#dictionary se marks remove karein aur updated data dikhayein.

studentinfo={"name":"Ali","rollNo":"1234","marks":45}
studentinfo.pop("marks")
print(studentinfo)