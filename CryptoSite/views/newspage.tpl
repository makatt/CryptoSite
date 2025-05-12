%# -*- coding: utf-8 -*-
% rebase('layout.tpl', title=title, year=year)

<div class="container mt-4">
    <h1 class="mb-4">{{ title }}</h1>
    
    % if error:
        <div class="alert alert-danger alert-dismissible fade show">
            {{ error }}
            <button type="button" class="close" data-dismiss="alert">
                <span>&times;</span>
            </button>
        </div>
    % end
    
    <div class="row">
        <!-- Список новостей -->
        <div class="col-md-8">
            <h2 class="mb-3">Последние новости</h2>
            
            % if not news_items:
                <div class="alert alert-info">
                    Пока нет новостей. Будьте первым, кто добавит новость!
                </div>
            % else:
                % for item in news_items:
                <div class="card mb-3 news-item">
                    <div class="card-body">
                        <h3 class="card-title">{{ item.get('title', '') }}</h3>
                        <div class="card-subtitle text-muted mb-2">
                            <small>
                                Опубликовано: {{ item.get('date', '') }} | Автор: {{ item.get('author', '') }}
                            </small>
                        </div>
                        <p class="card-text">{{ item.get('content', '') }}</p>
                    </div>
                </div>
                % end
            % end
        </div>
        
        <!-- Форма добавления новости -->
        <div class="col-md-4">
            <div class="card">
                <div class="card-header bg-primary text-white">
                    <h3 class="mb-0">Добавить новость</h3>
                </div>
                <div class="card-body">
                    <form method="POST" action="/newspage">
                        <div class="form-group">
                            <label for="title">Заголовок</label>
                            <input type="text" class="form-control" id="title" name="title" 
                                   value="{{ form_data.get('title', '') }}" required
                                   minlength="5" maxlength="100">
                        </div>
                        
                        <div class="form-group">
                            <label for="author">Автор</label>
                            <input type="text" class="form-control" id="author" name="author"
                                   value="{{ form_data.get('author', '') }}" required
                                   minlength="2" maxlength="50">
                        </div>
                        
                        <div class="form-group">
                            <label for="date">Дата публикации</label>
                            <input type="date" class="form-control" id="date" name="date"
                                   value="{{ form_data.get('date', '') }}" required>
                        </div>
                        
                        <div class="form-group">
                            <label for="content">Содержание</label>
                            <textarea class="form-control" id="content" name="content" 
                                      rows="5" required minlength="10">{{ form_data.get('content', '') }}</textarea>
                        </div>
                        
                        <button type="submit" class="btn btn-primary btn-block">
                            Опубликовать
                        </button>
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>

<style>
    .news-item {
        border-left: 4px solid #007bff;
        transition: all 0.3s ease;
    }
    .news-item:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
    }
</style>