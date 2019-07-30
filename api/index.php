<?php
require_once "env.php";

if (SECRET !== $_GET["secret"]) {
	http_response_code(401);
	die();
}

require_once "promotions.php";
http_response_code(200);
header("Content-Type: application/json");
$response = ["promotions" => $promotions];
echo json_encode($response, JSON_UNESCAPED_UNICODE);
?>
