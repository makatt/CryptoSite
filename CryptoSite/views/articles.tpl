% rebase('layout.tpl', title='Полезные статьи', year=year)

<div class="jumbotron bg-light">
    <div class="container">
        <h1 class="display-4">Полезные статьи</h1>
        <p class="lead">Поделитесь своими знаниями или узнайте что-то новое из публикаций сообщества</p>
    </div>
</div>

<div class="container my-5">
    <!-- Секция со статьями -->
    <section class="mb-5">
        <h2 class="mb-4 pb-2 border-bottom">Последние публикации</h2>

        % if not articles:
            <div class="alert alert-info text-center">
                <i class="fas fa-info-circle mr-2"></i>Пока нет статей. Будьте первым, кто поделится знаниями!
            </div>
        % else:
            <div class="row">
                % for i, item in enumerate(articles):
                <div class="col-md-6 mb-4">
                    <div class="card article-card bg-light {{ 'border-success' if i == 0 else '' }}" style="min-height: 100%;">

                        % if i == 0:
                        <div class="card-header bg-success text-white">
                            <span class="badge badge-light mr-2">Новое!</span> Самая свежая статья
                        </div>
                        % end
                        <div class="card-body">
                            <h5 class="card-title">{{item['author']}}</h5>
                            <h6 class="card-subtitle mb-3 text-muted">
                                <i class="far fa-calendar-alt mr-1"></i>{{item['date']}} 
                                <span class="mx-2">|</span>
                                <i class="fas fa-envelope mr-1"></i>{{item['email']}}
                            </h6>
                            <p class="card-text article-scroll">{{item['text']}}</p>

                        </div>
                    </div>
                </div>
                % end
            </div>
        % end
    </section>

    <!-- Секция с формой добавления -->
    <section class="p-4 rounded" style="background-color: #000; color: #fff;">


        <h2 class="mb-4 text-center">Добавить свою статью</h2>

        % if error:
        <div class="alert alert-danger alert-dismissible fade show">
            {{error}}
            <button type="button" class="close" data-dismiss="alert">
                <span>&times;</span>
            </button>
        </div>
        % end

        <form method="post" action="/articles" class="needs-validation" novalidate id="articleForm">
            <div class="form-row">
                <div class="col-md-6 mb-3">
                    <label for="author">Автор или компания</label>
                    <input type="text" class="form-control" id="author" name="author" 
                           value="{{author or ''}}" required pattern="^[^\d]+$">
                    <div class="invalid-feedback">
                        Пожалуйста, укажите имя без цифр.
                    </div>
                </div>
                <div class="col-md-6 mb-3">
                    <label for="date">Дата публикации</label>
                    <input type="date" class="form-control" id="date" name="date" 
                           value="{{date or ''}}" required>
                </div>
            </div>

            <div class="form-group">
                <label for="text">Текст статьи</label>
                <textarea class="form-control" id="text" name="text" rows="6" 
                          minlength="100" required>{{text or ''}}</textarea>
                <small class="form-text text-muted">
                    Минимум 100 символов.
                </small>
                <div class="invalid-feedback">
                    Пожалуйста, напишите статью длиной не менее 100 символов.
                </div>
            </div>

            <div class="form-group">
                <label for="email">Контактный e-mail</label>
                <input type="email" class="form-control" id="email" name="email"
                       value="{{email or ''}}" placeholder="example@mail.com" required>
                <div class="invalid-feedback">
                    Укажите корректный адрес электронной почты.
                </div>
            </div>

            <div class="text-center mt-4">
                <button type="submit" class="btn btn-primary btn-lg px-4">
                    <i class="fas fa-paper-plane mr-2"></i>Опубликовать статью
                </button>
            </div>
        </form>
    </section>
</div>

<script>
// Валидация формы
(function() {
    'use strict';
    window.addEventListener('load', function() {
        var form = document.getElementById('articleForm');
        form.addEventListener('submit', function(event) {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        }, false);
    }, false);
})();

// Устанавливаем текущую дату по умолчанию
document.addEventListener('DOMContentLoaded', function() {
    const dateInput = document.getElementById('date');
    if (dateInput && !dateInput.value) {
        const today = new Date();
        const formattedDate = today.toISOString().substr(0, 10);
        dateInput.value = formattedDate;
    }
});
</script>
