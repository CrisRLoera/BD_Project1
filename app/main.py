import sys
sys.path.insert(1, './emp')
sys.path.insert(2, './dept')

from crud_e import update_emp,insert_emp,delete_emp
from crud_d import update_dept,insert_dept,delete_dept

import customtkinter
import tkinter as tk
import connect


#-----------------------------------------------------------#

root = tk.Tk()
root.geometry('500x500')
root.title('DB Project')

def switch(indicator_lb,page):
    for child in options_fm.winfo_children():
        if isinstance(child,tk.Label):
            child['bg'] = root.cget('bg')
    indicator_lb['bg']='#0097e8'

    for fm in main_fm.winfo_children():
        fm.destroy()
        root.update()

    page()

options_fm = tk.Frame(root)

emp_btn = tk.Button(options_fm, text='Employees',font=('Arial',13),bd=0,fg='#0097e8',activeforeground='#0097e8',command=lambda :switch(emp_indicator_lb,emp_page))
emp_btn.place(x=0,y=0,width=125)

emp_indicator_lb = tk.Label(options_fm)
emp_indicator_lb.place(x=22,y=30,width=80,height=2)

dept_btn = tk.Button(options_fm, text='Department',font=('Arial',13),bd=0,fg='#0097e8',activeforeground='#0097e8',command=lambda :switch(dept_indicator_lb,dept_page))
dept_btn.place(x=125,y=0,width=125)

dept_indicator_lb = tk.Label(options_fm)
dept_indicator_lb.place(x=147,y=30,width=80,height=2)

options_fm.pack(pady=5)

options_fm.pack_propagate(False)
options_fm.configure(width=500,height=35)

def emp_page():
    emp_page_fm=tk.Frame(main_fm)
    
    pos = 0

    emp_page_lb_id = tk.Label(emp_page_fm, text='ID',font=('Arial',13),bd=0,fg='#0097e8')
    emp_page_lb_id.place(x=0,y=pos)
    emp_page_insrt_id = tk.Entry(emp_page_fm)
    emp_page_insrt_id.place(x=0,y=pos+35)
    pos = pos+70
    emp_id = emp_page_insrt_id.get()

    emp_page_lb_nm = tk.Label(emp_page_fm, text='Nombre',font=('Arial',13),bd=0,fg='#0097e8')
    emp_page_lb_nm.place(x=0,y=pos)
    emp_page_insrt_nm = tk.Entry(emp_page_fm)
    emp_page_insrt_nm.place(x=0,y=pos+35)
    pos = pos+70
    emp_name = emp_page_insrt_nm.get()

    emp_page_lb_job = tk.Label(emp_page_fm, text='Job',font=('Arial',13),bd=0,fg='#0097e8')
    emp_page_lb_job.place(x=0,y=pos)
    emp_page_insrt_job = tk.Entry(emp_page_fm)
    emp_page_insrt_job.place(x=0,y=pos+35)
    pos = pos+70
    emp_job = emp_page_insrt_job.get()

    emp_page_lb_mgr = tk.Label(emp_page_fm, text='Manager ID',font=('Arial',13),bd=0,fg='#0097e8')
    emp_page_lb_mgr.place(x=0,y=pos)
    emp_page_insrt_mgr = tk.Entry(emp_page_fm)
    emp_page_insrt_mgr.place(x=0,y=pos+35)
    pos = pos+70
    emp_mgr = emp_page_insrt_mgr.get()

    emp_page_lb_day = tk.Label(emp_page_fm, text='Día de contratación',font=('Arial',13),bd=0,fg='#0097e8')
    emp_page_lb_day.place(x=0,y=pos)
    emp_page_insrt_day = tk.Entry(emp_page_fm)
    emp_page_insrt_day.place(x=0,y=pos+35)
    pos = pos+70
    emp_day = emp_page_insrt_day.get()

    emp_page_lb_month = tk.Label(emp_page_fm, text='Mes de contratación',font=('Arial',13),bd=0,fg='#0097e8')
    emp_page_lb_month.place(x=0,y=pos)
    emp_page_insrt_month = tk.Entry(emp_page_fm)
    emp_page_insrt_month.place(x=0,y=pos+35)
    pos = pos+70
    emp_month = emp_page_insrt_month.get()

    pos = 0

    emp_page_lb_year = tk.Label(emp_page_fm, text='Año de contratación',font=('Arial',13),bd=0,fg='#0097e8')
    emp_page_lb_year.place(x=200,y=pos)
    emp_page_insrt_year = tk.Entry(emp_page_fm)
    emp_page_insrt_year.place(x=200,y=pos+35)
    pos = pos+70
    emp_year = emp_page_insrt_year.get()

    emp_page_lb_sal = tk.Label(emp_page_fm, text='Salario',font=('Arial',13),bd=0,fg='#0097e8')
    emp_page_lb_sal.place(x=200,y=pos)
    emp_page_insrt_sal = tk.Entry(emp_page_fm)
    emp_page_insrt_sal.place(x=200,y=pos+35)
    pos = pos+70
    emp_sal = emp_page_insrt_sal.get()

    emp_page_lb_comm = tk.Label(emp_page_fm, text='Comisión',font=('Arial',13),bd=0,fg='#0097e8')
    emp_page_lb_comm.place(x=200,y=pos)
    emp_page_insrt_comm = tk.Entry(emp_page_fm)
    emp_page_insrt_comm.place(x=200,y=pos+35)
    pos = pos+70
    emp_comm = emp_page_insrt_comm.get()

    emp_page_lb_dept = tk.Label(emp_page_fm, text='Departamento',font=('Arial',13),bd=0,fg='#0097e8')
    emp_page_lb_dept.place(x=200,y=pos)
    emp_page_insrt_dept = tk.Entry(emp_page_fm)
    emp_page_insrt_dept.place(x=200,y=pos+35)
    pos = pos+70
    emp_dept = emp_page_insrt_dept.get()

    emp_page_sumbit = tk.Button(emp_page_fm, text='Subi empleado',bg='white',font=('Arial',13),bd=0,fg='#0097e8',activeforeground='#0097e8',command=lambda :insert_emp(emp_id,emp_name,emp_job,emp_mgr,emp_day,emp_month,emp_year,emp_sal,emp_comm,emp_dept))
    emp_page_sumbit.place(x=200,y=pos+35)

    emp_page_fm.pack(fill=tk.BOTH, expand=True)

def dept_page():
    dept_page_fm=tk.Frame(main_fm)
    dept_page_lb = tk.Label(dept_page_fm, text='Inser',font=('Arial',13),bd=0,fg='#0097e8')
    dept_page_lb.pack(pady=80)
    dept_page_fm.pack(fill=tk.BOTH, expand=True)

main_fm= tk.Frame(root)
main_fm.pack(fill=tk.BOTH, expand=True)

root.mainloop()

cursor.close()
connection.close()