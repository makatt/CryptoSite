% rebase('layout.tpl', title='Litecoin (LTC)', year=year)


<div class="container">
    <div class="jumbotron">
        <h1>Лайткойн (LTC)</h1>
        <p class="lead">Лайткойн — это одна из первых криптовалют, созданная в 2011 году Чарли Ли. Она была разработана как "облегченная" версия Биткойна, с целью улучшения скорости транзакций и снижения комиссий.</p>
    </div>

    <div class="row">
        <div class="col-md-8">
            <h2>Основные особенности Лайткойн</h2>
            <ul class="list-group">
                <li class="list-group-item-ltc">
                    <strong>Быстрые транзакции:</strong> Лайткойн использует алгоритм хеширования Scrypt, который позволяет обрабатывать транзакции быстрее, чем Биткойн. Время создания блока — около 2,5 минут.
                </li>
                <li class="list-group-item-ltc">
                    <strong>Децентрализация:</strong> Как и Биткойн, Лайткойн работает на основе децентрализованной блокчейн-сети, что обеспечивает безопасность и прозрачность транзакций.
                </li>
                <li class="list-group-item-ltc">
                    <strong>Ограниченная эмиссия:</strong> Максимальное количество монет Лайткойн ограничено 84 миллионами.
                </li>
                <li class="list-group-item-ltc">
                    <strong>Низкие комиссии:</strong> Благодаря высокой скорости обработки транзакций, комиссии в сети Лайткойн остаются низкими.
                </li>
                <li class="list-group-item-ltc">
                    <strong>Активное сообщество:</strong> Лайткойн имеет сильное сообщество разработчиков и пользователей, которые продолжают развивать экосистему.
                </li>
            </ul>
        </div>
        <div class="col-md-4">
            <div class="card">
                <div class="card-body">
                    <h5 class="card-title">Технические данные</h5>
                    <ul class="list-unstyled">
                        <li><strong>Создатель:</strong> Чарли Ли</li>
                        <li><strong>Год создания:</strong> 2011</li>
                        <li><strong>Алгоритм:</strong> Scrypt</li>
                        <li><strong>Максимальное количество монет:</strong> 84 млн</li>
                        <li><strong>Время блока:</strong> 2,5 минуты</li>
                    </ul>
                </div>
            </div>
        </div>
    </div>

    <div class="row mt-4">
        <div class="col-md-12">
            <h2>Применение Лайткойн</h2>
            <div class="card">
                <div class="card-body">
                    <p class="card-text">
                        Лайткойн активно используется для быстрых и дешевых переводов между пользователями. Он также популярен среди инвесторов благодаря своей стабильности и ликвидности. Кроме того, Лайткойн внедряет новые технологии, такие как Lightning Network, для улучшения масштабируемости.
                    </p>
                </div>
            </div>
        </div>
    </div>

    <div class="row mt-4">
        <div class="col-md-12">
            <h2>Где купить Лайткойн</h2>
            <p>Лайткойн можно приобрести на большинстве крупных криптовалютных бирж, таких как:</p>
            <ul class="list-group">
                <li class="list-group-item-ltc"><a href="{{ binance }}" target="_blank">Binance</a></li>
                <li class="list-group-item-ltc"><a href="{{ coinbase }}" target="_blank">Coinbase</a></li>
                <li class="list-group-item-ltc"><a href="{{ kraken }}" target="_blank">Kraken</a></li>
            </ul>
        </div>
    </div>

    <div class="row mt-4">
        <div class="col-md-12">
            <h2>Дополнительные ресурсы</h2>
            <p>Узнайте больше о Лайткойн на официальном сайте и в сообществе:</p>
            <ul class="list-group">
                <li class="list-group-item-ltc"><a href="{{ litecoin_official }}" target="_blank">Официальный сайт Лайткойн</a></li>
                <li class="list-group-item-ltc"><a href="{{ reddit }}" target="_blank">Сообщество на Reddit</a></li>
            </ul>
        </div>
    </div>

    <div class="row mt-4">
        <div class="col-md-12">
            <h2>Активные пользователи Лайткойн</h2>
            
            <div class="row mt-4">
                <div class="col-md-6">
                    <h3>Добавить нового пользователя</h3>
                    <form method="POST" action="/litecoin" class="mb-4">
                        <div class="form-group">
                            <label for="username">Имя пользователя (никнейм):</label>
                            <input type="text" class="form-control" id="username" name="username" value="{{ username if defined('username') else '' }}" required>
                        </div>
                        
                        <div class="form-group">
                            <label for="description">Описание:</label>
                            <textarea class="form-control" id="description" name="description" rows="3" required>{{ description if defined('description') else '' }}</textarea>
                        </div>
                        
                        <div class="form-group">
                            <label for="date">Дата регистрации:</label>
                            <input type="date" class="form-control" id="date" name="date" value="{{ date if defined('date') else '' }}" required>
                        </div>
                        
                        <div class="form-group">
                            <label for="phone">Телефон (формат: +7XXXXXXXXXX, 11 цифр):</label>
                            <input type="tel" class="form-control" id="phone" name="phone" value="{{ phone if defined('phone') else '' }}" pattern="\+7\d{10}" required>
                        </div>
                        
                        % if defined('error') and error:
                        <div class="alert alert-danger" role="alert">
                            {{ error }}
                        </div>
                        % end
                        
                        <button type="submit" class="btn btn-primary">Добавить пользователя</button>
                    </form>
                </div>
            </div>
            
            % if defined('users') and users:
                <div class="list-group">
                    % for user in users:
                    <div class="list-group-item">
                        <div class="d-flex w-100 justify-content-between">
                            <h5 class="mb-1">{{ user['username'] }}</h5>
                            <small>Зарегистрирован: {{ user['date'] }}</small>
                        </div>
                        <p class="mb-1">{{ user['description'] }}</p>
                        <small>Телефон: {{ user['phone'] }}</small>
                    </div>
                    % end
                </div>
            % else:
                <p>Пока нет активных пользователей.</p>
            % end
        </div>
    </div>
</div>