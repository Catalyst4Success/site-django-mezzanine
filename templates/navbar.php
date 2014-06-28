<?php
$page = $_SERVER['REQUEST_URI'];
?>
<div id="navbarfiller">
    <div id="navbar" class="navbar navbar-default">
        <div class="container">
            <div class="navbar-header">
              <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#collapse-nav">
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
              </button>
                <a href="index.php" class="navbar-brand">
                    <img src="files/logotransparent.png" style="height: 45px;">
                    <div style="margin-left:7px; display: inline;">Catalyst for Success</div>
                </a>
            </div>
            <div class="collapse navbar-collapse" id="collapse-nav">
                <ul style="padding-left: 10px;" class="nav navbar-nav">
                    <li class="<?php if($page == '/index.php') echo 'active'; else echo 'hover-active';?>"><a href="index.php"><i class="fa fa-home"></i> HOME</a></li>
                    <li id="about" class="dropdown <?php if($page == '/about.php' || $page == '/videos.php' || $page == '/pressrelease.php') echo 'active'; else echo 'hover-active-dropdown';?>">
                    <a class="dropdown-toggle" href="about.php">
                        <i class="fa fa-question-circle"></i> ABOUT</a>
                    <ul class="dropdown-menu">
                        <li><a href="about.php">Our Goal</a></li>
                        <li><a href="videos.php">Videos</a></li>
                        <li><a href="pressrelease.php">Press Releases</a></li>
                    </ul>
                    </li>
                    <li class="<?php if($page == '/members.php') echo 'active'; else echo 'hover-active';?>"><a href="members.php"><i class="fa fa-users"></i> OUR TEAM</a></li>
                    <li class="<?php if($page == '/board.php') echo 'active'; else echo 'hover-active';?>"><a href="board.php"><i class="fa fa-flask"></i> ADVISORY BOARD</a></li>

                    <li class="dropdown <?php if($page == '/localchapters.php') echo 'active'; else echo 'hover-active-dropdown';?>">
                    <a class="dropdown-toggle" href="localchapters.php">
                        <i class="fa fa-book"></i> LOCAL CHAPTERS</a>
                    <ul class="dropdown-menu">
                        <li class="hidden-md hidden-lg hidden-sm"><a href="localchapters.php">About Local Chapters</a></li>
                        <li><a href="http://wv.catalyst4success.org">Westview High School</a></li>
                        </li>
                    </ul>

                    <li class="dropdown <?php if($page == '/signup.php') echo 'active'; else echo 'hover-active-dropdown';?>">
                    <a class="dropdown-toggle" href="signup.php">
                        <i class="fa fa-envelope"></i> CONTACT US</a>
                    <ul class="dropdown-menu">
                        <li><a href="signup.php">FAQ:</a></li>
                        <li><a href="signup.php#admin">Administrators</a></li>
                        <li><a href="signup.php#sponsors">Sponsors</a></li>
                        <li><a href="signup.php#members">Prospective members</a></li></ul>
                    </li>

                    <li class="<?php if($page == '/donate.php') echo 'active'; else echo 'hover-active';?>"><a href="donate.php"><i class="fa fa-gift"></i> DONATE</a></li>
                </ul>
            </div>
        </div>
    </div>
</div>
