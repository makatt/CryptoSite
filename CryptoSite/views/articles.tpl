% rebase('layout.tpl', title='Полезные статьи', year=year)

<div class="jumbotron">
    <h1>Полезные статьи</h1>
    <p class="lead">Поделитесь своими знаниями или прочитайте, что написали другие.</p>
</div>

<div class="row">
    <div class="col-md-6">
        <h2>Добавить статью</h2>
        % if error:
            <div class="alert alert-danger">{{error}}</div>
        % end
        <form method="post" action="/articles">
            <div class="form-group">
                <label for="author">Автор или Компания</label>
                <input type="text" class="form-control" id="author" name="author" value="{{author or ''}}">
            </div>
            <div class="form-group">
                <label for="text">Описание статьи</label>
                <textarea class="form-control" id="text" name="text">{{text or ''}}</textarea>
            </div>
            <div class="form-group">
                <label for="date">Дата (ГГГГ-ММ-ДД)</label>
                <input type="text" class="form-control" id="date" name="date" value="{{date or ''}}">
            </div>
            <div class="form-group">
                <label for="phone">Телефон (например, +79991234567)</label>
                <input type="text" class="form-control" id="phone" name="phone" value="{{phone or ''}}">
            </div>
            <button type="submit" class="btn btn-primary mt-2">Разместить</button>
        </form>
    </div>

    <div class="col-md-6">
        <h2>Список статей</h2>
        % if not articles:
            <p>Пока нет статей. Будьте первым!</p>
        % else:
            % for item in articles:
                <div class="card mb-3">
                    <div class="card-body">
                        <h5 class="card-title">{{item['author']}}</h5>
                        <h6 class="card-subtitle mb-2 text-muted">{{item['date']}} — {{item['phone']}}</h6>
                        <p class="card-text">{{item['text']}}</p>
                    </div>
                </div>
            % end
        % end
    </div>
</div>
