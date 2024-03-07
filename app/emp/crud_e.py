import cx_Oracle
import connect

def insert_emp(empno,e_name,e_job,e_mgr,day,month,year,e_sal,e_comm,e_dept):
    
    e_date = (f"{day}-{month}-{year}")
    
    e_id = int(empno)

    mgr = int(e_mgr)

    sal = int(e_sal)

    comm = int(e_comm)

    dept = int(e_dept)

    try:
        connect.cursor.callproc('Add_emp',(e_id,e_name,e_job, mgr,e_date,sal, comm,dept))
        print("Completado")
    except cx_Oracle.DatabaseError as e:
            error, = e.args
            if error.code == 20001:
                print("Error: El ID especificado ya existe en la base de datos.")
            elif error.code == 20002:
                print("Error: El ID especificado tiene que ser divisible entre 10.")
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
