<script>
function formValidation()
{
	var passid = document.registration.password;
	var ufname = document.registration.fname;
	var ulname = document.registration.lname;
	
	var ucontact = document.registration.contact;
	// var ucountry = document.registration.country;
	var uemail = document.registration.email;
	/*var umsex = document.registration.msex;
	var ufsex = document.registration.fsex; */
	if(passid_validation(passid,7,12))
	{
		if(allLetter(ufname))
		{
			if(allLetters(ulname))
			{
				 
					
						if(allnumeric(ucontact))
						{
							
							 
						}
					
				
			}
		}
	}
	return false;
}



function passid_validation(passid,mx,my)
{
var passid_len = passid.value.length;
if (passid_len == 0 ||passid_len >= my || passid_len < mx)
{
alert("Password should not be empty / length be between "+mx+" to "+my);
passid.focus();
return false;
}
return true;
}
function allLetter(ufname)
{ 
var letters = /^[A-Za-z]+$/;
if(uname.value.match(letters))
{
return true;
}
else
{
alert('Username must have alphabet characters only');
uname.focus();
return false;
}
}
function allLetters(ulname)
{ 
var letters = /^[A-Za-z]+$/;
if(uname.value.match(letters))
{
return true;
}
else
{
alert('Username must have alphabet characters only');
uname.focus();
return false;
}
}


/*function countryselect(ucountry)
{
if(ucountry.value == "Default")
{
alert('Select your country from the list');
ucountry.focus();
return false;
}
else
{
return true;
}
}*/
function allnumeric(ucontact)
{ 
var numbers = /^[0-9]{10}$/;
if(uzip.value.match(numbers))
{
return true;
}
else
{
alert('Contact must have numeric characters only');
uzip.focus();
return false;
}
}
function ValidateEmail(uemail)
{
var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
if(uemail.value.match(mailformat))
{
return true;
}
else
{
alert("You have entered an invalid email address!");
uemail.focus();
return false;
}
} 
/*function validsex(umsex,ufsex)
{
x=0;

if(umsex.checked) 
{
x++;
} if(ufsex.checked)
{
x++; 
}
if(x==0)
{
alert('Select Male/Female');
umsex.focus();
return false;
}
else
{
alert('Form Succesfully Submitted');
window.location.reload()
return true;
}*/
</script>