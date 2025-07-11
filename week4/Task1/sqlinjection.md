### ** SQL Injection - Web  Application Security**

The objective of this task was to understand how **SQL Injection (SQLi)** works in a web application and how to exploit it using common payloads on a vulnerable test application (**DVWA**). Then, i applied **input validation** and **prepared statements** to fix the vulnerability.

**Payloads i run on the website:****

#### **Payload 1: `' OR '1'='1`**

-   **Where:** Input box for `User ID` in the SQL Injection page.
    
-   **How it works:**  
    This payload closes the original query condition and adds `OR '1'='1'` which is always true.
    
-   **Result:**  
    Instead of fetching a single user, the query returned **all users** from the database.



#### **Payload 2: `-1' UNION SELECT NULL, database() --`**

-   **Where:** Same input.
    
-   **How it works:**  
    Forces the query to return the **current database name**.
    
-   **Result:**  
    The page displayed the DB name (`dvwa`).
    
    
   Some other  payloads include:
   ' UNION SELECT NULL, version() --
   ' --
   
**The Root Cause:**

$id = $_GET['id'];
$query = "SELECT first_name, surname FROM users WHERE user_id = '$id'";

The user input `$id` was **directly inserted** into the SQL query without validation or safe handling.

**Mitigation**

To fix this vulnerability, I updated the code to use **input validation** and **prepared**

**Input Validation:**
if (!is_numeric($id)) {
    die('Invalid ID');
}

This will allow only integer to be enter the the field.

**Prepared Statements**
Prepare statements are the modern solution to sql injection.The `?` acts as a safe placeholder, so user input cannot change the structure of the SQL query.



**Result After Fix**

-   When I ran the same payloads (`' OR '1'='1` or `UNION SELECT`), the input was blocked:
    
    -   Either the code showed `Invalid ID`
        
    -   Or the payload was treated as data only, so the injection failed.
        
-   The vulnerability was successfully mitigated.
