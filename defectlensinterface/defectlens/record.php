<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['id'])) {
    $id = $_POST['id'];
    $url = "http://localhost:8080/defectlens/api/v1/record/$id";

    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_HTTPGET, true);
    $response = curl_exec($ch);
    curl_close($ch);

    // Выводим ответ сервера для отладки

    $data = json_decode($response, true);
    if (json_last_error() !== JSON_ERROR_NONE) {
        echo "Ошибка декодирования JSON: " . json_last_error_msg();
        exit;
    }

    // Преобразуем строки в массивы байтов
    $data['coverPhoto'] = base64_decode($data['coverPhoto']);
    $data['screenPhoto'] = base64_decode($data['screenPhoto']);
    $data['keyboardPhoto'] = base64_decode($data['keyboardPhoto']);
    $data['basePhoto'] = base64_decode($data['basePhoto']);
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Record Details</title>
    <style>
        * {
            font-family: sans-serif;
        }
        .container {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10px;
            max-width: 400px;
            margin: auto;
        }
        .id-field {
            grid-column: span 2;
        }
        .image-box {
            justify-content: center;
            align-items: center;
            overflow: hidden;
            padding: 5px;
            max-height: 50vh;
            max-width: 50vh;
            border: 2px solid lightgrey;
            border-radius: 4px;
        }
        .image-box img {
            object-fit: cover;
            max-width: 50%;
            max-height: 50%;
        }
        button {
            grid-column: span 2;
            padding: 10px;
            background-color: black;
            color: white;
            border: none;
            cursor: pointer;
            border-radius: 4px;

        }
        button:hover {
            background-color: rgb(64, 64, 64);
        }
        .button-container {
            margin-top: 10px;
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10px;
            max-width: 400px;
            margin: 10px auto;
        }
    </style>
</head>
<body>
    <?php if (isset($data)): ?>
        <div class="container">
        <h2 class="id-field">ID записи: <?php echo htmlspecialchars($data['id']); ?></h2>
            <div class="image-box">
                <h3>Фото крышки:</h3>
                <img src="data:image/png;base64,<?php echo base64_encode($data['coverPhoto']); ?>" alt="Cover Photo">
                <p style="font-size: 16px">Царапина</p>
            </div>
            <div class="image-box">
                <h3>Фото экрана:</h3>
                <img src="data:image/png;base64,<?php echo base64_encode($data['screenPhoto']); ?>" alt="Screen Photo">
                <p style="font-size: 16px">Дефектов не обнаружено</p>
            </div>
            <div class="image-box">
                <h3>Фото клавиатуры:</h3>
                <img src="data:image/png;base64,<?php echo base64_encode($data['keyboardPhoto']); ?>" alt="Keyboard Photo">
                <p style="font-size: 16px">Проблемы с клавишами</p>
            </div>
            <div class="image-box">
                <h3>Фото корпуса:</h3>
                <img src="data:image/png;base64,<?php echo base64_encode($data['basePhoto']); ?>" alt="Base Photo">
                <p style="font-size: 16px">Царапина</p>
            </div>
            <input readonly value="<?php echo $data['serial']?>" name="serial" placeholder="Serial number" class="id-field">
        </div>
        <form action="http://localhost:5000/defectlensmodel/api/v1/process/download" method="get" class="button-container">
            <button type="submit">Получить отчет</button>
        </form>
    <?php endif; ?>
</body>
</html>
