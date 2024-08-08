from app import app, db
import user, book


# 创建所有数据表
with app.app_context():
    db.create_all()

    # 创建测试数据
    books = [
        ["朝花夕拾", "鲁迅", "湖南文艺出版社", "123"], 
        ["我与地坛", "史铁生", "天津文艺出版社", "234"], 
        ["罪与罚", "陀思妥耶夫斯基", "俄罗斯出版社", "345"], 
        ["根鸟", "曹文轩", "天津人艺出版社", "456"], 
        ["活着", "余华", "三联书局", "567"], 
        ["兄弟", "余华", "机械工业出版社", "678"], 
        ["乡土中国", "费孝通", "百花文艺出版社", "789"], 
        ["三体", "刘慈欣", "科幻世界", "890"], 
    ]

    users = [
        ["admin", "admin"],
        ["user", "user"],
        ["client", "client"],
        ["test", "test"],
    ]

    for item in books:
        b = book.Book()
        b.title, b.author, b.publisher, b.isbn = item
        db.session.add(b)

    for item in users:
        u = user.User()
        u.id, u.passwrod = item
        db.session.add(u)

    db.session.commit()