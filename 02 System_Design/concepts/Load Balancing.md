### Load balancer (LB)  
Is another critical piece of any distributed system. It helps to distribute load across multiple resources 
according to some metric (random, round-robin, random with weighting for memory or CPU utilization, etc.). 
LB also keeps track of the status of all the resources while distributing requests. If a server is not 
available to take new requests or is not responding or has elevated error rate, LB will stop sending traffic 
to such a server.  

To utilize full scalability and redundancy, we can try to balance the load at each layer of the system. We can 
add LBs at three places:    
*	Between the user and the web server  
*	Between web servers and an internal platform layer, like application servers or cache servers  
*	Between internal platform layer and database.  
 
### There are many ways to implement load balancing.  

###### Smart Clients  

A smart client will take a pool of service hosts and balances load across them. It also detects hosts that 
are not responding to avoid sending requests their way. Smart clients also have to detect recovered hosts, 
deal with adding new hosts, etc.  

Adding load-balancing functionality into the database (cache, service, etc.) client is usually an attractive 
solution for the developer. It looks easy to implement and manage especially when the system is not large. But 
as the system grows, LBs need to be evolved into standalone servers.  

###### Hardware Load Balancers  

The most expensive–but very high performance–solution to load balancing is to buy a dedicated hardware load 
balancer (something like a Citrix NetScaler). While they can solve a remarkable range of problems, hardware 
solutions are very expensive, and they are not trivial to configure.

As such, even large companies with large budgets will often avoid using dedicated hardware for all their 
load-balancing needs. Instead, they use them only as the first point of contact for user requests to their 
infrastructure and use other mechanisms (smart clients or the hybrid approach discussed in the next section) 
for load-balancing for traffic within their network.  

###### Software Load Balancers  

If we want to avoid the pain of creating a smart client, and since purchasing dedicated hardware is excessive, 
we can adopt a hybrid approach, called software load-balancers.  

HAProxy is one of the popular open source software LB. Load balancer can be placed between client and server or 
between two server side layers. If we can control the machine where the client is running, HAProxy could be 
running on the same machine. Each service we want to load balance can have a locally bound port 
(e.g., localhost:9000) on that machine, and the client will use this port to connect to the server. 
This port is, actually, managed by HAProxy; every client request on this port will be received by the 
proxy and then passed to the backend service in an efficient way (distributing load). If we can’t manage 
client’s machine, HAProxy can run on an intermediate server. Similarly, we can have proxies running between 
different server side components. HAProxy manages health checks and will remove or add machines to those pools. 
It also balances requests across all the machines in those pools.  

For most systems, we should start with a software load balancer and move to smart clients or hardware load 
balancing as need arises.  

# 算法  
### 均匀派发（Even Task Distribution Scheme）  
均匀派发是实现负载均衡最简单的策略，均衡派发的意思是指任务将均匀地派发到所有的服务器进程。在实现时，可以使用随机派
发或者轮流派发（Round Robin）。  
均匀派发策略假设集群内所有进程具有相同的处理能力，且任务处理用时相同。但实际上，由于进程部署环境的不同，其处理能力一
般不同，任务处理时间也不尽相同。因此均匀派发的策略并不能很好地将任务负载均滩到各个进程中。  

### DNS负载均衡  
我们知道，DNS提供域名解析服务，当我们访问某个站点时，实际上首先需要通过该站点域名的DNS服务器来获取指向该域名的IP地址，
在这过程中，DNS服务器完成了域名到IP地址的映射。由于这一映射可以是一对多的关系，因此DNS服务器可以充当负载均衡器的作用，
DNS服务器在派发IP地址时，正是使用轮流派发的方式来实现的。  

### 加权派发（Weighted Task Distribution Scheme）  
加权派发策略在派发任务时，会赋予服务器进程一个权值，即不同的进程会接受不同数量的任务，具体数量为权值确定。  
例如，三个进程的处理任务的能力比率为3:3:2，那么可以赋予这三个进程3:3:2的权值，即每8个任务中，3个发派给第一个进程，
3个发派给第二个进程，2个分派给第三个进程。   
加权派发策略考虑了进程处理能力的不同，因此更接近实际的应用。可是，加权派发策略也没有考虑任务处理的要求。  

### 粘滞会话（Sticky Session Scheme）  
前面两种负载均衡策略并没有考虑任务之间的依赖关系，在实际中，后面的任务处理常常会依赖于前面的任务。例如，对于同一个登录的用户的请求，用户购买的请求依赖于用户登录的请求，如果用户的登录信息保存在进程1中，那么，如果购买请求被分派到进程2或者进程3，那么购买请求将不能正确处理。这种请求间的依赖关系也称为粘滞会话（Sticky Session），负载均衡策略需要考虑粘滞会话的情况。  
粘滞会话的派发策略要求属于同一个会话的任务将会被分派到同一个进程中。虽然这可以正确处理任务，但是却带来任务派发不均匀的问题，因为一些会话可能包含更多的任务，一些会话包含更少的任务。   
粘滞会话的另一种处理策略是使用数据库或者缓存，将所有会话数据存储到数据库或者缓存中。集群内所有进程都可以通过访问数据库或者缓存来获取会话数据，进程内存都不保存会话数据，这样，负载均衡器便可以使用前面介绍的策略来派发任务。  

### 均匀任务队列派发（Even Size Task Queue Distribution Scheme）  
均匀任务队列派发策略跟加权派发策略类似，都考虑了进程的处理能力，不过其实现方式不同。在均匀队列派发策略下，负载均衡器为每个进程都创建一个大小相等的任务队列，这些任务队列包含了对应进程需要处理的任务。任务处理快的进程，其队列也会减少得快，这样负载均衡器会派发更多的任务给这个进程；相应地，任务处理慢的进程，其队列也会减少得慢，这样负载均衡器会派发更少的任务给这个进程。因此，通过这些任务队列，负载均衡器在派发任务时将进程处理任务的能力因素考虑了进去。  
### 单一队列（Autonomous Queue Scheme）  
与上面的均匀队列策略一样，单一队列策略也使用了队列来实现负载均衡。不同的是，单一队列策略只使用了一个队列。图6是单一队列策略的原理图。  
单一队列策略中，实际上并没有负载均衡器的存在。所有的服务器进程从队列中取出任务执行，如果某个进程出现宕机的情况，那么其他进程仍然可以继续执行任务。这样一来，任务队列并不需要知道服务进程的情况，只需要服务进程知道自己的任务队列，并不断执行任务即可。   
单一队列策略实际上也考虑到进程的处理能力，进程处理任务得越快，其从队列取出任务的速度也越快。  

### 轮询法（Round Robin）  
轮询法是负载均衡中最常用的算法，它容易理解也容易实现。   
轮询法是指负载均衡服务器（load balancer）将客户端请求按顺序轮流分配到后端服务器上，以达到负载均衡的目的。   
假设现在有6个客户端请求，2台后端服务器。当第一个请求到达负载均衡服务器时，负载均衡服务器会将这个请求分派到后端服务器1；当第二个请求到害时，负载均衡服务器会将这个请求分派到后端服务器2。然后第三个请求到达，由于只有两台后端服务器，故请求3会被分派到后端服务器1。依次类推，其示意图如图1所示。  

### 加权轮询法（Weighted Round Robin）  
简单的轮询法并不考虑后端机器的性能和负载差异。给性能高、负载低的机器配置较高的权重，让其处理较多的请求；而性能低、负载高的机器，配置较低的权重，让其处理较少的请求。加权轮询法可以很好地处理这一问题，它将请求顺序且按照权重分派到后端服务器。   
假设有6个客户端请求，2台后端服务器。后端服务器1被赋予权值5，后端服务器2被赋予赋予权值1。这样一来，客户端请求1，2，3，4，5都被分派到服务器1处理；客户端请求6被分派到服务器2处理。接下来，请求7，8，9，10，11被分派到服务器1，请求12被分派到服务器2，依次类推。这个请求分派的过程可以用图2来表示。  

### 最小连接数法（Least Connections）  
即使后端机器的性能和负载一样，不同客户端请求复杂度不一样导致处理时间也不一样。最小连接数法根据后端服务器当前的连接数情况，动态地选取其中积压连接数最小的一台服务器来处理当前的请求，尽可能提高后端服务器的利用效率，合理地将请求分流到每一台服务器。   
为什么根据连接数可以合理地利用服务器处理请求呢？   
考虑一个客户端请求的处理逻辑较复杂，需要服务器的处理时间较长，由于客户端需要等待服务器的响应，故需要保持与服务器的连接，这样一来，客户端就需要与服务器保持较长时间的连接。   
假设客户端请求1，2，3，4，5已被分派给服务器1和服务器2，其分派的情况如图3所示：  
此时，服务器上的请求1，请求3已处理完毕，与客户端的连接已断开。而请求2，4，5还在服务器上处理，即服务器还保持与这些请求的客户端的连接。   
如果再把请求分派到服务器2，则会导致服务器的请求更多，服务器2的负载更高。如果考虑服务器的连接数，当前服务器1的连接数为1，服务器2的连接数为2，将请求分派到服务器1，则负载相对均衡。采用最小连接数法的分派方法如图4所示：  

### 随机法（Random）  
随机法也很简单，就是随机选择一台后端服务器进行请求的处理。由于每次服务器被挑中的概率都一样，客户端的请求可以被均匀地分派到所有的后端服务器上。  

### 源地址哈希法（Source Hashing）  
源地址哈希的思想是根据获取客户端的IP地址，通过哈希函数计算得到的一个数值，用该数值对服务器列表的大小进行取模运算，得到的结果便是客服端要访问服务器的序号。采用源地址哈希法进行负载均衡，同一IP地址的客户端，当后端服务器列表不变时，它每次都会映射到同一台后端服务器进行访问。   
如果后端服务器是一缓存系统，当后端服务器增加或者减少时，采用简单的哈希取模的方法，会使得命中率大大降低，这个问题可以采用一致性哈希的方法来解决。   

参考资料  
https://blog.csdn.net/lihao21/article/details/53900447  
https://blog.csdn.net/lihao21/article/details/54695471  
