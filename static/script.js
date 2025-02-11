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

            } else if (type==all_types[all_types.length-1].id.toLowerCase()) {
                buttons[2].setAttribute("hidden", "")
            } else {
                buttons[1].setAttribute("hidden", "")
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
    }

    let cards = document.querySelectorAll(".card")
    cards = Array.from(cards).slice(1, cards.length);

    cards.forEach(card=>{
    list_tmp = [];

    card.querySelectorAll(".active").forEach(el2 =>  list_tmp.push(el2.textContent))
    items_selected[card.id.replace("card-", "")] = list_tmp
    })

    console.log(items_selected)
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
