<!-- Read and pharse xml file with XML errror catcher -->
<?php
 function call_Leo(){
	  // catches XML errors
	  libxml_use_internal_errors(TRUE);
	  //  path to xml file
	  $objXmlDocument = simplexml_load_file("Leo_V1.xml")
	  //if there is a problem with parshing
	  if($objXmlDocument == FALSE) {
		  print"error"
		  foreach(libxml_get_errors() as $error){
			  echo $error->message;
		  }
		  exit;
	  }
	  //savend as java script Object Notation
	  $objJsonDocument = json_encode($objXmlDocument);
	  $arrOutput = json_decode($objJsonDocument, TRUE);
	  echo "<pre>";
	  print_r($arrOutput);
	  }
	  
call_Leo()
?>
