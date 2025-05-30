% rebase('layout.tpl', title='Главная', year=year)

<div class="jumbotron">
    <h1>CryptoWorld</h1>
    <p class="lead">Добро пожаловать на CryptoWorld — ваш источник актуальных новостей и информации о криптовалютах. Мы предоставляем свежие данные о последних трендах, рыночных изменениях и новинках блокчейн-технологий. Узнайте все о криптовалютах, их движении на рынке, нововведениях и значимых событиях в мире цифровых активов.</p>
    <p><a href="/news" class="btn btn-primary btn-large">Читать последние новости &raquo;</a></p>
</div>

<div class="row">
    <div class="col-md-4">
        <h2>Как начать работать с криптовалютой</h2>
        <p>
            Узнайте основы криптовалют, включая то, как покупать, хранить и торговать цифровыми активами безопасно и эффективно.
        </p>
        <p><a class="btn btn-default" href="{{ coinbase_learn }}">Узнать больше &raquo;</a></p>
    </div>
    <div class="col-md-4">
        <h2>Топ криптовалют</h2>
        <p>Изучите самые популярные и широко используемые криптовалюты, такие как Биткойн, Эфириум и многие другие.</p>
        <p><a class="btn btn-default" href="{{ coinmarketcap }}">Узнать больше &raquo;</a></p>
    </div>
    <div class="col-md-4">
        <h2>Кошельки для криптовалют</h2>
        <p>Узнайте, как безопасно хранить свою криптовалюту с помощью аппаратных кошельков, программных кошельков и других решений.</p>
        <p><a class="btn btn-default" href="{{ trezor }}">Узнать больше &raquo;</a></p>
    </div>
</div>

<div class="row news-section">
    <div class="col-md-12">
    <div class="info-section p-4 mb-5 rounded shadow-sm">
        <h2 class="mb-3">Полезные статьи о криптовалютах</h2>
        <p>Изучайте подробные руководства, аналитику и советы от сообщества. Делитесь своими знаниями и будьте в курсе последних трендов в мире блокчейна и цифровых активов.</p>
        <p><a class="btn btn-success" href="/articles">Перейти к статьям &raquo;</a></p>
    </div>
</div>
</div>

<div class="row news-section">
    <div class="col-md-12">
    <div class="info-section p-4 mb-5 rounded shadow-sm">
        <h2 class="mb-3">Актуальные новинки</h2>
        <p>Новые актуальные монеты</p>
        <p><a class="btn btn-success" href="/newspage">Перейти к новинкам &raquo;</a></p>
    </div>
</div>
</div>

<div class="row how-it-works">
    <div class="col-md-12">
        <h2>Как работает криптовалюта</h2>
        <p>Узнайте основы технологии блокчейн и как криптовалюты добываются, торгуются и хранятся. Откройте для себя, как децентрализованные сети дают возможности людям и исключают необходимость в посредниках.</p>
        <p><a class="btn btn-success" href="{{ bitcoin_how_it_works }}">Узнать больше &raquo;</a></p>
    </div>
</div>

<div class="row featured-cryptos">
    <div class="col-md-12">
        <h2>Выделенные криптовалюты</h2>
<div class="crypto-item">
<img src="/static/images/bitcoin.svg" alt="Bitcoin Logo" style="height: 2em; vertical-align: middle; margin-left: 10px;">
<p></p>
    <h3 style="display: inline-block;">Биткойн (BTC)</h3>
    <p>Биткойн - первая и наиболее широко признанная криптовалюта, выпущенная в 2009 году анонимным лицом или группой под именем Сатоши Накамото.</p>
    <p><a class="btn btn-warning" href="{{ bitcoin_info }}">Узнать больше &raquo;</a></p>
</div>


        <div class="crypto-item">
            <h3>Эфириум (ETH)</h3>
            <p>Эфириум - децентрализованная платформа, на которой работают смарт-контракты, позволяя разработчикам создавать децентрализованные приложения (DApps).</p>
            <p><a class="btn btn-warning" href="{{ ethereum_page }}">Узнать больше &raquo;</a></p>
        </div>
        <div class="crypto-item">
            <h3>Лайткойн (LTC)</h3>
            <p>Лайткойн - криптовалюта с пиринговой сетью и открытым исходным кодом, обеспечивающая более быстрые транзакции с использованием другого алгоритма хеширования.</p>
            <p><a class="btn btn-warning" href="{{ litecoin_info }}">Узнать больше &raquo;</a></p>
        </div>
    </div>
</div>
