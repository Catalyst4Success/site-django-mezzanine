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
<br>
<div class="localchapters">
    <center>
        <h1 style="color:#FF0000">LOCAL CHAPTERS</h1>
        <p>Find your nearest Catalyst chapter to book an event or to get involved!</p>
    </center><br>
</div>
<div class="container hidden-xs hidden-sm hidden-md" style="width:70%">
    <div class="row" style="width:100%;">
        <div class="col-md-4 col-md-offset-1" style="padding-right:0px">
        <ul id="row" class="nav nav-pills nav-stacked">
            <li class="active" id="wv" onclick="changeChapter('wv')"><a href="#"><center>Westview High School</center></a></li>
            <li id="dn" onclick="changeChapter('dn')"><a href="#"><center>Del Norte High School</center></a></li>
            <li id="rb" onclick="changeChapter('rb')"><a href="#"><center>Rancho Bernardo High School</center></a></li>
            <li id="fp" onclick="changeChapter('fp')"><a href="#"><center>Francis Parker High School</center></a></li>
            <li id="ph" onclick="changeChapter('ph')"><a href="#"><center>Patrick Henry High School</center></a></li>
            <li id="ud" onclick="changeChapter('ud')"style="border-bottom:1px solid black;"><a href="#"><center>Upper Dublin High School</center></a></li>
        </ul>
        </div>
        <div class="col-md-7" id="map" style="border:1px solid black; border-left:0px; background-color:#7DCBE5 ">
            <div class="col-md-6">
                <img id="sd-map" src="files/C4S-SD-map.png" style="max-width:100%">
            </div>
            <div class="col-md-6" style="max-width:100%">
<center>
<br><br>
                <p style="font-weight:bold" id="school-name">Westview High School</p>
                <p id="school-address">13500 Camino Del Sur<br>San Diego, CA, 92129</p>
                <a id="school-website" href="http://wv.catalyst4success.org">http://wv.catalyst4success.org</a>
                <p id="school-contact">(858)212-7456<br>c4swestview@gmail.com</p>
</center>
            </div>
        </div>
    </div>
</div>
<div class="row" style="width:100%">
<br>
   <center><p>Can't find a chapter close to you? <a href="signup.php">Contact us</a> about booking an event or start your own chapter!</p></center> 
</div>
<br><div class="join-chapter">
<h2 style="color:white;"><center>Join a chapter!</center></h2>
</div>
<div class="container local-chapters-faq-1" style="width:70%">
<br><p style="font-weight:bold">My school has a chapter, how do I join?</p><p>Follow the link to your chapter's website. There you can find the contact information of leaders who will be happy to welcome you to
the Catalyst family.</p>
<br>
<p style="font-weight:bold">Should I join even if science isn't my 'thing'?</p><p>Yes, it doesn't take a genius. It takes a determined well rounded individual who is able to communicate effectively and respectfully. Our chapters also need artists, computer programmers, skilled writers, and graphic designers.</p>
<br><br>
</div>
<div class="start-chapter">
<h2 style="color:white;"><center>Or start a chapter!</center></h2>
</div>
<div class="container local-chapters-faq-2" style="width:70%">
<br><p style="font-weight:bold">My school doesn't have a chapter, can I start one?</p><p>Yes, yes you can! Starting a Catalyst chapter is a bit more involved than starting a usual club, but then, Catalyst is anything but usual!</p>
<br>
<p style="font-weight:bold">My high school is in or near San Diego country: </p><p>The first step is to contact a representative from the organization. We will visit your school to speak with your administrators about
the program. If everything checks out, we will help you complete your club application forms and select and train an interim leadership team to get the chapter off to a solid start.</p>
<br>
<p style="font-weight:bold">Anywhere else in the nation: </p><p>Starting a chapter begins with completing a pre-establishment checklist. Obtain the checklist by contacting the organization.</p>
<br>
<p style="font-weight:bold">My university is in or near San Diego county: </p><p>Before establishing yourself on campus, get together a group of interested individuals and contact our organization. We will meet
with you to discuss your first steps.</p>
<br><br>
<center>
<p style="color:#FFA319">I'm inquisitive, I have more questions!<br><br>Email us at info@catalyst4success.org with your inquiry.</p>
</div>

<br><br><br><br><br>
   <?php include("footer.php") ?>

$(window).on("load", function(){
    var rowheight = $("#row").innerHeight();
    $("#map").height(rowheight - 2);
    $("#sd-map").height(rowheight -2);
});

$(window).on('resize', function() {
    var rowheight = $("#row").innerHeight();
    console.log("test");
    $("#map").height(rowheight - 2);
    $("#sd-map").height(rowheight -2);
});

</script>
<script>
function changeChapter(chapter){
    $("#wv").attr("class", " ");
    $("#dn").attr("class", " ");
    $("#rb").attr("class", " ");
    $("#fp").attr("class", " ");
    $("#ph").attr("class", " ");
    $("#ud").attr("class", " ");
    $("#" + chapter).attr("class", "active");
    if(chapter == "wv"){
        $("#school-name").html("Westview High School");
        $("#school-address").html("13500 Camino Del Sur<br>San Diego, CA, 92129");
        $("#school-website").html("http://wv.catalyst4success.org");
        $("#school-website").attr("href", "http://wv.catalyst4success.org");
        $("#school-contact").html("(858)212-7456<br>c4swestview@gmail.com");
   }
if(chapter == "dn"){
        $("#school-name").html("Del Norte High School");
        $("#school-address").html("16601 Nighthawk Ln<br>San Diego, CA, 92127");
        $("#school-website").html("http://dn.catalyst4success.org");
        $("#school-website").attr("href", "http://dn.catalyst4success.org");
        $("#school-contact").html("");
   }
if(chapter == "rb"){
        $("#school-name").html("Rancho Bernardo High School");
        $("#school-address").html("13010 Paseo Lucido<br>San Diego, CA, 92128");
        $("#school-website").html("http://rb.catalyst4success.org");
        $("#school-website").attr("href", "http://rb.catalyst4success.org");
        $("#school-contact").html("");
   }
if(chapter == "fp"){
        $("#school-name").html("Francis Parker High School");
        $("#school-address").html("6501 Linda Vista Rd<br>San Diego, CA, 92111");
        $("#school-website").html("http://fp.catalyst4success.org");
        $("#school-website").attr("href", "http://fp.catalyst4success.org");
        $("#school-contact").html("");
   }
if(chapter == "ph"){
        $("#school-name").html("Patrick Henry High School");
        $("#school-address").html("6702 Wandermere Dr<br>San Diego, CA, 92120");
        $("#school-website").html("http://ph.catalyst4success.org");
        $("#school-website").attr("href", "http://ph.catalyst4success.org");
        $("#school-contact").html("");
   }
if(chapter == "ud"){
        $("#school-name").html("Upper Dublin High School");
        $("#school-address").html("800 Loch Alsh Ave<br>Fort Washington, PA, 19034");
        $("#school-website").html("http://ud.catalyst4success.org");
        $("#school-website").attr("href", "http://ud.catalyst4success.org");
        $("#school-contact").html("");
   }

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
