---
title: "Nginx 部署 Hugo"
date: 2021-11-19T19:10:52-05:00
draft: false
---
Hugo is a powerful static website generator, which can be hosted on Nginx, Github, Gitlab. Here, I will share my experience of
deploying a Hugo website with Nginx on the server.
## Hugo

### Command
```jsx
hugo new site websitename`
hugo builds your site
hugo --buildDrafts/-Dinclude content marked as draft
hugo server` high performance server
hugo server --buildDrafts/-D`include content marked as draft
```
参考
[Hugo builds your site](https://gohugo.io/commands/hugo/)


## Nginx部署

### 安装配置
参考
 [Nginx安装与配置](https://cloud.tencent.com/developer/article/1147804)

### Command

```jsx
cd /usr/local/nginx/sbin/nginx // 路径
./nginx -t // 查看状态
./nginx // 开启
./nginx -s reload // 重启
```

### 配置

```
/usr/local/nginx/conf/nginx.conf 为配置文件
/usr/local/nginx/sbin/nginx -c /usr/local/nginx/conf/nginx.conf 为重启 
```

### 腾讯云防火墙问题

```jsx
service iptables status // 查看防火墙状态
netstat -lnt | grep 80 // 检查80端口是否开放
```
- 或者检查腾讯云防火墙控制面板

参考[【Nginx】启动成功无法访问网页（完整的排除方案）](https://blog.csdn.net/yujing1314/article/details/105225325)


### SSL证书配置https

[Nginx 安装 SSL 配置 HTTPS 超详细完整全过程](https://segmentfault.com/a/1190000022673232)

- 或直接用腾讯云获取免费证书，绑定域名

### 踩坑

- 文件路径设置不对导致css不加载
    - 需查看developer tool: console