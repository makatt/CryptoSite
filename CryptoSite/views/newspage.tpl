%# -*- coding: utf-8 -*-
% rebase('layout.tpl', title=title, year=year)

<style>
    /* Основной черный фон для всей страницы */
    body {
        background-color: #000000;
        color: #ffffff;
    }
    
    /* Стили для карточек криптовалют */    
    .crypto-item {
        border-left: 4px solid #28a745;
        transition: all 0.3s ease;
        background-color: #1a1a1a;
        color: #ffffff;
    }
    .crypto-item:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(255, 255, 255, 0.1);
    }
    #highlight {
        background-color: rgba(40, 167, 69, 0.2);
        border-left: 4px solid #ffc107;
    }
    
    /* Стили для текста и заголовков */
    h1, h2, h3, h4, h5, h6 {
        color: #ffffff;
    }
    
    /* Стили для карточек и форм */
    .card {
        background-color: #1a1a1a;
        border: 1px solid #333;
    }
    
    /* Стили для списка */
    .list-group-item {
        background-color: #1a1a1a;
        color: #ffffff;
        border-color: #333;
    }
    
    /* Стили для формы */
    .form-control {
        background-color: #333;
        color: #ffffff;
        border-color: #555;
    }
    .form-control:focus {
        background-color: #444;
        color: #ffffff;
        border-color: #28a745;
    }
    
    /* Стили для алертов */
    .alert-info {
        background-color: #0066cc;
        color: #ffffff;
        border-color: #0055aa;
    }
    .alert-danger {
        background-color: #cc0000;
        color: #ffffff;
        border-color: #aa0000;
    }
    
    /* Стили для бейджей */
    .badge-success { background-color: #28a745; }
    .badge-warning { background-color: #ffc107; color: #000; }
    .badge-secondary { background-color: #6c757d; }
</style>

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
        <div class="col-md-8">
            <h2 class="mb-3">Новые криптовалюты</h2>
            
            % if not news_items:
                <div class="alert alert-info">
                    Пока нет информации о новых криптовалютах.
                </div>
            % else:
                % for item in news_items:
                <div class="card mb-3 crypto-item shadow-sm" % if str(item.get('id')) == request.query.get('highlight', ''): id="highlight" % end>
                    <div class="card-body">
                        <h3 class="card-title">{{ item.get('title', '') }} ({{ item.get('symbol', '') }})</h3>
                        <p class="card-text">{{ item.get('content', 'Нет описания') }}</p>
                        <ul class="list-group list-group-flush">
                            <li class="list-group-item">
                                <strong>Дата запуска:</strong> {{ item.get('date', '') }}
                            </li>
                            <li class="list-group-item">
                                <strong>Цена:</strong> ${{ item.get('price', 'N/A') }}
                            </li>
                            <li class="list-group-item">
                                <strong>Сайт:</strong> 
                                <a href="{{ item.get('website', '#') }}" target="_blank" style="color: #4da6ff;">
                                    {{ item.get('website', 'Не указан') }}
                                </a>
                            </li>
                            <li class="list-group-item">
                                <strong>Статус:</strong> 
                                <span class="status-badge status-badge-% if item.get('status') == 'active': active elif item.get('status') == 'upcoming': upcoming else: secondary %">
                                    {{ item.get('status', 'unknown') }}
                                </span>
                            </li>
                        </ul>
                    </div>
                </div>
                % end
            % end
        </div>
        
        <div class="col-md-4">
            <div class="card">
                <div class="card-header bg-success text-white">
                    <h3 class="mb-0">Добавить новую монету</h3>
                </div>
                <div class="card-body">
                    <form method="POST" action="/newspage">
                        <div class="form-group">
                            <label for="title">Название монеты</label>
                            <input type="text" class="form-control" id="title" name="title"
                                   value="{{ form_data.get('title', '') }}" required
                                   minlength="2" maxlength="100">
                        </div>

                        <div class="form-group">
                            <label for="symbol">Символ (например: BTC)</label>
                            <input type="text" class="form-control" id="symbol" name="symbol"
                                   value="{{ form_data.get('symbol', '') }}" required
                                   minlength="2" maxlength="10">
                        </div>

                        <div class="form-group">
                            <label for="date">Дата запуска</label>
                            <input type="date" class="form-control" id="date" name="date"
                                   value="{{ form_data.get('date', '') }}" required>
                        </div>

                        <div class="form-group">
                            <label for="price">Цена (USD)</label>
                            <input type="number" step="0.01" class="form-control" id="price" name="price"
                                   value="{{ form_data.get('price', '') }}" min="0">
                        </div>

                        <div class="form-group">
                            <label for="website">Официальный сайт</label>
                            <input type="url" class="form-control" id="website" name="website"
                                   value="{{ form_data.get('website', '') }}"
                                   placeholder="https://example.com   ">
                        </div>

                        <div class="form-group">
                            <label for="content">Описание</label>
                            <textarea class="form-control" id="content" name="content"
                                      rows="5" minlength="10" required>{{ form_data.get('content', '') }}</textarea>
                        </div>

                        <div class="form-group">
                            <label for="status">Статус</label>
                            <select class="form-control" id="status" name="status">
                                <option value="active" % if form_data.get('status') == 'active': selected % end>Активная</option>
                                <option value="upcoming" % if form_data.get('status') == 'upcoming' or not form_data: selected % end>Предстоящая</option>
                                <option value="archived" % if form_data.get('status') == 'archived': selected % end>Архивная</option>
                            </select>
                        </div>

                        <button type="submit" class="btn btn-success btn-block">
                            Добавить монету
                        </button>
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>