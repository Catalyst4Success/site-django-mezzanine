<!DOCTYPE html>
<!-- saved from url=(0030)http://bootswatch.com/default/ -->
<html lang="en"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<meta charset="utf-8">
<title>Catalyst 4 Success</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="custom/custom-bootstrap.css" media="screen">
<link rel="stylesheet" href="files/styles.css" media="screen">
<!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
<!--[if lt IE 9]>
      <script src="../bower_components/html5shiv/dist/html5shiv.js"></script>
      <script src="../bower_components/respond/dest/respond.min.js"></script>
    <![endif]-->
<link href="https://netdna.bootstrapcdn.com/font-awesome/4.0.3/css/font-awesome.css" rel="stylesheet">
</head>
<body>
   <?php include("navbar.php") ?>
<div class="container">
    <br>
    <center>
        <h1 style="color:#FFA319">Show Experiments</h1>
    </center>

    <ul id="mainnav" style="text-align:center;" class="nav nav-tabs">
        <li style="float:none; display:inline-block;" class="active"><a href="#balloon" data-toggle="tab">Exploding Balloon</a></li>
        <li style="float:none; display:inline-block;" class=""><a href="#flag" data-toggle="tab">American Flag</a></li>
        <li style="float:none; display:inline-block;" class=""><a href="#BvG" data-toggle="tab">Black vs Gold</a></li>
        <li style="float:none; display:inline-block;" class=""><a href="#CO2" data-toggle="tab">CO2 Staircase</a></li>
        <li style="float:none; display:inline-block;" class=""><a href="#combustion" data-toggle="tab">Combustion Reaction</a></li>
    </ul>
    <br>
    <div class="tab-content">
        <div class="tab-pane active" id="balloon"><center>
                <div class="video-container">
                    <iframe src="http://www.youtube.com/embed/9dkvP6MhdcQ?feature=player_detailpage" frameborder="0" allowfullscreen=""></iframe>
            </div></center>
        </div>
        <div class="tab-pane" id="flag"><center>
                <div class="video-container">
                    <iframe src="http://www.youtube.com/embed/ryGMWYSvTVg?feature=player_detailpage" frameborder="0" allowfullscreen=""></iframe>
            </div></center>
        </div>
        <div class="tab-pane" id="BvG"><center>
                <div class="video-container">
                    <iframe src="http://www.youtube.com/embed/vzeL6Ruvlq0?feature=player_detailpage" frameborder="0" allowfullscreen=""></iframe>
            </div></center>
        </div>
        <div class="tab-pane" id="CO2"><center>
                <div class="video-container">
                    <iframe src="http://www.youtube.com/embed/l7PpHhnCO-I?feature=player_detailpage" frameborder="0" allowfullscreen=""></iframe>
            </div></center>
        </div>
        <div class="tab-pane" id="combustion"><center>
                <div class="video-container">
                    <iframe src="http://www.youtube.com/embed/hQWyFAR8yXI?feature=player_detailpage" frameborder="0" allowfullscreen=""></iframe>
            </div></center>
        </div>
    </div> <!--End all tab content-->
</div>
<br><br><br><br><br>
   <?php include("footer.php") ?>

<script>
$(document).ready( function(){
        var welctop = $("#welcome").offset().top;
        var welcbottom = welctop + $("#welcome").height();
        $(window).scroll(function(){
            var top = $(window).scrollTop();
            var bottom = top + $(window).height();
            if(top > welcbottom || $(window).width() < 767){
            $("#navbar").prop('class', 'navbar navbar-default navbar-fixed-top');
            }
            else{
            $("#navbar").prop('class', 'navbar navbar-default');
            }
            });
        });
</script>
<script>
function goToByScroll(id){
    // Scroll
    $('html,body').animate({
scrollTop: $("#"+id).offset().top},
'slow');
    // Scroll
}

</script>

<script>
var width = $(window).width();
var hoverover;
$(document).ready( function(){

        navbarCollapseCheck();
        $(".hover-active-dropdown").hover(
            function() { $(this).attr("class", "dropdown hover-active-dropdown active")},
            function() { $(this).attr("class", "dropdown hover-active-dropdown")}
            );

        $(".hover-active").hover(
            function() { $(this).attr("class", "hover-active active")},
            function() { $(this).attr("class", "hover-active")}
            );
        });

function navbarCollapseCheck(){
    var width = $(window).width();
    if(width < 767){
        $(".dropdown-toggle").attr("data-toggle", "dropdown"); 
        $("#navbar").prop('class', 'navbar navbar-default navbar-fixed-top');
    }
    else{
        $(".dropdown-toggle").attr("data-toggle", " "); 
        $("#navbar").prop('class', 'navbar navbar-default');
    }
}


$(window).on('resize', function() {
        navbarCollapseCheck();
        });

</script>


