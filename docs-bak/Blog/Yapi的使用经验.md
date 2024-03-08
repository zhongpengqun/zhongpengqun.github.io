## Deploy Yapi via docker on Ubuntu

##### Install mongodb

```shell
ls
```


<a href="https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-ubuntu/"> 参考文章 </a>




##### 浏览器安装 cross-request chrome 插件
xxx

##### 全过程中我遇到的问题及解决方法
1.
```
bash: gpg: command not found
```
解决方法：
```shell
apt-get install gpg

// amd64 是你的cpu架构，我的因为是树莓派，所以是arm64
echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-7.0.gpg ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/7.0 multiverse" uj /etc/apt/sources.list.d/mongodb-org-7.0.list

echo "mongodb-org hold" | dpkg --set-selections
echo "mongodb-org-database hold" | dpkg --set-selections
echo "mongodb-org-server hold" | dpkg --set-selections
echo "mongodb-mongosh hold" | dpkg --set-selections
echo "mongodb-org-mongos hold" | dpkg --set-selections
echo "mongodb-org-tools hold" | dpkg --set-selections
```


2.
```
Error: getaddrinfo ENOTFOUND yapi.demo.qunar.com
```
解决方法：
<a href="https://github.com/YMFE/yapi/issues/2180#issuecomment-1423701471"> Github issues </a>


## Deploy Yapi, Docker部署
<a href="https://blog.csdn.net/Chimengmeng/article/details/132074922"> 参考文章 </a>


```shell
docker run -d \
   --name yapi3 \
   --link mongodb:mongo \
   --restart always \
   --net=yapi \
   -p 3000:3000 \
   -v /data/yapi/config.json:/yapi/config.json \
   zhongpengqun/yapi:latest \
   server/app.js
```


<img src="https://github.com/zhongpengqun/zhongpengqun.github.io/blob/main/docs/assets/blog/yapi-1.png?raw=true" width="100%" />

```
验证结果
执行脚本:
assert.notEqual(status, 404)
assert.deepEqual(body, {"code": 0})
Error: EROFS: read-only file system, mkdir '/sys/fs/cgroup/cpu/safeify'
Error: EROFS: read-only file system, mkdir '/sys/fs/cgroup/cpu/safeify'
```
解决方法：
<a href="https://blog.csdn.net/iaiti/article/details/125385365"> 参考文章 </a>

备份 sandbox.js
const Safeify = require('safeify').default;

module.exports = async function sandboxFn(context, script)
    // ...... safeify ......
    const safeVm = new Safeify({
        timeout: 3000,
        // zhong
        unrestricted: true,
        asyncTimeout: 60000
    })

    // ..................
    const result = await safeVm.run(script, context)

    // ............
    safeVm.destroy()
    return result
}






------------
3.  统一的权限控制和流量控制，降低开发成本





@string
@natural
// "@float(0, 1000, 1, 3)", // 0-1000小数,1-3位小数位
@float
@character
@boolean
@url
@domain
@ip
@id
@guid
@now
@timestamp
@date
@time
@datetime
// "@image(200x200)", 图片和大小
@image
@color
@hex
@rgba
@rgb
@hsl
// "phone|11": "@integer(0,9)", // 11个数字0-9间的数字
// "cardNum": "@integer(10000)", //大于1000的正整数
@integer
@email
@paragraph
@sentence
@word
@cparagraph
@ctitle
@title
@name
@cname
@cfirst
@clast
@first
@last
@csentence
@cword
@region
@province
@city
@county
@upper
@lower
@pick
@shuffle
@protocol


"regexp": /[a-z][A-Z][0-9]/,   三个之间随机的一个数


- 概念：测试集合

- 开启json5
    - `JSON5是对JSON的扩展，让人可以更容易手工编写和维护，用来减少一些JSON的限制，诸如json语法不支持注释，不支持字符串换行，所有的key都必须双引号，末尾不能有多余的逗号…等等，一大堆极其严格的要求和不支持的功能`


- 注：Test 脚本只有做自动化测试才执行
