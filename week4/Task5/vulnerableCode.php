<?php
// db.php - Simulates database connection
$conn = new mysqli("localhost", "root", "", "testdb");

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// index.php - Main page
session_start();

$username = $_POST['username'];
$password = $_POST['password'];

// SQL Injection risk!
$sql = "SELECT * FROM users WHERE username = '$username' AND password = '$password'";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    $_SESSION['user'] = $username;
    echo "Welcome, $username"; // XSS risk!
} else {
    echo "Invalid credentials. " . $conn->error; // Reveals DB errors!
}

$conn->close();
?>
