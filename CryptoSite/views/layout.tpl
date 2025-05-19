<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }} - CryptoWorld</title>
    <link rel="icon" type="image/svg+xml" href="/static/favicon.svg">

    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css?family=Orbitron:400,700|Poppins:400,700|Share+Tech+Mono&display=swap" rel="stylesheet">

    <!-- Bootstrap -->
    <!-- Bootstrap 5 -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>

    <!-- Font Awesome -->
    <link rel="stylesheet" href="/static/content/font-awesome.css">
    <link rel="stylesheet"
          href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css"
          integrity="sha512-Fo3rlrZj/k7ujTTXABfQaR0MdSGF7xkKUqHkPj+6H/64FQ1Qc+KYs88RY8U1bXapXOPQkU6s5xZ2xCz4l/3P2w=="
          crossorigin="anonymous" referrerpolicy="no-referrer" />

    <link rel="stylesheet" href="/static/content/site.css">
    <link rel="stylesheet" href="/static/content/articles.css">

    <!-- Modernizr -->
    <script src="/static/scripts/modernizr-2.6.2.js"></script>
</head>

<nav class="navbar navbar-expand-lg custom-navbar">
    <div class="container">
        <a class="navbar-brand" href="/">CryptoWorld - Мир криптовалют</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
                aria-controls="navbarNav" aria-expanded="false" aria-label="Переключить навигацию">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse justify-content-start" id="navbarNav">
            <ul class="navbar-nav">
                <li class="nav-item">
                    <a class="nav-link" href="/home">Главная</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="/news">Новости</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="/contact">Контакты</a>
                </li>
            </ul>
        </div>
    </div>
</nav>


<body>
    <div class="container body-content">
        {{!base}}
        <footer>
            <p>&copy; {{ year }} - Sapkat Besvol & CO</p>
        </footer>
    </div>

    <script src="/static/scripts/jquery-1.10.2.js"></script>
    <script src="/static/scripts/bootstrap.js"></script>
    <script src="/static/scripts/respond.js"></script>
</body>
</html>
