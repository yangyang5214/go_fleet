# go_fleet

### jobs

#### leetcode 每日一题

配置微信的自建应用，然后发送到指定的 **touser**

文档：https://work.weixin.qq.com/api/doc/90000/90135/90236#%E6%96%87%E6%9C%AC%E6%B6%88%E6%81%AF

```
cat /opt/wechat.json 
{
    "corpid": "xxx",
    "corpsecret": "xxxx"
    "agentid": "xxx",
    "touser": "xxxx"
}
```

run:

```
cd go_fleet/jobs
go run main.go
```