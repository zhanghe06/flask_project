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
email
phone
birthday
create_time
update_time
last_ip
```
用户授权信息表 user_auth
```
id
user_id
auth_type       登录类型（手机号 邮箱 用户名）或第三方应用名称（微信 微博等）
auth_key        标识（手机号 邮箱 用户名或第三方应用的唯一标识）
auth_secret     密码凭证（站内的保存密码，站外的不保存或保存token）
auth_expires    过期时间
verified        验证状态（手机号，邮箱是否验证　默认第三方登录都是已验证）
```

### 用户登录处理过程：

判断用户登录请求类型
```
邮箱/用户名/手机号/第三方
```

查询用户是否存在
```
SELECT * FROM user_auth WHERE auth_type='登录类型' and auth_key='账号标识'
```

校验用户凭证（密码）
```
SELECT * FROM user_auth WHERE id='user_auth.id' and auth_secret='password_hash(密码)'
```

查询用户信息
```
SELECT * FROM user WHERE id='user_id'
```


应用场景：

验证用户是否存在
```
SELECT * FROM user_auth WHERE auth_type='phone' and auth_key='手机号'
SELECT * FROM user_auth WHERE auth_type='email' and auth_key='邮箱'
SELECT * FROM user_auth WHERE auth_type='qq' and auth_key='QQ号码'
SELECT * FROM user_auth WHERE auth_type='weixin' and auth_key='微信UserName'
```
如果有记录，则直接登录成功，使用新的 token 更新原 token。


### 优点与缺点

- 缺点
    - sql 请求增加为 2 次
    - 用户同时存在邮箱、用户名、手机号等多种站内登录方式时，改密码时必须一起改
    - 代码量增加了，有些情况下逻辑判断增加了，难度增大了。

## 本地调试

github 直接设置本地地址调试即可

qq 需要准备可访问的域名，并验证，再修改 hosts 域名指向本机


## Web系统认证信息传递

服务端可以用 session 保持用户登陆状态，代价却是内存占用高，单台服务器变成有状态，无法简单扩展成集群。仅供演示

生产环境可以使用 cookie 实现

但是如果需要存储大量的会话数据，将数据从cookie移动到服务器是有意义的


## 第三方登录与本地注册、绑定流程的结合

- 用户直接注册（系统自动生成 uid）
    - 邮箱注册，验证邮件
    - 手机注册，验证短信
    - 校验通过，

- 用户本地登录
    - 未经校验，提示校验
    - 校验通过，执行登录

- 第三方登录，系统提示:
    - 绑定, 与本地系统账号绑定
    - 注册
    - 用户离开，不处理


## 会话管理

参考：http://flask.pocoo.org/snippets/75/

- 多终端同时登陆

- 多终端单台登陆

- 多系统共享登陆

session 在服务端存储的数据结构

{
    'session_id': {
        'user_name': '',
    }
}