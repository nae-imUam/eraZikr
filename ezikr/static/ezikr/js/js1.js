function mode(){
  $(document).ready(function(){
    var $x = $("#mode").text();
    if($x == "Fast"){
      $("#mode").html("Slow");
    } else {
      $("#mode").html("Fast");
    }
  })
}


$("#transbar").hide();
function trns(){
  console.log("in trns");
  $(document).ready(function(){
    var $nl = $("#gstr li").length;
    $("li").hide();
    $("#pbar").css("width", "0%");
    $("#transbar").show();
    $("#pbar").css("width", "100%");
    var $t = 3010 / $nl;
    $("li").each(function( index ) {

      window.setTimeout(function(){
        console.log("li");
      }, 200);
    });
    window.setTimeout(function (){$('#transbar').hide(); $("li").show();
 }, 3010);

  });
}
