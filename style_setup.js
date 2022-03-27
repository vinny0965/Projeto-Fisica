
var buttons = document.getElementsByTagName('button');
var button_style = 
`
background-color: #2ea44f; 
border: 1px solid rgba(27, 31, 35, .15); 
border-radius: 6px;
box-shadow: rgba(27, 31, 35, .1) 0 1px 0;
box-sizing: border-box;
color: #fff;
cursor: pointer;
display: inline-block;
font-family: -apple-system,system-ui,"Segoe UI",Helvetica,Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji";
font-size: 14px;
font-weight: 600;
line-height: 20px;
padding: 6px 16px;
position: relative;
text-align: center;
text-decoration: none;
user-select: none;
-webkit-user-select: none;
touch-action: manipulation;
vertical-align: middle;
white-space: nowrap;
`

for (let i = 0; i < buttons.length; i++) {
    let button = buttons[i];
    button.style.cssText = button_style
    if(button.innerText == "Executar"){
        var run_button = button
    }
}

var object_initial_velocity_label = document.getElementById('1');
var object_initial_velocity_input = document.getElementById('2');
var object_initial_aceleration_label = document.getElementById('3');
var object_initial_aceleration_input = document.getElementById('4');
var aceleration_variation_label = document.getElementById('7');

var label_style = 
`
    background-color: rgb(0, 105, 146);
    color: white;
    border: 1px solid rgba(27, 31, 35, 0.15);
    border-radius: 6px;
    line-height: 20px;
    height: 22px;
    padding: 6px 16px;
    text-align: center;
    display: inline-block;
    margin-right: -20px;
`
object_initial_velocity_label.style.cssText = label_style
object_initial_aceleration_label.style.cssText = label_style
aceleration_variation_label.style.cssText = label_style
aceleration_variation_label.style.cssText += 'width: 1100px;'

var input_style = 
`
    color: black;
    background: white;
    border-radius: 6px;
    font-size: 14px;
    line-height: 20px;
    padding: 6px 16px;
    text-align: center;
    width: 100;
`
object_initial_velocity_input.style.cssText = input_style
object_initial_aceleration_input.style.cssText = input_style

var graph_style = `margin: 30px; box-shadow: 2px 2px 15px black;`
var graph0_div = document.getElementById('graph0')
var graph1_div = document.getElementById('graph1')
var graph2_div = document.getElementById('graph2')

graph0_div.style.cssText += graph_style
graph1_div.style.cssText += graph_style
graph2_div.style.cssText += graph_style

var body = document.body
body_style = document.createElement('style');
body_style.type = 'text/css';
body.appendChild(body_style);
body.style.cssText = 'text-align: -webkit-center;'

var msg = ""
run_button.onclick = function readyToRun(){
    msg = ""
    if(object_initial_aceleration_input.value == ""){
        msg += "Informe a aceleração do objeto!\n"
    }
    if(isNaN(object_initial_aceleration_input.value)){
        msg += "Digite apenas numeros para informar a aceleração!\n"
    }
    if(object_initial_velocity_input.value == ""){
        msg += "Informe a avelocidade inicial do objeto!\n"
    }
    if(isNaN(object_initial_velocity_input.value)){
        msg += "Digite apenas numeros para informar a velocidade inicial!"
    }
    if(!msg == ""){
        alert(msg)
    }
}