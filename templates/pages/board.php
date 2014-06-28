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
<div>
<h1 style="color:#56C5C5;"><center>Advisory Board</center></h1>
</div>
<div class="row" style="padding-left: 25px; width:100%;">
        <div class="col-md-4">
            <img style="float: left; padding-right: 10px;" src="files/members/mfox.jpg">
            <h2>Dr. Marye Anne Fox</h2>
            <h4>UC San Diego Chancellor Emerita</h4>
	    <p>Dr. Fox, a world-renowned chemist, was the seventh chancellor of the University of California, San Diego and is a distinguished professor of chemistry. Before her appointment as UC San Diego.s Chancellor, Fox served as North Carolina State University's 12th chancellor, as distinguished university professor of chemistry at NC State (from 1998 to 2004) and as Waggoner Regents Chair in chemistry and Vice President for Research at the University of Texas at Austin. She has been elected to membership in the National Academy of Sciences and the American Philosophical Society, and to fellowships both in the American Academy of Arts and Sciences and the American Association of Advancement of Science. In October 2010, President Barack Obama named Fox to receive the National Medal of Science, the highest honor bestowed by the United States government on scientists, engineers and inventors. She has also received honorary degrees from 12 institutions in the U.S. and abroad.</p>
        </div>
        <div class="col-md-4">
                <img style="float: left; padding-right: 10px;" src="files/members/MarindaWu.jpg">
                <h2>Dr. Marinda Li Wu*</h2>
                <h4>2013 President of American Chemical Society</h4>
                <p>Dr. Wu graduated with a Ph.D from the University of Illinois and worked at Dow Chemical for almost 17 years. There, she led both fundamental and applied research in various applications involving polymers, medical devices, membrane separations, advanced electrochemical batteries and catalysis. She founded Science is Fun, an organization that aims to "improve education at all levels" and "promote science education". Dr. Wu has been a member of the American Chemical Society (ACS) since 1971 and has held many positions before being elected President of ACS. The ACS is the largest scientific society in the world with over 163,000 members with scientific backgrounds from over 100 countries around the globe. More information is available here: <a href="http://www.acs.org">www.acs.org</a></p>
		</div>
	   <div class="col-md-4">
       <img style="float: left; padding-right: 10px; height:133px;" src="files/members/dianne-jacob-s.jpg">
       <h2>Dianne Jacob*</h2>
       <h4>San Diego County Supervisor</h4>
       <p>Dianne Jacob was re-elected to San Diego County Board of Supervisors for an historic sixth term in 2012. The San Diego State University alumna is proud to represent the more than 620,000 constituents who live in the dynamic Second District, including more than 270,000 unincorporated residents. The district is the largest of the five and covers more than 2,000 square miles. It includes all of the unincorporated communities in East County, including the Ramona and Julian areas, and the cities of El Cajon, La Mesa, Lemon Grove, Santee and Poway, and communities of Allied Gardens, College Area, Del Cerro, Grantville, Navajo, Rolando and San Carlos in the City of San Diego. Prior to her election to the Board of Supervisors, Dianne worked as a teacher in the East County, and was a member of the Jamul-Dulzura Union School District Board for 17 years. She was active in the California School Boards Association and served as its President in 1987.</p>
   </div>
	   
</div>
<div class="row" style="padding-left: 25px; width:100%;">
  <div class="col-md-4">
                <img style="float: left; padding-right: 10px;" src="files/members/JohnCollins.jpg">
		<h2>Dr. John P. Collins</h2>
		<h4>Superintendent of Poway Unified School District</h4>
		<p>Dr. Collins received his doctorate in Educational Leadership from the Joint Doctoral Program at the University of California at San Diego/San Diego State University/ California State University at San Marcos. He came to the Poway Unified School District in 1989 as an assistant principal at Twin Peaks Middle School. He has since held many positions in Poway at the school and district level and currently serves as Superintendent of the Poway Unified School District. In addition, Dr. Collins serves as secretary for the Citizens. Oversight Committee for both Propositions U and C Bonds. He is also a member of the San Diego State University Ed.D. Educational Leadership Community Partnership Governance Committee and a member of Junior Achievement San Diego &amp; Imperial County Board of Directors.</p>
		</div>
   <div class="col-md-4">
                <img style="float: left; padding-right: 10px;" src="files/members/cassen.jpg">
		<h2>Todd Cassen</h2>
		<h4>Principal of Westview High School</h4>
		<p>A graduate of California State University at Long Beach, Mr. Cassen began his teaching career at Western High School in the Anaheim Union High School District. In 1995 Mr. Cassen and his family moved to San Diego, and in 1996 continued his teaching career at Poway High School within the Poway Unified School District. After six years at Poway High School Mr. Cassen accepted the position of Athletic Director for Westview High School, a new school in the district that was preparing to open its doors in the fall of 2002. For two years Mr. Cassen worked with all stakeholders in the community to build the Wolverine Athletic Program and set a strong foundation for the young program. In the fall of 2004 Mr. Cassen earned his Master.s Degree in Educational Administration from National University and transitioned into one of the Area Administrator roles on the Westview campus. After six years as an Area Administrator, Mr. Cassen was named as the Principal of Westview High School in January of 2011.</p>
		</div>
</div>
<center>*Honorary member</center>

       <?php include("footer.php") ?>
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
