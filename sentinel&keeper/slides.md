# Redis Sentinel & RedisKeeper
.fx: cover

<tianzhongbo@douban.com>

2012-09-20

---
## Problems
* Redis is a _store_, rather than a cache.
* Replication can only help with _scalability_, and _redundancy_.
* _Availability_ solutions are badly needed for production use.
* Considering the high throughput, _failover time_ should be minimized.

---
## RedisKeeper
* Homebrew dog food.
* Monitor & auto-failover solution for redis.
* Single node by default, distributed in the future.
* Working with Apache Zookeeper.
* A client-side wrapper is provided.

---
## Redis Sentinel
* Monitor & auto-failover tool provided by redis.
* A special execution mode of redis server
* Form a distributed system on top of redis protocol.
* Peer synchronization with custom API.
* Work in progress, currently in unstable branch.

<!-- 
vim: filetype=markdown
-->
