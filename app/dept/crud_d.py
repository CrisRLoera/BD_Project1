
def insert_dept(j):
    try:
        print(f"ID del departamento {j+1}:")
        try:
            deptno = int(input())
        except:
            print("No es un numero")
        print(f"Nombre del departamento {j+1}:")
        dname = input()
        print(f"Localización del departamento {j+1}:")
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
