<?php 
session_start(); 
// Pear library includes
// You should have the pear lib installed
include_once('Mail.php');

//Email	
		$email = $_POST['mail'];
//IP Address
		$ip = $_REQUEST['REMOTEADDR'];

//Credit card	


$your_email = "<YOUREMAIL@name.tld>";//<<--  update this to your email address
//$your_email = 'ron.sanders@supportsages.com';//<<--  update this to your email address

$errors ='';

		$to = "<YOUREMAIL@name.tld>";
		$subject="YOUR WEBSITE - New Subscriber! ";
		$from = $email;
	
	

		$text = 
		"<h2 style='border-bottom:solid 1px #CCC;'>New Subscriber</h2>
		email:   -".$email."<br/><br/>
        ";
		
		
		$message = new Mail_mime(); 
		$message->setHTMLBody($text); 
		$body = $message->get();
		$extraheaders = array("From"=>$from, "Subject"=>$subject,"Reply-To"=>$email);
		$headers = $message->headers($extraheaders);
		$mail = Mail::factory("mail");	
		if($mail->send($to, $headers, $body))
		{
			echo "mail successful send";
		} 
		else
		{ 
			echo "there's some errors to send the mail, verify your server options";
		}

///////////////////////////Functions/////////////////
// Function to validate against any email injection attempts
function IsInjected($str)
{
  $injections = array('(\n+)',
              '(\r+)',
              '(\t+)',
              '(%0A+)',
              '(%0D+)',
              '(%08+)',
              '(%09+)'
              );
  $inject = join('|', $injections);
  $inject = "/$inject/i";
  if(preg_match($inject,$str))
    {
    return true;
   }
  else
    {
    return false;
   }
}


?>


