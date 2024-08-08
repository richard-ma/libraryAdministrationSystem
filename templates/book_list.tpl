<html>
    <head>
        <title>Book list</title>
    </head>
    <body>
        <table>
            <tbody>
                <tr>
                    <th>#</th>
                    <th>书名</th>
                    <th>作者</th>
                    <th>出版社</th>
                    <th>ISBN</th>
                    <th>是否可借</th>
                    <th>借阅人</th>
                    <th>应还时间</th>
                    <th>操作</th>
                </tr>
{% for book in books %}
                <tr>
                    <td>{{ book.id }}</td>
                    <td><a href="{{ url_for("book_update", book_id=book.id) }}">{{ book.title }}</a></td>
                    <td>{{ book.author }}</td>
                    <td>{{ book.publisher }}</td>
                    <td>{{ book.isbn }}</td>
                    <td>{{ book.can_borrowed }}</td>
                    <td>{{ book.borrow_by | default("---") }}</td>
                    <td>{{ book.return_date | default("---") }}</td>
                    <td><a href="{{url_for("book_delete", book_id=book.id)}}">删除书籍</a></td>
                </tr>
{% endfor %}
            </tbody>
        </table>
    </body>
</html>