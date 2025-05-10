<?php
$host = "localhost";
$user = "userweb";
$pass = "password123";
$db = "praktikum";
$conn = new mysqli($host, $user, $pass, $db);
if ($conn->connect_error) {
    die("Koneksi gagal: " . $conn->connect_error);
}
?>