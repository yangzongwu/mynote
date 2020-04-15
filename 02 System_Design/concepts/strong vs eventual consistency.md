转（https://cloud.tencent.com/developer/article/1102914）  

# Strong Consistency  
Strong Consistency，也就是强一致性。传统的关系型数据库是天然的强一致性：当一条数据发生添加、更新操作时，强一致性保证，
在操作完成之后，所有之后查询该条记录的请求都会拿到最新的数据。由于大部分程序员都是从关系型数据库的时代成长起来，因此大
家下意识中会把 Strong Consistency 作为理所应当的事情，但是关系型数据库的 Strong Consistency 是依赖数据加锁实现的，
牺牲了系统的整体性能。  
![avatar](https://ask.qcloudimg.com/http-save/yehe-1675956/ot1mi33wng.png?imageView2/2/w/1620)  
如上图所示，如果该数据库中有三个节点 (node), 如果 update 操作发生在 node A, 当操作完毕时，node A 需要把最新信息 
replicate 到 node B/C, 这时为了保证 strong consistency, 所有在 node B/C 读取该条记录的请求都会被 block, 直到该
条数据完整的从 node A replicate 完毕。  

# Eventual Consistency  
Eventual Consistency 来了：它保证当一个 update/insert 发生后，所有的 read request 会最终 (eventual) 读取到操作发生后的值。
换句话说，假设一条 node A 中一条记录 x = 10, 下一个 update request set x = 20. 如果使用 Eventual Consistency 的架构，
那么之后发生的 read request 仍有可能拿到 x = 10. 只不过最终在未来某个时间点，所有 read request 都会拿到 x = 20. 
但这个时间点是不能保证的。  

#### DNS  
Eventual Consistency是真有用的。比如 Internet 离不开的 DNS 服务就是一个典型的 Eventual Consistency 模型。简单说，
DNS 是一个域名解析服务，当你输入 google.com 的时候他会帮你转化成 google.com 后的具体 IP 地址。如果你有一定的网站部
署经验，一定会遇到类似的情况：当你把自己的域名 (XXX.com) 绑定的 IP 从 IP 1 改到 IP 2 时，很长一段时间内，域名的访问
还是会 hit IP 1, 过了几十分钟，甚至几天，所有的 traffic 才被导到 IP 2.  

#### 为什么这么设计？  
DNS 是一个非常非常大规模的分布式服务。你每打开一个网页，都要经过 DNS 的域名解析。想象一下，如果 DNS 是一个 Strong 
Consistency 的架构，那么假设 google.com 改变了对应的 IP 地址时，世界上所有的 DNS node 都开始 block request to google.com, 
然后等更新完毕之后再 unblock, 这个过程中大家只能对着浏览器发呆，不骂娘才怪。  

但是使用 Eventual Consistency, 也许让 developer 的日子难过一些：迁移过程中需要保证 both old and new IPs 都用能使用，
但对于用户的体验来说，这是无脑选择。  
