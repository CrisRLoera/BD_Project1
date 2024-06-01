import sys
import cx_Oracle

username = 'SYSTEM'
password = 'admin'
host = 'localhost'
port = '1521'
service_name = 'XE'

dsn = cx_Oracle.makedsn(host, port, service_name)

connection = cx_Oracle.connect(username, password, dsn)

cursor = connection.cursor()

def insert_emp():
    print("Escribe el id del empleado:")
    empno=int(input())
    print("Escribe el nombre del empleado:")
    e_name=input()
    print("Escribe el trabajo del empleado:")
    e_job=input()
    print("Escribe el id del manager del empleado:")
    e_mgr=int(input())
    
    print("Escribe el día de contartación:")
    day=int(input())
    print("Escribe el mes de contartación:")
    month=int(input())
    print("Escribe el año de contartación:")
    year=int(input())
    print("Escribe el salario del empleado:")
    e_sal=int(input())
    print("Escribe la comisión del empleado:")
    e_comm=int(input())
    print("Escribe el departamento del empleado:")
    e_dept=int(input())

    e_date = (f"{day}-{month}-{year}")
    try:
        cursor.callproc('Add_emp',(empno,e_name,e_job, e_mgr,e_date,e_sal, e_comm,e_dept))
        print("Completado")
    except cx_Oracle.DatabaseError as e:
            error, = e.args
            if error.code == 20001:
                print("Error: El ID especificado ya existe en la base de datos.")
            else:
                print("Error inesperado:", error.message)

def update_emp():
    print("ID del empleado:")
    try:
        empno = int(input())
        print("Campo a cambiar:")
        print("1 Nombre del empleado")
        print("2 Trabajo del empleado")
        print("3 Manager del empleado")
        print("4 Fecha de contratacipon")
        print("5 Salario")
        print("6 Comisión")
        print("7 Departamento")
        opt = int(input())
        camp = ""
        if(opt==1):
            camp="ENAME"
        elif(opt==2):
            camp="JOB"
        elif(opt==3):
            camp="MGR"
        elif(opt==4):
            camp="HIREDATE"
        elif(opt==5):
            camp="SAL"
        elif(opt==6):
            camp="COMM"
        elif(opt==7):
            camp="DEPTNO"
        else:
            print("NO se conoce la opción")
            exit()
        if(opt!=1 and opt!=2 and opt!=4):
            try:
                print("Nuevo valor:")
                new = int(input())
            except:
                print("No es un numero")
                exit()
        elif(opt==4):
            print("NUEVA FECHA:")
            print("Ingresa día:")
            try:
                day = int(input())
            except:
                print("No es un numero")
                exit()
            print("Ingresa mes:")
            try:
                month = int(input())
            except:
                print("No es un numero")
                exit()
            print("Ingresa año:")
            try:
                year = int(input())
            except:
                print("No es un numero")
                exit()
            new = (f"{day}-{month}-{year}")
        else:
            print("Nuevo valor:")
            new = input()
        try:
            cursor.callproc('Update_emp',(empno,camp,new))
            print("Completado")
        except cx_Oracle.DatabaseError as e:
            error, = e.args
            if error.code == 20001:
                print("Error: El ID especificado no existe en la base de datos.")
            else:
                print("Error inesperado:", error.message)
    except:
        print("No es un numero")

def delete_emp():
    print("ID del empleado:")
    try:
        empno = int(input())
        try:
            cursor.callproc('Delete_emp',[empno])
            print("Completado")
        except cx_Oracle.DatabaseError as e:
            error, = e.args
            if error.code == 20001:
                print("Error: El ID especificado no existe en la base de datos.")
            else:
                print("Error inesperado:", error.message)
    except:
        print("No es un numero")


def insert_dept():
    print("Incerte:")
    try:
        print("ID del departamento:")
        try:
            deptno = int(input())
        except:
            print("No es un numero")
        print("Nombre del departamento:")
        dname = input()
        print("Localización del departamento:")
        loc = input()

        cursor.callproc('Add_depto',(deptno,dname,loc))

        print("Completado")
    except cx_Oracle.DatabaseError as e:
            error, = e.args
            if error.code == 20001:
                print("Error: El ID especificado ya existe en la base de datos.")
            elif error.code == 20002:
                print("Error: El ID especificado tiene que ser divisible entre 10.")
            else:
                print("Error inesperado:", error.message)

def update_dept():
    print("ID del departamento:")
    try:
        deptno = int(input())
        print("Campo a cambiar:")
        print("1 Nombre del departamento")
        print("2 Localización del departamento")
        opt = int(input())
        camp = ""
        if(opt==1):
            camp="DNAME"
        elif(opt==2):
            camp="LOC"
        else:
            print("NO se conoce la opción")
            exit()
            
        print("Nuevo valor:")
        new = input()
        try:
            cursor.callproc('Update_depto',(deptno,camp,new))
            print("Completado")
        except cx_Oracle.DatabaseError as e:
            error, = e.args
            if error.code == 20001:
                print("Error: El ID especificado no existe en la base de datos.")
            else:
                print("Error inesperado:", error.message)
    except:
        print("No es un numero")

def delete_dept():
    print("ID del departamento:")
    try:
        deptno = int(input())
        try:
            cursor.callproc('Delete_depto',[deptno])
            print("Completado")
        except cx_Oracle.DatabaseError as e:
            error, = e.args
            if error.code == 20001:
                print("Error: El ID especificado no existe en la base de datos.")
            else:
                print("Error inesperado:", error.message)
    except:
        print("No es un numero")

def select_num_emp_by_id():
    print("ID del departamento:")
    try:
        deptno = int(input())
        try:
            numero_empleados = cursor.var(cx_Oracle.NUMBER)
            cursor.execute("BEGIN :result := noEmp_depto(:id_dept); END;", result=numero_empleados, id_dept=deptno)
            print("Total de empleados en ",deptno," es ",numero_empleados.getvalue())
        except cx_Oracle.DatabaseError as e:
            error, = e.args
            if error.code == 20001:
                print("Error: El ID especificado no existe en la base de datos.")
            else:
                print("Error inesperado:", error.message)
    except:
        print("No es un numero")
        
opt=0
while(opt!=9):
    print("Menú")
    print("1.-Incertar empleado")
    print("2.-Incertar departamento")
    print("3.-Actualizar empleado")
    print("4.-Actualizar departamento")
    print("5.-Eliminar empleado")
    print("6.-Eliminar departamento")
    print("7.-Ver número de empleados asignados a departamento")
    print("Incerte una opción:")
    opt=int(input())
    if(opt==1):
        insert_emp()
    elif(opt==2):
        insert_dept()
    elif(opt==3):
        update_emp()
    elif(opt==4):
        update_dept()
    elif(opt==5):
        delete_emp()
    elif(opt==6):
        delete_dept()
    elif(opt==7):
        select_num_emp_by_id()

cursor.close()
connection.close()