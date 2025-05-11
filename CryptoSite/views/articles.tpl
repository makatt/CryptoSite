<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Полезные статьи</title>
    <link rel="stylesheet" href="/static/styles.css">
</head>
<body>
    <h1>Полезные статьи</h1>

    % if error:
        <p style="color:red">{{error}}</p>
    % end

    <form method="post" action="/articles">
        <label>Автор или Компания:</label><br>
        <input type="text" name="author" value="{{author or ''}}"><br>

        <label>Описание статьи:</label><br>
        <textarea name="text">{{text or ''}}</textarea><br>

        <label>Дата (ГГГГ-ММ-ДД):</label><br>
        <input type="text" name="date" value="{{date or ''}}"><br>

        <label>Телефон (например, +79991234567):</label><br>
        <input type="text" name="phone" value="{{phone or ''}}"><br><br>

        <input type="submit" value="Разместить">
    </form>

    <hr>
    <h2>Список статей</h2>
    % for item in articles:
        <div>
            <strong>{{item['author']}}</strong> ({{item['date']}}) — {{item['phone']}}<br>
            <p>{{item['text']}}</p>
            <hr>
        </div>
    % end
</body>
</html>
