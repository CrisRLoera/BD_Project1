CREATE OR REPLACE PROCEDURE Add_depto(i_deptno NUMBER, dname VARCHAR2,loc VARCHAR2)
IS
    id_count NUMBER;
    OpSql VARCHAR2(500);
BEGIN
    SELECT COUNT(*)
    INTO id_count
    FROM DEPT
    WHERE deptno = i_deptno;
    IF id_count > 0 THEN
        RAISE_APPLICATION_ERROR(-20001, 'El ID ya existe');
    END IF;
    IF (i_deptno/10) = 0 THEN
        RAISE_APPLICATION_ERROR(-20002, 'El ID debe ser divisible entre 10');
    END IF;
    OpSql := 'INSERT INTO DEPT VALUES (:dnum,:dnam,:dloc)';
    EXECUTE IMMEDIATE OpSql USING i_deptno,dname,loc;
    COMMIT;
END;