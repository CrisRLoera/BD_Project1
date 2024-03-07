CREATE OR REPLACE PROCEDURE Delete_depto(ideptno NUMBER)
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
    OpSql := 'DELETE FROM DEPT WHERE deptno = :did' ;
    EXECUTE IMMEDIATE OpSql USING ideptno;
    COMMIT;
END;