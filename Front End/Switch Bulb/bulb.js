let btn = document.getElementById('toggleBtn')
let bulb = document.getElementById('bulb')
btn.addEventListener('click',toggleBulb)

function toggleBulb(e){
    if(btn.textContent.includes('On')){
        bulb.src = "/img/Bulb_ON.PNG"
        btn.textContent = "Turn Off"
    }else{
        btn.textContent = "Turn On"
        bulb.src = "/img/Bulb_OFF.PNG"
    }
}
