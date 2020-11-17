<html>
<body>

<?php
function XMLDOCdump(){
	$xmlDoc = new DOMDocument();
	$xmlDoc->load("IRIDIUM.xml");
	
	$x = $xmlDoc->documentElement;
	foreach ($x->childNodes AS $item) {
		print $item->nodeName . " = " . $item->nodeValue . "<br>";
		}
}
XMLDOCdump()
?>