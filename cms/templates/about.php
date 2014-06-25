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
<div class="about">
    <center>
        <h1 style="color:#9ACD32">About Catalyst for Success</h1>
        <p> Inspiring a new generation of scientists</p>
        <a href="https://www.youtube.com/watch?v=3wbIP_jWF0s">
            <img src="files/mission.jpg" style="width:20%; min-width:250px;"><br><br></a>
    </center>
    <p style="padding-left:15%; padding-right:15%;">Catalyst for Success, a registered 501(c)(3) non-profit organization, was founded in 2012 by Jason Ge, a junior in high school and a silver medalist from Team USA at the International Chemistry Olympiad. All of our activities and programs are planned out and executed by high school students. Our goal is to promote STEM (science, technology, engineering, and math) for young students in order to inspire them to become the world's future scientists and innovators.</p><br><br>
</div>

<div class="our-programs">
    <h1><center>OUR PROGRAMS</center></h1>
</div>
    <center>
    <img style="width:49.8%;" src="files/about-show.jpg">
    <img style="width:49.8%;" src="files/about-handson.jpg">
    </center>
<div class="row" style="padding-left: 25px; width:100%;">
    <div class="col-md-6 hands-on">
        <center>
            <h2 style="color:#FFA319">The Magic Show</h2>
            <p style="color:#FFA319">The first component of our program focuses around a chemistry magic show that consists of many cool demonstrations that present science in a fun and engaging way, not just a "textbook" subject. Since beginning this program in February 2013, we have already reached over 20,000 students through our magic shows.</p>
        </div>
    </center>
    <div class="col-md-6 hands-on">
        <center>
            <h2 style="color:#9ACD32">Hands-On Activities</h2>
            <p style="color:#9ACD32"> The magic shows are a wonderful way of getting students interested in science. But we didn't want to stop at interest. We want to provide a way for students to engage with science in a very interactive way. Thats why we also provide hands-on activities for students where they get the opportunity to experiment and test out their passion for science. Since starting this component of our program in mid-March, we have already reached out to nearly 100 classrooms with our hands on activities.
        </center>
    </div>

    <div class="row" style="padding-left: 25px; width:100%;">
        <div class="col-md-6 col-md-offset-3">
            <center>
                <h2 style="color:#800080">Since February 2013 we have...</h2>
                <p style="color:#800080"> Performed over 60 shows for over 20,000 students from in the Poway, San Diego, Chula Vista, Del Mar, Jamul, and Oceanside districts.</p>
                <p style="color:#800080"> Conducted hands-on science labs with dozens of classrooms</p>
                <p style="color:#800080"> Started 5 local high school chapters in San Diego and one chapter in Philadelphia, Pennsylvania.</p>
            </center>
        </div>
    </div>


</div>
<br><br>
<div class="local-chapters">
    <h1><center>LOCAL CHAPTERS</center></h1>
</div>
<div class="row" style="padding-left: 25px; width:100%;">
    <div class="col-md-8 col-md-offset-2">
        <br>
        <p>Our local high school chapters are branches of the organization that allow us to reach out to a larger part of the community. We have San Diego chapters established at Westview High School, Rancho Bernardo High School, Poway High School, Patrick Henry High School, and Del Norte High School. And we are happy to welcome our newest chapter at Upper Dublin in Philadelphia, Pennsylvania!</p>
        <center><p>For more information about individual chapters and instructions on how to start a new chapter, please visit our <a href="localchapters.php">Local Chapters</a> page.</p></center>
    </div>
</div>
<br><br>
<div class="show-experiments">
    <h1><center>THE SHOW EXPERIMENTS</center></h1>
</div>
<div class="row" style="padding-left: 25px; width:100%;">
    <div class="col-md-8 col-md-offset-2">
        <br>
        <center>
            <p>In order to inspire kids through science, we believe that they need to know the fundamentals behind our show experiments. Here are videos of the chemistry experiments in our shows, which also explain the science behind the experiments.</p>
        </center>
    </div>
</div>
<br>
<div class="row" style="padding-left: 25px; width:100%;">
    <div class="col-sm-2 col-sm-offset-2">
        <center>
            <a href="videos.php#balloon">
                <img src="files/balloon.png" alt="...">
            </a>
            <p>Hydrogen Balloon</p>
        </center>
    </div>
    <div class="col-sm-2 col-sm-offset-1">
        <center>
            <a href="videos.php#CO2">
                <img src="files/staircase.png" alt="...">
            </a>
            <p>CO2 Staircase</p>
        </center>
    </div>

    <div class="col-sm-2 col-sm-offset-1">
        <center>
            <a href="videos.php#flag">
                <img src="files/flag.png" alt="...">
            </a>
            <p>American Flag</p>
        </center>
    </div>

</div>
<br>
<div class="row" style="padding-left: 25px; width:100%;">
    <a href="videos.php">
        <center><button type="button" class="btn btn-warning">See More</button></center>
    </a>
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

</body></html>
