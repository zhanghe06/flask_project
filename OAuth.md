### GitHub

Setup Application：[https://github.com/settings/applications/new](https://github.com/settings/applications/new)


### QQ

QQ 互联：[http://connect.qq.com/manage/](http://connect.qq.com/manage/)


### WeiBo

微博开放平台：[http://open.weibo.com/](http://open.weibo.com/)


## 第三方登录系统数据库设计

登录方式：
username + password
phone + password
open_id + access_token


抽象成　用户基础信息表　和　用户授权信息表
用户信息表和用户授权表是一对多的关系

用户基础信息表 user
```
id
nickname
avatar
```
用户授权信息表 user_auth
```
id
user_id
identity_type 登录类型（手机号 邮箱 用户名）或第三方应用名称（微信 微博等）
identifier 标识（手机号 邮箱 用户名或第三方应用的唯一标识）
credential 密码凭证（站内的保存密码，站外的不保存或保存token）
```

### 用户登录处理过程：

判断用户登录请求类型
```
邮箱/用户名/手机号/第三方
```

查询用户是否存在
```
SELECT * FROM user_auth WHERE identity_type='登录类型' and identifier='账号标识'
```

校验用户凭证（密码）
```
SELECT * FROM user_auth WHERE id='user_auth.id' and credential='password_hash(密码)'
```

查询用户信息
```
SELECT * FROM user WHERE id='user_id'
```


应用场景：

验证用户是否存在
```
SELECT * FROM user_auth WHERE type='phone' and identifier='手机号'
SELECT * FROM user_auth WHERE type='email' and identifier='邮箱'
SELECT * FROM user_auth WHERE type='qq' and identifier='QQ号码'
SELECT * FROM user_auth WHERE type='weixin' and identifier='微信UserName'
```
如果有记录，则直接登录成功，使用新的 token 更新原 token。


## 本地调试

github 直接设置本地地址调试即可

qq 需要准备可访问的域名，并验证，再修改 hosts 域名指向本机
