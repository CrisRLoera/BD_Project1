CREATE OR REPLACE PROCEDURE Update_emp(i_empno NUMBER,camp VARCHAR2,new_val VARCHAR2)
IS
    id_count NUMBER;
    OpSql VARCHAR2(500);
BEGIN
    SELECT COUNT(*)
    INTO id_count
    FROM EMP
    WHERE empno = i_empno;
    IF id_count = 0 THEN
        RAISE_APPLICATION_ERROR(-20001, 'El ID especificado no existe');
    END IF;
    OpSql := 'UPDATE EMP SET '||camp||' = :enew WHERE empno = :eid' ;
    EXECUTE IMMEDIATE OpSql USING new_val,i_empno;
    COMMIT;
END;