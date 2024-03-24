![1-distributed_web_infrastructure](https://github.com/SohaibHegazy/alx-system_engineering-devops/assets/143375340/8c2e5aaf-c888-4f4c-8531-6fd25c7d6b19)

For every additional element, why you are adding it:

I added the load balancer to distribute the requests between nodes, which gives better repsponse time.

What distribution algorithm your load balancer is configured with and how it works:

The load balancer works with round ribon distribution algorithm, which distributes the load to the servers in turn according to the server's weight.

Is your load-balancer enabling an Active-Active or Active-Passive setup, explain the difference between both:

The load balancer enables an Active-Active setup, where both servers are running in the same time and the balancer distributes the load by turn, when one of the servers is down for maintenance, the load is redirected to the running server. while in the Active-Passive setup, only one server will be running, and the other one will be standby, the standby server is continuously updated with requests and responds done by the running one, so that whenever the primary server is down, the standby server can take over and run.

How a database Primary-Replica (Master-Slave) cluster works:

A Primary-Replica makes one server as a Primary server and the other server as a Replica of the Primary. Primary server read/write requests while the Replica server reads only. Data is synchronized between the Primary and Replica servers.

What is the difference between the Primary node and the Replica node in regard to the application?

The primary node performs the write operations while the replica performs the read operations.


what the issues are with this infrastructure:

Where are SPOF:
There are some SPOFs, such as containing one load balancer.

Security issues:
No SSL certificate used (HTTPS), which means that the data is not encrypted and anyone can read it.
Also, there is no firewalls on the servers nor on the load balancer.

No monitoring:
The nodes are not monitored and we can't know the status of them
