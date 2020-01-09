var fname = prompt("Enter First Name:");
var lname = prompt("Enter Last Name:");
var age = prompt("Enter Age:");
var height = prompt("Enter Height in centimeters:");
var petname = prompt("Enter Nickname:");

if ((fname.charAt(0)==lname.charAt(0)) && (age>20 && age<30) && (height>=170) && (petname.charAt(petname.length - 1)=='y')) {
  console.log("Congrats! You have cleared the Spy Test.");
}
else {
  console.log("Sorry, Nothing Here");
}
