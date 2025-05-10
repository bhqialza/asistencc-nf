<?php
include 'connect.php';
$nama = $_POST['nama'];
$email = $_POST['email'];
$sql = "INSERT INTO users (nama, email) VALUES ('$nama', '$email')";
if ($conn->query($sql) === TRUE) {
    echo "Data berhasil disimpan. <a href='tampil.php'>Lihat Data</a>";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}
$conn->close();
?>