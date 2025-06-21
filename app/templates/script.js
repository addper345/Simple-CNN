let hold = false;

function createGrid() {
    // if(document.getElementById('container') == null){
    //     container = document.createElement('div');
    //     document.getElementsByTagName('body').appendChild(container);
    // }
    for(let i = 1; i<=28; i++){
        container = document.getElementById("container");
        container.addEventListener("mousedown", ()=> {
            hold = true;
        })
        container.addEventListener("mouseup", () => {
            hold = false;
        })
        row = document.createElement('div');
        row.setAttribute("class", "row");
        row.setAttribute("draggable", "false");
        container.appendChild(row);
        for(let j = 1; j<=28; j++){
            square = document.createElement('div');
            square.classList.add("square");
            square.setAttribute("id", `${i},${j}`);  
            square.setAttribute("draggable", "false");
            square.addEventListener("mouseover", drawHold);
            row.appendChild(square);
          
        }

    }

}

function drawHold(e) {
    target = e.currentTarget;
    if(hold){
        draw(e);
    }
}

function draw(e) {
    let square = e.currentTarget;
    let id = square.id;
    id = id.split(',');
    for(let i = 0; i<2; i++){
        for(let j = 0; j<2; j++){
            let a = i+Number(id[0]);
            let b = j+Number(id[1]);
            if(a<=28 && b<=28){
                square = document.getElementById(`${a},${b}`);
                square.style.backgroundColor = "black";
            }
        }
    }
}


createGrid();

let button = document.querySelector("button");


button.addEventListener("onclick");
