% rebase('layout.tpl', title='Новые криптовалюты', year=year)

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