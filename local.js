document.addEventListener("DOMContentLoaded", function(){
$('.preloader-background').delay(900).fadeOut('slow');

$('.preloader-wrapper')
    .delay(900)
    .fadeOut();
});

$(document).ready(function() {
$('select').material_select();
});
    

var editor = ace.edit("jsEditor");
editor.getSession().setMode("ace/mode/python");
editor.setTheme("ace/theme/twilight");
document.getElementById('jsEditor').style.fontSize='20px';
var x=1;
function toggletheme()
{
Materialize.Toast.removeAll();
if(x)
{
    Materialize.toast('Light theme', 4000);
    editor.setTheme("ace/theme/github");
}
else
{
    Materialize.toast('Dark theme', 4000);
    editor.setTheme("ace/theme/twilight");
}
x=!x;
}

function contentcopy()
{
var papa = editor.session.getTextRange(editor.getSelectionRange());
if(papa == "")
{
    var sel = editor.selection.toJSON(); 
    editor.selectAll();
    editor.focus();
    document.execCommand('copy');
    editor.selection.fromJSON(sel); 
}
else
{
    document.execCommand('copy');
}
Materialize.Toast.removeAll();
Materialize.toast('Copied to clipbord', 4000);
}

var textarea = $('textarea[name="ditor"]');
textarea.val(editor.getSession().getValue());
editor.getSession().on("change", function () {
textarea.val(editor.getSession().getValue());
});

$('.button-collapse').sideNav({
menuWidth: 300,
edge: 'left',
closeOnClick: false,
draggable: true
});

var slider = document.getElementById("fontsize");
slider.oninput = function()
{
var sizee = this.value;
document.getElementById('jsEditor').style.fontSize=sizee +'px';
}
