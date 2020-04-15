(https://www.esds.co.in/blog/what-is-the-difference-between-horizontal-vertical-scaling/#sthash.sB8SZFOn.dpbs)
##### In cloud web solutions, there are two main scaling strategies – Horizontal Scaling & Vertical Scaling.  
Let’s assume you are going to holiday trip with your team. Actual problem is there are 50 members in your team & 
travel agent has sent only one bus having capacity of 25 passengers. What you will do? You need at least 2 buses. 
What you can do is either you can ask for two buses or you can ask for double-decker bus which can carry 50 
passengers at a time .  Conclusion is you need to scale the basic resource (bus). If you choose option of 
double-decker then it is called ‘Vertical Scaling’ as you haven’t increased the number of buses, you just 
increased the capacity of a bus.  If you have opt for two buses then it is ‘Horizontal Scaling’ as you have 
increased the number of buses (resources).  

#  Vertical Scaling  

To increase the capacity if we increase resources in same logical unit/server then it is vertical scaling.
E.g. Add more CPUs in existing sever. If system is not handled by one CPU then increase the CPU to 3 or 4.
Another example is server is having 8 GB RAM then scale it to 16 GB. Same applicable to storages also.  

Consider you have a business website. As business grows you website gets more hits. Due to increase in 
hits your  server   performance starts degrading. To handle the load you need to scale the resources by 
adding CPUs(Processors),RAM, disk capacity etc. So in this case if you are using vertical scaling strategy 
then you need to enhance the capabilities of same server/node which will handle the load properly .Vertical 
scaling means boosting the power of individual server.  

The example in image shows same concept. To serve more passengers instead of adding one more bus we are just 
increasing the capacity of same bus by adding one floor to bus to accommodate 50 passengers.  

Vertical scaling is also called Scale up approach.  

# Horizontal Scaling  

As mentioned in above website example, when your business grows at the same time hits also grows so the responsibility 
of your server/node grows.  So to reduce this responsibility what we can do is we can add one more server with same 
capacity along with existing server. Now these two servers can handle the traffic effectively. This is what called 
horizontal scaling. We have not changed capacity of individual server but we decreased the load on server.

Horizontal scaling means enhancing the performance of server /node by adding more instances of server to your pool 
of servers so that load can be spread.

Horizontal scaling means scaling out. Horizontal scalability can be achieved with the help of clustering, 
distributed file system, load – balancing.

To address performance issues you can use either vertical scaling or horizontal scaling or both in cloud environments.

In cloud market some auto scalable models are present which are smarter than traditional scaling models and gives 
best performance & no down time.
