<?php
require_once "person.php";

// Create 5 Person objects (2 without address line 2)
$people = [
    new Person("John", "Doe", "123 Main St", "", "Richmond", "VA", "23220"),
    new Person("Sarah", "Miller", "45 Oak Ave", "Apt 2B", "Norfolk", "VA", "23510"),
    new Person("Michael", "Smith", "789 Pine Rd", "", "Chesapeake", "VA", "23320"),
    new Person("Emily", "Johnson", "22 River Dr", "Suite 300", "Virginia Beach", "VA", "23451"),
    new Person("David", "Brown", "900 Sunset Blvd", "", "Newport News", "VA", "23601")
];
?>
<!DOCTYPE html>
<html>
<head>
    <title>Your Name - Week 2 Performance Assessment</title>
    <style>
        table {
            width: 60%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        th, td {
            border: 1px solid #444;
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #ddd;
        }
    </style>
</head>
<body>

<h1><?php echo Person::labelHeader(); ?></h1>

<table>
    <tr>
        <th><?php echo Person::labelFullName(); ?></th>
        <th><?php echo Person::labelAddress(); ?></th>
        <th><?php echo Person::labelCityStateZip(); ?></th>
    </tr>

    <?php foreach ($people as $person): ?>
        <tr>
            <td><?php echo $person->getFullName(); ?></td>
            <td><?php echo $person->getFullAddress(); ?></td>
            <td><?php echo $person->getCityStateZip(); ?></td>
        </tr>
    <?php endforeach; ?>

</table>

</body>
</html>
