CREATE OR REPLACE PROCEDURE Add_emp(i_empno NUMBER, ename VARCHAR2,ejob VARCHAR2,emgr VARCHAR2,hire_date VARCHAR2,sal NUMBER,comm NUMBER,dept NUMBER)
IS
    id_count NUMBER;
    OpSql VARCHAR2(500);
    t_date DATE;
BEGIN
    SELECT COUNT(*)
    INTO id_count
    FROM EMP
    WHERE EMPNO = i_empno;
    IF id_count > 0 THEN
        RAISE_APPLICATION_ERROR(-20001, 'El ID ya existe');
    END IF;
    t_date := TO_DATE(hire_date, 'DD-MM-YYYY');
    OpSql := 'INSERT INTO EMP VALUES (:dnum,:enam,:ej,:emg,:dat,:s,:c,:dep)';
    EXECUTE IMMEDIATE OpSql USING i_empno,ename,ejob,emgr,t_date,sal,comm,dept;
    COMMIT;
END;