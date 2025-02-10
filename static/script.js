function selected(element){
    let selected = element.classList.contains("active")
    let actions = ["active", "btn-secondary"]
    if (selected) {
        actions.forEach(e=>{
            element.classList.remove(e)
        })
    
    } else {
        actions.forEach(e=>{
            element.classList.add(e)
        })
        
    }
}

function card_selected(){
    let radios = document.querySelectorAll(".btn-group [name='btnradio']")

    document.querySelectorAll(".card").forEach(el=>{
        el.setAttribute("hidden","")
    })

    radios.forEach(e=>{
        if (e.checked) {
            let type = document.querySelector(`[for='${e.id}']`).textContent
            let card = document.querySelector(`#card-${type}`)
            let buttons = card.querySelectorAll(".buttons-controler .btn")
            let all_types = document.querySelectorAll("[options]")
            type = type.toLowerCase()
            
            card.removeAttribute("hidden")
            
            if (type == all_types[0].id.toLowerCase()){
                buttons[0].classList.add("disabled")
                buttons[1].setAttribute("hidden", "")
                console.log(0)

            } else if (type==all_types[all_types.length-1].id.toLowerCase()) {
                buttons[2].setAttribute("hidden", "")
            } else {
                buttons[1].setAttribute("hidden", "")
                console.log(2)
            }
            
    }
})

}

function next_previous(forward = true){
    let i = 0;
    btn_checks = document.querySelectorAll(".btn-group .btn-check")

    for (let e of btn_checks) {
        if (e.checked) {
            break;
        }
        i++;
    }
    
    
    if (forward){

        document.querySelectorAll(".btn-group input")[i+1].checked = true;
    }else {
        document.querySelectorAll(".btn-group input")[i-1].checked = true;
    }

    card_selected()
}

function update_value_range(element){
    document.getElementById('rangeValue').innerText = element.value;
}
  
function get_items_selected(){
    items_selected = {
        "geral": {
            "nome":null,
            "n_pessoas": null
        },
        "carnes": [],
        "bebidas": []
    }

    let carnes = document.querySelector("#carnes").children
    let carnes_array = Array.from(carnes)
    carnes_array.forEach(e=> {
        if(e.classList.contains("active")){
          items_selected["carnes"].push(e.textContent)  
        }
    })

    let bebidas = document.querySelector("#bebidas").children
    let bebidas_array = Array.from(bebidas)
    bebidas_array.forEach(e=> {
        if(e.classList.contains("active")){
          items_selected["bebidas"].push(e.textContent)  
        }
    })


    if (document.querySelector("#name_client").value == ""){
        alert("o nome cliente está vazio")
        return (null)
    }

    if (items_selected["carnes"].length == 0 ){
        alert("Nenhuma carne selecionada")
        return (null)

    }

    
    if (items_selected["bebidas"].length == 0){
        alert("Nenhuma bebida selecionada")
        return (null)

    }

    items_selected["geral"]["nome"] = document.querySelector("#name_client").value
    items_selected["geral"]["n_pessoas"] = document.querySelector("#n_clients").value

    //enviarDados(items_selected)
    return(items_selected)
}

function enviarDados(data) {
    fetch('http://localhost:5000/receber_dados', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        console.log('Success:', result);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function select_first_card(){
    document.querySelector("#card-geral")
}


card_selected()