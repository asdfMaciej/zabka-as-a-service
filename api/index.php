<?php
require_once "env.php";

if (strtolower(SECRET) != strtolower($_GET["secret"])) {
	http_response_code(401);
	die();
}

require_once "promotions.php";
http_response_code(200);
header("Content-Type: application/json");
$response = ["date" => $datetime, "promotions" => $promotions];
echo json_encode($response, JSON_UNESCAPED_UNICODE);
?>
