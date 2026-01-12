<?php
namespace lastname_validator; // <-- replace "lastname" with your actual last name

class ValidationException extends \Exception {}

/**
 * Checks if a value is non-empty (passed by value, returns value).
 */
function isRequired($value): bool {
    return trim((string)$value) !== '';
}

/**
 * Validates the Name field: "Lastname, Firstname"
 * Uses REGEX and by-reference parameter for error message.
 */
function validateName(string $name, string &$error): bool {
    $error = '';

    if (!isRequired($name)) {
        $error = "Required Entry";
        return false;
    }

    // Regex: Lastname (>=2 chars), comma, Firstname (>=1 char)
    $pattern = '/^\s*([A-Za-z\'\-]{2,})\s*,\s*([A-Za-z\'\-]{1,})\s*$/';

    if (!preg_match($pattern, $name, $matches)) {
        $error = "Name must be formatted as Lastname, Firstname";
        return false;
    }

    return true;
}

/**
 * Validates Date of Birth using exceptions.
 * Format: MM/DD/YYYY and must be a valid calendar date.
 * This demonstrates use of Exceptions and a by-value parameter.
 */
function validateDob(string $dob): bool {
    if (!isRequired($dob)) {
        throw new ValidationException("Required Entry");
    }

    if (!preg_match('/^\d{2}\/\d{2}\/\d{4}$/', $dob)) {
        throw new ValidationException("Date must be in MM/DD/YYYY format");
    }

    $parts = explode('/', $dob);
    $month = (int)$parts[0];
    $day   = (int)$parts[1];
    $year  = (int)$parts[2];

    if (!checkdate($month, $day, $year)) {
        throw new ValidationException("Invalid calendar date");
    }

    return true;
}

/**
 * Validates Email using PHP built-in format validation (filter_var).
 * Uses by-reference parameter for error message.
 */
function validateEmail(string $email, string &$error): bool {
    $error = '';

    if (!isRequired($email)) {
        $error = "Required Entry";
        return false;
    }

    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $error = "Invalid email address format";
        return false;
    }

    return true;
}

/**
 * Validates Favorite Integer using PHP built-in integer validation.
 */
function validateFavoriteInteger(string $value, string &$error): bool {
    $error = '';

    if (!isRequired($value)) {
        $error = "Required Entry";
        return false;
    }

    if (filter_var($value, FILTER_VALIDATE_INT) === false) {
        $error = "Favorite Integer must be a valid integer";
        return false;
    }

    return true;
}

/**
 * Validates Nickname.
 * Not required, but if present must be at least 2 characters.
 */
function validateNickname(string $nickname, string &$error): bool {
    $error = '';

    if (!isRequired($nickname)) {
        // Not required; no error if empty
        return true;
    }

    if (mb_strlen(trim($nickname)) < 2) {
        $error = "Nickname must be at least 2 characters";
        return false;
    }

    return true;
}
