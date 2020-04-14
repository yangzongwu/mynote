Sharding is necessary if a dataset is too large to be stored in a single database. ... 
Sharding allows a database cluster to scale along with its data and traffic growth. 
Sharding is also referred as horizontal partitioning. The distinction of horizontal vs 
vertical comes from the traditional tabular view of a database  


什么是一致性Hash算法？  
(https://blog.csdn.net/bntX2jSQfEHy7/article/details/79549368)  


(https://www.acodersjourney.com/database-sharding/)
# What is Sharding or Data Partitioning?  
Sharding (also known as Data Partitioning) is the process of splitting a large dataset into 
many small partitions which are placed on different machines. Each partition is known as a "shard".  

Each shard has the same database schema as the original database. Most data is distributed such that 
each row appears in exactly one shard. The combined data from all shards is the same as the data from 
the original database.

# What scalability problems are solved by Sharding?  
As more users are onboarded on your system, you'll experience performance degradation with a single 
database server architecture . Your read queries and updates will start become slower and your network 
bandwidth may be start to saturate . You'll probably start running out of disk space on your database 
server at some point.  

Sharding helps to fix all the above issues by distributing data across a cluster of machines. In theory, 
you can have a huge number of shards thereby providing virtually unlimited horizontal scaling for your database.  

# Is each shard located on a different machine ?  
Each shard may be located on the same machine (coresident) or on different machines(remote).   

The motivation for co-resident partitioning is to reduce the size of individual indexes and reduce the 
amount of I/O (input/output) that is needed to update records.

The motivation for remote partitioning is to increase the bandwidth of access to data by having more RAM 
in which to store data, by avoiding disk access, or by having more network interfaces and disk I/O channels available.  

# What are some common Sharding or Data Partitioning Schemes ?
* Horizontal or Range Based Sharding
* Vertical Sharding
* Key or hash based sharding
* Directory based sharding
