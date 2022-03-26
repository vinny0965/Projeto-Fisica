
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
}

velocity_label      = document.getElementById('1');
velocity_input      = document.getElementById('2');
aceleration_label   = document.getElementById('3');
aceleration_input   = document.getElementById('4');

var label_style = 
`
background-color: rgb(0, 105, 146);
color: white;
border: 1px solid rgba(27, 31, 35, 0.15);
border-radius: 6px;
font-size: 14px;
font-weight: 600;
line-height: 20px;
height: 22px;
width: 100px;
padding: 6px 16px;
text-align: center;
display: inline-block;
margin-right: -20;
`
velocity_label.style.cssText    = label_style
aceleration_label.style.cssText = label_style

var input_style = 
`
color: black;
background:white;
border-radius: 6px;
box-shadow: rgba(27, 31, 35, .1) 0 1px 0;
box-sizing: border-box;
font-size: 14px;
font-weight: 600;
line-height: 20px;
padding: 6px 16px;
text-align: center;
`
velocity_input.style.cssText    = input_style
aceleration_input.style.cssText = input_style

var canvas = document.querySelectorAll('canvas')
var scene_div = document.getElementsByClassName('glowscript-canvas-wrapper ui-resizable')

var graph0_div = document.getElementById('graph0')
var graph1_div = document.getElementById('graph1')
var graph2_div = document.getElementById('graph2')

var graph_style = `margin: 30px; box-shadow: 2px 2px 15px black;`

graph0_div.style.cssText += graph_style
graph1_div.style.cssText += graph_style
graph2_div.style.cssText += graph_style

var body = document.body
body_style = document.createElement('style');
body_style.type = 'text/css';
body.appendChild(body_style);
body.style.cssText = 'text-align: -webkit-center;'