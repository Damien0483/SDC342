<?php
class Person {

    // ---------- Private Properties ----------
    private $firstName;
    private $lastName;
    private $address1;
    private $address2;
    private $city;
    private $state;
    private $zip;

    // ---------- Constructor ----------
    public function __construct($firstName, $lastName, $address1, $address2, $city, $state, $zip) {
        $this->firstName = $firstName;
        $this->lastName = $lastName;
        $this->address1 = $address1;
        $this->address2 = $address2;
        $this->city = $city;
        $this->state = $state;
        $this->zip = $zip;
    }

    // ---------- Getters & Setters ----------
    public function getFirstName() { return $this->firstName; }
    public function setFirstName($firstName) { $this->firstName = $firstName; }

    public function getLastName() { return $this->lastName; }
    public function setLastName($lastName) { $this->lastName = $lastName; }

    public function getAddress1() { return $this->address1; }
    public function setAddress1($address1) { $this->address1 = $address1; }

    public function getAddress2() { return $this->address2; }
    public function setAddress2($address2) { $this->address2 = $address2; }

    public function getCity() { return $this->city; }
    public function setCity($city) { $this->city = $city; }

    public function getState() { return $this->state; }
    public function setState($state) { $this->state = $state; }

    public function getZip() { return $this->zip; }
    public function setZip($zip) { $this->zip = $zip; }

    // ---------- Formatted Output Methods ----------
    public function getFullName() {
        return $this->lastName . ", " . $this->firstName;
    }

    public function getFullAddress() {
        if (!empty($this->address2)) {
            return $this->address1 . ", " . $this->address2;
        }
        return $this->address1;
    }

    public function getCityStateZip() {
        return $this->city . ", " . $this->state . " " . $this->zip;
    }

    // ---------- Static Label Methods ----------
    public static function labelHeader() {
        return "Name and Address Information";
    }

    public static function labelFullName() {
        return "Full Name";
    }

    public static function labelAddress() {
        return "Address";
    }

    public static function labelCityStateZip() {
        return "City/State/Zip";
    }
}
?>
