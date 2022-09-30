$("#crt").hide();
$("#printbtn").hide();
$("#muhar").hide();
$("#lab").hide();
$("#name").hide();
$("#bar").hide();
var $id = $("#tid").text();
var $target = $("#target").text();
var $time = $("#time").text();
var $count = localStorage.getItem($id);
var $mode = localStorage.getItem("mode");


function setCount($id, $count) {
  localStorage.setItem($id, $count);
}

if($mode == null){
  setCount("mode", "Slow");
} else {
  $('#mode').html($mode);
}

if($count == null){
  setCount($id, 0);
} else {
  $('#done').html($count);
}


$width = ((parseInt($count)) * 100) / parseInt($target)
var $x = $width + "%";
$("#done").css("width", $x);


function mode(){
  $(document).ready(function(){
    var $x = $("#mode").text();
    if($x == "Fast"){
      $("#mode").html("Slow");
      localStorage.setItem("mode", "Slow")
    } else {
      $("#mode").html("Fast");
      localStorage.setItem("mode", "Fast")

    }
  })
}

function disAble(){
  $(document).ready(function(){

    $('#tcom').hide();

    $('#btn1').hide();
    $('#mode').hide();
    $('#back').hide();
    $("#mcom").show();
    $('#name').show();
    $("#muhar").show();
    $("#printbtn").show();
    $("#progress").css({"font-size":"17px"});


  });
}

$("#transbar").hide();
function trns(){
  $(document).ready(function(){
    $('#btn1').attr('disabled','true');

    var $done = $("#done").text();
    $done = parseInt($done) + 1;
    if($done >= 0 && $done < $target){
      setCount($id, $done);
      $("#done").html($done);
    } else if($done >= $target) {
      $("#done").html("TASK COMPLETED");
      disAble();
    }
    $done = $done + "%";
    $("#done").css("width", $done);

    $("#pbar").css("width", "0%");
    $("#transbar").show();
    $("#pbar").show();
    var $t = parseInt($time)*1000;
    if($("#mode").text() == "Slow"){
      $t = ($t*3)/5;
      var $targ = "width " + $t;
      $("#pbar").css("transition", $targ);
    }
    $("#pbar").css("width", "100%");

    window.setTimeout(function (){
      $('#transbar').hide();
      $("#btn1").removeAttr('disabled');
    }, $t);

  });
}

function PrintCerti(){
  $('.navbar').hide();
  $('#back').hide();
  $('#printbtn').hide();
  $('#footer').hide();
  window.print();
    return false;
}
