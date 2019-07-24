from employee import Employee

lst_emp = []

def load_emp():
    with open("empdata.txt")as f:
        fdata=f.readlines()
        for data in fdata:
            edata=data.strip("\n").split(",")
            empno=int(edata[0])
            ename=edata[1]
            qualification=edata[2]
            salary=edata[3]
            dept_name=edata[4]
            emp=Employee(empno,ename,qualification,salary,dept_name)
            lst_emp.append(emp)
    print(f"Total employee count: {len(lst_emp)}")

def showDeptNames():
    dnames=set(map(lambda emp:emp.dept_name,lst_emp))
    for name in dnames:
        print(name)
        

def ShowQualification():
    qualifications = set(map(lambda emp:emp.qualification,lst_emp))
    for qualification in qualifications:
        print(qualification)

def maxSalaryEmp():
    max_sal=max(list(map(lambda x:x.salary,lst_emp)))
    lst = list(filter(lambda x:x.salary ==max_sal,lst_emp))
    for emp in lst:
        emp.show_info()

def showEmpCountByDeptName():
    pass

def ShowTotalSalByDeptName():
    pass
    
load_emp()
showDeptNames()
ShowQualification()
maxSalaryEmp()

















"""emp_1= Employee(1,"Sunny","Mtech",56000,"CS")
emp_2= Employee(2,"Bunny","Mtech",46000,"IS")

emp_1.show_info()
emp_2.show_info()
emp_1.inc_salary(2000)
emp_1.show_info()
emp_2.show_info()"""