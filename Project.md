## 项目简介

### 业务关系

申请单 1:n 票据单（付款、收款） 1:1 订单


表：user_auth
设置联合唯一：UNIQUE (`auth_type`, `auth_key`)
被锁定，被删除的用户不能再用此账号重复注册。


账号绑定
```
会员主账号
绑定第三方
一个主账号只能绑定一种类型的一个三方账号
一种类型的一个三方账号也只能绑定一个主账号
```


会员层级（membership）
MongoDB 单个文档有16M的限制，内嵌不要太多，可以用引用替代
如下，仅仅保留父节点id即可
```
{
    "user_id": "",
    "user_pid": "",
}
```

会员登录日志（login_log_member）
```
{
    "user_id": "",
    "time": "",
    "ip": "",
}
```

后台登录日志（login_log_admin）
```
{
    "user_id": "",
    "time": "",
    "ip": "",
}
```

后台操作日志（operation_log_admin）
```
{
    "admin_id": "",
    "op_type": "",
    "op_content": "",
    "time": "",
    "ip": "",
}
```
