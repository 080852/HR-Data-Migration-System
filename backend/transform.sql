INSERT INTO modern_employees
SELECT
    emp_id,
    SPLIT_PART(full_name, ' ', 1),
    SPLIT_PART(full_name, ' ', 2),
    TO_DATE(REPLACE(dob, '/', '-'), 'DD-MM-YYYY'),
    CASE dept_code
        WHEN 'HR' THEN 'Human Resources'
        WHEN 'FN' THEN 'Finance'
        WHEN 'IT' THEN 'Information Technology'
        ELSE 'Other'
    END,
    email,
    CAST(REPLACE(REPLACE(salary, ',', ''), '.00', '') AS INT),
    CASE gender WHEN 'M' THEN 'Male' WHEN 'F' THEN 'Female' ELSE 'Other' END
FROM legacy_employees
WHERE POSITION('@' IN email) > 1 AND POSITION('.' IN email) > 1;
