### 创建swarm
    docker swarm init --advertise-addr=eth0
    docker info|grep "swarm" 查看swarm信息
### 添加节点
    docker swarm join-token manager 获取添加管理节点的命令
    docker swarm join-token worker 获取添加工作节点的命令
    docker node ls 列出节点
    docker node rm NODE_NAME 移除节点
### 权限
    docker node promote NODE_NAME 提权
    docker node demote NODE_NAME 撤权
## docker-compose+docker swarm
    docker stack deploy -c docker-compose.yml app
    docker service ls 查询所有服务
    docker stack ls 查询所有堆栈
    docker ps 如果多节点 每个节点上面显示都不同
    docker stack services app 查询app堆栈信息
    docker stack ps app 查询app堆栈任务
    docker service ps app_redis 查询app_redis服务的任务
    docker stack rm app 移除app堆栈的所有服务
    docker service rm app_redis 移除一个活多个服务
