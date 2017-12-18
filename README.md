BloodHound
==========

- Assumption: The location where people read their email from is where they live.
- Given: An email address
- To find: Physical location of that email address.
- Procedure:
    - Send a specially crafted email to that address.
        - We include a transparent image/dummy request for JS/CSS in the HTML which is stored on servers controlled by us.
        - Thus we can log who requested that image and from where (Agent).
    - Wait for the person to open that email.
    - Log the IP address of the person who opened that email.
    - Lookup IP address to geographical location.
- Implications: With a large enough email list you can geographically map an organization.


Notes
-----

Server can be as simple as [server.py](server.py). The HTML to be sent can be as simple as

```html
<html>
<head>
<script src='https://self.controlled.server/resource'></script>
</head>
<body>hi</body>
</html>
```
