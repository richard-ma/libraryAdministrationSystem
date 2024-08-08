<html>
    <head>
        <title>Book Detail</title>
    </head>
    <body>
        <form action="{{ url_for("book_update", book_id=id) }}" method="post">
        <label>id</label><input type="text" name="id" value="{{ id }}" />
        <label>书名</label><input type="text" name="title" value="{{ title }}" />
        <label>作者</label><input type="text" name="author" value="{{ author }}" />
        <label>出版社</label><input type="text" name="publisher" value="{{ publisher }}" />
        <label>ISBN</label><input type="text" name="isbn" value="{{ isbn }}" />
        <input type="submit" />
        </form>
    </body>
</html>