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

createGrid();
