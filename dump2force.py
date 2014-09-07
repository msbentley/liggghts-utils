



<!DOCTYPE html>
<html>
<head>
 <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" >
 <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" >
 
 <meta name="ROBOTS" content="NOARCHIVE">
 
 <link rel="icon" type="image/vnd.microsoft.icon" href="https://ssl.gstatic.com/codesite/ph/images/phosting.ico">
 
 
 <script type="text/javascript">
 
 
 
 
 var codesite_token = "ABZ6GAeaVWkSyXBNykXH6PaWSzufsKAcwQ:1410095814397";
 
 
 var CS_env = {"projectHomeUrl": "/p/liggghts-force-chains", "loggedInUserEmail": "msbentley@gmail.com", "profileUrl": "/u/108811474385654924234/", "assetHostPath": "https://ssl.gstatic.com/codesite/ph", "projectName": "liggghts-force-chains", "token": "ABZ6GAeaVWkSyXBNykXH6PaWSzufsKAcwQ:1410095814397", "assetVersionPath": "https://ssl.gstatic.com/codesite/ph/17097911804237236952", "domainName": null, "relativeBaseUrl": ""};
 var _gaq = _gaq || [];
 _gaq.push(
 ['siteTracker._setAccount', 'UA-18071-1'],
 ['siteTracker._trackPageview']);
 
 (function() {
 var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
 ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
 (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(ga);
 })();
 
 </script>
 
 
 <title>dump2force.py - 
 liggghts-force-chains -
 
 
 A python tool to generate VTK force chain data from LIGGGHTS simulations - Google Project Hosting
 </title>
 <link type="text/css" rel="stylesheet" href="https://ssl.gstatic.com/codesite/ph/17097911804237236952/css/core.css">
 
 <link type="text/css" rel="stylesheet" href="https://ssl.gstatic.com/codesite/ph/17097911804237236952/css/ph_detail.css" >
 
 
 <link type="text/css" rel="stylesheet" href="https://ssl.gstatic.com/codesite/ph/17097911804237236952/css/d_sb.css" >
 
 
 
<!--[if IE]>
 <link type="text/css" rel="stylesheet" href="https://ssl.gstatic.com/codesite/ph/17097911804237236952/css/d_ie.css" >
<![endif]-->
 <style type="text/css">
 .menuIcon.off { background: no-repeat url(https://ssl.gstatic.com/codesite/ph/images/dropdown_sprite.gif) 0 -42px }
 .menuIcon.on { background: no-repeat url(https://ssl.gstatic.com/codesite/ph/images/dropdown_sprite.gif) 0 -28px }
 .menuIcon.down { background: no-repeat url(https://ssl.gstatic.com/codesite/ph/images/dropdown_sprite.gif) 0 0; }
 
 
 
  tr.inline_comment {
 background: #fff;
 vertical-align: top;
 }
 div.draft, div.published {
 padding: .3em;
 border: 1px solid #999; 
 margin-bottom: .1em;
 font-family: arial, sans-serif;
 max-width: 60em;
 }
 div.draft {
 background: #ffa;
 } 
 div.published {
 background: #e5ecf9;
 }
 div.published .body, div.draft .body {
 padding: .5em .1em .1em .1em;
 max-width: 60em;
 white-space: pre-wrap;
 white-space: -moz-pre-wrap;
 white-space: -pre-wrap;
 white-space: -o-pre-wrap;
 word-wrap: break-word;
 font-size: 1em;
 }
 div.draft .actions {
 margin-left: 1em;
 font-size: 90%;
 }
 div.draft form {
 padding: .5em .5em .5em 0;
 }
 div.draft textarea, div.published textarea {
 width: 95%;
 height: 10em;
 font-family: arial, sans-serif;
 margin-bottom: .5em;
 }

 
 .nocursor, .nocursor td, .cursor_hidden, .cursor_hidden td {
 background-color: white;
 height: 2px;
 }
 .cursor, .cursor td {
 background-color: darkblue;
 height: 2px;
 display: '';
 }
 
 
.list {
 border: 1px solid white;
 border-bottom: 0;
}

 
 </style>
</head>
<body class="t4">
<script type="text/javascript">
 window.___gcfg = {lang: 'en'};
 (function() 
 {var po = document.createElement("script");
 po.type = "text/javascript"; po.async = true;po.src = "https://apis.google.com/js/plusone.js";
 var s = document.getElementsByTagName("script")[0];
 s.parentNode.insertBefore(po, s);
 })();
</script>
<div class="headbg">

 <div id="gaia">
 

 <span>
 
 
 
 <a href="#" id="multilogin-dropdown" onclick="return false;"
 ><u><b>msbentley@gmail.com</b></u> <small>&#9660;</small></a>
 
 
 | <a href="/u/108811474385654924234/" id="projects-dropdown" onclick="return false;"
 ><u>My favorites</u> <small>&#9660;</small></a>
 | <a href="/u/108811474385654924234/" onclick="_CS_click('/gb/ph/profile');"
 title="Profile, Updates, and Settings"
 ><u>Profile</u></a>
 | <a href="https://www.google.com/accounts/Logout?continue=https%3A%2F%2Fcode.google.com%2Fp%2Fliggghts-force-chains%2Fsource%2Fbrowse%2Ftrunk%2Fdump2force.py" 
 onclick="_CS_click('/gb/ph/signout');"
 ><u>Sign out</u></a>
 
 </span>

 </div>

 <div class="gbh" style="left: 0pt;"></div>
 <div class="gbh" style="right: 0pt;"></div>
 
 
 <div style="height: 1px"></div>
<!--[if lte IE 7]>
<div style="text-align:center;">
Your version of Internet Explorer is not supported. Try a browser that
contributes to open source, such as <a href="http://www.firefox.com">Firefox</a>,
<a href="http://www.google.com/chrome">Google Chrome</a>, or
<a href="http://code.google.com/chrome/chromeframe/">Google Chrome Frame</a>.
</div>
<![endif]-->



 <table style="padding:0px; margin: 0px 0px 10px 0px; width:100%" cellpadding="0" cellspacing="0"
 itemscope itemtype="http://schema.org/CreativeWork">
 <tr style="height: 58px;">
 
 
 
 <td id="plogo">
 <link itemprop="url" href="/p/liggghts-force-chains">
 <a href="/p/liggghts-force-chains/">
 
 <img src="https://ssl.gstatic.com/codesite/ph/images/defaultlogo.png" alt="Logo" itemprop="image">
 
 </a>
 </td>
 
 <td style="padding-left: 0.5em">
 
 <div id="pname">
 <a href="/p/liggghts-force-chains/"><span itemprop="name">liggghts-force-chains</span></a>
 </div>
 
 <div id="psum">
 <a id="project_summary_link"
 href="/p/liggghts-force-chains/"><span itemprop="description">A python tool to generate VTK force chain data from LIGGGHTS simulations</span></a>
 
 </div>
 
 
 </td>
 <td style="white-space:nowrap;text-align:right; vertical-align:bottom;">
 
 <form action="/hosting/search">
 <input size="30" name="q" value="" type="text">
 
 <input type="submit" name="projectsearch" value="Search projects" >
 </form>
 
 </tr>
 </table>

</div>

 
<div id="mt" class="gtb"> 
 <a href="/p/liggghts-force-chains/" class="tab ">Project&nbsp;Home</a>
 
 
 
 
 
 
 <a href="/p/liggghts-force-chains/w/list" class="tab ">Wiki</a>
 
 
 
 
 
 <a href="/p/liggghts-force-chains/issues/list"
 class="tab ">Issues</a>
 
 
 
 
 
 <a href="/p/liggghts-force-chains/source/checkout"
 class="tab active">Source</a>
 
 
 
 
 
 <a href="/p/liggghts-force-chains/admin"
 class="tab inactive">Administer</a>
 
 
 
 
 <div class=gtbc></div>
</div>
<table cellspacing="0" cellpadding="0" width="100%" align="center" border="0" class="st">
 <tr>
 
 
 
 
 
 
 <td class="subt">
 <div class="st2">
 <div class="isf">
 
 


 <span class="inst1"><a href="/p/liggghts-force-chains/source/checkout">Checkout</a></span> &nbsp;
 <span class="inst2"><a href="/p/liggghts-force-chains/source/browse/">Browse</a></span> &nbsp;
 <span class="inst3"><a href="/p/liggghts-force-chains/source/list">Changes</a></span> &nbsp;
 
 
 
 
 
 <a href="/p/liggghts-force-chains/issues/entry?show=review&former=sourcelist">Request code review</a>
 
 
 
 </form>
 <script type="text/javascript">
 
 function codesearchQuery(form) {
 var query = document.getElementById('q').value;
 if (query) { form.action += '%20' + query; }
 }
 </script>
 </div>
</div>

 </td>
 
 
 
 <td align="right" valign="top" class="bevel-right"></td>
 </tr>
</table>


<script type="text/javascript">
 var cancelBubble = false;
 function _go(url) { document.location = url; }
</script>
<div id="maincol"
 
>

 




<div class="expand">
<div id="colcontrol">
<style type="text/css">
 #file_flipper { white-space: nowrap; padding-right: 2em; }
 #file_flipper.hidden { display: none; }
 #file_flipper .pagelink { color: #0000CC; text-decoration: underline; }
 #file_flipper #visiblefiles { padding-left: 0.5em; padding-right: 0.5em; }
</style>
<table id="nav_and_rev" class="list"
 cellpadding="0" cellspacing="0" width="100%">
 <tr>
 
 <td nowrap="nowrap" class="src_crumbs src_nav" width="33%">
 <strong class="src_nav">Source path:&nbsp;</strong>
 <span id="crumb_root">
 
 <a href="/p/liggghts-force-chains/source/browse/">svn</a>/&nbsp;</span>
 <span id="crumb_links" class="ifClosed"><a href="/p/liggghts-force-chains/source/browse/trunk/">trunk</a><span class="sp">/&nbsp;</span>dump2force.py</span>
 
 


 </td>
 
 
 <td nowrap="nowrap" width="33%" align="center">
 <a href="/p/liggghts-force-chains/source/browse/trunk/dump2force.py?edit=1"
 ><img src="https://ssl.gstatic.com/codesite/ph/images/pencil-y14.png"
 class="edit_icon">Edit file</a>
 </td>
 
 
 <td nowrap="nowrap" width="33%" align="right">
 <table cellpadding="0" cellspacing="0" style="font-size: 100%"><tr>
 
 
 <td class="flipper">
 <ul class="leftside">
 
 <li><a href="/p/liggghts-force-chains/source/browse/trunk/dump2force.py?r=4" title="Previous">&lsaquo;r4</a></li>
 
 </ul>
 </td>
 
 <td class="flipper"><b>r5</b></td>
 
 </tr></table>
 </td> 
 </tr>
</table>

<div class="fc">
 
 
 
<style type="text/css">
.undermouse span {
 background-image: url(https://ssl.gstatic.com/codesite/ph/images/comments.gif); }
</style>
<table class="opened" id="review_comment_area"
onmouseout="gutterOut()"><tr>
<td id="nums">
<pre><table width="100%"><tr class="nocursor"><td></td></tr></table></pre>
<pre><table width="100%" id="nums_table_0"><tr id="gr_svn5_1"

 onmouseover="gutterOver(1)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',1);">&nbsp;</span
></td><td id="1"><a href="#1">1</a></td></tr
><tr id="gr_svn5_2"

 onmouseover="gutterOver(2)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',2);">&nbsp;</span
></td><td id="2"><a href="#2">2</a></td></tr
><tr id="gr_svn5_3"

 onmouseover="gutterOver(3)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',3);">&nbsp;</span
></td><td id="3"><a href="#3">3</a></td></tr
><tr id="gr_svn5_4"

 onmouseover="gutterOver(4)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',4);">&nbsp;</span
></td><td id="4"><a href="#4">4</a></td></tr
><tr id="gr_svn5_5"

 onmouseover="gutterOver(5)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',5);">&nbsp;</span
></td><td id="5"><a href="#5">5</a></td></tr
><tr id="gr_svn5_6"

 onmouseover="gutterOver(6)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',6);">&nbsp;</span
></td><td id="6"><a href="#6">6</a></td></tr
><tr id="gr_svn5_7"

 onmouseover="gutterOver(7)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',7);">&nbsp;</span
></td><td id="7"><a href="#7">7</a></td></tr
><tr id="gr_svn5_8"

 onmouseover="gutterOver(8)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',8);">&nbsp;</span
></td><td id="8"><a href="#8">8</a></td></tr
><tr id="gr_svn5_9"

 onmouseover="gutterOver(9)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',9);">&nbsp;</span
></td><td id="9"><a href="#9">9</a></td></tr
><tr id="gr_svn5_10"

 onmouseover="gutterOver(10)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',10);">&nbsp;</span
></td><td id="10"><a href="#10">10</a></td></tr
><tr id="gr_svn5_11"

 onmouseover="gutterOver(11)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',11);">&nbsp;</span
></td><td id="11"><a href="#11">11</a></td></tr
><tr id="gr_svn5_12"

 onmouseover="gutterOver(12)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',12);">&nbsp;</span
></td><td id="12"><a href="#12">12</a></td></tr
><tr id="gr_svn5_13"

 onmouseover="gutterOver(13)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',13);">&nbsp;</span
></td><td id="13"><a href="#13">13</a></td></tr
><tr id="gr_svn5_14"

 onmouseover="gutterOver(14)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',14);">&nbsp;</span
></td><td id="14"><a href="#14">14</a></td></tr
><tr id="gr_svn5_15"

 onmouseover="gutterOver(15)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',15);">&nbsp;</span
></td><td id="15"><a href="#15">15</a></td></tr
><tr id="gr_svn5_16"

 onmouseover="gutterOver(16)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',16);">&nbsp;</span
></td><td id="16"><a href="#16">16</a></td></tr
><tr id="gr_svn5_17"

 onmouseover="gutterOver(17)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',17);">&nbsp;</span
></td><td id="17"><a href="#17">17</a></td></tr
><tr id="gr_svn5_18"

 onmouseover="gutterOver(18)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',18);">&nbsp;</span
></td><td id="18"><a href="#18">18</a></td></tr
><tr id="gr_svn5_19"

 onmouseover="gutterOver(19)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',19);">&nbsp;</span
></td><td id="19"><a href="#19">19</a></td></tr
><tr id="gr_svn5_20"

 onmouseover="gutterOver(20)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',20);">&nbsp;</span
></td><td id="20"><a href="#20">20</a></td></tr
><tr id="gr_svn5_21"

 onmouseover="gutterOver(21)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',21);">&nbsp;</span
></td><td id="21"><a href="#21">21</a></td></tr
><tr id="gr_svn5_22"

 onmouseover="gutterOver(22)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',22);">&nbsp;</span
></td><td id="22"><a href="#22">22</a></td></tr
><tr id="gr_svn5_23"

 onmouseover="gutterOver(23)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',23);">&nbsp;</span
></td><td id="23"><a href="#23">23</a></td></tr
><tr id="gr_svn5_24"

 onmouseover="gutterOver(24)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',24);">&nbsp;</span
></td><td id="24"><a href="#24">24</a></td></tr
><tr id="gr_svn5_25"

 onmouseover="gutterOver(25)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',25);">&nbsp;</span
></td><td id="25"><a href="#25">25</a></td></tr
><tr id="gr_svn5_26"

 onmouseover="gutterOver(26)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',26);">&nbsp;</span
></td><td id="26"><a href="#26">26</a></td></tr
><tr id="gr_svn5_27"

 onmouseover="gutterOver(27)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',27);">&nbsp;</span
></td><td id="27"><a href="#27">27</a></td></tr
><tr id="gr_svn5_28"

 onmouseover="gutterOver(28)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',28);">&nbsp;</span
></td><td id="28"><a href="#28">28</a></td></tr
><tr id="gr_svn5_29"

 onmouseover="gutterOver(29)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',29);">&nbsp;</span
></td><td id="29"><a href="#29">29</a></td></tr
><tr id="gr_svn5_30"

 onmouseover="gutterOver(30)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',30);">&nbsp;</span
></td><td id="30"><a href="#30">30</a></td></tr
><tr id="gr_svn5_31"

 onmouseover="gutterOver(31)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',31);">&nbsp;</span
></td><td id="31"><a href="#31">31</a></td></tr
><tr id="gr_svn5_32"

 onmouseover="gutterOver(32)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',32);">&nbsp;</span
></td><td id="32"><a href="#32">32</a></td></tr
><tr id="gr_svn5_33"

 onmouseover="gutterOver(33)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',33);">&nbsp;</span
></td><td id="33"><a href="#33">33</a></td></tr
><tr id="gr_svn5_34"

 onmouseover="gutterOver(34)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',34);">&nbsp;</span
></td><td id="34"><a href="#34">34</a></td></tr
><tr id="gr_svn5_35"

 onmouseover="gutterOver(35)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',35);">&nbsp;</span
></td><td id="35"><a href="#35">35</a></td></tr
><tr id="gr_svn5_36"

 onmouseover="gutterOver(36)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',36);">&nbsp;</span
></td><td id="36"><a href="#36">36</a></td></tr
><tr id="gr_svn5_37"

 onmouseover="gutterOver(37)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',37);">&nbsp;</span
></td><td id="37"><a href="#37">37</a></td></tr
><tr id="gr_svn5_38"

 onmouseover="gutterOver(38)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',38);">&nbsp;</span
></td><td id="38"><a href="#38">38</a></td></tr
><tr id="gr_svn5_39"

 onmouseover="gutterOver(39)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',39);">&nbsp;</span
></td><td id="39"><a href="#39">39</a></td></tr
><tr id="gr_svn5_40"

 onmouseover="gutterOver(40)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',40);">&nbsp;</span
></td><td id="40"><a href="#40">40</a></td></tr
><tr id="gr_svn5_41"

 onmouseover="gutterOver(41)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',41);">&nbsp;</span
></td><td id="41"><a href="#41">41</a></td></tr
><tr id="gr_svn5_42"

 onmouseover="gutterOver(42)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',42);">&nbsp;</span
></td><td id="42"><a href="#42">42</a></td></tr
><tr id="gr_svn5_43"

 onmouseover="gutterOver(43)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',43);">&nbsp;</span
></td><td id="43"><a href="#43">43</a></td></tr
><tr id="gr_svn5_44"

 onmouseover="gutterOver(44)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',44);">&nbsp;</span
></td><td id="44"><a href="#44">44</a></td></tr
><tr id="gr_svn5_45"

 onmouseover="gutterOver(45)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',45);">&nbsp;</span
></td><td id="45"><a href="#45">45</a></td></tr
><tr id="gr_svn5_46"

 onmouseover="gutterOver(46)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',46);">&nbsp;</span
></td><td id="46"><a href="#46">46</a></td></tr
><tr id="gr_svn5_47"

 onmouseover="gutterOver(47)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',47);">&nbsp;</span
></td><td id="47"><a href="#47">47</a></td></tr
><tr id="gr_svn5_48"

 onmouseover="gutterOver(48)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',48);">&nbsp;</span
></td><td id="48"><a href="#48">48</a></td></tr
><tr id="gr_svn5_49"

 onmouseover="gutterOver(49)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',49);">&nbsp;</span
></td><td id="49"><a href="#49">49</a></td></tr
><tr id="gr_svn5_50"

 onmouseover="gutterOver(50)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',50);">&nbsp;</span
></td><td id="50"><a href="#50">50</a></td></tr
><tr id="gr_svn5_51"

 onmouseover="gutterOver(51)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',51);">&nbsp;</span
></td><td id="51"><a href="#51">51</a></td></tr
><tr id="gr_svn5_52"

 onmouseover="gutterOver(52)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',52);">&nbsp;</span
></td><td id="52"><a href="#52">52</a></td></tr
><tr id="gr_svn5_53"

 onmouseover="gutterOver(53)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',53);">&nbsp;</span
></td><td id="53"><a href="#53">53</a></td></tr
><tr id="gr_svn5_54"

 onmouseover="gutterOver(54)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',54);">&nbsp;</span
></td><td id="54"><a href="#54">54</a></td></tr
><tr id="gr_svn5_55"

 onmouseover="gutterOver(55)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',55);">&nbsp;</span
></td><td id="55"><a href="#55">55</a></td></tr
><tr id="gr_svn5_56"

 onmouseover="gutterOver(56)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',56);">&nbsp;</span
></td><td id="56"><a href="#56">56</a></td></tr
><tr id="gr_svn5_57"

 onmouseover="gutterOver(57)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',57);">&nbsp;</span
></td><td id="57"><a href="#57">57</a></td></tr
><tr id="gr_svn5_58"

 onmouseover="gutterOver(58)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',58);">&nbsp;</span
></td><td id="58"><a href="#58">58</a></td></tr
><tr id="gr_svn5_59"

 onmouseover="gutterOver(59)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',59);">&nbsp;</span
></td><td id="59"><a href="#59">59</a></td></tr
><tr id="gr_svn5_60"

 onmouseover="gutterOver(60)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',60);">&nbsp;</span
></td><td id="60"><a href="#60">60</a></td></tr
><tr id="gr_svn5_61"

 onmouseover="gutterOver(61)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',61);">&nbsp;</span
></td><td id="61"><a href="#61">61</a></td></tr
><tr id="gr_svn5_62"

 onmouseover="gutterOver(62)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',62);">&nbsp;</span
></td><td id="62"><a href="#62">62</a></td></tr
><tr id="gr_svn5_63"

 onmouseover="gutterOver(63)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',63);">&nbsp;</span
></td><td id="63"><a href="#63">63</a></td></tr
><tr id="gr_svn5_64"

 onmouseover="gutterOver(64)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',64);">&nbsp;</span
></td><td id="64"><a href="#64">64</a></td></tr
><tr id="gr_svn5_65"

 onmouseover="gutterOver(65)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',65);">&nbsp;</span
></td><td id="65"><a href="#65">65</a></td></tr
><tr id="gr_svn5_66"

 onmouseover="gutterOver(66)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',66);">&nbsp;</span
></td><td id="66"><a href="#66">66</a></td></tr
><tr id="gr_svn5_67"

 onmouseover="gutterOver(67)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',67);">&nbsp;</span
></td><td id="67"><a href="#67">67</a></td></tr
><tr id="gr_svn5_68"

 onmouseover="gutterOver(68)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',68);">&nbsp;</span
></td><td id="68"><a href="#68">68</a></td></tr
><tr id="gr_svn5_69"

 onmouseover="gutterOver(69)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',69);">&nbsp;</span
></td><td id="69"><a href="#69">69</a></td></tr
><tr id="gr_svn5_70"

 onmouseover="gutterOver(70)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',70);">&nbsp;</span
></td><td id="70"><a href="#70">70</a></td></tr
><tr id="gr_svn5_71"

 onmouseover="gutterOver(71)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',71);">&nbsp;</span
></td><td id="71"><a href="#71">71</a></td></tr
><tr id="gr_svn5_72"

 onmouseover="gutterOver(72)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',72);">&nbsp;</span
></td><td id="72"><a href="#72">72</a></td></tr
><tr id="gr_svn5_73"

 onmouseover="gutterOver(73)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',73);">&nbsp;</span
></td><td id="73"><a href="#73">73</a></td></tr
><tr id="gr_svn5_74"

 onmouseover="gutterOver(74)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',74);">&nbsp;</span
></td><td id="74"><a href="#74">74</a></td></tr
><tr id="gr_svn5_75"

 onmouseover="gutterOver(75)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',75);">&nbsp;</span
></td><td id="75"><a href="#75">75</a></td></tr
><tr id="gr_svn5_76"

 onmouseover="gutterOver(76)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',76);">&nbsp;</span
></td><td id="76"><a href="#76">76</a></td></tr
><tr id="gr_svn5_77"

 onmouseover="gutterOver(77)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',77);">&nbsp;</span
></td><td id="77"><a href="#77">77</a></td></tr
><tr id="gr_svn5_78"

 onmouseover="gutterOver(78)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',78);">&nbsp;</span
></td><td id="78"><a href="#78">78</a></td></tr
><tr id="gr_svn5_79"

 onmouseover="gutterOver(79)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',79);">&nbsp;</span
></td><td id="79"><a href="#79">79</a></td></tr
><tr id="gr_svn5_80"

 onmouseover="gutterOver(80)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',80);">&nbsp;</span
></td><td id="80"><a href="#80">80</a></td></tr
><tr id="gr_svn5_81"

 onmouseover="gutterOver(81)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',81);">&nbsp;</span
></td><td id="81"><a href="#81">81</a></td></tr
><tr id="gr_svn5_82"

 onmouseover="gutterOver(82)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',82);">&nbsp;</span
></td><td id="82"><a href="#82">82</a></td></tr
><tr id="gr_svn5_83"

 onmouseover="gutterOver(83)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',83);">&nbsp;</span
></td><td id="83"><a href="#83">83</a></td></tr
><tr id="gr_svn5_84"

 onmouseover="gutterOver(84)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',84);">&nbsp;</span
></td><td id="84"><a href="#84">84</a></td></tr
><tr id="gr_svn5_85"

 onmouseover="gutterOver(85)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',85);">&nbsp;</span
></td><td id="85"><a href="#85">85</a></td></tr
><tr id="gr_svn5_86"

 onmouseover="gutterOver(86)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',86);">&nbsp;</span
></td><td id="86"><a href="#86">86</a></td></tr
><tr id="gr_svn5_87"

 onmouseover="gutterOver(87)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',87);">&nbsp;</span
></td><td id="87"><a href="#87">87</a></td></tr
><tr id="gr_svn5_88"

 onmouseover="gutterOver(88)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',88);">&nbsp;</span
></td><td id="88"><a href="#88">88</a></td></tr
><tr id="gr_svn5_89"

 onmouseover="gutterOver(89)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',89);">&nbsp;</span
></td><td id="89"><a href="#89">89</a></td></tr
><tr id="gr_svn5_90"

 onmouseover="gutterOver(90)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',90);">&nbsp;</span
></td><td id="90"><a href="#90">90</a></td></tr
><tr id="gr_svn5_91"

 onmouseover="gutterOver(91)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',91);">&nbsp;</span
></td><td id="91"><a href="#91">91</a></td></tr
><tr id="gr_svn5_92"

 onmouseover="gutterOver(92)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',92);">&nbsp;</span
></td><td id="92"><a href="#92">92</a></td></tr
><tr id="gr_svn5_93"

 onmouseover="gutterOver(93)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',93);">&nbsp;</span
></td><td id="93"><a href="#93">93</a></td></tr
><tr id="gr_svn5_94"

 onmouseover="gutterOver(94)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',94);">&nbsp;</span
></td><td id="94"><a href="#94">94</a></td></tr
><tr id="gr_svn5_95"

 onmouseover="gutterOver(95)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',95);">&nbsp;</span
></td><td id="95"><a href="#95">95</a></td></tr
><tr id="gr_svn5_96"

 onmouseover="gutterOver(96)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',96);">&nbsp;</span
></td><td id="96"><a href="#96">96</a></td></tr
><tr id="gr_svn5_97"

 onmouseover="gutterOver(97)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',97);">&nbsp;</span
></td><td id="97"><a href="#97">97</a></td></tr
><tr id="gr_svn5_98"

 onmouseover="gutterOver(98)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',98);">&nbsp;</span
></td><td id="98"><a href="#98">98</a></td></tr
><tr id="gr_svn5_99"

 onmouseover="gutterOver(99)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',99);">&nbsp;</span
></td><td id="99"><a href="#99">99</a></td></tr
><tr id="gr_svn5_100"

 onmouseover="gutterOver(100)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',100);">&nbsp;</span
></td><td id="100"><a href="#100">100</a></td></tr
><tr id="gr_svn5_101"

 onmouseover="gutterOver(101)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',101);">&nbsp;</span
></td><td id="101"><a href="#101">101</a></td></tr
><tr id="gr_svn5_102"

 onmouseover="gutterOver(102)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',102);">&nbsp;</span
></td><td id="102"><a href="#102">102</a></td></tr
><tr id="gr_svn5_103"

 onmouseover="gutterOver(103)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',103);">&nbsp;</span
></td><td id="103"><a href="#103">103</a></td></tr
><tr id="gr_svn5_104"

 onmouseover="gutterOver(104)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',104);">&nbsp;</span
></td><td id="104"><a href="#104">104</a></td></tr
><tr id="gr_svn5_105"

 onmouseover="gutterOver(105)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',105);">&nbsp;</span
></td><td id="105"><a href="#105">105</a></td></tr
><tr id="gr_svn5_106"

 onmouseover="gutterOver(106)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',106);">&nbsp;</span
></td><td id="106"><a href="#106">106</a></td></tr
><tr id="gr_svn5_107"

 onmouseover="gutterOver(107)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',107);">&nbsp;</span
></td><td id="107"><a href="#107">107</a></td></tr
><tr id="gr_svn5_108"

 onmouseover="gutterOver(108)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',108);">&nbsp;</span
></td><td id="108"><a href="#108">108</a></td></tr
><tr id="gr_svn5_109"

 onmouseover="gutterOver(109)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',109);">&nbsp;</span
></td><td id="109"><a href="#109">109</a></td></tr
><tr id="gr_svn5_110"

 onmouseover="gutterOver(110)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',110);">&nbsp;</span
></td><td id="110"><a href="#110">110</a></td></tr
><tr id="gr_svn5_111"

 onmouseover="gutterOver(111)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',111);">&nbsp;</span
></td><td id="111"><a href="#111">111</a></td></tr
><tr id="gr_svn5_112"

 onmouseover="gutterOver(112)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',112);">&nbsp;</span
></td><td id="112"><a href="#112">112</a></td></tr
><tr id="gr_svn5_113"

 onmouseover="gutterOver(113)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',113);">&nbsp;</span
></td><td id="113"><a href="#113">113</a></td></tr
><tr id="gr_svn5_114"

 onmouseover="gutterOver(114)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',114);">&nbsp;</span
></td><td id="114"><a href="#114">114</a></td></tr
><tr id="gr_svn5_115"

 onmouseover="gutterOver(115)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',115);">&nbsp;</span
></td><td id="115"><a href="#115">115</a></td></tr
><tr id="gr_svn5_116"

 onmouseover="gutterOver(116)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',116);">&nbsp;</span
></td><td id="116"><a href="#116">116</a></td></tr
><tr id="gr_svn5_117"

 onmouseover="gutterOver(117)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',117);">&nbsp;</span
></td><td id="117"><a href="#117">117</a></td></tr
><tr id="gr_svn5_118"

 onmouseover="gutterOver(118)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',118);">&nbsp;</span
></td><td id="118"><a href="#118">118</a></td></tr
><tr id="gr_svn5_119"

 onmouseover="gutterOver(119)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',119);">&nbsp;</span
></td><td id="119"><a href="#119">119</a></td></tr
><tr id="gr_svn5_120"

 onmouseover="gutterOver(120)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',120);">&nbsp;</span
></td><td id="120"><a href="#120">120</a></td></tr
><tr id="gr_svn5_121"

 onmouseover="gutterOver(121)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',121);">&nbsp;</span
></td><td id="121"><a href="#121">121</a></td></tr
><tr id="gr_svn5_122"

 onmouseover="gutterOver(122)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',122);">&nbsp;</span
></td><td id="122"><a href="#122">122</a></td></tr
><tr id="gr_svn5_123"

 onmouseover="gutterOver(123)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',123);">&nbsp;</span
></td><td id="123"><a href="#123">123</a></td></tr
><tr id="gr_svn5_124"

 onmouseover="gutterOver(124)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',124);">&nbsp;</span
></td><td id="124"><a href="#124">124</a></td></tr
><tr id="gr_svn5_125"

 onmouseover="gutterOver(125)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',125);">&nbsp;</span
></td><td id="125"><a href="#125">125</a></td></tr
><tr id="gr_svn5_126"

 onmouseover="gutterOver(126)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',126);">&nbsp;</span
></td><td id="126"><a href="#126">126</a></td></tr
><tr id="gr_svn5_127"

 onmouseover="gutterOver(127)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',127);">&nbsp;</span
></td><td id="127"><a href="#127">127</a></td></tr
><tr id="gr_svn5_128"

 onmouseover="gutterOver(128)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',128);">&nbsp;</span
></td><td id="128"><a href="#128">128</a></td></tr
><tr id="gr_svn5_129"

 onmouseover="gutterOver(129)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',129);">&nbsp;</span
></td><td id="129"><a href="#129">129</a></td></tr
><tr id="gr_svn5_130"

 onmouseover="gutterOver(130)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',130);">&nbsp;</span
></td><td id="130"><a href="#130">130</a></td></tr
><tr id="gr_svn5_131"

 onmouseover="gutterOver(131)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',131);">&nbsp;</span
></td><td id="131"><a href="#131">131</a></td></tr
><tr id="gr_svn5_132"

 onmouseover="gutterOver(132)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',132);">&nbsp;</span
></td><td id="132"><a href="#132">132</a></td></tr
><tr id="gr_svn5_133"

 onmouseover="gutterOver(133)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',133);">&nbsp;</span
></td><td id="133"><a href="#133">133</a></td></tr
><tr id="gr_svn5_134"

 onmouseover="gutterOver(134)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',134);">&nbsp;</span
></td><td id="134"><a href="#134">134</a></td></tr
><tr id="gr_svn5_135"

 onmouseover="gutterOver(135)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',135);">&nbsp;</span
></td><td id="135"><a href="#135">135</a></td></tr
><tr id="gr_svn5_136"

 onmouseover="gutterOver(136)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',136);">&nbsp;</span
></td><td id="136"><a href="#136">136</a></td></tr
><tr id="gr_svn5_137"

 onmouseover="gutterOver(137)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',137);">&nbsp;</span
></td><td id="137"><a href="#137">137</a></td></tr
><tr id="gr_svn5_138"

 onmouseover="gutterOver(138)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',138);">&nbsp;</span
></td><td id="138"><a href="#138">138</a></td></tr
><tr id="gr_svn5_139"

 onmouseover="gutterOver(139)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',139);">&nbsp;</span
></td><td id="139"><a href="#139">139</a></td></tr
><tr id="gr_svn5_140"

 onmouseover="gutterOver(140)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',140);">&nbsp;</span
></td><td id="140"><a href="#140">140</a></td></tr
><tr id="gr_svn5_141"

 onmouseover="gutterOver(141)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',141);">&nbsp;</span
></td><td id="141"><a href="#141">141</a></td></tr
><tr id="gr_svn5_142"

 onmouseover="gutterOver(142)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',142);">&nbsp;</span
></td><td id="142"><a href="#142">142</a></td></tr
><tr id="gr_svn5_143"

 onmouseover="gutterOver(143)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',143);">&nbsp;</span
></td><td id="143"><a href="#143">143</a></td></tr
><tr id="gr_svn5_144"

 onmouseover="gutterOver(144)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',144);">&nbsp;</span
></td><td id="144"><a href="#144">144</a></td></tr
><tr id="gr_svn5_145"

 onmouseover="gutterOver(145)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',145);">&nbsp;</span
></td><td id="145"><a href="#145">145</a></td></tr
><tr id="gr_svn5_146"

 onmouseover="gutterOver(146)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',146);">&nbsp;</span
></td><td id="146"><a href="#146">146</a></td></tr
><tr id="gr_svn5_147"

 onmouseover="gutterOver(147)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',147);">&nbsp;</span
></td><td id="147"><a href="#147">147</a></td></tr
><tr id="gr_svn5_148"

 onmouseover="gutterOver(148)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',148);">&nbsp;</span
></td><td id="148"><a href="#148">148</a></td></tr
><tr id="gr_svn5_149"

 onmouseover="gutterOver(149)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',149);">&nbsp;</span
></td><td id="149"><a href="#149">149</a></td></tr
><tr id="gr_svn5_150"

 onmouseover="gutterOver(150)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',150);">&nbsp;</span
></td><td id="150"><a href="#150">150</a></td></tr
><tr id="gr_svn5_151"

 onmouseover="gutterOver(151)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',151);">&nbsp;</span
></td><td id="151"><a href="#151">151</a></td></tr
><tr id="gr_svn5_152"

 onmouseover="gutterOver(152)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',152);">&nbsp;</span
></td><td id="152"><a href="#152">152</a></td></tr
><tr id="gr_svn5_153"

 onmouseover="gutterOver(153)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',153);">&nbsp;</span
></td><td id="153"><a href="#153">153</a></td></tr
><tr id="gr_svn5_154"

 onmouseover="gutterOver(154)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',154);">&nbsp;</span
></td><td id="154"><a href="#154">154</a></td></tr
><tr id="gr_svn5_155"

 onmouseover="gutterOver(155)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',155);">&nbsp;</span
></td><td id="155"><a href="#155">155</a></td></tr
><tr id="gr_svn5_156"

 onmouseover="gutterOver(156)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',156);">&nbsp;</span
></td><td id="156"><a href="#156">156</a></td></tr
><tr id="gr_svn5_157"

 onmouseover="gutterOver(157)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',157);">&nbsp;</span
></td><td id="157"><a href="#157">157</a></td></tr
><tr id="gr_svn5_158"

 onmouseover="gutterOver(158)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',158);">&nbsp;</span
></td><td id="158"><a href="#158">158</a></td></tr
><tr id="gr_svn5_159"

 onmouseover="gutterOver(159)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',159);">&nbsp;</span
></td><td id="159"><a href="#159">159</a></td></tr
><tr id="gr_svn5_160"

 onmouseover="gutterOver(160)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',160);">&nbsp;</span
></td><td id="160"><a href="#160">160</a></td></tr
><tr id="gr_svn5_161"

 onmouseover="gutterOver(161)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',161);">&nbsp;</span
></td><td id="161"><a href="#161">161</a></td></tr
><tr id="gr_svn5_162"

 onmouseover="gutterOver(162)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',162);">&nbsp;</span
></td><td id="162"><a href="#162">162</a></td></tr
><tr id="gr_svn5_163"

 onmouseover="gutterOver(163)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',163);">&nbsp;</span
></td><td id="163"><a href="#163">163</a></td></tr
><tr id="gr_svn5_164"

 onmouseover="gutterOver(164)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',164);">&nbsp;</span
></td><td id="164"><a href="#164">164</a></td></tr
><tr id="gr_svn5_165"

 onmouseover="gutterOver(165)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',165);">&nbsp;</span
></td><td id="165"><a href="#165">165</a></td></tr
><tr id="gr_svn5_166"

 onmouseover="gutterOver(166)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',166);">&nbsp;</span
></td><td id="166"><a href="#166">166</a></td></tr
><tr id="gr_svn5_167"

 onmouseover="gutterOver(167)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',167);">&nbsp;</span
></td><td id="167"><a href="#167">167</a></td></tr
><tr id="gr_svn5_168"

 onmouseover="gutterOver(168)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',168);">&nbsp;</span
></td><td id="168"><a href="#168">168</a></td></tr
><tr id="gr_svn5_169"

 onmouseover="gutterOver(169)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',169);">&nbsp;</span
></td><td id="169"><a href="#169">169</a></td></tr
><tr id="gr_svn5_170"

 onmouseover="gutterOver(170)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',170);">&nbsp;</span
></td><td id="170"><a href="#170">170</a></td></tr
><tr id="gr_svn5_171"

 onmouseover="gutterOver(171)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',171);">&nbsp;</span
></td><td id="171"><a href="#171">171</a></td></tr
><tr id="gr_svn5_172"

 onmouseover="gutterOver(172)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',172);">&nbsp;</span
></td><td id="172"><a href="#172">172</a></td></tr
><tr id="gr_svn5_173"

 onmouseover="gutterOver(173)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',173);">&nbsp;</span
></td><td id="173"><a href="#173">173</a></td></tr
><tr id="gr_svn5_174"

 onmouseover="gutterOver(174)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',174);">&nbsp;</span
></td><td id="174"><a href="#174">174</a></td></tr
><tr id="gr_svn5_175"

 onmouseover="gutterOver(175)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',175);">&nbsp;</span
></td><td id="175"><a href="#175">175</a></td></tr
><tr id="gr_svn5_176"

 onmouseover="gutterOver(176)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',176);">&nbsp;</span
></td><td id="176"><a href="#176">176</a></td></tr
><tr id="gr_svn5_177"

 onmouseover="gutterOver(177)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',177);">&nbsp;</span
></td><td id="177"><a href="#177">177</a></td></tr
><tr id="gr_svn5_178"

 onmouseover="gutterOver(178)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',178);">&nbsp;</span
></td><td id="178"><a href="#178">178</a></td></tr
><tr id="gr_svn5_179"

 onmouseover="gutterOver(179)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',179);">&nbsp;</span
></td><td id="179"><a href="#179">179</a></td></tr
><tr id="gr_svn5_180"

 onmouseover="gutterOver(180)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',180);">&nbsp;</span
></td><td id="180"><a href="#180">180</a></td></tr
><tr id="gr_svn5_181"

 onmouseover="gutterOver(181)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',181);">&nbsp;</span
></td><td id="181"><a href="#181">181</a></td></tr
><tr id="gr_svn5_182"

 onmouseover="gutterOver(182)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',182);">&nbsp;</span
></td><td id="182"><a href="#182">182</a></td></tr
><tr id="gr_svn5_183"

 onmouseover="gutterOver(183)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',183);">&nbsp;</span
></td><td id="183"><a href="#183">183</a></td></tr
><tr id="gr_svn5_184"

 onmouseover="gutterOver(184)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',184);">&nbsp;</span
></td><td id="184"><a href="#184">184</a></td></tr
><tr id="gr_svn5_185"

 onmouseover="gutterOver(185)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',185);">&nbsp;</span
></td><td id="185"><a href="#185">185</a></td></tr
><tr id="gr_svn5_186"

 onmouseover="gutterOver(186)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',186);">&nbsp;</span
></td><td id="186"><a href="#186">186</a></td></tr
><tr id="gr_svn5_187"

 onmouseover="gutterOver(187)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',187);">&nbsp;</span
></td><td id="187"><a href="#187">187</a></td></tr
><tr id="gr_svn5_188"

 onmouseover="gutterOver(188)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',188);">&nbsp;</span
></td><td id="188"><a href="#188">188</a></td></tr
><tr id="gr_svn5_189"

 onmouseover="gutterOver(189)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',189);">&nbsp;</span
></td><td id="189"><a href="#189">189</a></td></tr
><tr id="gr_svn5_190"

 onmouseover="gutterOver(190)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',190);">&nbsp;</span
></td><td id="190"><a href="#190">190</a></td></tr
><tr id="gr_svn5_191"

 onmouseover="gutterOver(191)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',191);">&nbsp;</span
></td><td id="191"><a href="#191">191</a></td></tr
><tr id="gr_svn5_192"

 onmouseover="gutterOver(192)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',192);">&nbsp;</span
></td><td id="192"><a href="#192">192</a></td></tr
><tr id="gr_svn5_193"

 onmouseover="gutterOver(193)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',193);">&nbsp;</span
></td><td id="193"><a href="#193">193</a></td></tr
><tr id="gr_svn5_194"

 onmouseover="gutterOver(194)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',194);">&nbsp;</span
></td><td id="194"><a href="#194">194</a></td></tr
><tr id="gr_svn5_195"

 onmouseover="gutterOver(195)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',195);">&nbsp;</span
></td><td id="195"><a href="#195">195</a></td></tr
><tr id="gr_svn5_196"

 onmouseover="gutterOver(196)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',196);">&nbsp;</span
></td><td id="196"><a href="#196">196</a></td></tr
><tr id="gr_svn5_197"

 onmouseover="gutterOver(197)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',197);">&nbsp;</span
></td><td id="197"><a href="#197">197</a></td></tr
><tr id="gr_svn5_198"

 onmouseover="gutterOver(198)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',198);">&nbsp;</span
></td><td id="198"><a href="#198">198</a></td></tr
><tr id="gr_svn5_199"

 onmouseover="gutterOver(199)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',199);">&nbsp;</span
></td><td id="199"><a href="#199">199</a></td></tr
><tr id="gr_svn5_200"

 onmouseover="gutterOver(200)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',200);">&nbsp;</span
></td><td id="200"><a href="#200">200</a></td></tr
><tr id="gr_svn5_201"

 onmouseover="gutterOver(201)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',201);">&nbsp;</span
></td><td id="201"><a href="#201">201</a></td></tr
><tr id="gr_svn5_202"

 onmouseover="gutterOver(202)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',202);">&nbsp;</span
></td><td id="202"><a href="#202">202</a></td></tr
><tr id="gr_svn5_203"

 onmouseover="gutterOver(203)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',203);">&nbsp;</span
></td><td id="203"><a href="#203">203</a></td></tr
><tr id="gr_svn5_204"

 onmouseover="gutterOver(204)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',204);">&nbsp;</span
></td><td id="204"><a href="#204">204</a></td></tr
><tr id="gr_svn5_205"

 onmouseover="gutterOver(205)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',205);">&nbsp;</span
></td><td id="205"><a href="#205">205</a></td></tr
><tr id="gr_svn5_206"

 onmouseover="gutterOver(206)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',206);">&nbsp;</span
></td><td id="206"><a href="#206">206</a></td></tr
><tr id="gr_svn5_207"

 onmouseover="gutterOver(207)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',207);">&nbsp;</span
></td><td id="207"><a href="#207">207</a></td></tr
><tr id="gr_svn5_208"

 onmouseover="gutterOver(208)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',208);">&nbsp;</span
></td><td id="208"><a href="#208">208</a></td></tr
><tr id="gr_svn5_209"

 onmouseover="gutterOver(209)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',209);">&nbsp;</span
></td><td id="209"><a href="#209">209</a></td></tr
><tr id="gr_svn5_210"

 onmouseover="gutterOver(210)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',210);">&nbsp;</span
></td><td id="210"><a href="#210">210</a></td></tr
><tr id="gr_svn5_211"

 onmouseover="gutterOver(211)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',211);">&nbsp;</span
></td><td id="211"><a href="#211">211</a></td></tr
><tr id="gr_svn5_212"

 onmouseover="gutterOver(212)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',212);">&nbsp;</span
></td><td id="212"><a href="#212">212</a></td></tr
><tr id="gr_svn5_213"

 onmouseover="gutterOver(213)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',213);">&nbsp;</span
></td><td id="213"><a href="#213">213</a></td></tr
><tr id="gr_svn5_214"

 onmouseover="gutterOver(214)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',214);">&nbsp;</span
></td><td id="214"><a href="#214">214</a></td></tr
><tr id="gr_svn5_215"

 onmouseover="gutterOver(215)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',215);">&nbsp;</span
></td><td id="215"><a href="#215">215</a></td></tr
><tr id="gr_svn5_216"

 onmouseover="gutterOver(216)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',216);">&nbsp;</span
></td><td id="216"><a href="#216">216</a></td></tr
><tr id="gr_svn5_217"

 onmouseover="gutterOver(217)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',217);">&nbsp;</span
></td><td id="217"><a href="#217">217</a></td></tr
><tr id="gr_svn5_218"

 onmouseover="gutterOver(218)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',218);">&nbsp;</span
></td><td id="218"><a href="#218">218</a></td></tr
><tr id="gr_svn5_219"

 onmouseover="gutterOver(219)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',219);">&nbsp;</span
></td><td id="219"><a href="#219">219</a></td></tr
><tr id="gr_svn5_220"

 onmouseover="gutterOver(220)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',220);">&nbsp;</span
></td><td id="220"><a href="#220">220</a></td></tr
><tr id="gr_svn5_221"

 onmouseover="gutterOver(221)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',221);">&nbsp;</span
></td><td id="221"><a href="#221">221</a></td></tr
><tr id="gr_svn5_222"

 onmouseover="gutterOver(222)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',222);">&nbsp;</span
></td><td id="222"><a href="#222">222</a></td></tr
><tr id="gr_svn5_223"

 onmouseover="gutterOver(223)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',223);">&nbsp;</span
></td><td id="223"><a href="#223">223</a></td></tr
><tr id="gr_svn5_224"

 onmouseover="gutterOver(224)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',224);">&nbsp;</span
></td><td id="224"><a href="#224">224</a></td></tr
><tr id="gr_svn5_225"

 onmouseover="gutterOver(225)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',225);">&nbsp;</span
></td><td id="225"><a href="#225">225</a></td></tr
><tr id="gr_svn5_226"

 onmouseover="gutterOver(226)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',226);">&nbsp;</span
></td><td id="226"><a href="#226">226</a></td></tr
><tr id="gr_svn5_227"

 onmouseover="gutterOver(227)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',227);">&nbsp;</span
></td><td id="227"><a href="#227">227</a></td></tr
><tr id="gr_svn5_228"

 onmouseover="gutterOver(228)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',228);">&nbsp;</span
></td><td id="228"><a href="#228">228</a></td></tr
><tr id="gr_svn5_229"

 onmouseover="gutterOver(229)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',229);">&nbsp;</span
></td><td id="229"><a href="#229">229</a></td></tr
><tr id="gr_svn5_230"

 onmouseover="gutterOver(230)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',230);">&nbsp;</span
></td><td id="230"><a href="#230">230</a></td></tr
><tr id="gr_svn5_231"

 onmouseover="gutterOver(231)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',231);">&nbsp;</span
></td><td id="231"><a href="#231">231</a></td></tr
><tr id="gr_svn5_232"

 onmouseover="gutterOver(232)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',232);">&nbsp;</span
></td><td id="232"><a href="#232">232</a></td></tr
><tr id="gr_svn5_233"

 onmouseover="gutterOver(233)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',233);">&nbsp;</span
></td><td id="233"><a href="#233">233</a></td></tr
><tr id="gr_svn5_234"

 onmouseover="gutterOver(234)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',234);">&nbsp;</span
></td><td id="234"><a href="#234">234</a></td></tr
><tr id="gr_svn5_235"

 onmouseover="gutterOver(235)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',235);">&nbsp;</span
></td><td id="235"><a href="#235">235</a></td></tr
><tr id="gr_svn5_236"

 onmouseover="gutterOver(236)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',236);">&nbsp;</span
></td><td id="236"><a href="#236">236</a></td></tr
><tr id="gr_svn5_237"

 onmouseover="gutterOver(237)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',237);">&nbsp;</span
></td><td id="237"><a href="#237">237</a></td></tr
><tr id="gr_svn5_238"

 onmouseover="gutterOver(238)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',238);">&nbsp;</span
></td><td id="238"><a href="#238">238</a></td></tr
><tr id="gr_svn5_239"

 onmouseover="gutterOver(239)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',239);">&nbsp;</span
></td><td id="239"><a href="#239">239</a></td></tr
><tr id="gr_svn5_240"

 onmouseover="gutterOver(240)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',240);">&nbsp;</span
></td><td id="240"><a href="#240">240</a></td></tr
><tr id="gr_svn5_241"

 onmouseover="gutterOver(241)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',241);">&nbsp;</span
></td><td id="241"><a href="#241">241</a></td></tr
><tr id="gr_svn5_242"

 onmouseover="gutterOver(242)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',242);">&nbsp;</span
></td><td id="242"><a href="#242">242</a></td></tr
><tr id="gr_svn5_243"

 onmouseover="gutterOver(243)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',243);">&nbsp;</span
></td><td id="243"><a href="#243">243</a></td></tr
><tr id="gr_svn5_244"

 onmouseover="gutterOver(244)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',244);">&nbsp;</span
></td><td id="244"><a href="#244">244</a></td></tr
><tr id="gr_svn5_245"

 onmouseover="gutterOver(245)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',245);">&nbsp;</span
></td><td id="245"><a href="#245">245</a></td></tr
><tr id="gr_svn5_246"

 onmouseover="gutterOver(246)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',246);">&nbsp;</span
></td><td id="246"><a href="#246">246</a></td></tr
><tr id="gr_svn5_247"

 onmouseover="gutterOver(247)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',247);">&nbsp;</span
></td><td id="247"><a href="#247">247</a></td></tr
><tr id="gr_svn5_248"

 onmouseover="gutterOver(248)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',248);">&nbsp;</span
></td><td id="248"><a href="#248">248</a></td></tr
><tr id="gr_svn5_249"

 onmouseover="gutterOver(249)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',249);">&nbsp;</span
></td><td id="249"><a href="#249">249</a></td></tr
><tr id="gr_svn5_250"

 onmouseover="gutterOver(250)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',250);">&nbsp;</span
></td><td id="250"><a href="#250">250</a></td></tr
><tr id="gr_svn5_251"

 onmouseover="gutterOver(251)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',251);">&nbsp;</span
></td><td id="251"><a href="#251">251</a></td></tr
><tr id="gr_svn5_252"

 onmouseover="gutterOver(252)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',252);">&nbsp;</span
></td><td id="252"><a href="#252">252</a></td></tr
><tr id="gr_svn5_253"

 onmouseover="gutterOver(253)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',253);">&nbsp;</span
></td><td id="253"><a href="#253">253</a></td></tr
><tr id="gr_svn5_254"

 onmouseover="gutterOver(254)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',254);">&nbsp;</span
></td><td id="254"><a href="#254">254</a></td></tr
><tr id="gr_svn5_255"

 onmouseover="gutterOver(255)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',255);">&nbsp;</span
></td><td id="255"><a href="#255">255</a></td></tr
><tr id="gr_svn5_256"

 onmouseover="gutterOver(256)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',256);">&nbsp;</span
></td><td id="256"><a href="#256">256</a></td></tr
><tr id="gr_svn5_257"

 onmouseover="gutterOver(257)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',257);">&nbsp;</span
></td><td id="257"><a href="#257">257</a></td></tr
><tr id="gr_svn5_258"

 onmouseover="gutterOver(258)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',258);">&nbsp;</span
></td><td id="258"><a href="#258">258</a></td></tr
><tr id="gr_svn5_259"

 onmouseover="gutterOver(259)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',259);">&nbsp;</span
></td><td id="259"><a href="#259">259</a></td></tr
><tr id="gr_svn5_260"

 onmouseover="gutterOver(260)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',260);">&nbsp;</span
></td><td id="260"><a href="#260">260</a></td></tr
><tr id="gr_svn5_261"

 onmouseover="gutterOver(261)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',261);">&nbsp;</span
></td><td id="261"><a href="#261">261</a></td></tr
><tr id="gr_svn5_262"

 onmouseover="gutterOver(262)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',262);">&nbsp;</span
></td><td id="262"><a href="#262">262</a></td></tr
><tr id="gr_svn5_263"

 onmouseover="gutterOver(263)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',263);">&nbsp;</span
></td><td id="263"><a href="#263">263</a></td></tr
><tr id="gr_svn5_264"

 onmouseover="gutterOver(264)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',264);">&nbsp;</span
></td><td id="264"><a href="#264">264</a></td></tr
><tr id="gr_svn5_265"

 onmouseover="gutterOver(265)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',265);">&nbsp;</span
></td><td id="265"><a href="#265">265</a></td></tr
><tr id="gr_svn5_266"

 onmouseover="gutterOver(266)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',266);">&nbsp;</span
></td><td id="266"><a href="#266">266</a></td></tr
><tr id="gr_svn5_267"

 onmouseover="gutterOver(267)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',267);">&nbsp;</span
></td><td id="267"><a href="#267">267</a></td></tr
><tr id="gr_svn5_268"

 onmouseover="gutterOver(268)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',268);">&nbsp;</span
></td><td id="268"><a href="#268">268</a></td></tr
><tr id="gr_svn5_269"

 onmouseover="gutterOver(269)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',269);">&nbsp;</span
></td><td id="269"><a href="#269">269</a></td></tr
><tr id="gr_svn5_270"

 onmouseover="gutterOver(270)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',270);">&nbsp;</span
></td><td id="270"><a href="#270">270</a></td></tr
><tr id="gr_svn5_271"

 onmouseover="gutterOver(271)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',271);">&nbsp;</span
></td><td id="271"><a href="#271">271</a></td></tr
><tr id="gr_svn5_272"

 onmouseover="gutterOver(272)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',272);">&nbsp;</span
></td><td id="272"><a href="#272">272</a></td></tr
><tr id="gr_svn5_273"

 onmouseover="gutterOver(273)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',273);">&nbsp;</span
></td><td id="273"><a href="#273">273</a></td></tr
><tr id="gr_svn5_274"

 onmouseover="gutterOver(274)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',274);">&nbsp;</span
></td><td id="274"><a href="#274">274</a></td></tr
><tr id="gr_svn5_275"

 onmouseover="gutterOver(275)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',275);">&nbsp;</span
></td><td id="275"><a href="#275">275</a></td></tr
><tr id="gr_svn5_276"

 onmouseover="gutterOver(276)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',276);">&nbsp;</span
></td><td id="276"><a href="#276">276</a></td></tr
><tr id="gr_svn5_277"

 onmouseover="gutterOver(277)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',277);">&nbsp;</span
></td><td id="277"><a href="#277">277</a></td></tr
><tr id="gr_svn5_278"

 onmouseover="gutterOver(278)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn5',278);">&nbsp;</span
></td><td id="278"><a href="#278">278</a></td></tr
></table></pre>
<pre><table width="100%"><tr class="nocursor"><td></td></tr></table></pre>
</td>
<td id="lines">
<pre><table width="100%"><tr class="cursor_stop cursor_hidden"><td></td></tr></table></pre>
<pre class="prettyprint lang-py"><table id="src_table_0"><tr
id=sl_svn5_1

 onmouseover="gutterOver(1)"

><td class="source">#!/usr/bin/python<br></td></tr
><tr
id=sl_svn5_2

 onmouseover="gutterOver(2)"

><td class="source">&quot;&quot;&quot;<br></td></tr
><tr
id=sl_svn5_3

 onmouseover="gutterOver(3)"

><td class="source">A simple routine to load in a LIGGGHTS hybrid dump file containing<br></td></tr
><tr
id=sl_svn5_4

 onmouseover="gutterOver(4)"

><td class="source">contact and contact force data and convert into a .vtk unstructured<br></td></tr
><tr
id=sl_svn5_5

 onmouseover="gutterOver(5)"

><td class="source">grid which can be used to visualise the force network.<br></td></tr
><tr
id=sl_svn5_6

 onmouseover="gutterOver(6)"

><td class="source"><br></td></tr
><tr
id=sl_svn5_7

 onmouseover="gutterOver(7)"

><td class="source">evtk is used to write binary VTK files:<br></td></tr
><tr
id=sl_svn5_8

 onmouseover="gutterOver(8)"

><td class="source">https://bitbucket.org/pauloh/pyevtk<br></td></tr
><tr
id=sl_svn5_9

 onmouseover="gutterOver(9)"

><td class="source"><br></td></tr
><tr
id=sl_svn5_10

 onmouseover="gutterOver(10)"

><td class="source">The pizza.py bdump command is used to handle LIGGGHTS dump files and<br></td></tr
><tr
id=sl_svn5_11

 onmouseover="gutterOver(11)"

><td class="source">therefore PYTHONPATH must include the pizza/src location.<br></td></tr
><tr
id=sl_svn5_12

 onmouseover="gutterOver(12)"

><td class="source"><br></td></tr
><tr
id=sl_svn5_13

 onmouseover="gutterOver(13)"

><td class="source">NOTE: bdump is NOT included in granular pizza, and should be taken<br></td></tr
><tr
id=sl_svn5_14

 onmouseover="gutterOver(14)"

><td class="source">from the standard LAMMPS pizza package!<br></td></tr
><tr
id=sl_svn5_15

 onmouseover="gutterOver(15)"

><td class="source"><br></td></tr
><tr
id=sl_svn5_16

 onmouseover="gutterOver(16)"

><td class="source">NOTE: it is impossible to tell from the bdump header which values<br></td></tr
><tr
id=sl_svn5_17

 onmouseover="gutterOver(17)"

><td class="source">have been requested in the compute, so check that your compute<br></td></tr
><tr
id=sl_svn5_18

 onmouseover="gutterOver(18)"

><td class="source">and dump match the format here - this will be checked in future!<br></td></tr
><tr
id=sl_svn5_19

 onmouseover="gutterOver(19)"

><td class="source"><br></td></tr
><tr
id=sl_svn5_20

 onmouseover="gutterOver(20)"

><td class="source">&quot;&quot;&quot;<br></td></tr
><tr
id=sl_svn5_21

 onmouseover="gutterOver(21)"

><td class="source"><br></td></tr
><tr
id=sl_svn5_22

 onmouseover="gutterOver(22)"

><td class="source">from evtk.vtk import VtkFile, VtkGroup, VtkUnstructuredGrid<br></td></tr
><tr
id=sl_svn5_23

 onmouseover="gutterOver(23)"

><td class="source">from bdump import bdump<br></td></tr
><tr
id=sl_svn5_24

 onmouseover="gutterOver(24)"

><td class="source">import numpy as np<br></td></tr
><tr
id=sl_svn5_25

 onmouseover="gutterOver(25)"

><td class="source">import sys, os<br></td></tr
><tr
id=sl_svn5_26

 onmouseover="gutterOver(26)"

><td class="source"><br></td></tr
><tr
id=sl_svn5_27

 onmouseover="gutterOver(27)"

><td class="source"># TODO: use a try/except here to check for missing modules, and fallback to ASCII VTK if evtk not found<br></td></tr
><tr
id=sl_svn5_28

 onmouseover="gutterOver(28)"

><td class="source"># TODO: ask for timestep or timestep range as input (code is NOT efficient and large files = long runtimes!)<br></td></tr
><tr
id=sl_svn5_29

 onmouseover="gutterOver(29)"

><td class="source"># TODO: write celldata for contact area and heat flux (if present)<br></td></tr
><tr
id=sl_svn5_30

 onmouseover="gutterOver(30)"

><td class="source"><br></td></tr
><tr
id=sl_svn5_31

 onmouseover="gutterOver(31)"

><td class="source"># Check for command line arguments<br></td></tr
><tr
id=sl_svn5_32

 onmouseover="gutterOver(32)"

><td class="source">if len(sys.argv) != 2:<br></td></tr
><tr
id=sl_svn5_33

 onmouseover="gutterOver(33)"

><td class="source">        sys.exit(&#39;Usage: dump2forcenetwork.py &lt;filename&gt;, where filename is typically dump.&lt;runname&gt;&#39;)<br></td></tr
><tr
id=sl_svn5_34

 onmouseover="gutterOver(34)"

><td class="source">        <br></td></tr
><tr
id=sl_svn5_35

 onmouseover="gutterOver(35)"

><td class="source">elif len(sys.argv) == 2: # we have one input param, that should be parsed as a filename<br></td></tr
><tr
id=sl_svn5_36

 onmouseover="gutterOver(36)"

><td class="source">    filename = str(sys.argv[1])<br></td></tr
><tr
id=sl_svn5_37

 onmouseover="gutterOver(37)"

><td class="source">    if not os.path.isfile(filename):<br></td></tr
><tr
id=sl_svn5_38

 onmouseover="gutterOver(38)"

><td class="source">        sys.exit(&#39;File &#39; + filename + &#39; does not exist!&#39;)<br></td></tr
><tr
id=sl_svn5_39

 onmouseover="gutterOver(39)"

><td class="source"><br></td></tr
><tr
id=sl_svn5_40

 onmouseover="gutterOver(40)"

><td class="source">splitname = filename.split(&#39;.&#39;)<br></td></tr
><tr
id=sl_svn5_41

 onmouseover="gutterOver(41)"

><td class="source"><br></td></tr
><tr
id=sl_svn5_42

 onmouseover="gutterOver(42)"

><td class="source">if len(splitname) == 2 and splitname[0].lower() == &#39;dump&#39;:<br></td></tr
><tr
id=sl_svn5_43

 onmouseover="gutterOver(43)"

><td class="source">    fileprefix = splitname[1]<br></td></tr
><tr
id=sl_svn5_44

 onmouseover="gutterOver(44)"

><td class="source">else:<br></td></tr
><tr
id=sl_svn5_45

 onmouseover="gutterOver(45)"

><td class="source">    fileprefix = splitname[0]<br></td></tr
><tr
id=sl_svn5_46

 onmouseover="gutterOver(46)"

><td class="source"><br></td></tr
><tr
id=sl_svn5_47

 onmouseover="gutterOver(47)"

><td class="source">inputpath = os.path.abspath(filename)<br></td></tr
><tr
id=sl_svn5_48

 onmouseover="gutterOver(48)"

><td class="source">inputdir = os.path.split(inputpath)[0]<br></td></tr
><tr
id=sl_svn5_49

 onmouseover="gutterOver(49)"

><td class="source"><br></td></tr
><tr
id=sl_svn5_50

 onmouseover="gutterOver(50)"

><td class="source"># create a sub-directory for the output .vtu files<br></td></tr
><tr
id=sl_svn5_51

 onmouseover="gutterOver(51)"

><td class="source">outputdir = os.path.join(inputdir,fileprefix)<br></td></tr
><tr
id=sl_svn5_52

 onmouseover="gutterOver(52)"

><td class="source">try:<br></td></tr
><tr
id=sl_svn5_53

 onmouseover="gutterOver(53)"

><td class="source">    os.mkdir(outputdir)<br></td></tr
><tr
id=sl_svn5_54

 onmouseover="gutterOver(54)"

><td class="source">except:<br></td></tr
><tr
id=sl_svn5_55

 onmouseover="gutterOver(55)"

><td class="source">    pass<br></td></tr
><tr
id=sl_svn5_56

 onmouseover="gutterOver(56)"

><td class="source"><br></td></tr
><tr
id=sl_svn5_57

 onmouseover="gutterOver(57)"

><td class="source"># Read in the dump file - since we can have many contacts (i.e. &gt;&gt; nparticles)<br></td></tr
><tr
id=sl_svn5_58

 onmouseover="gutterOver(58)"

><td class="source"># and many timesteps I will deal with one timestep at a time in memory,<br></td></tr
><tr
id=sl_svn5_59

 onmouseover="gutterOver(59)"

><td class="source"># write to the appropriate .vtu file for a single timestep, then move on.<br></td></tr
><tr
id=sl_svn5_60

 onmouseover="gutterOver(60)"

><td class="source"><br></td></tr
><tr
id=sl_svn5_61

 onmouseover="gutterOver(61)"

><td class="source">forcedata = bdump(filename,0)<br></td></tr
><tr
id=sl_svn5_62

 onmouseover="gutterOver(62)"

><td class="source"><br></td></tr
><tr
id=sl_svn5_63

 onmouseover="gutterOver(63)"

><td class="source">groupfile = fileprefix<br></td></tr
><tr
id=sl_svn5_64

 onmouseover="gutterOver(64)"

><td class="source">groupfile = os.path.join(inputdir,groupfile)<br></td></tr
><tr
id=sl_svn5_65

 onmouseover="gutterOver(65)"

><td class="source">groupfile = VtkGroup(groupfile)<br></td></tr
><tr
id=sl_svn5_66

 onmouseover="gutterOver(66)"

><td class="source"><br></td></tr
><tr
id=sl_svn5_67

 onmouseover="gutterOver(67)"

><td class="source">fileindex = 0<br></td></tr
><tr
id=sl_svn5_68

 onmouseover="gutterOver(68)"

><td class="source">timestep = forcedata.next()<br></td></tr
><tr
id=sl_svn5_69

 onmouseover="gutterOver(69)"

><td class="source"><br></td></tr
><tr
id=sl_svn5_70

 onmouseover="gutterOver(70)"

><td class="source"># check that we have the right number of colums (&gt;11)<br></td></tr
><tr
id=sl_svn5_71

 onmouseover="gutterOver(71)"

><td class="source">#<br></td></tr
><tr
id=sl_svn5_72

 onmouseover="gutterOver(72)"

><td class="source"># NOTE: the first timesteps are often blank, and then natoms returns 0, so this doesn&#39;t really work...<br></td></tr
><tr
id=sl_svn5_73

 onmouseover="gutterOver(73)"

><td class="source">#<br></td></tr
><tr
id=sl_svn5_74

 onmouseover="gutterOver(74)"

><td class="source">if forcedata.snaps[fileindex].natoms !=0 and len(forcedata.snaps[0].atoms[0]) &lt; 12:<br></td></tr
><tr
id=sl_svn5_75

 onmouseover="gutterOver(75)"

><td class="source">    print &quot;Error - dump file requires at least all parameters from a compute pair/gran/local id pos force (12 in total)&quot;<br></td></tr
><tr
id=sl_svn5_76

 onmouseover="gutterOver(76)"

><td class="source">    sys.exit()<br></td></tr
><tr
id=sl_svn5_77

 onmouseover="gutterOver(77)"

><td class="source"><br></td></tr
><tr
id=sl_svn5_78

 onmouseover="gutterOver(78)"

><td class="source"># loop through available timesteps<br></td></tr
><tr
id=sl_svn5_79

 onmouseover="gutterOver(79)"

><td class="source"># <br></td></tr
><tr
id=sl_svn5_80

 onmouseover="gutterOver(80)"

><td class="source">while timestep &gt;= 0:<br></td></tr
><tr
id=sl_svn5_81

 onmouseover="gutterOver(81)"

><td class="source"><br></td></tr
><tr
id=sl_svn5_82

 onmouseover="gutterOver(82)"

><td class="source">    # default data are stored as pos1 (3) pos2 (3) id1 id2 periodic_flag force (3) -&gt; 12 columns<br></td></tr
><tr
id=sl_svn5_83

 onmouseover="gutterOver(83)"

><td class="source">    #<br></td></tr
><tr
id=sl_svn5_84

 onmouseover="gutterOver(84)"

><td class="source">    # if contactArea is enabled, that&#39;s one more (13) and heatflux (14)<br></td></tr
><tr
id=sl_svn5_85

 onmouseover="gutterOver(85)"

><td class="source">    #<br></td></tr
><tr
id=sl_svn5_86

 onmouseover="gutterOver(86)"

><td class="source">    # assign names to atom columns (1-N)<br></td></tr
><tr
id=sl_svn5_87

 onmouseover="gutterOver(87)"

><td class="source">    forcedata.map(1,&quot;x1&quot;,2,&quot;y1&quot;,3,&quot;z1&quot;,4,&quot;x2&quot;,5,&quot;y2&quot;,6,&quot;z2&quot;,7,&quot;id1&quot;,8,&quot;id2&quot;,9,&quot;periodic&quot;,10,&quot;fx&quot;,11,&quot;fy&quot;,12,&quot;fz&quot;)<br></td></tr
><tr
id=sl_svn5_88

 onmouseover="gutterOver(88)"

><td class="source">    # forcedata.map(1,&quot;x1&quot;,2,&quot;y1&quot;,3,&quot;z1&quot;,4,&quot;x2&quot;,5,&quot;y2&quot;,6,&quot;z2&quot;,7,&quot;id1&quot;,8,&quot;id2&quot;,9,&quot;periodic&quot;,10,&quot;fx&quot;,11,&quot;fy&quot;,12,&quot;fz&quot;,13,&quot;area&quot;,14,&quot;heatflux&quot;)<br></td></tr
><tr
id=sl_svn5_89

 onmouseover="gutterOver(89)"

><td class="source"><br></td></tr
><tr
id=sl_svn5_90

 onmouseover="gutterOver(90)"

><td class="source">    # check for contact data (some timesteps may have no particles in contact)<br></td></tr
><tr
id=sl_svn5_91

 onmouseover="gutterOver(91)"

><td class="source">    #<br></td></tr
><tr
id=sl_svn5_92

 onmouseover="gutterOver(92)"

><td class="source">    # NB. if one loads two datasets into ParaView with defined timesteps, but in which<br></td></tr
><tr
id=sl_svn5_93

 onmouseover="gutterOver(93)"

><td class="source">    # one datasets has some missing, data for the previous timestep are still displayed - <br></td></tr
><tr
id=sl_svn5_94

 onmouseover="gutterOver(94)"

><td class="source">    # this means that it is better here to generate &quot;empty&quot; files for these timesteps.<br></td></tr
><tr
id=sl_svn5_95

 onmouseover="gutterOver(95)"

><td class="source"><br></td></tr
><tr
id=sl_svn5_96

 onmouseover="gutterOver(96)"

><td class="source">    if forcedata.snaps[fileindex].natoms == 0:   <br></td></tr
><tr
id=sl_svn5_97

 onmouseover="gutterOver(97)"

><td class="source">        vtufile = fileprefix+&#39;_&#39;+str(timestep)+&#39;.vtu&#39;<br></td></tr
><tr
id=sl_svn5_98

 onmouseover="gutterOver(98)"

><td class="source">        vtufile = os.path.join(outputdir,vtufile)<br></td></tr
><tr
id=sl_svn5_99

 onmouseover="gutterOver(99)"

><td class="source">        vtuwrite = file(vtufile,&#39;w&#39;)<br></td></tr
><tr
id=sl_svn5_100

 onmouseover="gutterOver(100)"

><td class="source">        vtuwrite.write(&quot;&quot;&quot;&lt;?xml version=&quot;1.0&quot;?&gt;<br></td></tr
><tr
id=sl_svn5_101

 onmouseover="gutterOver(101)"

><td class="source">&lt;VTKFile byte_order=&quot;LittleEndian&quot; version=&quot;0.1&quot; type=&quot;UnstructuredGrid&quot;&gt;<br></td></tr
><tr
id=sl_svn5_102

 onmouseover="gutterOver(102)"

><td class="source">&lt;UnstructuredGrid&gt;<br></td></tr
><tr
id=sl_svn5_103

 onmouseover="gutterOver(103)"

><td class="source">        &lt;Piece NumberOfCells=&quot;0&quot; NumberOfPoints=&quot;0&quot;&gt;<br></td></tr
><tr
id=sl_svn5_104

 onmouseover="gutterOver(104)"

><td class="source">                &lt;Cells&gt;<br></td></tr
><tr
id=sl_svn5_105

 onmouseover="gutterOver(105)"

><td class="source">                        &lt;DataArray NumberOfComponents=&quot;1&quot; offset=&quot;0&quot; type=&quot;Int64&quot; Name=&quot;connectivity&quot;/&gt;<br></td></tr
><tr
id=sl_svn5_106

 onmouseover="gutterOver(106)"

><td class="source">                        &lt;DataArray NumberOfComponents=&quot;1&quot; offset=&quot;0&quot; type=&quot;Int64&quot; Name=&quot;offsets&quot;/&gt;<br></td></tr
><tr
id=sl_svn5_107

 onmouseover="gutterOver(107)"

><td class="source">                        &lt;DataArray NumberOfComponents=&quot;1&quot; offset=&quot;0&quot; type=&quot;Int64&quot; Name=&quot;types&quot;/&gt;<br></td></tr
><tr
id=sl_svn5_108

 onmouseover="gutterOver(108)"

><td class="source"><br></td></tr
><tr
id=sl_svn5_109

 onmouseover="gutterOver(109)"

><td class="source">                &lt;/Cells&gt;<br></td></tr
><tr
id=sl_svn5_110

 onmouseover="gutterOver(110)"

><td class="source">        &lt;/Piece&gt;<br></td></tr
><tr
id=sl_svn5_111

 onmouseover="gutterOver(111)"

><td class="source">&lt;/UnstructuredGrid&gt;<br></td></tr
><tr
id=sl_svn5_112

 onmouseover="gutterOver(112)"

><td class="source">&lt;/VTKFile&gt;&quot;&quot;&quot;)<br></td></tr
><tr
id=sl_svn5_113

 onmouseover="gutterOver(113)"

><td class="source">        <br></td></tr
><tr
id=sl_svn5_114

 onmouseover="gutterOver(114)"

><td class="source">    else:<br></td></tr
><tr
id=sl_svn5_115

 onmouseover="gutterOver(115)"

><td class="source"><br></td></tr
><tr
id=sl_svn5_116

 onmouseover="gutterOver(116)"

><td class="source">        # number of cells = number of interactions (i.e. entries in the dump file)<br></td></tr
><tr
id=sl_svn5_117

 onmouseover="gutterOver(117)"

><td class="source">        ncells = len(forcedata.snaps[fileindex].atoms)<br></td></tr
><tr
id=sl_svn5_118

 onmouseover="gutterOver(118)"

><td class="source"><br></td></tr
><tr
id=sl_svn5_119

 onmouseover="gutterOver(119)"

><td class="source">        # number of periodic interactions<br></td></tr
><tr
id=sl_svn5_120

 onmouseover="gutterOver(120)"

><td class="source">        periodic = np.array(forcedata.snaps[fileindex].atoms[:,forcedata.names[&quot;periodic&quot;]],dtype=bool)<br></td></tr
><tr
id=sl_svn5_121

 onmouseover="gutterOver(121)"

><td class="source">        nperiodic = sum(periodic)<br></td></tr
><tr
id=sl_svn5_122

 onmouseover="gutterOver(122)"

><td class="source"><br></td></tr
><tr
id=sl_svn5_123

 onmouseover="gutterOver(123)"

><td class="source">        # number of non-periodic interactions (which will be written out)<br></td></tr
><tr
id=sl_svn5_124

 onmouseover="gutterOver(124)"

><td class="source">        nconnex = ncells - nperiodic<br></td></tr
><tr
id=sl_svn5_125

 onmouseover="gutterOver(125)"

><td class="source"><br></td></tr
><tr
id=sl_svn5_126

 onmouseover="gutterOver(126)"

><td class="source">        # extract the IDs as an array of integers<br></td></tr
><tr
id=sl_svn5_127

 onmouseover="gutterOver(127)"

><td class="source">        id1 = np.array(forcedata.snaps[fileindex].atoms[:,forcedata.names[&quot;id1&quot;]],dtype=long)<br></td></tr
><tr
id=sl_svn5_128

 onmouseover="gutterOver(128)"

><td class="source">        id2 = np.array(forcedata.snaps[fileindex].atoms[:,forcedata.names[&quot;id2&quot;]],dtype=long)<br></td></tr
><tr
id=sl_svn5_129

 onmouseover="gutterOver(129)"

><td class="source"><br></td></tr
><tr
id=sl_svn5_130

 onmouseover="gutterOver(130)"

><td class="source">        # and convert to lists<br></td></tr
><tr
id=sl_svn5_131

 onmouseover="gutterOver(131)"

><td class="source">        id1 = id1.tolist()<br></td></tr
><tr
id=sl_svn5_132

 onmouseover="gutterOver(132)"

><td class="source">        id2 = id2.tolist()<br></td></tr
><tr
id=sl_svn5_133

 onmouseover="gutterOver(133)"

><td class="source"><br></td></tr
><tr
id=sl_svn5_134

 onmouseover="gutterOver(134)"

><td class="source">        # concatenate into a single list<br></td></tr
><tr
id=sl_svn5_135

 onmouseover="gutterOver(135)"

><td class="source">        ids = []<br></td></tr
><tr
id=sl_svn5_136

 onmouseover="gutterOver(136)"

><td class="source">        ids = id1[:]<br></td></tr
><tr
id=sl_svn5_137

 onmouseover="gutterOver(137)"

><td class="source">        ids.extend(id2)<br></td></tr
><tr
id=sl_svn5_138

 onmouseover="gutterOver(138)"

><td class="source"><br></td></tr
><tr
id=sl_svn5_139

 onmouseover="gutterOver(139)"

><td class="source">        # convert to a set and back to remove duplicates, then sort<br></td></tr
><tr
id=sl_svn5_140

 onmouseover="gutterOver(140)"

><td class="source">        ids = list(set(ids))<br></td></tr
><tr
id=sl_svn5_141

 onmouseover="gutterOver(141)"

><td class="source">        ids.sort()<br></td></tr
><tr
id=sl_svn5_142

 onmouseover="gutterOver(142)"

><td class="source"><br></td></tr
><tr
id=sl_svn5_143

 onmouseover="gutterOver(143)"

><td class="source">        # number of points = number of unique IDs (particles)<br></td></tr
><tr
id=sl_svn5_144

 onmouseover="gutterOver(144)"

><td class="source">        npoints = len(ids)<br></td></tr
><tr
id=sl_svn5_145

 onmouseover="gutterOver(145)"

><td class="source"><br></td></tr
><tr
id=sl_svn5_146

 onmouseover="gutterOver(146)"

><td class="source">        # create empty arrays to hold x,y,z data<br></td></tr
><tr
id=sl_svn5_147

 onmouseover="gutterOver(147)"

><td class="source">        x = np.zeros( npoints, dtype=np.float64)<br></td></tr
><tr
id=sl_svn5_148

 onmouseover="gutterOver(148)"

><td class="source">        y = np.zeros( npoints, dtype=np.float64)<br></td></tr
><tr
id=sl_svn5_149

 onmouseover="gutterOver(149)"

><td class="source">        z = np.zeros( npoints, dtype=np.float64)<br></td></tr
><tr
id=sl_svn5_150

 onmouseover="gutterOver(150)"

><td class="source"><br></td></tr
><tr
id=sl_svn5_151

 onmouseover="gutterOver(151)"

><td class="source">        print &#39;Timestep:&#39;,str(timestep),&#39;npoints=&#39;,str(npoints),&#39;ncells=&#39;,str(ncells),&#39;nperiodic=&#39;,nperiodic<br></td></tr
><tr
id=sl_svn5_152

 onmouseover="gutterOver(152)"

><td class="source"><br></td></tr
><tr
id=sl_svn5_153

 onmouseover="gutterOver(153)"

><td class="source">        # Point data = location of each unique particle<br></td></tr
><tr
id=sl_svn5_154

 onmouseover="gutterOver(154)"

><td class="source">        #<br></td></tr
><tr
id=sl_svn5_155

 onmouseover="gutterOver(155)"

><td class="source">        # The order of this data is important since we use the position of each particle<br></td></tr
><tr
id=sl_svn5_156

 onmouseover="gutterOver(156)"

><td class="source">        # in this list to reference particle connectivity! We will use the order of the <br></td></tr
><tr
id=sl_svn5_157

 onmouseover="gutterOver(157)"

><td class="source">        # sorted ids array to determine this.<br></td></tr
><tr
id=sl_svn5_158

 onmouseover="gutterOver(158)"

><td class="source"><br></td></tr
><tr
id=sl_svn5_159

 onmouseover="gutterOver(159)"

><td class="source">        counter = 0   <br></td></tr
><tr
id=sl_svn5_160

 onmouseover="gutterOver(160)"

><td class="source">        for id in ids:<br></td></tr
><tr
id=sl_svn5_161

 onmouseover="gutterOver(161)"

><td class="source">            if id in id1:<br></td></tr
><tr
id=sl_svn5_162

 onmouseover="gutterOver(162)"

><td class="source">                index = id1.index(id)<br></td></tr
><tr
id=sl_svn5_163

 onmouseover="gutterOver(163)"

><td class="source">                xtemp,ytemp,ztemp = forcedata.snaps[fileindex].atoms[index,forcedata.names[&quot;x1&quot;]], \<br></td></tr
><tr
id=sl_svn5_164

 onmouseover="gutterOver(164)"

><td class="source">                        forcedata.snaps[fileindex].atoms[index,forcedata.names[&quot;y1&quot;]], \<br></td></tr
><tr
id=sl_svn5_165

 onmouseover="gutterOver(165)"

><td class="source">                        forcedata.snaps[fileindex].atoms[index,forcedata.names[&quot;z1&quot;]]<br></td></tr
><tr
id=sl_svn5_166

 onmouseover="gutterOver(166)"

><td class="source">            else:<br></td></tr
><tr
id=sl_svn5_167

 onmouseover="gutterOver(167)"

><td class="source">                index = id2.index(id)<br></td></tr
><tr
id=sl_svn5_168

 onmouseover="gutterOver(168)"

><td class="source">                xtemp,ytemp,ztemp = forcedata.snaps[fileindex].atoms[index,forcedata.names[&quot;x2&quot;]], \<br></td></tr
><tr
id=sl_svn5_169

 onmouseover="gutterOver(169)"

><td class="source">                        forcedata.snaps[fileindex].atoms[index,forcedata.names[&quot;y2&quot;]], \<br></td></tr
><tr
id=sl_svn5_170

 onmouseover="gutterOver(170)"

><td class="source">                        forcedata.snaps[fileindex].atoms[index,forcedata.names[&quot;z2&quot;]]<br></td></tr
><tr
id=sl_svn5_171

 onmouseover="gutterOver(171)"

><td class="source">            <br></td></tr
><tr
id=sl_svn5_172

 onmouseover="gutterOver(172)"

><td class="source">            x[counter]=xtemp<br></td></tr
><tr
id=sl_svn5_173

 onmouseover="gutterOver(173)"

><td class="source">            y[counter]=ytemp<br></td></tr
><tr
id=sl_svn5_174

 onmouseover="gutterOver(174)"

><td class="source">            z[counter]=ztemp           <br></td></tr
><tr
id=sl_svn5_175

 onmouseover="gutterOver(175)"

><td class="source">            counter += 1<br></td></tr
><tr
id=sl_svn5_176

 onmouseover="gutterOver(176)"

><td class="source"><br></td></tr
><tr
id=sl_svn5_177

 onmouseover="gutterOver(177)"

><td class="source">        # Now create the connectivity list - this corresponds to pairs of IDs, but referencing<br></td></tr
><tr
id=sl_svn5_178

 onmouseover="gutterOver(178)"

><td class="source">        # the order of the ids array, so now we loop through 0..ncells and have to connect <br></td></tr
><tr
id=sl_svn5_179

 onmouseover="gutterOver(179)"

><td class="source">        # id1 and id2, so I need to see where in ids these correspond to<br></td></tr
><tr
id=sl_svn5_180

 onmouseover="gutterOver(180)"

><td class="source"><br></td></tr
><tr
id=sl_svn5_181

 onmouseover="gutterOver(181)"

><td class="source">        # If the periodic flag is set for a given interactions, DO NOT connect the points<br></td></tr
><tr
id=sl_svn5_182

 onmouseover="gutterOver(182)"

><td class="source">        # (to avoid lines that cross the simulation domain)<br></td></tr
><tr
id=sl_svn5_183

 onmouseover="gutterOver(183)"

><td class="source">            <br></td></tr
><tr
id=sl_svn5_184

 onmouseover="gutterOver(184)"

><td class="source">        # Mask out periodic interactions from the cell (connectivity) array<br></td></tr
><tr
id=sl_svn5_185

 onmouseover="gutterOver(185)"

><td class="source">        # newList = [word for (word, mask) in zip(s,b) if mask]<br></td></tr
><tr
id=sl_svn5_186

 onmouseover="gutterOver(186)"

><td class="source">        id1_masked = [ident for (ident,mask) in zip(id1,np.invert(periodic)) if mask]<br></td></tr
><tr
id=sl_svn5_187

 onmouseover="gutterOver(187)"

><td class="source">        id2_masked = [ident for (ident,mask) in zip(id2,np.invert(periodic)) if mask]<br></td></tr
><tr
id=sl_svn5_188

 onmouseover="gutterOver(188)"

><td class="source"><br></td></tr
><tr
id=sl_svn5_189

 onmouseover="gutterOver(189)"

><td class="source">        # create an empty array to hold particle pairs<br></td></tr
><tr
id=sl_svn5_190

 onmouseover="gutterOver(190)"

><td class="source">        connections = np.zeros( 2*nconnex, dtype=int )<br></td></tr
><tr
id=sl_svn5_191

 onmouseover="gutterOver(191)"

><td class="source"><br></td></tr
><tr
id=sl_svn5_192

 onmouseover="gutterOver(192)"

><td class="source">        for pair in range(nconnex):<br></td></tr
><tr
id=sl_svn5_193

 onmouseover="gutterOver(193)"

><td class="source">            connections[2*pair],connections[2*pair+1] = ids.index(id1_masked[pair]),ids.index(id2_masked[pair])<br></td></tr
><tr
id=sl_svn5_194

 onmouseover="gutterOver(194)"

><td class="source">            <br></td></tr
><tr
id=sl_svn5_195

 onmouseover="gutterOver(195)"

><td class="source">        # The offset array is simply generated from 2*(1..ncells)<br></td></tr
><tr
id=sl_svn5_196

 onmouseover="gutterOver(196)"

><td class="source">        offset=(np.arange(nconnex,dtype=int)+1)*2<br></td></tr
><tr
id=sl_svn5_197

 onmouseover="gutterOver(197)"

><td class="source"><br></td></tr
><tr
id=sl_svn5_198

 onmouseover="gutterOver(198)"

><td class="source">        # The type array is simply ncells x 3 (i.e. a VTKLine type)<br></td></tr
><tr
id=sl_svn5_199

 onmouseover="gutterOver(199)"

><td class="source">        celltype = np.ones(nconnex,dtype=int)*3<br></td></tr
><tr
id=sl_svn5_200

 onmouseover="gutterOver(200)"

><td class="source"><br></td></tr
><tr
id=sl_svn5_201

 onmouseover="gutterOver(201)"

><td class="source">        # Finally we need force data for each cell<br></td></tr
><tr
id=sl_svn5_202

 onmouseover="gutterOver(202)"

><td class="source">        force = np.sqrt( np.array(forcedata.snaps[fileindex].atoms[:,forcedata.names[&quot;fx&quot;]],dtype=np.float64)**2 + \<br></td></tr
><tr
id=sl_svn5_203

 onmouseover="gutterOver(203)"

><td class="source">                         np.array(forcedata.snaps[fileindex].atoms[:,forcedata.names[&quot;fy&quot;]],dtype=np.float64)**2 + \<br></td></tr
><tr
id=sl_svn5_204

 onmouseover="gutterOver(204)"

><td class="source">                         np.array(forcedata.snaps[fileindex].atoms[:,forcedata.names[&quot;fz&quot;]],dtype=np.float64)**2 )<br></td></tr
><tr
id=sl_svn5_205

 onmouseover="gutterOver(205)"

><td class="source"><br></td></tr
><tr
id=sl_svn5_206

 onmouseover="gutterOver(206)"

><td class="source">        # And, optionally, contact area and heat flux (using the same connectivity)<br></td></tr
><tr
id=sl_svn5_207

 onmouseover="gutterOver(207)"

><td class="source">        # area = np.array(forcedata.snaps[fileindex].atoms[:,forcedata.names[&quot;area&quot;]],dtype=np.float64)<br></td></tr
><tr
id=sl_svn5_208

 onmouseover="gutterOver(208)"

><td class="source">        # heatflux = np.array(forcedata.snaps[fileindex].atoms[:,forcedata.names[&quot;heatflux&quot;]],dtype=np.float64)<br></td></tr
><tr
id=sl_svn5_209

 onmouseover="gutterOver(209)"

><td class="source"><br></td></tr
><tr
id=sl_svn5_210

 onmouseover="gutterOver(210)"

><td class="source">        # Now we have enough data to create the file:<br></td></tr
><tr
id=sl_svn5_211

 onmouseover="gutterOver(211)"

><td class="source">        # Points - (x,y,z) (npoints)<br></td></tr
><tr
id=sl_svn5_212

 onmouseover="gutterOver(212)"

><td class="source">        # Cells<br></td></tr
><tr
id=sl_svn5_213

 onmouseover="gutterOver(213)"

><td class="source">        #   Connectivity - connections (nconnex,2)<br></td></tr
><tr
id=sl_svn5_214

 onmouseover="gutterOver(214)"

><td class="source">        #   Offset - offset (nconnex)<br></td></tr
><tr
id=sl_svn5_215

 onmouseover="gutterOver(215)"

><td class="source">        #   type - celltype (nconnex)<br></td></tr
><tr
id=sl_svn5_216

 onmouseover="gutterOver(216)"

><td class="source">        # Celldata<br></td></tr
><tr
id=sl_svn5_217

 onmouseover="gutterOver(217)"

><td class="source">        #   force    (nconnex)<br></td></tr
><tr
id=sl_svn5_218

 onmouseover="gutterOver(218)"

><td class="source">        #   area     (nconnex)<br></td></tr
><tr
id=sl_svn5_219

 onmouseover="gutterOver(219)"

><td class="source">        #   heatflux (nconnex)<br></td></tr
><tr
id=sl_svn5_220

 onmouseover="gutterOver(220)"

><td class="source"><br></td></tr
><tr
id=sl_svn5_221

 onmouseover="gutterOver(221)"

><td class="source">        # create a VTK unstructured grid (.vtu) file<br></td></tr
><tr
id=sl_svn5_222

 onmouseover="gutterOver(222)"

><td class="source">        vtufile = fileprefix+&#39;_&#39;+str(timestep)<br></td></tr
><tr
id=sl_svn5_223

 onmouseover="gutterOver(223)"

><td class="source">        vtufile = os.path.join(outputdir,vtufile)<br></td></tr
><tr
id=sl_svn5_224

 onmouseover="gutterOver(224)"

><td class="source">        w = VtkFile(vtufile, VtkUnstructuredGrid)<br></td></tr
><tr
id=sl_svn5_225

 onmouseover="gutterOver(225)"

><td class="source">        vtufile += &#39;.vtu&#39;<br></td></tr
><tr
id=sl_svn5_226

 onmouseover="gutterOver(226)"

><td class="source"><br></td></tr
><tr
id=sl_svn5_227

 onmouseover="gutterOver(227)"

><td class="source">        w.openGrid()<br></td></tr
><tr
id=sl_svn5_228

 onmouseover="gutterOver(228)"

><td class="source">        w.openPiece(npoints=npoints, ncells=nconnex)<br></td></tr
><tr
id=sl_svn5_229

 onmouseover="gutterOver(229)"

><td class="source"><br></td></tr
><tr
id=sl_svn5_230

 onmouseover="gutterOver(230)"

><td class="source">        # Set up Points (x,y,z) data XML<br></td></tr
><tr
id=sl_svn5_231

 onmouseover="gutterOver(231)"

><td class="source">        w.openElement(&quot;Points&quot;)<br></td></tr
><tr
id=sl_svn5_232

 onmouseover="gutterOver(232)"

><td class="source">        w.addData(&quot;points&quot;, (x,y,z) )<br></td></tr
><tr
id=sl_svn5_233

 onmouseover="gutterOver(233)"

><td class="source">        w.closeElement(&quot;Points&quot;)<br></td></tr
><tr
id=sl_svn5_234

 onmouseover="gutterOver(234)"

><td class="source"><br></td></tr
><tr
id=sl_svn5_235

 onmouseover="gutterOver(235)"

><td class="source">        # Set up Cell data<br></td></tr
><tr
id=sl_svn5_236

 onmouseover="gutterOver(236)"

><td class="source">        w.openElement(&quot;Cells&quot;)<br></td></tr
><tr
id=sl_svn5_237

 onmouseover="gutterOver(237)"

><td class="source">        w.addData(&quot;connectivity&quot;, connections )<br></td></tr
><tr
id=sl_svn5_238

 onmouseover="gutterOver(238)"

><td class="source">        w.addData(&quot;offsets&quot;, offset)<br></td></tr
><tr
id=sl_svn5_239

 onmouseover="gutterOver(239)"

><td class="source">        w.addData(&quot;types&quot;, celltype)<br></td></tr
><tr
id=sl_svn5_240

 onmouseover="gutterOver(240)"

><td class="source">        w.closeElement(&quot;Cells&quot;)<br></td></tr
><tr
id=sl_svn5_241

 onmouseover="gutterOver(241)"

><td class="source"><br></td></tr
><tr
id=sl_svn5_242

 onmouseover="gutterOver(242)"

><td class="source">        # Set up force data<br></td></tr
><tr
id=sl_svn5_243

 onmouseover="gutterOver(243)"

><td class="source">        w.openData(&quot;Cell&quot;)<br></td></tr
><tr
id=sl_svn5_244

 onmouseover="gutterOver(244)"

><td class="source">        w.addData(&quot;force&quot;, force)<br></td></tr
><tr
id=sl_svn5_245

 onmouseover="gutterOver(245)"

><td class="source">        # w.addData(&quot;area&quot;, area)<br></td></tr
><tr
id=sl_svn5_246

 onmouseover="gutterOver(246)"

><td class="source">        # w.addData(&quot;heatflux&quot;, heatflux)<br></td></tr
><tr
id=sl_svn5_247

 onmouseover="gutterOver(247)"

><td class="source">        w.closeData(&quot;Cell&quot;)<br></td></tr
><tr
id=sl_svn5_248

 onmouseover="gutterOver(248)"

><td class="source"><br></td></tr
><tr
id=sl_svn5_249

 onmouseover="gutterOver(249)"

><td class="source">        # and contact area<br></td></tr
><tr
id=sl_svn5_250

 onmouseover="gutterOver(250)"

><td class="source">        # w.openData(&quot;Cell&quot;, scalars = &quot;area&quot;)<br></td></tr
><tr
id=sl_svn5_251

 onmouseover="gutterOver(251)"

><td class="source">        # w.addData(&quot;area&quot;, area)<br></td></tr
><tr
id=sl_svn5_252

 onmouseover="gutterOver(252)"

><td class="source">        # w.closeData(&quot;Cell&quot;)<br></td></tr
><tr
id=sl_svn5_253

 onmouseover="gutterOver(253)"

><td class="source"><br></td></tr
><tr
id=sl_svn5_254

 onmouseover="gutterOver(254)"

><td class="source">        # and heat flux<br></td></tr
><tr
id=sl_svn5_255

 onmouseover="gutterOver(255)"

><td class="source">        # w.openData(&quot;Cell&quot;, scalars = &quot;heatflux&quot;)<br></td></tr
><tr
id=sl_svn5_256

 onmouseover="gutterOver(256)"

><td class="source">        # w.addData(&quot;heatflux&quot;, heatflux)<br></td></tr
><tr
id=sl_svn5_257

 onmouseover="gutterOver(257)"

><td class="source">        # w.closeData(&quot;Cell&quot;)<br></td></tr
><tr
id=sl_svn5_258

 onmouseover="gutterOver(258)"

><td class="source"><br></td></tr
><tr
id=sl_svn5_259

 onmouseover="gutterOver(259)"

><td class="source">        # Wrap up<br></td></tr
><tr
id=sl_svn5_260

 onmouseover="gutterOver(260)"

><td class="source">        w.closePiece()<br></td></tr
><tr
id=sl_svn5_261

 onmouseover="gutterOver(261)"

><td class="source">        w.closeGrid()<br></td></tr
><tr
id=sl_svn5_262

 onmouseover="gutterOver(262)"

><td class="source"><br></td></tr
><tr
id=sl_svn5_263

 onmouseover="gutterOver(263)"

><td class="source">        # Append binary data<br></td></tr
><tr
id=sl_svn5_264

 onmouseover="gutterOver(264)"

><td class="source">        w.appendData( (x,y,z) )<br></td></tr
><tr
id=sl_svn5_265

 onmouseover="gutterOver(265)"

><td class="source">        w.appendData(connections).appendData(offset).appendData(celltype)<br></td></tr
><tr
id=sl_svn5_266

 onmouseover="gutterOver(266)"

><td class="source">        # w.appendData(force).appendData(area).appendData(heatflux)<br></td></tr
><tr
id=sl_svn5_267

 onmouseover="gutterOver(267)"

><td class="source">        w.appendData(force)<br></td></tr
><tr
id=sl_svn5_268

 onmouseover="gutterOver(268)"

><td class="source">        w.save()<br></td></tr
><tr
id=sl_svn5_269

 onmouseover="gutterOver(269)"

><td class="source"><br></td></tr
><tr
id=sl_svn5_270

 onmouseover="gutterOver(270)"

><td class="source">    # Add this file to the group of all timesteps<br></td></tr
><tr
id=sl_svn5_271

 onmouseover="gutterOver(271)"

><td class="source">    groupfile.addFile(filepath = os.path.relpath(vtufile,inputdir), sim_time = timestep)<br></td></tr
><tr
id=sl_svn5_272

 onmouseover="gutterOver(272)"

><td class="source"><br></td></tr
><tr
id=sl_svn5_273

 onmouseover="gutterOver(273)"

><td class="source">    fileindex += 1<br></td></tr
><tr
id=sl_svn5_274

 onmouseover="gutterOver(274)"

><td class="source">    timestep = forcedata.next()<br></td></tr
><tr
id=sl_svn5_275

 onmouseover="gutterOver(275)"

><td class="source"><br></td></tr
><tr
id=sl_svn5_276

 onmouseover="gutterOver(276)"

><td class="source"># end of main loop - close group file<br></td></tr
><tr
id=sl_svn5_277

 onmouseover="gutterOver(277)"

><td class="source">groupfile.save()<br></td></tr
><tr
id=sl_svn5_278

 onmouseover="gutterOver(278)"

><td class="source"><br></td></tr
></table></pre>
<pre><table width="100%"><tr class="cursor_stop cursor_hidden"><td></td></tr></table></pre>
</td>
</tr></table>

 
<script type="text/javascript">
 var lineNumUnderMouse = -1;
 
 function gutterOver(num) {
 gutterOut();
 var newTR = document.getElementById('gr_svn5_' + num);
 if (newTR) {
 newTR.className = 'undermouse';
 }
 lineNumUnderMouse = num;
 }
 function gutterOut() {
 if (lineNumUnderMouse != -1) {
 var oldTR = document.getElementById(
 'gr_svn5_' + lineNumUnderMouse);
 if (oldTR) {
 oldTR.className = '';
 }
 lineNumUnderMouse = -1;
 }
 }
 var numsGenState = {table_base_id: 'nums_table_'};
 var srcGenState = {table_base_id: 'src_table_'};
 var alignerRunning = false;
 var startOver = false;
 function setLineNumberHeights() {
 if (alignerRunning) {
 startOver = true;
 return;
 }
 numsGenState.chunk_id = 0;
 numsGenState.table = document.getElementById('nums_table_0');
 numsGenState.row_num = 0;
 if (!numsGenState.table) {
 return; // Silently exit if no file is present.
 }
 srcGenState.chunk_id = 0;
 srcGenState.table = document.getElementById('src_table_0');
 srcGenState.row_num = 0;
 alignerRunning = true;
 continueToSetLineNumberHeights();
 }
 function rowGenerator(genState) {
 if (genState.row_num < genState.table.rows.length) {
 var currentRow = genState.table.rows[genState.row_num];
 genState.row_num++;
 return currentRow;
 }
 var newTable = document.getElementById(
 genState.table_base_id + (genState.chunk_id + 1));
 if (newTable) {
 genState.chunk_id++;
 genState.row_num = 0;
 genState.table = newTable;
 return genState.table.rows[0];
 }
 return null;
 }
 var MAX_ROWS_PER_PASS = 1000;
 function continueToSetLineNumberHeights() {
 var rowsInThisPass = 0;
 var numRow = 1;
 var srcRow = 1;
 while (numRow && srcRow && rowsInThisPass < MAX_ROWS_PER_PASS) {
 numRow = rowGenerator(numsGenState);
 srcRow = rowGenerator(srcGenState);
 rowsInThisPass++;
 if (numRow && srcRow) {
 if (numRow.offsetHeight != srcRow.offsetHeight) {
 numRow.firstChild.style.height = srcRow.offsetHeight + 'px';
 }
 }
 }
 if (rowsInThisPass >= MAX_ROWS_PER_PASS) {
 setTimeout(continueToSetLineNumberHeights, 10);
 } else {
 alignerRunning = false;
 if (startOver) {
 startOver = false;
 setTimeout(setLineNumberHeights, 500);
 }
 }
 }
 function initLineNumberHeights() {
 // Do 2 complete passes, because there can be races
 // between this code and prettify.
 startOver = true;
 setTimeout(setLineNumberHeights, 250);
 window.onresize = setLineNumberHeights;
 }
 initLineNumberHeights();
</script>

 
 
 <div id="log">
 <div style="text-align:right">
 <a class="ifCollapse" href="#" onclick="_toggleMeta(this); return false">Show details</a>
 <a class="ifExpand" href="#" onclick="_toggleMeta(this); return false">Hide details</a>
 </div>
 <div class="ifExpand">
 
 
 <div class="pmeta_bubble_bg" style="border:1px solid white">
 <div class="round4"></div>
 <div class="round2"></div>
 <div class="round1"></div>
 <div class="box-inner">
 <div id="changelog">
 <p>Change log</p>
 <div>
 <a href="/p/liggghts-force-chains/source/detail?spec=svn5&amp;r=5">r5</a>
 by msbentley@gmail.com
 on Jul 13, 2012
 &nbsp; <a href="/p/liggghts-force-chains/source/diff?spec=svn5&r=5&amp;format=side&amp;path=/trunk/dump2force.py&amp;old_path=/trunk/dump2force.py&amp;old=4">Diff</a>
 </div>
 <pre>Updating error message for 12 required
params, setting default to only
id,pos,force</pre>
 </div>
 
 
 
 
 
 
 <script type="text/javascript">
 var detail_url = '/p/liggghts-force-chains/source/detail?r=5&spec=svn5';
 var publish_url = '/p/liggghts-force-chains/source/detail?r=5&spec=svn5#publish';
 // describe the paths of this revision in javascript.
 var changed_paths = [];
 var changed_urls = [];
 
 changed_paths.push('/trunk/dump2force.py');
 changed_urls.push('/p/liggghts-force-chains/source/browse/trunk/dump2force.py?r\x3d5\x26spec\x3dsvn5');
 
 var selected_path = '/trunk/dump2force.py';
 
 
 function getCurrentPageIndex() {
 for (var i = 0; i < changed_paths.length; i++) {
 if (selected_path == changed_paths[i]) {
 return i;
 }
 }
 }
 function getNextPage() {
 var i = getCurrentPageIndex();
 if (i < changed_paths.length - 1) {
 return changed_urls[i + 1];
 }
 return null;
 }
 function getPreviousPage() {
 var i = getCurrentPageIndex();
 if (i > 0) {
 return changed_urls[i - 1];
 }
 return null;
 }
 function gotoNextPage() {
 var page = getNextPage();
 if (!page) {
 page = detail_url;
 }
 window.location = page;
 }
 function gotoPreviousPage() {
 var page = getPreviousPage();
 if (!page) {
 page = detail_url;
 }
 window.location = page;
 }
 function gotoDetailPage() {
 window.location = detail_url;
 }
 function gotoPublishPage() {
 window.location = publish_url;
 }
</script>

 
 <style type="text/css">
 #review_nav {
 border-top: 3px solid white;
 padding-top: 6px;
 margin-top: 1em;
 }
 #review_nav td {
 vertical-align: middle;
 }
 #review_nav select {
 margin: .5em 0;
 }
 </style>
 <div id="review_nav">
 <table><tr><td>Go to:&nbsp;</td><td>
 <select name="files_in_rev" onchange="window.location=this.value">
 
 <option value="/p/liggghts-force-chains/source/browse/trunk/dump2force.py?r=5&amp;spec=svn5"
 selected="selected"
 >/trunk/dump2force.py</option>
 
 </select>
 </td></tr></table>
 
 
 <div id="review_instr" class="closed">
 <a class="ifOpened" href="/p/liggghts-force-chains/source/detail?r=5&spec=svn5#publish">Publish your comments</a>
 <div class="ifClosed">Double click a line to add a comment</div>
 </div>
 
 </div>
 
 
 </div>
 <div class="round1"></div>
 <div class="round2"></div>
 <div class="round4"></div>
 </div>
 <div class="pmeta_bubble_bg" style="border:1px solid white">
 <div class="round4"></div>
 <div class="round2"></div>
 <div class="round1"></div>
 <div class="box-inner">
 <div id="older_bubble">
 <p>Older revisions</p>
 
 
 <div class="closed" style="margin-bottom:3px;" >
 <a class="ifClosed" onclick="return _toggleHidden(this)"><img src="https://ssl.gstatic.com/codesite/ph/images/plus.gif" ></a>
 <a class="ifOpened" onclick="return _toggleHidden(this)"><img src="https://ssl.gstatic.com/codesite/ph/images/minus.gif" ></a>
 <a href="/p/liggghts-force-chains/source/detail?spec=svn5&r=4">r4</a>
 by msbentley@gmail.com
 on Oct 7, 2011
 &nbsp; <a href="/p/liggghts-force-chains/source/diff?spec=svn5&r=4&amp;format=side&amp;path=/trunk/dump2force.py&amp;old_path=/trunk/dump2force.py&amp;old=1">Diff</a>
 <br>
 <pre class="ifOpened">Added support for periodic boundaries,
contact area and heat transfer</pre>
 </div>
 
 <div class="closed" style="margin-bottom:3px;" >
 <a class="ifClosed" onclick="return _toggleHidden(this)"><img src="https://ssl.gstatic.com/codesite/ph/images/plus.gif" ></a>
 <a class="ifOpened" onclick="return _toggleHidden(this)"><img src="https://ssl.gstatic.com/codesite/ph/images/minus.gif" ></a>
 <a href="/p/liggghts-force-chains/source/detail?spec=svn5&r=1">r1</a>
 by msbentley@gmail.com
 on Sep 16, 2011
 &nbsp; <a href="/p/liggghts-force-chains/source/diff?spec=svn5&r=1&amp;format=side&amp;path=/trunk/dump2force.py&amp;old_path=/trunk/dump2force.py&amp;old=">Diff</a>
 <br>
 <pre class="ifOpened">Initial upload</pre>
 </div>
 
 
 <a href="/p/liggghts-force-chains/source/list?path=/trunk/dump2force.py&start=5">All revisions of this file</a>
 </div>
 </div>
 <div class="round1"></div>
 <div class="round2"></div>
 <div class="round4"></div>
 </div>
 
 <div class="pmeta_bubble_bg" style="border:1px solid white">
 <div class="round4"></div>
 <div class="round2"></div>
 <div class="round1"></div>
 <div class="box-inner">
 <div id="fileinfo_bubble">
 <p>File info</p>
 
 <div>Size: 10886 bytes,
 278 lines</div>
 
 <div><a href="//liggghts-force-chains.googlecode.com/svn/trunk/dump2force.py">View raw file</a></div>
 </div>
 
 <div id="props">
 <p>File properties</p>
 <dl>
 
 <dt>svn:executable</dt>
 <dd>*</dd>
 
 </dl>
 </div>
 
 </div>
 <div class="round1"></div>
 <div class="round2"></div>
 <div class="round4"></div>
 </div>
 </div>
 </div>


</div>

</div>
</div>

<script src="https://ssl.gstatic.com/codesite/ph/17097911804237236952/js/prettify/prettify.js"></script>
<script type="text/javascript">prettyPrint();</script>


<script src="https://ssl.gstatic.com/codesite/ph/17097911804237236952/js/source_file_scripts.js"></script>

 <script type="text/javascript" src="https://ssl.gstatic.com/codesite/ph/17097911804237236952/js/kibbles.js"></script>
 <script type="text/javascript">
 var lastStop = null;
 var initialized = false;
 
 function updateCursor(next, prev) {
 if (prev && prev.element) {
 prev.element.className = 'cursor_stop cursor_hidden';
 }
 if (next && next.element) {
 next.element.className = 'cursor_stop cursor';
 lastStop = next.index;
 }
 }
 
 function pubRevealed(data) {
 updateCursorForCell(data.cellId, 'cursor_stop cursor_hidden');
 if (initialized) {
 reloadCursors();
 }
 }
 
 function draftRevealed(data) {
 updateCursorForCell(data.cellId, 'cursor_stop cursor_hidden');
 if (initialized) {
 reloadCursors();
 }
 }
 
 function draftDestroyed(data) {
 updateCursorForCell(data.cellId, 'nocursor');
 if (initialized) {
 reloadCursors();
 }
 }
 function reloadCursors() {
 kibbles.skipper.reset();
 loadCursors();
 if (lastStop != null) {
 kibbles.skipper.setCurrentStop(lastStop);
 }
 }
 // possibly the simplest way to insert any newly added comments
 // is to update the class of the corresponding cursor row,
 // then refresh the entire list of rows.
 function updateCursorForCell(cellId, className) {
 var cell = document.getElementById(cellId);
 // we have to go two rows back to find the cursor location
 var row = getPreviousElement(cell.parentNode);
 row.className = className;
 }
 // returns the previous element, ignores text nodes.
 function getPreviousElement(e) {
 var element = e.previousSibling;
 if (element.nodeType == 3) {
 element = element.previousSibling;
 }
 if (element && element.tagName) {
 return element;
 }
 }
 function loadCursors() {
 // register our elements with skipper
 var elements = CR_getElements('*', 'cursor_stop');
 var len = elements.length;
 for (var i = 0; i < len; i++) {
 var element = elements[i]; 
 element.className = 'cursor_stop cursor_hidden';
 kibbles.skipper.append(element);
 }
 }
 function toggleComments() {
 CR_toggleCommentDisplay();
 reloadCursors();
 }
 function keysOnLoadHandler() {
 // setup skipper
 kibbles.skipper.addStopListener(
 kibbles.skipper.LISTENER_TYPE.PRE, updateCursor);
 // Set the 'offset' option to return the middle of the client area
 // an option can be a static value, or a callback
 kibbles.skipper.setOption('padding_top', 50);
 // Set the 'offset' option to return the middle of the client area
 // an option can be a static value, or a callback
 kibbles.skipper.setOption('padding_bottom', 100);
 // Register our keys
 kibbles.skipper.addFwdKey("n");
 kibbles.skipper.addRevKey("p");
 kibbles.keys.addKeyPressListener(
 'u', function() { window.location = detail_url; });
 kibbles.keys.addKeyPressListener(
 'r', function() { window.location = detail_url + '#publish'; });
 
 kibbles.keys.addKeyPressListener('j', gotoNextPage);
 kibbles.keys.addKeyPressListener('k', gotoPreviousPage);
 
 
 kibbles.keys.addKeyPressListener('h', toggleComments);
 
 }
 </script>
<script src="https://ssl.gstatic.com/codesite/ph/17097911804237236952/js/code_review_scripts.js"></script>
<script type="text/javascript">
 function showPublishInstructions() {
 var element = document.getElementById('review_instr');
 if (element) {
 element.className = 'opened';
 }
 }
 var codereviews;
 function revsOnLoadHandler() {
 // register our source container with the commenting code
 var paths = {'svn5': '/trunk/dump2force.py'}
 codereviews = CR_controller.setup(
 {"projectHomeUrl": "/p/liggghts-force-chains", "loggedInUserEmail": "msbentley@gmail.com", "profileUrl": "/u/108811474385654924234/", "assetHostPath": "https://ssl.gstatic.com/codesite/ph", "projectName": "liggghts-force-chains", "token": "ABZ6GAeaVWkSyXBNykXH6PaWSzufsKAcwQ:1410095814397", "assetVersionPath": "https://ssl.gstatic.com/codesite/ph/17097911804237236952", "domainName": null, "relativeBaseUrl": ""}, '', 'svn5', paths,
 CR_BrowseIntegrationFactory);
 
 // register our source container with the commenting code
 // in this case we're registering the container and the revison
 // associated with the contianer which may be the primary revision
 // or may be a previous revision against which the primary revision
 // of the file is being compared.
 codereviews.registerSourceContainer(document.getElementById('lines'), 'svn5');
 
 codereviews.registerActivityListener(CR_ActivityType.REVEAL_DRAFT_PLATE, showPublishInstructions);
 
 codereviews.registerActivityListener(CR_ActivityType.REVEAL_PUB_PLATE, pubRevealed);
 codereviews.registerActivityListener(CR_ActivityType.REVEAL_DRAFT_PLATE, draftRevealed);
 codereviews.registerActivityListener(CR_ActivityType.DISCARD_DRAFT_COMMENT, draftDestroyed);
 
 
 
 
 
 
 
 var initialized = true;
 reloadCursors();
 }
 window.onload = function() {keysOnLoadHandler(); revsOnLoadHandler();};

</script>
<script type="text/javascript" src="https://ssl.gstatic.com/codesite/ph/17097911804237236952/js/dit_scripts.js"></script>

 
 
 
 <script type="text/javascript" src="https://ssl.gstatic.com/codesite/ph/17097911804237236952/js/ph_core.js"></script>
 
 
 
 
</div> 

<div id="footer" dir="ltr">
 <div class="text">
 <a href="/projecthosting/terms.html">Terms</a> -
 <a href="http://www.google.com/privacy.html">Privacy</a> -
 <a href="/p/support/">Project Hosting Help</a>
 </div>
</div>
 <div class="hostedBy" style="margin-top: -20px;">
 <span style="vertical-align: top;">Powered by <a href="http://code.google.com/projecthosting/">Google Project Hosting</a></span>
 </div>

 
 


 
 </body>
</html>

