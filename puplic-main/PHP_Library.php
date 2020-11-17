<?php 
function open_DB($DB_V) {
	$DB_open = fopen("IRIDIUM.xml","r") or die("Unable to Open File");
	echo fread($DB_open,filesize("IRIDIUM.xml"));
	fclose();
}

function Read_DB() {
	$xml=simplexml_load_file("IRIDIUM.xml")or die("Unable to open file");
	print($xml);
}

function ASN() {
	$xmlDoc = new DOMDocument();
	$xmlDoc -> load("IRIDIUM.xml");
	$x = $xmlDoc->documentElement;
	foreach ($x->Sattelite() AS $Sat_Info) {
		echo $Sat_Info->OBJECT_NAME . ": " . $Sat_Info ;
		echo $Sat_Info->OBJECT_ID . ": " . $Sat_Info ;
		echo $Sat_Info ->CENTER_NAME . ": " . $Sat_Info ;
		echo $Sat_Info->REF_FRAME .": " . $Sat_Info ;
		echo $Sat_Info->TIME_SYSTEM . ": " . $Sat_Info ;
		echo $Sat_Info->MEAN_ELEMENT_THEORY . ": " . $Sat_Info ;
		echo $Sat_Info->EPOCH . ": " . $Sat_Info ;
		echo $Sat_Info->MEAN_MOTION . ": " . $Sat_Info ;
		echo $Sat_Info->ECCENTRICITY . ": " . $Sat_Info ;
		echo $Sat_Info->INCLINATION . ": " . $Sat_Info ;
		echo $Sat_Info->RA_OF_ASC_NODE . ": " . $Sat_Info ;
		echo $Sat_Info->ARG_OF_PERICENTER . ": " . $Sat_Info ;
		echo $Sat_Info->MEAN_ANOMALY . ": " . $Sat_Info ;
		echo $Sat_Info->EPHEMERIS_TYPE . ": " . $Sat_Info ;
		echo $Sat_Info->CLASSIFICATION_TYPE . ": " . $Sat_Info ;
		echo $Sat_Info->NORAD_CAT_ID . ": " . $Sat_Info ;
		echo $Sat_Info->ELEMENT_SET_NO . ": " . $Sat_Info ;
		echo $Sat_Info->REV_AT_EPOCH . ": " . $Sat_Info ;
		echo $Sat_Info->BSTAR . ": " . $Sat_Info ;
		echo $Sat_Info->MEAN_MOTION_DOT . ": " . $Sat_Info ;
		echo $Sat_Info->MEAN_MOTION_DDOT . ": " . $Sat_Info ;
		}
		print $xmlDoc->saveXML();
}
ASN()
?> 

