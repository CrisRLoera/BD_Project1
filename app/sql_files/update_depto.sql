CREATE OR REPLACE PROCEDURE Update_depto(ideptno NUMBER,camp VARCHAR2,new_val VARCHAR2)
IS
    id_count NUMBER;
    OpSql VARCHAR2(500);
BEGIN
    SELECT COUNT(*)
    INTO id_count
    FROM DEPT
    WHERE deptno = ideptno;
    IF id_count = 0 THEN
        RAISE_APPLICATION_ERROR(-20001, 'El ID especificado no existe');
    END IF;
    OpSql := 'UPDATE DEPT SET '||camp||' = :dnew WHERE deptno = :did' ;
    EXECUTE IMMEDIATE OpSql USING new_val,ideptno;
    COMMIT;
END;