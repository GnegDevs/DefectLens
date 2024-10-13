<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $url = 'http://localhost:8080/defectlens/api/v1/upload/images';
    $data = [];

    if (isset($_FILES['cover_photo']) && $_FILES['cover_photo']['error'] == UPLOAD_ERR_OK) {
        $data['cover_photo'] = new CURLFile($_FILES['cover_photo']['tmp_name'], $_FILES['cover_photo']['type'], $_FILES['cover_photo']['name']);
    }
    if (isset($_FILES['screen_photo']) && $_FILES['screen_photo']['error'] == UPLOAD_ERR_OK) {
        $data['screen_photo'] = new CURLFile($_FILES['screen_photo']['tmp_name'], $_FILES['screen_photo']['type'], $_FILES['screen_photo']['name']);
    }
    if (isset($_FILES['keyboard_photo']) && $_FILES['keyboard_photo']['error'] == UPLOAD_ERR_OK) {
        $data['keyboard_photo'] = new CURLFile($_FILES['keyboard_photo']['tmp_name'], $_FILES['keyboard_photo']['type'], $_FILES['keyboard_photo']['name']);
    }
    if (isset($_FILES['base_photo']) && $_FILES['base_photo']['error'] == UPLOAD_ERR_OK) {
        $data['base_photo'] = new CURLFile($_FILES['base_photo']['tmp_name'], $_FILES['base_photo']['type'], $_FILES['base_photo']['name']);
    }
    if (isset($_POST['serial'])) {
        $data['serial'] = $_POST['serial'];
    }

    if (!empty($data)) {
        $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, $url);
        curl_setopt($ch, CURLOPT_POST, 1);
        curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        
        $response = curl_exec($ch);
        curl_close($ch);

        if (is_numeric($response)) {
            $id = intval($response);
        } else {
            echo "Ошибка: неверный формат ответа.";
        }
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Загрузить фотографии</title>
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
        .id-container {
            display: grid;
            gap: 10px;
            max-width: 400px;
            margin: 10px auto;
        }
        .id-field {
            grid-column: span 2;
        }
        .image-box {
            padding: 5px;
            min-height: 16vh;
            border: 2px solid black;
            border-radius: 4px;
        }
        .container label {
            display: block;
            margin-bottom: 5px;
        }
        .container input[type="file"] {
            width: 100%;
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
    </style>
</head>
<body>
    <form action="index.php" method="post" enctype="multipart/form-data" class="container">
        <div class="image-box">
            <label for="cover_photo">Фото крышки:</label>
            <input type="file" name="cover_photo" id="cover_photo"><br>
        </div>
        <div class="image-box">
            <label for="screen_photo">Фото экрана:</label>
            <input type="file" name="screen_photo" id="screen_photo"><br>
        </div>
        <div class="image-box">
            <label for="keyboard_photo">Фото клавиатуры:</label>
            <input type="file" name="keyboard_photo" id="keyboard_photo"><br>
        </div>
        <div class="image-box">
            <label for="base_photo">Фото корпуса:</label>
            <input type="file" name="base_photo" id="base_photo"><br>
        </div>
        <input name="serial" placeholder="Серийный номер" class="id-field">
        <button type="submit">Загрузить запись</button>
    </form>

    <form action="record.php" method="post" class="id-container">
        <?php if (isset($id)): ?>
            <p style="font-size: 16px">ID записи ноутбука, нажмите кнопку ниже для обработки:</p>
            <input name="id" value="<?php echo $id; ?>" class="id-field">
        <?php else: ?>
            <p style="font-size: 16px">or</p>
            <input name="id" placeholder="ID записи" class="id-field">
        <?php endif; ?>
            <button type="submit">Проверить ноутбук по ID записи</button>
    </form>
</body>
</html>
