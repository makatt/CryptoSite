<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{{ title }} - CryptoWorld</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet" />
    <style>
        body {
            background-color: #121212; /* Темный фон */
            font-family: Arial, sans-serif;
            color: #e0e0e0; /* Светлый цвет текста по умолчанию */
        }

        /* Заголовок и шапка */
        .header {
            background-color: #1f1f1f;
            padding: 15px 0;
            border-bottom: 1px solid #333;
            margin-bottom: 30px;
        }

        .header h1 {
            color: #ffffff;
        }

        /* Основной контейнер для новостей */
        .crypto-container {
            background-color: #1f1f1f;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.5);
            padding: 20px;
            margin-bottom: 30px;
        }

        /* Элементы криптовалют */
        .crypto-item {
            padding: 15px 0;
            border-bottom: 1px solid #333;
        }

        .crypto-item:last-child {
            border-bottom: none;
        }

        .crypto-name {
            font-weight: bold;
            font-size: 1.1rem;
            margin-bottom: 5px;
            color: #ffffff;
        }

        .crypto-symbol {
            color: #aaa;
            font-size: 0.9rem;
        }

        .crypto-details {
            margin-top: 10px;
            color: #ccc;
            font-size: 0.9rem;
        }

        .crypto-meta {
            display: flex;
            flex-wrap: wrap;
            gap: 15px;
            margin-top: 10px;
        }

        .meta-item {
            display: flex;
            align-items: center;
        }

        .meta-label {
            font-weight: 600;
            margin-right: 5px;
            color: #bbb;
        }

        .status-badge {
            padding: 3px 8px;
            border-radius: 4px;
            font-size: 0.8rem;
            font-weight: 500;
            background-color: #388e3c;
            color: #fff;
        }

        /* Форма добавления */
        .form-container {
            background-color: #1f1f1f;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.5);
            padding: 25px;
        }

        .form-title {
            font-size: 1.5rem;
            margin-bottom: 20px;
            color: #fff;
        }

        /* Выровнять форму в столбик */
        .form-group {
            display: flex;
            flex-direction: column;
            margin-bottom: 15px;
        }

        .form-label {
            margin-bottom: 8px;
            font-weight: 500;
            color: #ccc;
        }

        .form-control {
            padding: 10px 12px;
            border: 1px solid #555;
            border-radius: 4px;
            font-size: 1rem;
            background-color: #2b2b2b;
            color: #fff;
        }

        .form-control:focus {
            border-color: #80bdff;
            outline: 0;
            box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, 0.25);
        }

        textarea.form-control {
            min-height: 100px;
        }

        .submit-btn {
            background-color: #4caf50;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 4px;
            font-size: 1rem;
            cursor: pointer;
            width: 100%;
            transition: background-color 0.3s;
        }

        .submit-btn:hover {
            background-color: #3d8b40;
        }

        /* Таблица формы - убрана, так как форма теперь в столбик */
        /* Удалены стили для таблицы формы */

        /* Адаптация для кнопки закрытия алерта */
        .btn-close {
            filter: invert(100%);
        }
    </style>
</head>
<body>

<div class="header">
    <div class="container">
        <h1>{{ title }}</h1>
    </div>
</div>

<div class="container">
    % if error:
        <div class="alert alert-danger alert-dismissible fade show" role="alert">
            {{ error }}
            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Закрыть"></button>
        </div>
    % end

    <div class="row">
        <div class="col-md-8">
            <div class="crypto-container">
                <h2>Новые криптовалюты</h2>
                
                % if not news_items:
                    <div class="alert alert-info text-dark">
                        Пока нет информации о новых криптовалютах.
                    </div>
                % else:
                    % for item in news_items:
                    <div class="crypto-item">
                        <div class="crypto-name">{{ item.get('title', '') }} <span class="crypto-symbol">({{ item.get('symbol', '') }})</span></div>
                        <div class="crypto-details">{{ item.get('content', 'Нет описания') }}</div>
                        <div class="crypto-meta">
                            <div class="meta-item">
                                <span class="meta-label">Дата запуска:</span>
                                <span>{{ item.get('date', '') }}</span>
                            </div>
                            <div class="meta-item">
                                <span class="meta-label">Цена:</span>
                                <span>${{ item.get('price', 'N/A') }}</span>
                            </div>
                            % if item.get('website'):
                            <div class="meta-item">
                                <span class="meta-label">Сайт:</span>
                                <a href="{{ item.get('website', '#') }}" target="_blank" class="text-decoration-none text-info">{{ item.get('website', 'Не указан') }}</a>
                            </div>
                            % end
                            <div class="meta-item">
                                <span class="meta-label">Статус:</span>
                                <span class="status-badge">
                                    {{ {'active': 'Активная', 'upcoming': 'Предстоящая'}.get(item.get('status'), 'Неизвестно') }}
                                </span>
                            </div>
                        </div>
                    </div>
                    % end
                % end
            </div>
        </div>

        <div class="col-md-4">
            <div class="form-container">
                <h3 class="form-title">Добавить новую монету</h3>
                <form method="POST" action="/newspage" class="d-flex flex-column">
                    <!-- Название -->
                    <div class="form-group">
                        <label for="title" class="form-label">Название монеты</label>
                        <input type="text" class="form-control" id="title" name="title"
                               value="{{ form_data.get('title', '') }}" required />
                    </div>
                    <!-- Символ и дата в одну строку -->
                    <div class="d-flex gap-3">
                        <div class="form-group flex-fill">
                            <label for="symbol" class="form-label">Символ (например: BTC)</label>
                            <input type="text" class="form-control" id="symbol" name="symbol"
                                   value="{{ form_data.get('symbol', '') }}" required />
                        </div>
                        <div class="form-group flex-fill">
                            <label for="date" class="form-label">Дата запуска</label>
                            <input type="date" class="form-control" id="date" name="date"
                                   value="{{ form_data.get('date', '') }}" required />
                        </div>
                    </div>
                    <!-- Цена -->
                    <div class="form-group">
                        <label for="price" class="form-label">Цена (USD)</label>
                        <input type="number" step="0.01" class="form-control" id="price" name="price"
                               value="{{ form_data.get('price', '') }}" />
                    </div>
                    <!-- Официальный сайт -->
                    <div class="form-group">
                        <label for="website" class="form-label">Официальный сайт</label>
                        <input type="url" class="form-control" id="website" name="website"
                               value="{{ form_data.get('website', '') }}"
                               placeholder="https://example.com" />
                    </div>
                    <!-- Описание -->
                    <div class="form-group">
                        <label for="content" class="form-label">Описание</label>
                        <textarea class="form-control" id="content" name="content"
                                  rows="3" required>{{ form_data.get('content', '') }}</textarea>
                    </div>
                    <!-- Статус -->
                    <div class="form-group">
                        <label for="status" class="form-label">Статус</label>
                        <select class="form-control" id="status" name="status">
                            <option value="active" % if form_data.get('status') == 'active': selected % end>Активная</option>
                            <option value="upcoming" % if form_data.get('status') == 'upcoming' or not form_data: selected % end>Предстоящая</option>
                            <option value="archived" % if form_data.get('status') == 'archived': selected % end>Архивная</option>
                        </select>
                    </div>
                    <!-- Кнопка отправки -->
                    <button type="submit" class="submit-btn mt-3">
                        Добавить монету
                    </button>
                </form>
            </div>
        </div>
    </div>
</div>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
