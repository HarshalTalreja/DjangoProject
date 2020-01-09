
var begin = prompt("Do you want to start student roster: (y/n)");
list = [];
if (begin == 'y') {
  var start = prompt("Enter the command- add, remove, display or quit");
  while(start != 'quit'){
    if (start == 'add') {
      var newitem = prompt("Enter the name to be added:");
      list.push(newitem);
    }
    else if (start == 'display') {
      console.log(list);
    }
    else if (start == 'remove') {
      var remove = prompt("Enter the name you want to remove:");
      const index = list.indexOf(remove);
      if (index>-1) {
        list.splice(index, 1);
      }
    }
    else {
      alert("Invalid Input! Enter Again.")
    }
    start = prompt("Enter the command- add, remove, display or quit");
  }
  alert("Thank you for using roster!");
}
else if (begin == 'n') {
  alert("No problem, you can begin roster by refreshing the page.")
}
else {
  alert("Invalid Input, refresh the page to start again.");
}
