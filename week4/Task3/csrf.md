**Testing and Exploiting Cross-Site Request Forgery (CSRF) in a Web Application**

**Objective:**
The goal of this task was to identify whether the “Change Email” functionality in the target web application is vulnerable to Cross-Site Request Forgery (CSRF), demonstrate how an attacker could exploit it, and provide a solution to prevent this vulnerability.

**Test Performed:**  
I tested the “Change Email” function of the target application. The form allowed a logged-in user to change their account email address by sending a POST request with the new email value. I inspected the request and confirmed that the form did not use any CSRF protection mechanisms such as CSRF tokens or SameSite cookie settings.

**Steps to Reproduce:**

1.  I created a malicious HTML page (hosted on the Exploit Server) with a hidden form that sends a POST request to the application’s `change-email` endpoint.
    
2.  The form contained a hidden input field that sets the email to an attacker-controlled value.
    
3.  The page used JavaScript to automatically submit the form when the victim opens the page.
    
4.  I tested this on my own account first to confirm that the email was changed without my explicit action.
    
5.  I then delivered this exploit to the lab’s victim user using the provided exploit delivery function.
    

The attack succeeded: the victim’s account email was changed without their consent.


To protect against CSRF, the web application should implement a **CSRF token mechanism**:

**How it works:**

-   The server generates a unique, unpredictable token for each user session.
    
-   This token is included as a hidden input in every sensitive form (like changing an email or password).
    
-   When the form is submitted, the server checks that the submitted token matches the one stored in the user’s session.
    
-   If the token is missing or invalid, the server rejects the request.
    

**Example (fixed form):**

`<form  action="/my-account/change-email"  method="POST"> <input  type="hidden"  name="csrf_token"  value="abc123XYZ"> <input  type="email"  name="email"> <button  type="submit">Change Email</button> </form>` 

**On the server side:**

1.  When the page loads, the server generates a random `csrf_token` and saves it in the user’s session.
    
2.  The form includes the same token as a hidden field.
    
3.  When the form is submitted, the server checks: _Does the submitted token match the session token?_
    
4.  If yes, the request is valid. If no, it is blocked.

**Additional Good Practices:**

-   Use the `SameSite` cookie attribute to help prevent cross-site cookies from being sent on unsafe requests.
    
-   Use POST requests (not GET) for any actions that modify data.
