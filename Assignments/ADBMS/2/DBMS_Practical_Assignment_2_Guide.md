# ADBMS Practical 2: Functions, Syntax & Concepts Guide

> **Scope:** Reference guide for implementing Number, Aggregate, Character, Conversion, and Date functions in SQL without direct assignment solutions.

---

## 1. Schema & Table Design Considerations

### Table Creation (`CREATE TABLE`)
Defines the structure, attributes, and constraints of a table:
```sql
CREATE TABLE table_name (
    column1 datatype constraints,
    column2 datatype,
    ...
);
```

### Note on Assignment Schema
The assignment specifies the following columns:
`(Emp_no, E_name, E_address, E_ph_no, Dept_no, Dept_name, Job_id, Designation, Salary)`

> [!IMPORTANT]
> Because several practical questions evaluate joining dates (`joined after 1981`, specific join dates) and employee experience, your table schema will need a date column (e.g. `Join_date DATE` or `Hire_date DATE`) to store and query those values properly.

### Database / Table Deletion (`DROP`)
Removes the structure and all stored records permanently:
```sql
-- Remove a specific table:
DROP TABLE table_name;

-- Remove an entire database (MySQL / PostgreSQL):
DROP DATABASE database_name;
```

---

## 2. Basic Filtering, Sorting & Selection

### General Query Structure
```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

### Relational & Logical Operators
* **Relational:** `=`, `!=` (or `<>`), `>`, `<`, `>=`, `<=`
* **Logical:** `AND`, `OR`, `NOT`

```sql
-- Combining multiple conditions:
SELECT * FROM sample_table 
WHERE status = 'ACTIVE' AND amount > 5000;
```

### Membership Operators (`IN` / `NOT IN`)
Used to test whether a value matches any value in a defined list, or to exclude a set of values:
```sql
-- Inclusive match (replaces chained ORs):
SELECT * FROM sample_table 
WHERE category IN ('TYPE_A', 'TYPE_B', 'TYPE_C');

-- Exclusion match:
SELECT * FROM sample_table 
WHERE status NOT IN ('REJECTED', 'PENDING');
```

### Pattern Matching (`LIKE`)
Used for wildcards in string evaluations:
* `%` matches zero, one, or multiple characters.
* `_` matches exactly one character.

```sql
-- Values starting with a specific letter:
WHERE name LIKE 'A%'

-- Values ending with a specific letter:
WHERE name LIKE '%Z'

-- Values containing a substring:
WHERE name LIKE '%pattern%'

-- Values with a specific prefix and length (e.g., starts with 'H' followed by at least 4 characters):
WHERE name LIKE 'H____%'
```

### Eliminating Duplicates (`DISTINCT`)
Returns unique values from a column or combination of columns:
```sql
SELECT DISTINCT column_name 
FROM table_name;
```

### Sorting Data (`ORDER BY`)
Sorts retrieved records by one or more columns:
```sql
-- Ascending order (default):
SELECT * FROM sample_table 
ORDER BY column_name ASC;

-- Descending order:
SELECT * FROM sample_table 
ORDER BY column_name DESC;
```

---

## 3. SQL Functions by Category

### A. Aggregate Functions
Aggregate functions perform a calculation on a set of values and return a single summary value.
> When used with a `WHERE` clause, the aggregation applies only to the matching filtered subset.

| Function | Purpose | Syntax Example |
| :--- | :--- | :--- |
| `MAX(col)` | Finds the highest value | `SELECT MAX(price) FROM products;` |
| `MIN(col)` | Finds the lowest value | `SELECT MIN(price) FROM products;` |
| `SUM(col)` | Calculates the total sum | `SELECT SUM(score) FROM results;` |
| `AVG(col)` | Calculates arithmetic mean | `SELECT AVG(score) FROM results;` |
| `COUNT(col)`| Counts non-null entries | `SELECT COUNT(id) FROM records;` |

---

### B. Character / String Functions
Operate on text values and return either string or numeric values.

* **Substring Extraction (`SUBSTR` / `SUBSTRING`):**
  Extracts characters from a string starting at an index for a given length.
  ```sql
  -- Oracle & MySQL syntax:
  SELECT SUBSTR(string_column, 1, 5) FROM sample_table;
  -- Standard / MySQL syntax:
  SELECT SUBSTRING(string_column, 1, 5) FROM sample_table;
  ```
* **Casing Functions (`UPPER`, `LOWER`):**
  Converts casing for consistent display or matching.
  ```sql
  SELECT UPPER(first_name), LOWER(email) FROM users;
  ```
* **String Length (`LENGTH`):**
  ```sql
  SELECT LENGTH(description) FROM items;
  ```

---

### C. Number Functions & Direct Arithmetic
Used for mathematical manipulations.

* **Direct Arithmetic on Columns:**
  Standard arithmetic operators (`+`, `-`, `*`, `/`) can be applied directly in projections.
  ```sql
  -- Compute daily value from monthly amount:
  SELECT column_value / 30 AS daily_rate FROM table_name;
  ```
* **Rounding (`ROUND`):**
  Rounds a numeric value to a specified number of decimal places.
  ```sql
  SELECT ROUND(1234.5678, 2) FROM DUAL; -- Produces 1234.57
  ```
* **Truncation (`TRUNC` in Oracle / `FLOOR` or `TRUNCATE` in MySQL):**
  Discards decimal digits without rounding up.
  ```sql
  SELECT TRUNC(1234.5678, 2) FROM DUAL; -- Produces 1234.56
  ```

---

### D. Date Functions & Elapsed Time / Experience Calculations

#### Fetching Current Date
* **Oracle:** `SYSDATE`
* **MySQL:** `CURDATE()` or `CURRENT_DATE`

#### Filtering by Dates / Years
```sql
-- Direct date comparison (standard ISO format: YYYY-MM-DD):
WHERE date_column > '1981-12-31'

-- Extracting year component:
WHERE EXTRACT(YEAR FROM date_column) > 1981
```

#### Calculating Experience / Date Differences
* **Oracle SQL:**
  * Difference in days: `SYSDATE - date_column`
  * Difference in months: `MONTHS_BETWEEN(SYSDATE, date_column)`
  * Experience in years:
    ```sql
    ROUND(MONTHS_BETWEEN(SYSDATE, date_column) / 12, 1)
    ```
* **MySQL:**
  * Difference in days: `DATEDIFF(CURDATE(), date_column)`
  * Experience in years:
    ```sql
    TIMESTAMPDIFF(YEAR, date_column, CURDATE())
    ```

---

### E. Conversion Functions

Used when translating data between strings, dates, and numbers.

* **Oracle Conversion Functions:**
  * `TO_CHAR(date_or_number, 'format')`
    ```sql
    SELECT TO_CHAR(date_column, 'YYYY') FROM sample_table;
    SELECT TO_CHAR(date_column, 'DD-MON-YYYY') FROM sample_table;
    ```
  * `TO_DATE('string', 'format')`
    ```sql
    WHERE date_column = TO_DATE('01-MAY-1981', 'DD-MON-YYYY')
    ```
  * `TO_NUMBER('string')`

* **Standard / MySQL Conversion Functions:**
  * `STR_TO_DATE('01-05-1981', '%d-%m-%Y')`
  * `CAST(column_name AS target_type)`

