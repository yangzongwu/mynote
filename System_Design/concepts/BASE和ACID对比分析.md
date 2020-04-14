转载 https://blog.csdn.net/u014439239/article/details/80269849  
# CAP理论  
# CAP – Consistency, Availability, Partition Tolerance  
* C表示一致性，为最终一致性。  
* A表示可用性，三副本保证数据安全。  
* P表示分区容错性，表示某些节点crash系统是否还能正常工作。  
其中一致性、可用性、分区容错性不能够同时满足，只能够对其一致性或可用性进行取舍。  
#  CAP两种选择  
分布式数据库因相对于关系型数据库最显著的特性是，数据保存在多个节点上这种属性。P（Partition Tolerance）的特性一定要保留，所以只能在一致性和可用性上考虑。  
* 放弃A（Availability）  
我们需要保证一致性, 原子性. 当一个数据被别人操作或数据节点出现异常时, 你就必须等待, 等待时就无法保证可用性.。
* 放弃C（Consistency）  
相比较一些场景，一致性性并不是那么高，需要的是比较高的可用性。短时间内不需要数据的一致性，最终会在其他节点同步完成保持一致。  

放弃一致性即为BASE模式，当节点放弃可用性即为ACID模式。  
# ACID  
关系数据库, 最大的特点就是事务处理, 即满足ACID；  
ACID可以理解为ACID最重要的含义，就是Atomicity和Isolation ，即强制一致性，要么全做要么不做，所有用户看到的数据一致。强调数据的可靠性, 一致性和可用性。
ACID 为 Atomicity, Consistency, Isolation, and Durability，其中ACID分别表示为：  
* 原子性（Atomicity）：事务中的操作要么都做，要么都不做。  
* 一致性（Consistency）：系统必须始终处在强一致状态下。  
* 隔离性（Isolation）：一个事务的执行不能被其他事务所干扰。  
* 持续性（Durability）：一个已提交的事务对数据库中数据的改变是永久性的。  

保证ACID是传统关系型数据库中事务管理的重要任务，几种事务类型为：未提交读、可提交读、可重复读、可序列化。  
# BASE  
分布式数据库, 最大的特点就是分布式，即满足BASE，ASE方法通过牺牲一致性和孤立性来提高可用性和系统性能。  
BASE为Basically Available, Soft-state, Eventually consistent，其中BASE分别代表：  
* 基本可用（Basically Available）：系统能够基本运行、一直提供服务。  
* 软状态（Soft-state）：系统不要求一直保持强一致状态。  
* 最终一致性（Eventual consistency）：系统需要在某一时刻后达到一致性要求。  

表示为支持可用性，牺牲一部分一致性，可以显著的提升系统的伸缩性，数据为最终一致。和ACID为相反的方向。其中事务支持不会很高。  
