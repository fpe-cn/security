# Netcraft responder

----
## Netcraft
See [official website](https://www.netcraft.com/cybercrime/phishing-site-takedown/)

> Netcraft’s countermeasures service helps organisations to combat these techniques. Once a phishing site has been detected, Netcraft immediately responds with a set of actions which will significantly limit access to the site, and will ultimately cause the 
fraudulent content to be eliminated 
Netcraft’s approach is distinguished from other providers of takedown services through its ability to immediately block access to the site for users of a wide range of technologies. 

----
## Responder
 

### Goal
This responder was made with the purpose of improving takedown of fraudulent website. 
Instead of report it by a specific form on Netcraft website, you can report it in 1-click directly in the case. Then you have the takedown result with the associated ticket number.

### Requirements
You have to fill three parameters used to the API authentication.

* account_username : *username of the account used to report website*

* account_password : *password of the account used to report website*

* account_region : *name of the region allowed for the account*


### Input

* Fraudulent website URL (datatype: url)

### Output

If it works :

* "URL reported. Ticket #XXXXX"
* "URL already reported. Ticket #XXXXX"
* "URL undergoing verification"
* "Sub-domain already reported"

or

* "Error" (authentication or connexion issue)
* "Incorrect datatype. URL expexted"

A new tag is added to the artifact (Netcraft:reported) 



### Example

![Examples](https://raw.githubusercontent.com/fpe-cn/security/master/thehive/responder/netcraft/example.png "Examples")
