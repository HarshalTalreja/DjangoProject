var restart_button = document.querySelector("#restartButton");
var table_cell = document.querySelectorAll("td");

function clearBoard() {
  for (var i = 0; i < table_cell.length; i++) {
    table_cell[i].textContent = '';
  }
}

function changeTile(tile) {
  if (this.textContent === '') {
    this.textContent = 'X';
  }
  else if (this.textContent === 'X') {
    this.textContent = 'O';
  }
  else {
    this.textContent = '';
  }
}

restartButton.addEventListener('click', clearBoard)

for (var i = 0; i < table_cell.length; i++) {
  table_cell[i].addEventListener('click', changeTile)
}
