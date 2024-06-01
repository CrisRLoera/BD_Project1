CREATE OR REPLACE FUNCTION noEmp_depto(
    dept_id NUMBER
)
RETURN NUMBER
IS
    num_emp NUMBER;
    OpSql VARCHAR2(1000);
BEGIN
    OpSql := 'SELECT COUNT(*) FROM EMP WHERE deptno = :dept_id';

    EXECUTE IMMEDIATE OpSql INTO num_emp USING dept_id;
    RETURN num_emp;
END noEmp_depto;