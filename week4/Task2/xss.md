**Executing a cross-site scripting (XSS) Attack**

**Objective**

Test DVWA for **Reflected Cross-Site Scripting (XSS)** and apply defenses using **Input sanitization & output encoding **.

 **Payloads Tested**
 `<script>alert('XSS')</script>`

✅ Alert appeared

`<img src="x" onerror="alert('XSS')">`

✅ Alert appeared

`<svg/onload=alert('XSS')>`

✅ Alert appeared

`"><script>alert('XSS')</script>`

  **Root Cause**

-   The input was directly reflected into the HTML page.
    
-   No **escaping** or **encoding** was used.
    
-   The browser treated input as executable code.

 **Retest Results**

-   Same payloads now appear **as text**.
    
-   No alerts pop up.
    
-   Reflected XSS fully blocked.



 **Solution Implemented**
 
 1- Input Sanitization/Validation using regex:
 
if (!preg_match("/^[a-zA-Z ]*$/", $name)) {
        die("Invalid input — letters and spaces only!");
    }


  2-  Used:

 `htmlspecialchars($input, ENT_QUOTES, 'UTF-8')` in PHP

This encodes:

-   `<` → `&lt;`
    
-   `>` → `&gt;`
    
-   `"` → `&quot;`

now the browser will show the script as output directly without executing it.



**Conclusion**

-   **Issue:** Reflected XSS worked when input was output directly without escaping.
    
-   **Fix:** Escaping/encoding output stops malicious scripts from executing.
    
-   **Best Practice:** Always escape user input when rendering in HTML.
