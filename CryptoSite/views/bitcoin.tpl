% rebase('layout.tpl', title='Bitcoin', year=year)

<div class="row">
    <div class="col-md-12">
        <h2>Bitcoin: Основная информация</h2>

        <!-- График Bitcoin из TradingView -->
        <div class="tradingview-widget-container">
            <div class="tradingview-widget-container__widget"></div>
            <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-symbol-overview.js" async>
            {
                "symbols": [
                    ["Bitcoin","BTCUSD"]
                ],
                "chartOnly": false,
                "width": "100%",
                "height": "500",
                "locale": "ru",
                "colorTheme": "light",
                "autosize": true,
                "showVolume": true,
                "showMA": true,
                "hideDateRanges": false,
                "hideMarketStatus": false,
                "hideSymbolLogo": false,
                "scalePosition": "right",
                "scaleMode": "Normal",
                "fontFamily": "-apple-system, BlinkMacSystemFont, Trebuchet MS, Roboto, Ubuntu, sans-serif",
                "fontSize": "10",
                "noTimeScale": false,
                "valuesTracking": "1",
                "changeMode": "price-and-percent",
                "chartType": "area",
                "maLineColor": "#2962FF",
                "maLineWidth": 1,
                "maLength": 9,
                "lineWidth": 2,
                "lineType": 0
            }
            </script>
        </div>
        <!-- Конец графика -->

        <div class="bitcoin-info">
            <h3>Что такое Bitcoin?</h3>
            <p>
                Bitcoin (BTC) — это первая и самая известная криптовалюта, созданная в 2009 году человеком или группой людей под псевдонимом Сатоши Накамото. Bitcoin работает на технологии блокчейн, которая обеспечивает децентрализацию и безопасность транзакций.
            </p>
        </div>

        <div class="bitcoin-info">
            <h3>Как работает Bitcoin?</h3>
            <p>
                Bitcoin использует технологию блокчейн, которая представляет собой цепочку блоков, содержащих информацию о транзакциях. Каждый блок связан с предыдущим, что делает систему прозрачной и защищенной от изменений. Майнеры подтверждают транзакции, решая сложные математические задачи, и получают за это вознаграждение в виде новых биткойнов.
            </p>
        </div>

        <div class="bitcoin-info">
            <h3>Преимущества Bitcoin</h3>
            <ul>
                <li><strong>Децентрализация:</strong> Bitcoin не контролируется ни одним правительством или организацией.</li>
                <p><a class="btn btn-default btn-sm" href="/decentralization">Узнать больше &raquo;</a></p>
                <li><strong>Анонимность:</strong> Пользователи могут совершать транзакции без раскрытия личной информации.</li>
                <li><strong>Безопасность:</strong> Блокчейн обеспечивает высокий уровень защиты данных.</li>
                <li><strong>Глобальность:</strong> Bitcoin можно использовать в любой точке мира.</li>
            </ul>
        </div>

        <div class="bitcoin-info">
            <h3>Недостатки Bitcoin</h3>
            <ul>
                <li><strong>Волатильность:</strong> Цена Bitcoin может сильно колебаться за короткий период времени.</li>
                <li><strong>Ограниченная масштабируемость:</strong> Сеть Bitcoin может обрабатывать ограниченное количество транзакций в секунду.</li>
                <li><strong>Регуляторные риски:</strong> В некоторых странах Bitcoin может быть запрещен или ограничен.</li>
            </ul>
        </div>

        <div class="bitcoin-info">
            <h3>Как купить Bitcoin?</h3>
            <p>
                Bitcoin можно купить на криптовалютных биржах, таких как Binance, Coinbase или Kraken. Для этого необходимо зарегистрироваться на платформе, пройти верификацию и пополнить счет. После этого можно приобрести Bitcoin за фиатные деньги или другие криптовалюты.
            </p>
        </div>

        <div class="bitcoin-info">
            <h3>Как хранить Bitcoin?</h3>
            <p>
                Bitcoin можно хранить в криптовалютных кошельках. Существует несколько типов кошельков:
            </p>
            <ul>
                <li><strong>Аппаратные кошельки:</strong> Наиболее безопасный вариант, например, Ledger или Trezor.</li>
                <li><strong>Программные кошельки:</strong> Приложения для компьютера или смартфона, такие как Electrum или Exodus.</li>
                <li><strong>Онлайн-кошельки:</strong> Удобны для быстрого доступа, но менее безопасны, например, Blockchain.com.</li>
            </ul>
        </div>

        <div class="bitcoin-info">
            <h3>Будущее Bitcoin</h3>
            <p>
                Будущее Bitcoin остается предметом споров среди экспертов. Некоторые считают, что Bitcoin станет "цифровым золотом" и будет использоваться как средство сбережения. Другие полагают, что его роль в мировой экономике будет ограничена из-за конкуренции со стороны других криптовалют и технологий.
            </p>
        </div>

        <div class="text-center">
            <p><a class="btn btn-primary" href="/news">Вернуться к новостям &raquo;</a></p>
        </div>
    </div>
</div>
<hr/>
<h2 class="mb-4 pb-2 border-bottom">Отзывы</h2>

% if error:
  <div class="alert alert-danger alert-dismissible fade show" role="alert">
    {{ error }}
    <button type="button" class="close" data-dismiss="alert" aria-label="Закрыть">
      <span aria-hidden="true">&times;</span>
    </button>
  </div>
% end

<form method="post" class="needs-validation mb-5" novalidate accept-charset="UTF-8">
  <div class="form-row">
    <div class="col-md-6 mb-3">
      <label for="name">Имя</label>
      <input type="text" class="form-control" id="name" name="name"
             value="{{ form_data.get('name','') }}" required pattern="^[^\d]+$">
      <div class="invalid-feedback">
        Пожалуйста, введите корректное имя (без цифр).
      </div>
    </div>

    <div class="col-md-6 mb-3">
      <label for="phone">Телефон</label>
      <input type="tel" class="form-control" id="phone" name="phone"
             value="{{ form_data.get('phone','') }}" placeholder="+7XXXXXXXXXX"
             pattern="^\+7\d{10}$" required>
      <div class="invalid-feedback">
        Укажите номер в формате +7XXXXXXXXXX.
      </div>
    </div>
  </div>

  <div class="form-group">
    <label for="text">Комментарий</label>
    <textarea class="form-control" id="text" name="text" rows="4"
              required minlength="10">{{ form_data.get('text','') }}</textarea>
    <small class="form-text text-muted">
      Минимум 10 символов.
    </small>
    <div class="invalid-feedback">
      Пожалуйста, введите комментарий не короче 10 символов.
    </div>
  </div>

  <div class="text-center mt-4">
    <button type="submit" class="btn btn-primary btn-lg px-4">
      <i class="fas fa-comment-dots mr-2"></i>Оставить отзыв
    </button>
  </div>
</form>

% if reviews:
  <ul class="list-group">
  % for r in reviews:
    <li class="list-group-item review-list">
      <h5 class="mb-1">{{ r['name'] }} <small class="text-muted">({{ r['date'] }})</small></h5>
      <p class="mb-1">{{ r['text'] }}</p>
      <small class="text-muted"><i class="fas fa-phone-alt mr-1"></i>{{ r['phone'] }}</small>
    </li>
  % end
  </ul>
% else:
  <div class="alert alert-info text-center">
    <i class="fas fa-info-circle mr-2"></i>Пока нет ни одного отзыва.
  </div>
% end
