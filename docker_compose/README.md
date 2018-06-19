### 下载   
    wget http://labfile.oss-cn-hangzhou.aliyuncs.com/courses/980/software/docker-compose-Linux-x86_64
### 安装
    sudo mv docker-compose-Linux-x86_64 /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose
### 运行
    cd app && docker-compose up
    docker-compose up -d 后台运行
    docker-compose ps 查看容器
    docker-compose images 查看镜像
### 删除
    docker-compose down
