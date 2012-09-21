# Redis Sentinel & <br /> RedisKeeper
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

[Rediskeeper on Code](http://code.dapps.douban.com/rediskeeper)

---
## Redis Sentinel
* Monitor & auto-failover tool provided by redis.
* A special execution mode of redis server
* Form a distributed system on top of redis protocol.
* Peer synchronization with custom API.
* Work in progress, currently in unstable branch.

[Redis Unstable on GitHub](https://github.com/antirez/redis/branches/unstable)

---
## General Process

1. Load cluster configurations
1. Use INFO command to get current master.
1. Monitor all masters and slaves, with polling statuses.
1. Start failover process when master down or unresponsive.
1. Notify all clients about the configuration change, when failover process done.

---
## Failure Detection
* Redis Sentinel
    * Server is pinged every second, and queried by INFO every 10s.
    * Server becomes unresponsive without replies in 30s by default.
* RedisKeeper
    * Servers are queried every second, by INFO command.
    * Server is marked unusable when error occurs.

---
## Status Agreement
* Redis Sentinel
    * Mark unresponsive server as _Subjective Down_ or _SDOWN_, locally.
    * As master in SDOWN, every sentinel is asked for the master status.
    * _Objective Down_ or _ODOWN_ means marked as SDOWN by a majority.
* RedisKeeper (Planning)
    * Status decided only by the leader.
    * Agreement reached in assistance of zookeeper.

---
## Leader Election
* Redis Sentinel
    * Sentinel available with the lowest runid is _Subjective Leader_.
    * Chatty protocol to query Subjective Leaders
    * Subjective Leader of a majority becomes _Objective Leader_.
* RedisKeeper(Planning)
    * Using zookeeper.
---
## Promoted Slave Selection
* Redis Sentinel
    * Available slave with the lowest priority.
    * Available slave with the lowest runid.
* RedisKeeper
    * Available master with the most slaves.
    * Available server with the most connections.
    * Available server with the longest uptime.

---
## Peer Discovery & Notification
* Redis Sentinel
    * With master's Pub/Sub channel
    * Publish message every 5s to others.
    * Client subscribe sentinel's channels for notification
* RedisKeeper
    * Using zookeeper's notification event.

---
## Tilt Mode
* Redis Sentinel
    * Time-sensitive protocols.
    * Enter tilt mode when timer skews
    * Stop acting at all
    * Leave tilt mode when everything is normal for 30s.

---

<!-- 
vim: filetype=markdown
-->
