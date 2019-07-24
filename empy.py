from q_29 import Employee

lst_emp = []

def load_emp():
    with open("emp.txt") as f:
        fdata = f.readlines()
        for data in fdata:
            edata=data.strip("\n").split(",")
            empno = int(edata[0])
            ename = edata[1]
            qualification = edata[2]
            salary = edata[3]
            dept_name = edata[4]
            emp = Employee(empno, ename, qualification,salary, dept_name)
            lst_emp.append(emp)
    print(f"Total Emp Count: {len(lst_emp)}")

def showDeptName():
    dnames = set(map(lambda emp:emp.dept_name,lst_emp))
    for dname in dnames:
        print(dname)

def showALLQUALIFICATION():
    qualification = set(map(lambda emp:emp.qualification,lst_emp))
    for qual in qualification:
        print(qual)

def maxSalary():
    salary = list(map(lambda emp:emp.salary,lst_emp))
    names = list(filter(lambda x:x.salary == max(salary),lst_emp))
    print(max(salary))
    for ele in names:
        print(ele.ename)

load_emp()
print("All Dept Names")
showDeptName()
print("ALl Qualification")
showALLQUALIFICATION()
print("Max Salary")
maxSalary()