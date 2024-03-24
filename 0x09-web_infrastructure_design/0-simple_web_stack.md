![0-simple_web_stack](https://github.com/SohaibHegazy/alx-system_engineering-devops/assets/143375340/60f1ae8f-a3bf-40f2-90bb-6146bb7d0e78)

What is a Server?
A computer hardware or software that provides services to other computers, which are usually referred to as clients.

What is the role of the domain name?
To provide a human-friendly alias for an IP Address. The IP address and domain name alias are mapped in the Domain Name System (DNS)

What type of DNS record www is in www.foobar.com?
type of DNS record is "A record"

What is the role of the web server?
Web server receives the HTTP or HTTPS requests, and responds with the content or with an error message

What is the role of the application server?
To install, operate and host applications and associated services

What is the role of the database?
To store collection of organized data and make is easy to access, manage, and update

What is the server using to communicate with the computer of the user requesting the website?
TCP/IP protocol

what the issues are with this infrastructure:
SPOF:
This infrastructure is all single point of failure, for example if the application server is down, every thing is dow. Same with the database server and the web server

Downtime when maintenance needed:
because of the absence of redundancy, when we run maintenance, the website will be down, which will cause a big downtime

Cannot scale if too much incoming traffic:
because of the usage of one server only, and accordingly the absence of a load balancer it will not be easy to scale as the server can't handle huge amount of requests on its ow
