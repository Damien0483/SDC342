<?php
// Replace "lastname" with your actual last name to match validator.php
require_once 'validator.php';
use lastname_validator\ValidationException;
use function lastname_validator\validateName;
use function lastname_validator\validateDob;
use function lastname_validator\validateEmail;
use function lastname_validator\validateFavoriteInteger;
use function lastname_validator\validateNickname;

$name = $dob = $email = $favoriteInteger = $nickname = '';
$nameError = $dobError = $emailError = $favoriteIntegerError = $nicknameError = '';
$overallMessage = '';
$hasSubmitted = ($_SERVER['REQUEST_METHOD'] === 'POST');

if ($hasSubmitted) {
    $name            = $_POST['name']            ?? '';
    $dob             = $_POST['dob']             ?? '';
    $email           = $_POST['email']           ?? '';
    $favoriteInteger = $_POST['favoriteInteger'] ?? '';
    $nickname        = $_POST['nickname']        ?? '';

    $allValid = true;

    // Name validation (uses REGEX and by-ref parameter)
    if (!validateName($name, $nameError)) {
        $allValid = false;
    }

    // DOB validation (uses Exceptions)
    try {
        validateDob($dob);
    } catch (ValidationException $ex) {
        $dobError = $ex->getMessage();
        $allValid = false;
    }

    // Email validation (uses PHP built-in format check)
    if (!validateEmail($email, $emailError)) {
        $allValid = false;
    }

    // Favorite Integer validation (uses built-in integer validation)
    if (!validateFavoriteInteger($favoriteInteger, $favoriteIntegerError)) {
        $allValid = false;
    }

    // Nickname validation (optional, min length 2 if present)
    if (!validateNickname($nickname, $nicknameError)) {
        $allValid = false;
    }

    if ($allValid) {
        $overallMessage = "All fields valid";
    } else {
        $overallMessage = "Errors found, please check your entries";
    }
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Your Name Wk 1 Performance Assessment</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        form {
            max-width: 500px;
        }
        .form-row {
            margin-bottom: 12px;
        }
        label {
            display: block;
            font-weight: bold;
            margin-bottom: 4px;
        }
        input[type="text"] {
            width: 100%;
            padding: 6px;
            box-sizing: border-box;
        }
        .error {
            color: red;
            font-size: 0.9em;
            margin-top: 2px;
            display: block;
        }
        .overall-result {
            margin-top: 16px;
        }
        .overall-result input {
            width: 100%;
            padding: 6px;
            box-sizing: border-box;
            font-weight: bold;
        }
        .button-row {
            margin-top: 10px;
        }
    </style>
</head>
<body>
    <h1>Your Name Wk 1 Performance Assessment</h1>

    <form method="post" action="">
        <div class="form-row">
            <label for="name">Name (Lastname, Firstname) *</label>
            <input type="text" id="name" name="name"
                   value="<?php echo htmlspecialchars($name); ?>">
            <?php if ($hasSubmitted && $nameError !== ''): ?>
                <span class="error"><?php echo htmlspecialchars($nameError); ?></span>
            <?php endif; ?>
        </div>

        <div class="form-row">
            <label for="dob">Date of Birth (MM/DD/YYYY) *</label>
            <input type="text" id="dob" name="dob"
                   value="<?php echo htmlspecialchars($dob); ?>">
            <?php if ($hasSubmitted && $dobError !== ''): ?>
                <span class="error"><?php echo htmlspecialchars($dobError); ?></span>
            <?php endif; ?>
        </div>

        <div class="form-row">
            <label for="email">Email Address *</label>
            <input type="text" id="email" name="email"
                   value="<?php echo htmlspecialchars($email); ?>">
            <?php if ($hasSubmitted && $emailError !== ''): ?>
                <span class="error"><?php echo htmlspecialchars($emailError); ?></span>
            <?php endif; ?>
        </div>

        <div class="form-row">
            <label for="favoriteInteger">Favorite Integer *</label>
            <input type="text" id="favoriteInteger" name="favoriteInteger"
                   value="<?php echo htmlspecialchars($favoriteInteger); ?>">
            <?php if ($hasSubmitted && $favoriteIntegerError !== ''): ?>
                <span class="error"><?php echo htmlspecialchars($favoriteIntegerError); ?></span>
            <?php endif; ?>
        </div>

        <div class="form-row">
            <label for="nickname">Nickname (optional)</label>
            <input type="text" id="nickname" name="nickname"
                   value="<?php echo htmlspecialchars($nickname); ?>">
            <?php if ($hasSubmitted && $nicknameError !== ''): ?>
                <span class="error"><?php echo htmlspecialchars($nicknameError); ?></span>
            <?php endif; ?>
        </div>

        <div class="button-row">
            <button type="submit">Validate</button>
        </div>

        <div class="overall-result">
            <label for="overall">Validation Result</label>
            <input type="text" id="overall" name="overall" readonly
                   value="<?php echo htmlspecialchars($overallMessage); ?>">
        </div>
    </form>
</body>
</html>
