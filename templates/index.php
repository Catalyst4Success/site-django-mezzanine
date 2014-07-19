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
<div class="welcome" id="welcome">
    <div class="welcome-text">
        <div class="row">
            <div class="col-md-8 col-md-offset-2">
                <img src="files/logotransparent.png" style="width:50%;" ><br><br>
                <h1 style="font-family:Lato">Catalyst for Success</h1>
                <h2>inspiring a new generation of scientists</h2>    
            </div>
                <i class="fa fa-chevron-down fa-2x down-arrow" style="color:white; position: absolute; left:50%; top:90%; cursor:pointer;" onclick="goToByScroll('navbarfiller')"></i>
        </div>
    </div>      
</div>
<?php include("navbar.php") ?>
<div class="our-mission">
    <center><h1 style="display:inline-block;">Our Mission: </h1><h1 style="font-family: Lato; display:inline-block; color:black; padding-left:20px;"> to inspire</h1></center>
    <div class="row" style="padding-top: 20px; padding-bottom:20px;" >
        <div class="col-md-6">
            <img src="files/mission.jpg" style="width: 100%;" >
        </div>
        <div class="col-md-6">
            <h3 style="color:#800080">Catalyst for Success is a registered non-profit organization that aims to promote STEM education in order to inspire a new generation of scientists.</h3> <p>We provide chemistry magic shows consisting of many cool demonstrations that present science in a fun and engaging way. In addition, we follow up our assemblies by providing classrooms with personalized "hands on" activities where the children can try learn 'Next Generation' science standards in subjects ranging from biology to computer science. </p>
            <p>
            <h3 style="color:#FA8072">Since February 2013, we have...</h3>
            <ul>
                <li>Performed for over 20,000 students from schools in the Poway, San Diego, Chula Vista, Del Mar, Jamul, and Oceanside Districts</li> 
                <li>Conducted hands-on science labs with hundreds of classrooms</li>
                </p>
            </ul>
        </div>
    </div>
    <a href="about.php"><center><button type="button" class="btn btn-primary">Learn More</button></center></a>
</div>
<div class="quote">
    <h1><center>"For all I know we may have the next Einstein sitting in one of these 1100 kids, you have to open the resources to, tap into what they have, and see what you get."</center></h1>
		<h2 style="padding-left:50%;">-De Passé, Director of Operations, Feaster Charter School<h2>
        </div>
        <div class="latest-news">
            <div class="row" style="padding-top:30px;">
                <div class="col-md-3">
                    <h1 style="font-family:Lato">LATEST NEWS:</h1>
                    <h2>because we're always working on something new</h2>
                </div>
                <div class="col-md-9">
                    <div class="row">
                        <div class="col-md-4">
     <a href="press.php?id=11">                   
     <img src="pressreleases/1.jpg" style="border:2px solid black;" width="100%">
     </a>
<center><p>UC San Diego Chancellor Emerita Marye Anne Fox Joins Catalyst Advisory Board</p></center>
                        </div>

                        <div class="col-md-4">
     <a href="press.php?id=10">                    
    <img src="pressreleases/2.jpg" style="border:2px solid black;" width="100%">
</a>                        
<center><p>Catalyst welcomes First County Official to Advisory Board</p></center>
</div>
                        <div class="col-md-4">
<a href="press.php?id=9">
    <img src="pressreleases/3.jpg"  style="border:2px solid black;" width="100%">
</a>
<center><p>New Year, New Experiments, New Chapters, No Stopping</p></center>
</div>
                        <div id="latest-news-button"><a href="pressrelease.php"><button style="margin-top:5%" type="button" class="btn btn-success pull-right">Learn More</button></a></div>
                    </div>
                </div>
            </div>
        </div>
        <div class="map hidden-xs" id="map">
            <img id="map-image" src="files/catamap.jpg" style="visibility: hidden;" width="100%">
            <div id="map-button"><a href="localchapters.php"><button type="button" class="btn btn-danger">More Ways to Get Involved</button></a></div>
        </div>
        <div class="didyouknow">
            <div class="row">
                <div class="col-md-4">
                    <center><h1>Did you know...</h1></center>
                </div>
                <div class="col-md-6">
                    <h4><?php include("fact.php") ?>
</h4>
<a href="facts.php"><center><button type="button" class="btn btn-danger">More Fun Facts</button></center></a>

                </div>
            </div>
        </div>
        <?php include("footer.php") ?>


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

        </body></html>
