# libraryAdministrationSystem

## 安装flask
1. pip install flask

## 最小化flask程序
1. 编写hello world的app.py程序
1. 运行程序并在浏览器中得到结果

## 使用sqlalchemy操作数据库
1. 安装sqlalchemy以及flask相关插件
1. 设置数据库路径和参数
1. 创建init.py初始化app

## 书籍信息
1. 书籍类Book
    1. 书籍id：整型（只有整型可以自增）
    1. 书籍名称：字符串
    1. 作者：字符串
    1. 出版社：字符串
    1. ISBN码：字符串
    1. 是否可借：布尔/默认True
    1. 借阅人id：字符串/默认None
    1. 应还时间：日期/默认None
1. 书籍类方法：
    1. borrow_by(user)
        1. 将书籍是否可借设置为False
        1. 借阅人id设置为user.get_id()
        1. 应还时间为当前日期加30天
        1. 保存修改
1. 页面设计
    1. 书籍列表
    1. 添加书籍
    1. 删除书籍
    1. 书籍信息更新

## 用户信息
1. 用户类User
    1.用户id：字符串（为用户名，由用户指定）
    1.密码：字符串
1. 用户类方法：
    1. get_id()
        1.返回当前用户的id
    1. check_password(password)
        1. 读取用户存储的password
        1. 返回用户存储的password和参数password是否一致
1. 页面设计
    1. 用户登陆
    1. 用户登陆失败
    1. 用户注册

## 安装使用
1. pip install -r requirements.txt
1. python init.py
1. flask run/flask run --debug(调试模式)