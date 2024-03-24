![2-secured_and_monitored_web_infrastructure](https://github.com/SohaibHegazy/alx-system_engineering-devops/assets/143375340/d471038c-f7c2-4a6a-b1c1-fa00ebf1ba85)

For every additional element, why you are adding it?

I added the new firewalls at each node to provide security. Also, I added the SSL certificate to insure the encryption of data. The addition of 3 monitoring clients, one at each node and one at the load balancer to monitor the status of them and alert the administrator to act accordingly

What are firewalls for?

Firewalls are for protecting the network by blocking the unauthorized users through blocking the incoming traffic matching the aforementioned criteria.

Why is the traffic served over HTTPS?

HTTPS provides secured version of HTTP using SSL certificates (or TLS), this prevents the man-in-the-middle attacks (MITM) and network sniffers from sniffing the traffic which could expose valuable information.

What monitoring is used for?

Monitoring is used to analyse the performance of servers, and alert the administrators if needed. It provides key metrics about the servers to the administrators and automatically tests the accessibility and response time. It alerts for errors such as corrupt/missing files, security vulnerabilities/violations, and many other issues.

How the monitoring tool is collecting data?

It provides key metrics about the servers to the administrators and automatically tests the accessibility and response time. It alerts for errors such as corrupt/missing files, security vulnerabilities/violations, and many other issues.

Explain what to do if you want to monitor your web server QPS?

To monitor the web server queries per second (QPS):
1- Select a monitoring tool to collect the data
2- Install agents
3- Set proper alerts
4- collect data

what the issues are with this infrastructure:

Why terminating SSL at the load balancer level is an issue?
Because this makes the data between the load balancer and the nodes exposed (not encrypted)

Why having only one MySQL server capable of accepting writes is an issue?
Because this is considered SPOF, as if the server is down for any reason, the whole site will be down

Why having servers with all the same components (database, web server and application server) might be a problem?
Because this gives poor and slow performance, as the resources are used by all, this will also make it hard to scale up.
