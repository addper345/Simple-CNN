function createGrid() {
    if(document.getElementById('container') == null){
        container = document.createElement('div');
        document.getElementsByTagName('body').appendChild(container);
    }
    
    for(let i = 1; i<=28; i++){
        container = document.getElementById("container");
        row = document.createElement('div');
        row.setAttribute("class", "row");
        container.appendChild(row);
        for(let j = 1; j<=28; j++){
            square = document.createElement('div');
            square.classList.add("square");
            square.classList.add("${i},${j}")
            row.appendChild(square);
        }

    }

}

function draw(e) {
    square = e.currentTarget;
    let id = square.id;
    id = square.id.split(',');
    for(let i = 0; i<2; i++){
        for(let j = 0; j<2; j++){
            a = i+Number(id[0]);
            b = j+Number(id[1]);
            if(a<=28 && b<=28){
                square = document.getElementById("${a},${b}");
                square.style.color = "black";
            }
        }
    }
}

createGrid();
