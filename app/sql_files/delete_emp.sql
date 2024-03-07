CREATE OR REPLACE PROCEDURE Delete_emp(i_empno NUMBER)
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
    OpSql := 'DELETE FROM EMP WHERE empno = :eid' ;
    EXECUTE IMMEDIATE OpSql USING i_empno;
    COMMIT;
END;