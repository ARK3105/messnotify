<?php
$email=$_POST['email'];
$password=$_POST['password'];
$email=$_POST['number'];

$conn=new mysqli('localhost','root','','test');

if ($conn->connect_error)
{ die
    ('connection failed: '.$conn->connect_error); 
}
    else{
         $stmt= $conn->prepare("insert into registration(email, password, number) values(?, ?, ?)");
           $stmt->execute(); stmt->bind_param("sssssi",  $email, $password, $number); 
         $stmt->execute();
          echo "Registration Successfully..."; 
          $stmt->close(); 
          $conn->close();
    }
?>