
**Web Application Security - Secure Coding Practices**

 The vulnerable.php file attached with this document has the following security flaws that hacker can use to exploit 
it.

The Code has the following flaws:
Problem


❌ **SQL Injection**

`$sql` uses raw user input

Attacker can inject SQL commands

❌ **No Input Validation**

`$username` and `$password`

No checks for malicious input

❌ **XSS**

`echo "Welcome, $username";`

Username is printed without escaping

❌ **Bad Session Handling**

`$_SESSION` not secured

No session ID regeneration, no cookie flags

❌ **Insecure Error Handling**

`echo $conn->error;`

Database errors exposed to user


**Applied Security practices** 

The following security practices is applied to the code the final secure code is attached with this on the name secureCode.php

-> Add Input Validation
I only allowed alphanumeric usernames (letters, numbers) and passwords at least 6 characters long.

-> Use Prepared Statements
The use of prepared statement avoid SQL injection risk as it doesn't directly query the user input.
s
-> Escape Output
Escape the output to prevent XSS attack.

-> Hide Error Details
 Show only general error to the user as error sometime give clue to the hacker 

-> secure session 
only allow https for session and same-site= strict to avoid CSRF attack and allow http only to allow java-script don't touch the code.





