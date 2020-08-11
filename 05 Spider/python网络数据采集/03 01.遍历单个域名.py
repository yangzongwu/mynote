import random
import re
import datetime
from urllib.request import urlopen
from bs4 import BeautifulSoup


def getUrl01(html):
    """
    会包含大量无效链接
    """
    #html=urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
    bsObj = BeautifulSoup(html, 'html.parser')
    for link in bsObj.findAll("a"):
        if 'href' in link.attrs:
            print(link.attrs['href'])


def getUrl02(html):
    """
    • 它们都在id 是bodyContent 的div 标签里
    • URL 链接不包含分号
    • URL 链接都以/wiki/ 开头
    但是这么找出来的都是静态
    """
    bsObj = BeautifulSoup(html)
    for link in bsObj.find("div", {"id":"bodyContent"})\
            .findAll("a",href=re.compile("^(/wiki/)((?!:).)*$")):
        if 'href' in link.attrs:
            print(link.attrs['href'])


def getUrl(html):
    """
    打印本页面链接，随机打印链接中的链接
    """
    random.seed(datetime.datetime.now())
    def getLinks(articleUrl):
        html = urlopen("http://en.wikipedia.org" + articleUrl)
        bsObj = BeautifulSoup(html)
        return bsObj.find("div",{"id":"bodyContent"}).\
            findAll("a",href=re.compile("^(/wiki/)((?!:).)*$"))
    links = getLinks("/wiki/Kevin_Bacon")
    while len(links) > 0:
        newArticle = links[random.randint(0, len(links) - 1)].attrs["href"]
        print(newArticle)
        links = getLinks(newArticle)

html_doc = """


<!DOCTYPE html>
<html class="client-nojs" lang="en" dir="ltr">
<head>
<meta charset="UTF-8"/>
<title>Eric Idle - Wikipedia</title>
<script>document.documentElement.className="client-js";RLCONF={"wgBreakFrames":!1,"wgSeparatorTransformTable":["",""],"wgDigitTransformTable":["",""],"wgDefaultDateFormat":"dmy","wgMonthNames":["","January","February","March","April","May","June","July","August","September","October","November","December"],"wgRequestId":"27ef4dac-1136-4635-b04b-1b9c54a1da38","wgCSPNonce":!1,"wgCanonicalNamespace":"","wgCanonicalSpecialPageName":!1,"wgNamespaceNumber":0,"wgPageName":"Eric_Idle","wgTitle":"Eric Idle","wgCurRevisionId":968641123,"wgRevisionId":968641123,"wgArticleId":52042,"wgIsArticle":!0,"wgIsRedirect":!1,"wgAction":"view","wgUserName":null,"wgUserGroups":["*"],"wgCategories":["All articles with dead external links","Articles with dead external links from December 2013","Webarchive template wayback links","Use British English from November 2012","Use dmy dates from October 2017","Articles with hCards","Articles with IBDb links",
"Internet Off-Broadway Database person ID same as Wikidata","Wikipedia articles with BNE identifiers","Wikipedia articles with BNF identifiers","Wikipedia articles with GND identifiers","Wikipedia articles with ISNI identifiers","Wikipedia articles with LCCN identifiers","Wikipedia articles with MusicBrainz identifiers","Wikipedia articles with NKC identifiers","Wikipedia articles with NTA identifiers","Wikipedia articles with SELIBR identifiers","Wikipedia articles with SUDOC identifiers","Wikipedia articles with Trove identifiers","Wikipedia articles with VIAF identifiers","Wikipedia articles with WorldCat identifiers","1943 births","20th-century English comedians","20th-century English male actors","20th-century English composers","20th-century English novelists","20th-century English singers","21st-century English comedians","21st-century English male actors","21st-century British composers","21st-century English novelists","21st-century English singers","Actors from County Durham"
,"Alumni of Pembroke College, Cambridge","Drama Desk Award winners","English comedy musicians","British novelty song performers","British surrealist artists","English comedy writers","English dramatists and playwrights","British expatriate male actors in the United States","British male comedy actors","English male comedians","English male composers","English male dramatists and playwrights","English male film actors","English male novelists","English male radio actors","English male television actors","English male voice actors","English musical theatre composers","English singer-songwriters","English television writers","Grammy Award winners","Living people","Male screenwriters","Monty Python members","Musicians from Tyne and Wear","People educated at the Royal Wolverhampton School","People from South Shields","People from Wolverhampton","The Rutles members","Male television writers","English atheists","English agnostics"],"wgPageContentLanguage":"en","wgPageContentModel":"wikitext",
"wgRelevantPageName":"Eric_Idle","wgRelevantArticleId":52042,"wgIsProbablyEditable":!0,"wgRelevantPageIsProbablyEditable":!0,"wgRestrictionEdit":[],"wgRestrictionMove":[],"wgMediaViewerOnClick":!0,"wgMediaViewerEnabledByDefault":!0,"wgPopupsReferencePreviews":!1,"wgPopupsConflictsWithNavPopupGadget":!1,"wgVisualEditor":{"pageLanguageCode":"en","pageLanguageDir":"ltr","pageVariantFallbacks":"en"},"wgMFDisplayWikibaseDescriptions":{"search":!0,"nearby":!0,"watchlist":!0,"tagline":!1},"wgWMESchemaEditAttemptStepOversample":!1,"wgULSCurrentAutonym":"English","wgNoticeProject":"wikipedia","wgCentralAuthMobileDomain":!1,"wgEditSubmitButtonLabelPublish":!0,"wgULSPosition":"interlanguage","wgWikibaseItemId":"Q210741"};RLSTATE={"ext.globalCssJs.user.styles":"ready","site.styles":"ready","noscript":"ready","user.styles":"ready","ext.globalCssJs.user":"ready","user":"ready","user.options":"loading","ext.cite.styles":"ready","skins.vector.styles.legacy":"ready",
"jquery.makeCollapsible.styles":"ready","mediawiki.toc.styles":"ready","ext.visualEditor.desktopArticleTarget.noscript":"ready","ext.uls.interlanguage":"ready","ext.wikimediaBadges":"ready","wikibase.client.init":"ready"};RLPAGEMODULES=["ext.cite.ux-enhancements","site","mediawiki.page.startup","mediawiki.page.ready","jquery.makeCollapsible","mediawiki.toc","skins.vector.legacy.js","ext.gadget.ReferenceTooltips","ext.gadget.charinsert","ext.gadget.extra-toolbar-buttons","ext.gadget.refToolbar","ext.gadget.switcher","ext.centralauth.centralautologin","mmv.head","mmv.bootstrap.autostart","ext.popups","ext.visualEditor.desktopArticleTarget.init","ext.visualEditor.targetLoader","ext.eventLogging","ext.wikimediaEvents","ext.navigationTiming","ext.uls.compactlinks","ext.uls.interface","ext.cx.eventlogging.campaigns","ext.quicksurveys.init","ext.centralNotice.geoIP","ext.centralNotice.startUp"];</script>
<script>(RLQ=window.RLQ||[]).push(function(){mw.loader.implement("user.options@1hzgi",function($,jQuery,require,module){/*@nomin*/mw.user.tokens.set({"patrolToken":"+\\","watchToken":"+\\","csrfToken":"+\\"});
});});</script>
<link rel="stylesheet" href="/w/load.php?lang=en&amp;modules=ext.cite.styles%7Cext.uls.interlanguage%7Cext.visualEditor.desktopArticleTarget.noscript%7Cext.wikimediaBadges%7Cjquery.makeCollapsible.styles%7Cmediawiki.toc.styles%7Cskins.vector.styles.legacy%7Cwikibase.client.init&amp;only=styles&amp;skin=vector"/>
<script async="" src="/w/load.php?lang=en&amp;modules=startup&amp;only=scripts&amp;raw=1&amp;skin=vector"></script>
<meta name="ResourceLoaderDynamicStyles" content=""/>
<link rel="stylesheet" href="/w/load.php?lang=en&amp;modules=site.styles&amp;only=styles&amp;skin=vector"/>
<meta name="generator" content="MediaWiki 1.35.0-wmf.41"/>
<meta name="referrer" content="origin"/>
<meta name="referrer" content="origin-when-crossorigin"/>
<meta name="referrer" content="origin-when-cross-origin"/>
<meta property="og:image" content="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Eric_Idle_2014.jpg/1200px-Eric_Idle_2014.jpg"/>
<link rel="alternate" type="application/x-wiki" title="Edit this page" href="/w/index.php?title=Eric_Idle&amp;action=edit"/>
<link rel="edit" title="Edit this page" href="/w/index.php?title=Eric_Idle&amp;action=edit"/>
<link rel="apple-touch-icon" href="/static/apple-touch/wikipedia.png"/>
<link rel="shortcut icon" href="/static/favicon/wikipedia.ico"/>
<link rel="search" type="application/opensearchdescription+xml" href="/w/opensearch_desc.php" title="Wikipedia (en)"/>
<link rel="EditURI" type="application/rsd+xml" href="//en.wikipedia.org/w/api.php?action=rsd"/>
<link rel="license" href="//creativecommons.org/licenses/by-sa/3.0/"/>
<link rel="alternate" type="application/atom+xml" title="Wikipedia Atom feed" href="/w/index.php?title=Special:RecentChanges&amp;feed=atom"/>
<link rel="canonical" href="https://en.wikipedia.org/wiki/Eric_Idle"/>
<link rel="dns-prefetch" href="//login.wikimedia.org"/>
<link rel="dns-prefetch" href="//meta.wikimedia.org" />
<!--[if lt IE 9]><script src="/w/resources/lib/html5shiv/html5shiv.js"></script><![endif]-->
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject mw-editable page-Eric_Idle rootpage-Eric_Idle skin-vector action-view skin-vector-legacy minerva--history-page-action-enabled">
<div id="mw-page-base" class="noprint"></div>
<div id="mw-head-base" class="noprint"></div>
<div id="content" class="mw-body" role="main">
	<a id="top"></a>
	<div id="siteNotice" class="mw-body-content"><!-- CentralNotice --></div>
	<div class="mw-indicators mw-body-content">
	</div>
	<h1 id="firstHeading" class="firstHeading" lang="en">Eric Idle</h1>
	<div id="bodyContent" class="mw-body-content">
		<div id="siteSub" class="noprint">From Wikipedia, the free encyclopedia</div>
		<div id="contentSub"></div>
		<div id="contentSub2"></div>

		<div id="jump-to-nav"></div>
		<a class="mw-jump-link" href="#mw-head">Jump to navigation</a>
		<a class="mw-jump-link" href="#searchInput">Jump to search</a>
		<div id="mw-content-text" lang="en" dir="ltr" class="mw-content-ltr"><div class="mw-parser-output"><p class="mw-empty-elt">

</p>
<table class="infobox biography vcard" style="width:22em"><tbody><tr><th colspan="2" style="text-align:center;font-size:125%;font-weight:bold"><div class="fn" style="display:inline">Eric Idle</div></th></tr><tr><td colspan="2" style="text-align:center"><a href="/wiki/File:Eric_Idle_2014.jpg" class="image"><img alt="Eric Idle 2014.jpg" src="//upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Eric_Idle_2014.jpg/220px-Eric_Idle_2014.jpg" decoding="async" width="220" height="165" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Eric_Idle_2014.jpg/330px-Eric_Idle_2014.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Eric_Idle_2014.jpg/440px-Eric_Idle_2014.jpg 2x" data-file-width="2592" data-file-height="1944" /></a><div>Idle in 2014</div></td></tr><tr><th scope="row">Born</th><td><span style="display:none"> (<span class="bday">1943-03-29</span>) </span>29 March 1943<span class="noprint ForceAgeToShow"> (age&#160;77)</span><br /><div style="display:inline" class="birthplace"><a href="/wiki/South_Shields" title="South Shields">South Shields</a>, <a href="/wiki/County_Durham" title="County Durham">County Durham</a>, England</div></td></tr><tr><th scope="row">Alma&#160;mater</th><td><a href="/wiki/Pembroke_College,_Cambridge" title="Pembroke College, Cambridge">Pembroke College, Cambridge</a></td></tr><tr><th scope="row">Occupation</th><td class="role"><div class="hlist hlist-separated"><ul><li>Actor</li><li>comedian</li><li>composer</li><li>musician</li><li>singer-songwriter</li><li>writer</li></ul></div></td></tr><tr><th scope="row">Years&#160;active</th><td>1967–present</td></tr><tr><th scope="row"><div style="white-space:nowrap;">Notable work</div></th><td><a href="/wiki/Monty_Python" title="Monty Python">Monty Python</a><br /><a href="/wiki/The_Rutles" title="The Rutles">The Rutles</a><br /><i><a href="/wiki/Spamalot" title="Spamalot">Spamalot</a></i></td></tr><tr><th scope="row"><span class="nowrap">Spouse(s)</span></th><td><div style="display:inline;line-height:normal;margin:2px 0px;"><a href="/wiki/Lyn_Ashley" title="Lyn Ashley">Lyn Ashley</a><br />&#40;<abbr title="married">m.</abbr>&#160;1969&#59;&#32;<abbr title="divorced">div.</abbr>&#160;1975&#41;</div><br /><div style="display:inline;line-height:normal;margin:2px 0px;">Tania Kosevich&#32;&#40;<abbr title="married">m.</abbr>&#160;1981&#41;</div><sup id="cite_ref-1" class="reference"><a href="#cite_note-1">&#91;1&#93;</a></sup></td></tr><tr><th scope="row">Children</th><td>2</td></tr><tr><th scope="row">Website</th><td><span class="url"><a rel="nofollow" class="external text" href="http://ericidle.com/">ericidle<wbr />.com</a></span></td></tr></tbody></table>
<p><b>Eric Idle</b> (born 29 March 1943) is an English actor, comedian, author and musician. Idle is a former member of the British surreal comedy group <a href="/wiki/Monty_Python" title="Monty Python">Monty Python</a>, a member of the <a href="/wiki/Satire" title="Satire">parody</a> rock band <a href="/wiki/The_Rutles" title="The Rutles">The Rutles</a>, and the writer, for the music and lyrics, of the <a href="/wiki/Broadway_theatre" title="Broadway theatre">Broadway</a> musical <i><a href="/wiki/Spamalot" title="Spamalot">Spamalot</a></i> (based on <i><a href="/wiki/Monty_Python_and_the_Holy_Grail" title="Monty Python and the Holy Grail">Monty Python and the Holy Grail</a></i>).
</p><p>Known for his elaborate <a href="/wiki/Wordplay" class="mw-redirect" title="Wordplay">wordplay</a> and musical numbers, Idle performed many of Python's songs, including “<a href="/wiki/Always_Look_on_the_Bright_Side_of_Life" title="Always Look on the Bright Side of Life">Always Look on the Bright Side of Life</a>” (from <i><a href="/wiki/Monty_Python%27s_Life_of_Brian" title="Monty Python&#39;s Life of Brian">Life of Brian</a></i>), and the “<a href="/wiki/Galaxy_Song" title="Galaxy Song">Galaxy Song</a>” (from <i><a href="/wiki/Monty_Python%27s_The_Meaning_of_Life" title="Monty Python&#39;s The Meaning of Life">The Meaning of Life</a></i>).<sup id="cite_ref-Eggers_2-0" class="reference"><a href="#cite_note-Eggers-2">&#91;2&#93;</a></sup> After <i><a href="/wiki/Monty_Python%27s_Flying_Circus" title="Monty Python&#39;s Flying Circus">Monty Python's Flying Circus</a></i>, he hosted <i><a href="/wiki/Saturday_Night_Live" title="Saturday Night Live">Saturday Night Live</a></i> in the US four times in the first five seasons. Idle's initially successful solo career faltered in the 1990s with the failures of his 1993 film <i><a href="/wiki/Splitting_Heirs" title="Splitting Heirs">Splitting Heirs</a></i> (written, produced by, and starring him) and 1998's <i><a href="/wiki/An_Alan_Smithee_Film:_Burn_Hollywood_Burn" title="An Alan Smithee Film: Burn Hollywood Burn">An Alan Smithee Film: Burn Hollywood Burn</a></i> (in which he starred). He revived his career by returning to the source of his worldwide fame, adapting Monty Python material for other media. Following the success of the musical <i>Spamalot</i> (which won the <a href="/wiki/Tony_Award" title="Tony Award">Tony Award</a> for <a href="/wiki/Tony_Award_for_Best_Musical" title="Tony Award for Best Musical">Best Musical</a>), he also wrote <i><a href="/wiki/Not_the_Messiah_(He%27s_a_Very_Naughty_Boy)" title="Not the Messiah (He&#39;s a Very Naughty Boy)">Not the Messiah</a></i>, an <a href="/wiki/Oratorio" title="Oratorio">oratorio</a> derived from the <i>Life of Brian</i>.<sup id="cite_ref-3" class="reference"><a href="#cite_note-3">&#91;3&#93;</a></sup> He featured in a one-hour symphony of British Music when he performed to a global audience at the <a href="/wiki/2012_Summer_Olympics_closing_ceremony" title="2012 Summer Olympics closing ceremony">London 2012 Olympic Games closing ceremony</a>.<sup id="cite_ref-4" class="reference"><a href="#cite_note-4">&#91;4&#93;</a></sup>
</p>
<div id="toc" class="toc" role="navigation" aria-labelledby="mw-toc-heading"><input type="checkbox" role="button" id="toctogglecheckbox" class="toctogglecheckbox" style="display:none" /><div class="toctitle" lang="en" dir="ltr"><h2 id="mw-toc-heading">Contents</h2><span class="toctogglespan"><label class="toctogglelabel" for="toctogglecheckbox"></label></span></div>
<ul>
<li class="toclevel-1 tocsection-1"><a href="#Early_life_and_education"><span class="tocnumber">1</span> <span class="toctext">Early life and education</span></a></li>
<li class="toclevel-1 tocsection-2"><a href="#Career"><span class="tocnumber">2</span> <span class="toctext">Career</span></a>
<ul>
<li class="toclevel-2 tocsection-3"><a href="#Pre-Python_career_(1965–1969)"><span class="tocnumber">2.1</span> <span class="toctext">Pre-Python career (1965–1969)</span></a></li>
<li class="toclevel-2 tocsection-4"><a href="#Monty_Python_(1969–1983,_2014)"><span class="tocnumber">2.2</span> <span class="toctext">Monty Python (1969–1983, 2014)</span></a></li>
<li class="toclevel-2 tocsection-5"><a href="#Post-Python_career_(1973–present)"><span class="tocnumber">2.3</span> <span class="toctext">Post-<i>Python</i> career (1973–present)</span></a></li>
</ul>
</li>
<li class="toclevel-1 tocsection-6"><a href="#Other_credits"><span class="tocnumber">3</span> <span class="toctext">Other credits</span></a>
<ul>
<li class="toclevel-2 tocsection-7"><a href="#Writing"><span class="tocnumber">3.1</span> <span class="toctext">Writing</span></a></li>
<li class="toclevel-2 tocsection-8"><a href="#Songwriting"><span class="tocnumber">3.2</span> <span class="toctext">Songwriting</span></a></li>
</ul>
</li>
<li class="toclevel-1 tocsection-9"><a href="#Personal_life"><span class="tocnumber">4</span> <span class="toctext">Personal life</span></a></li>
<li class="toclevel-1 tocsection-10"><a href="#Tributes"><span class="tocnumber">5</span> <span class="toctext">Tributes</span></a></li>
<li class="toclevel-1 tocsection-11"><a href="#Filmography"><span class="tocnumber">6</span> <span class="toctext">Filmography</span></a>
<ul>
<li class="toclevel-2 tocsection-12"><a href="#Film"><span class="tocnumber">6.1</span> <span class="toctext">Film</span></a></li>
<li class="toclevel-2 tocsection-13"><a href="#Television"><span class="tocnumber">6.2</span> <span class="toctext">Television</span></a></li>
<li class="toclevel-2 tocsection-14"><a href="#Video_games"><span class="tocnumber">6.3</span> <span class="toctext">Video games</span></a></li>
<li class="toclevel-2 tocsection-15"><a href="#Stage"><span class="tocnumber">6.4</span> <span class="toctext">Stage</span></a></li>
<li class="toclevel-2 tocsection-16"><a href="#Bibliography"><span class="tocnumber">6.5</span> <span class="toctext">Bibliography</span></a></li>
</ul>
</li>
<li class="toclevel-1 tocsection-17"><a href="#References"><span class="tocnumber">7</span> <span class="toctext">References</span></a></li>
<li class="toclevel-1 tocsection-18"><a href="#External_links"><span class="tocnumber">8</span> <span class="toctext">External links</span></a></li>
</ul>
</div>

<h2><span class="mw-headline" id="Early_life_and_education">Early life and education</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Eric_Idle&amp;action=edit&amp;section=1" title="Edit section: Early life and education">edit</a><span class="mw-editsection-bracket">]</span></span></h2>
<p>Idle was born in Harton Hospital, in <a href="/wiki/South_Shields" title="South Shields">South Shields</a>, <a href="/wiki/County_Durham" title="County Durham">County Durham</a>, to which his mother had been evacuated from the north west of England. His mother, Norah Barron Sanderson,<sup id="cite_ref-5" class="reference"><a href="#cite_note-5">&#91;5&#93;</a></sup> was a <a href="/wiki/Health_visitor" title="Health visitor">health visitor</a> and his father, Ernest Idle,<sup id="cite_ref-Tel170207_6-0" class="reference"><a href="#cite_note-Tel170207-6">&#91;6&#93;</a></sup><sup id="cite_ref-7" class="reference"><a href="#cite_note-7">&#91;7&#93;</a></sup> served in the <a href="/wiki/Royal_Air_Force" title="Royal Air Force">Royal Air Force</a> during World War II, only to be killed in a road accident while hitchhiking home for Christmas in December 1945.<sup id="cite_ref-8" class="reference"><a href="#cite_note-8">&#91;8&#93;</a></sup><sup id="cite_ref-9" class="reference"><a href="#cite_note-9">&#91;9&#93;</a></sup> Idle spent part of his childhood in <a href="/wiki/Wallasey" title="Wallasey">Wallasey</a> on the <a href="/wiki/Wirral_Peninsula" title="Wirral Peninsula">Wirral peninsula</a>,<sup id="cite_ref-10" class="reference"><a href="#cite_note-10">&#91;10&#93;</a></sup> and attended St George's Primary School.<sup id="cite_ref-11" class="reference"><a href="#cite_note-11">&#91;11&#93;</a></sup> His mother had difficulty coping with a full-time job and bringing up a child, so when Idle was seven, she enrolled him in the <a href="/wiki/Royal_Wolverhampton_School" class="mw-redirect" title="Royal Wolverhampton School">Royal Wolverhampton School</a> as a <a href="/wiki/Boarding_school" title="Boarding school">boarder</a>. At this time, the school was a charitable foundation dedicated to the education and maintenance of children who had lost one or both parents.<sup id="cite_ref-McCabe_12-0" class="reference"><a href="#cite_note-McCabe-12">&#91;12&#93;</a></sup> Idle is quoted as saying: "It was a physically <a href="/wiki/Physical_abuse" title="Physical abuse">abusive</a>, <a href="/wiki/Bullying" title="Bullying">bullying</a>, harsh environment for a kid to grow up in. I got used to dealing with groups of boys and getting on with life in unpleasant circumstances and being smart and funny and subversive at the expense of authority. Perfect training for Python."<sup id="cite_ref-McCabe_12-1" class="reference"><a href="#cite_note-McCabe-12">&#91;12&#93;</a></sup>
</p><p>Idle stated that the two things that made his life bearable were listening to <a href="/wiki/Radio_Luxembourg_(English)" class="mw-redirect" title="Radio Luxembourg (English)">Radio Luxembourg</a> under the bedclothes and watching the local football team, <a href="/wiki/Wolverhampton_Wanderers_F.C." title="Wolverhampton Wanderers F.C.">Wolverhampton Wanderers</a>.<sup id="cite_ref-13" class="reference"><a href="#cite_note-13">&#91;13&#93;</a></sup> Despite this, he disliked other sports and would sneak out of school every Thursday afternoon to the local cinema. Idle was eventually caught watching the X-rated film <i><a href="/wiki/Butterfield_8" class="mw-redirect" title="Butterfield 8">Butterfield 8</a></i> (suitable for audiences aged 16 years and over under the <a href="/wiki/History_of_British_Film_Certificates#1951–1970" class="mw-redirect" title="History of British Film Certificates">contemporary film certificates</a>) and stripped of his <a href="/wiki/Prefect#Academic" title="Prefect">prefecture</a>, though by that time he was <a href="/wiki/Head_boy" class="mw-redirect" title="Head boy">head boy</a>. Idle had already refused to be senior boy in the school cadet force, as he supported the <a href="/wiki/Campaign_for_Nuclear_Disarmament" title="Campaign for Nuclear Disarmament">Campaign for Nuclear Disarmament</a> and had participated in the yearly <a href="/wiki/Aldermaston_Marches" title="Aldermaston Marches">Aldermaston March</a>.<sup id="cite_ref-McCabe_12-2" class="reference"><a href="#cite_note-McCabe-12">&#91;12&#93;</a></sup> Idle maintains that there was little to do at the school, and boredom drove him to study hard and consequently win a place at <a href="/wiki/University_of_Cambridge" title="University of Cambridge">Cambridge University</a>.<sup id="cite_ref-McCabe_12-3" class="reference"><a href="#cite_note-McCabe-12">&#91;12&#93;</a></sup>
</p>
<h2><span class="mw-headline" id="Career">Career</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Eric_Idle&amp;action=edit&amp;section=2" title="Edit section: Career">edit</a><span class="mw-editsection-bracket">]</span></span></h2>
<h3><span id="Pre-Python_career_.281965.E2.80.931969.29"></span><span class="mw-headline" id="Pre-Python_career_(1965–1969)">Pre-Python career (1965–1969)</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Eric_Idle&amp;action=edit&amp;section=3" title="Edit section: Pre-Python career (1965–1969)">edit</a><span class="mw-editsection-bracket">]</span></span></h3>
<p>Idle attended <a href="/wiki/Pembroke_College,_Cambridge" title="Pembroke College, Cambridge">Pembroke College, Cambridge</a>, where he studied <a href="/wiki/English_studies" title="English studies">English</a>. At Pembroke, he was invited to join the prestigious <a href="/wiki/Footlights" title="Footlights">Cambridge University Footlights Club</a> by the president of the Footlights Club, <a href="/wiki/Tim_Brooke-Taylor" title="Tim Brooke-Taylor">Tim Brooke-Taylor</a>, and Footlights Club member <a href="/wiki/Bill_Oddie" title="Bill Oddie">Bill Oddie</a>.
</p>
<style data-mw-deduplicate="TemplateStyles:r960796168">.mw-parser-output .templatequote{overflow:hidden;margin:1em 0;padding:0 40px}.mw-parser-output .templatequote .templatequotecite{line-height:1.5em;text-align:left;padding-left:1.6em;margin-top:0}</style><blockquote class="templatequote"><p>I'd never heard of the Footlights when I got there, but we had a tradition of college smoking-concerts, and I sent in some sketches parodying a play that had just been done. Tim Brooke-Taylor and Bill Oddie auditioned me for the Footlights smoker, and that led to me discovering about and getting into the Footlights, which was great.<sup id="cite_ref-14" class="reference"><a href="#cite_note-14">&#91;14&#93;</a></sup></p></blockquote>
<p>Idle started at Cambridge only a year after future fellow-Pythons <a href="/wiki/Graham_Chapman" title="Graham Chapman">Graham Chapman</a> and <a href="/wiki/John_Cleese" title="John Cleese">John Cleese</a>. He became <a href="/wiki/Footlights_President" class="mw-redirect" title="Footlights President">Footlights President</a> in 1965 and was the first to allow women to join the club.<sup id="cite_ref-15" class="reference"><a href="#cite_note-15">&#91;15&#93;</a></sup> Idle starred in the children's television comedy series <i><a href="/wiki/Do_Not_Adjust_Your_Set" title="Do Not Adjust Your Set">Do Not Adjust Your Set</a></i> co-starring his future Python castmates <a href="/wiki/Terry_Jones" title="Terry Jones">Terry Jones</a> and <a href="/wiki/Michael_Palin" title="Michael Palin">Michael Palin</a>. <a href="/wiki/Terry_Gilliam" title="Terry Gilliam">Terry Gilliam</a> provided animations for the show. The show's cast also included comic actors <a href="/wiki/David_Jason" title="David Jason">David Jason</a> and <a href="/wiki/Denise_Coffey" title="Denise Coffey">Denise Coffey</a>. Idle also appeared as guest in some episodes of the television series <i><a href="/wiki/At_Last_the_1948_Show" title="At Last the 1948 Show">At Last the 1948 Show</a></i>, which co-featured Cleese and Chapman.<sup id="cite_ref-16" class="reference"><a href="#cite_note-16">&#91;16&#93;</a></sup>
</p>
<h3><span id="Monty_Python_.281969.E2.80.931983.2C_2014.29"></span><span class="mw-headline" id="Monty_Python_(1969–1983,_2014)">Monty Python (1969–1983, 2014)</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Eric_Idle&amp;action=edit&amp;section=4" title="Edit section: Monty Python (1969–1983, 2014)">edit</a><span class="mw-editsection-bracket">]</span></span></h3>
<div role="note" class="hatnote navigation-not-searchable">Further information: <a href="/wiki/Monty_Python" title="Monty Python">Monty Python</a></div>
<p>Idle wrote for Python mostly by himself, at his own pace, although he sometimes found it difficult in having to present material to the others and make it seem funny without the back-up support of a partner. The other Pythons usually worked in teams and Cleese admitted that this was slightly unfair&#160;– when the Pythons voted on which sketches should appear in a show, "he (Idle) only got one vote". However, he also says that Idle was an independent person and worked best on his own. Idle himself admitted this was sometimes difficult: "You had to convince five others. And they were not the most un-egotistical of writers, either."
</p><p>Idle's work in Python is often characterised by an obsession with language and communication: many of his characters have verbal peculiarities, such as the man who speaks in <a href="/wiki/Anagram" title="Anagram">anagrams</a>, the man who says words in the wrong order, and the butcher who alternates between rudeness and politeness every time he speaks. A number of his sketches involve extended monologues (for example the customer in the "Travel Agency" sketch who won't stop talking about his unpleasant experiences with holidays), and he would frequently spoof the unnatural language and speech patterns of television presenters. Unlike Palin, Idle is said to be the master of insincere characters, from the <a href="/wiki/David_Frost" title="David Frost">David Frost</a>-esque Timmy Williams, to small-time crook Stig O'Tracy, who tries to deny the fact that <a href="/wiki/Organised_crime" class="mw-redirect" title="Organised crime">organised crime</a> master Dinsdale Piranha nailed his head to the floor.
</p><p>The second-youngest member of the Pythons, Idle was closest in spirit to the teenagers who made up much of Python's fanbase. Python sketches dealing most with contemporary obsessions like <a href="/wiki/Pop_music" title="Pop music">pop music</a>, sexual permissiveness and <a href="/wiki/Recreational_drug_use" title="Recreational drug use">recreational drugs</a> are usually Idle's work, often characterised by <a href="/wiki/Double_entendre" title="Double entendre">double entendre</a>, sexual references, and other "naughty" subject matter&#160;– most famously demonstrated in "<a href="/wiki/Nudge_Nudge" title="Nudge Nudge">Nudge Nudge</a>." Idle originally wrote "Nudge, Nudge" for <a href="/wiki/Ronnie_Barker" title="Ronnie Barker">Ronnie Barker</a>, but it was rejected because there was 'no joke in the words'.<sup id="cite_ref-17" class="reference"><a href="#cite_note-17">&#91;17&#93;</a></sup>
</p><p>A talented guitarist, Idle composed many of the group's most famous musical numbers, most notably "<a href="/wiki/Always_Look_on_the_Bright_Side_of_Life" title="Always Look on the Bright Side of Life">Always Look on the Bright Side of Life</a>", the closing number of <i><a href="/wiki/Monty_Python%27s_Life_of_Brian" title="Monty Python&#39;s Life of Brian">Life of Brian</a></i>, which has grown to become a Python signature tune. He was responsible for the "<a href="/wiki/Galaxy_Song" title="Galaxy Song">Galaxy Song</a>" from <i><a href="/wiki/Monty_Python%27s_The_Meaning_of_Life" title="Monty Python&#39;s The Meaning of Life">The Meaning of Life</a></i> and "<a href="/wiki/Eric_the_Half-a-Bee" title="Eric the Half-a-Bee">Eric the Half-a-Bee</a>", a whimsical tune that first appeared on the <i><a href="/wiki/Monty_Python%27s_Previous_Record" title="Monty Python&#39;s Previous Record">Previous Record</a></i> album.
</p>
<h3><span id="Post-Python_career_.281973.E2.80.93present.29"></span><span class="mw-headline" id="Post-Python_career_(1973–present)">Post-<i>Python</i> career (1973–present)</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Eric_Idle&amp;action=edit&amp;section=5" title="Edit section: Post-Python career (1973–present)">edit</a><span class="mw-editsection-bracket">]</span></span></h3>
<div class="thumb tright"><div class="thumbinner" style="width:222px;"><a href="/wiki/File:Eric_Idle_(2).jpg" class="image"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Eric_Idle_%282%29.jpg/220px-Eric_Idle_%282%29.jpg" decoding="async" width="220" height="267" class="thumbimage" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Eric_Idle_%282%29.jpg/330px-Eric_Idle_%282%29.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Eric_Idle_%282%29.jpg/440px-Eric_Idle_%282%29.jpg 2x" data-file-width="699" data-file-height="847" /></a>  <div class="thumbcaption"><div class="magnify"><a href="/wiki/File:Eric_Idle_(2).jpg" class="internal" title="Enlarge"></a></div>Eric Idle in 2003</div></div></div>
<p>After the success of <i>Python</i> in the early 1970s, all six members pursued solo projects. Idle's first solo work was his own <a href="/wiki/BBC_Radio_1" title="BBC Radio 1">BBC Radio One</a> show, <i>Radio Five</i> (pre-dating the real <a href="/wiki/BBC_Radio_5_(former)" title="BBC Radio 5 (former)">Radio Five</a> station by 18 years). This ran for two seasons from 1973 to 1974 and involved Idle performing sketches and links to records, with himself playing nearly all the multi-tracked parts.
</p><p>On television, Idle created <i><a href="/wiki/Rutland_Weekend_Television" title="Rutland Weekend Television">Rutland Weekend Television</a></i> (RWT), a sketch show on <a href="/wiki/BBC_Two" title="BBC Two">BBC2</a>, written by himself, with music by <a href="/wiki/Neil_Innes" title="Neil Innes">Neil Innes</a>. RWT was 'Britain's smallest television network'. The name was a parody of <a href="/wiki/London_Weekend_Television" title="London Weekend Television">London Weekend Television</a>, the independent television franchise contractor that provided Londoners with their <a href="/wiki/ITV_(TV_network)" title="ITV (TV network)">ITV</a> services at weekends; <a href="/wiki/Rutland" title="Rutland">Rutland</a> had been England's smallest county, but had recently been 'abolished' in an administrative shake-up. To make the joke complete, the programme went out on a weekday. Other regular performers were <a href="/wiki/David_Battley" title="David Battley">David Battley</a>, <a href="/wiki/Henry_Woolf" title="Henry Woolf">Henry Woolf</a>, <a href="/wiki/Gwen_Taylor" title="Gwen Taylor">Gwen Taylor</a> and <a href="/wiki/Terence_Bayler" title="Terence Bayler">Terence Bayler</a>. <a href="/wiki/George_Harrison" title="George Harrison">George Harrison</a> made a guest appearance on one episode.
</p><p>A legacy of RWT was the creation, with Innes, of <a href="/wiki/The_Rutles" title="The Rutles">the Rutles</a>, an affectionate parody of <a href="/wiki/The_Beatles" title="The Beatles">the Beatles</a>. The band became a popular phenomenon, especially in the U.S. where Idle was appearing on <i><a href="/wiki/Saturday_Night_Live" title="Saturday Night Live">Saturday Night Live</a></i>&#160;– fans would send in Beatles LPs with their sleeves altered to show the Rutles. In 1978, the Rutles' <a href="/wiki/Mockumentary" title="Mockumentary">mockumentary</a> film <i><a href="/wiki/All_You_Need_Is_Cash" title="All You Need Is Cash">All You Need Is Cash</a></i>, a collaboration between Python members and <i>Saturday Night Live</i>, was aired on <a href="/wiki/NBC" title="NBC">NBC</a> television, as written by Idle, with music by Innes. Idle appeared in the film as "Dirk McQuickly" (the <a href="/wiki/Paul_McCartney" title="Paul McCartney">Paul McCartney</a>-styled character of the group), as well as the main commentator, while Innes appeared as "Ron Nasty" (the band's stand-in for <a href="/wiki/John_Lennon" title="John Lennon">John Lennon</a>). Actors appearing in the film included <i>Saturday Night Live</i><span class="nowrap" style="padding-left:0.1em;">&#39;s</span> <a href="/wiki/John_Belushi" title="John Belushi">John Belushi</a>, <a href="/wiki/Bill_Murray" title="Bill Murray">Bill Murray</a> and <a href="/wiki/Gilda_Radner" title="Gilda Radner">Gilda Radner</a>, as well as fellow Python <a href="/wiki/Michael_Palin" title="Michael Palin">Michael Palin</a>, but also real musicians of the 1960s such as former Beatle <a href="/wiki/George_Harrison" title="George Harrison">George Harrison</a>, as well as <a href="/wiki/Mick_Jagger" title="Mick Jagger">Mick Jagger</a> and <a href="/wiki/Paul_Simon" title="Paul Simon">Paul Simon</a>. Idle wrote and directed the Rutles comeback in 2008 for a live show Rutlemania! to celebrate the 30th anniversary.<sup id="cite_ref-18" class="reference"><a href="#cite_note-18">&#91;18&#93;</a></sup> The performances took place in Los Angeles and New York City with a Beatles tribute band.<sup id="cite_ref-19" class="reference"><a href="#cite_note-19">&#91;19&#93;</a></sup>
</p><p>In 1986, Idle provided the voice of Wreck-Gar, the leader of the Junkions (a race of robots built out of junk that can only speak in film catchphrases and advertising slogans) in <i><a href="/wiki/The_Transformers:_The_Movie" title="The Transformers: The Movie">The Transformers: The Movie</a></i>. In 1987, he took part in the <a href="/wiki/English_National_Opera" title="English National Opera">English National Opera</a> production of the <a href="/wiki/Gilbert_and_Sullivan" title="Gilbert and Sullivan">Gilbert and Sullivan</a> <a href="/wiki/Comic_opera" title="Comic opera">comic opera</a> <i><a href="/wiki/The_Mikado" title="The Mikado">The Mikado</a></i>, in which he appeared in the role of the Lord High Executioner, Ko-Ko. In 1989, he appeared in the U.S. comedy television series <i><a href="/wiki/Nearly_Departed" title="Nearly Departed">Nearly Departed</a></i>, about a ghost who haunts the family inhabiting his former home; the series lasted for six episodes as a summer replacement series.
</p>
<div class="quotebox pullquote floatleft" style="width:29%;&#32;;"><style data-mw-deduplicate="TemplateStyles:r887775652">.mw-parser-output .quotebox{background-color:#F9F9F9;border:1px solid #aaa;box-sizing:border-box;padding:10px;font-size:88%;max-width:100%}.mw-parser-output .quotebox.floatleft{margin:0.5em 1.4em 0.8em 0}.mw-parser-output .quotebox.floatright{margin:0.5em 0 0.8em 1.4em}.mw-parser-output .quotebox.centered{margin:0.5em auto 0.8em auto}.mw-parser-output .quotebox.floatleft p,.mw-parser-output .quotebox.floatright p{font-style:inherit}.mw-parser-output .quotebox-title{background-color:#F9F9F9;text-align:center;font-size:larger;font-weight:bold}.mw-parser-output .quotebox-quote.quoted:before{font-family:"Times New Roman",serif;font-weight:bold;font-size:large;color:gray;content:" “ ";vertical-align:-45%;line-height:0}.mw-parser-output .quotebox-quote.quoted:after{font-family:"Times New Roman",serif;font-weight:bold;font-size:large;color:gray;content:" ” ";line-height:0}.mw-parser-output .quotebox .left-aligned{text-align:left}.mw-parser-output .quotebox .right-aligned{text-align:right}.mw-parser-output .quotebox .center-aligned{text-align:center}.mw-parser-output .quotebox cite{display:block;font-style:normal}@media screen and (max-width:360px){.mw-parser-output .quotebox{min-width:100%;margin:0 0 0.8em!important;float:none!important}}</style>
<div class="quotebox-quote left-aligned" style="">"Idle has always, it seemed, been happy to have been a Python, happy to talk about Python, happy to revisit the group's glory days. Even though he has gone on to his own work – dozens of films, plays, TV shows, albums, books and screenplays – he is perhaps the most active standard-bearer for the group. It was Idle who toured extensively in 2000 and 2003, performing Python songs with a band and back-up singers. He went on the road with the <i>Eric Idle Exploits Monty Python Tour</i>, then with the <i>Greedy Bastard Tour</i>, which was documented extensively on the Python website he launched in 1996."</div>
<p><cite class="left-aligned" style="">—Dave Eggers in <i><a href="/wiki/The_Guardian" title="The Guardian">The Guardian</a></i>, September 2006.<sup id="cite_ref-Eggers_2-1" class="reference"><a href="#cite_note-Eggers-2">&#91;2&#93;</a></sup></cite>
</p>
</div>
<p>Idle received good critical notices appearing in projects written and directed by others&#160;– such as <a href="/wiki/Terry_Gilliam" title="Terry Gilliam">Terry Gilliam</a>'s <i><a href="/wiki/The_Adventures_of_Baron_Munchausen" title="The Adventures of Baron Munchausen">The Adventures of Baron Munchausen</a></i> (1989), alongside <a href="/wiki/Robbie_Coltrane" title="Robbie Coltrane">Robbie Coltrane</a> in <i><a href="/wiki/Nuns_on_the_Run" title="Nuns on the Run">Nuns on the Run</a></i> (1990) and in <i><a href="/wiki/Casper_(film)" title="Casper (film)">Casper</a></i> (1995). He also played Ratty in Terry Jones' version of <i><a href="/wiki/The_Wind_in_the_Willows_(1996_film)" title="The Wind in the Willows (1996 film)">The Wind in the Willows</a></i> (1996). However, his own creative projects&#160;– such as the film <i><a href="/wiki/Splitting_Heirs" title="Splitting Heirs">Splitting Heirs</a></i> (1993), a comedy he wrote, starred in and executive-produced&#160;– were mostly unsuccessful with critics and audiences.
</p><p>In 1994, Idle appeared as Dr. Nigel Channing, chairman of the Imagination Institute and host of an 'Inventor of the Year' awards show in the <a href="/wiki/3-D_film" class="mw-redirect" title="3-D film">three-dimensional</a> film <i><a href="/wiki/Honey,_I_Shrunk_the_Audience!" title="Honey, I Shrunk the Audience!">Honey, I Shrunk the Audience!</a></i>, which was an attraction at the <a href="/wiki/Imagination!_(Epcot)" title="Imagination! (Epcot)">Imagination Pavilion</a> at <a href="/wiki/Walt_Disney_World" title="Walt Disney World">Walt Disney World</a>'s <a href="/wiki/Epcot" title="Epcot">Epcot</a> from 1994 until 2010 and at <a href="/wiki/Disneyland_Park_(Anaheim)" class="mw-redirect" title="Disneyland Park (Anaheim)">Disneyland</a> from 1998 until 2010. The film also stars <a href="/wiki/Rick_Moranis" title="Rick Moranis">Rick Moranis</a> and other members of the cast of the 1989 feature film <i><a href="/wiki/Honey,_I_Shrunk_the_Kids" title="Honey, I Shrunk the Kids">Honey, I Shrunk the Kids</a></i>. In 1999, he reprised the role in the short-lived second incarnation of the <a href="/wiki/Journey_into_Imagination" class="mw-redirect" title="Journey into Imagination">Journey into Imagination</a> ride at Epcot, replacing <a href="/wiki/Figment_(Disney_character)" class="mw-redirect" title="Figment (Disney character)">Figment</a> and Dreamfinder as the host. Due to an outcry from Disney fans, the attraction was reworked in 2001, reintroducing Figment into the ride while also retaining Idle's role as Nigel Channing. Idle is also writer and star of the 3-D film <i>Pirates&#160;– 4D</i> for Busch Entertainment Corporation.
</p><p>In 1995, Idle voiced <a href="/wiki/Rincewind" title="Rincewind">Rincewind the "Wizzard"</a> in <a href="/wiki/Discworld_(computer_game)" class="mw-redirect" title="Discworld (computer game)">a computer adventure game</a> based on <a href="/wiki/Terry_Pratchett" title="Terry Pratchett">Terry Pratchett</a>'s <i><a href="/wiki/Discworld" title="Discworld">Discworld</a></i> novels. In 1996, he reprised his role as Rincewind for <a href="/wiki/Discworld_2" class="mw-redirect" title="Discworld 2">the game's sequel</a>,<sup id="cite_ref-20" class="reference"><a href="#cite_note-20">&#91;20&#93;</a></sup> and composed and sang its theme song, "That's Death". In 1998, Idle appeared in the lead role in the poorly received film <i><a href="/wiki/Burn_Hollywood_Burn" class="mw-redirect" title="Burn Hollywood Burn">Burn Hollywood Burn</a></i>. That same year, he also provided the voice of Devon, a dragon, in <a href="/wiki/Warner_Bros." title="Warner Bros.">Warner Bros.</a> <a href="/wiki/Animated_film" class="mw-redirect" title="Animated film">Animated film</a> <i><a href="/wiki/Quest_for_Camelot" title="Quest for Camelot">Quest for Camelot</a></i> and as Slyly, the albino Arctic fox in <i><a href="/wiki/Rudolph_the_Red-Nosed_Reindeer:_The_Movie" title="Rudolph the Red-Nosed Reindeer: The Movie">Rudolph the Red-Nosed Reindeer: The Movie</a></i>.
</p><p>In recent years, Idle has provided voice work for animation, such as in <i><a href="/wiki/South_Park:_Bigger,_Longer_%26_Uncut" title="South Park: Bigger, Longer &amp; Uncut">South Park: Bigger, Longer &amp; Uncut</a></i>, in which he voiced Dr. Vosknocker. He has also made three appearances on <i><a href="/wiki/The_Simpsons" title="The Simpsons">The Simpsons</a></i> as famous documentarian <a href="/wiki/Declan_Desmond" class="mw-redirect" title="Declan Desmond">Declan Desmond</a>, so far the only appearance on the show by a Python. Idle provided the voice of <a href="/wiki/Merlin_(Shrek)" class="mw-redirect" title="Merlin (Shrek)">Merlin the magician</a> in the <a href="/wiki/DreamWorks_Animation" title="DreamWorks Animation">DreamWorks</a> animated film <i><a href="/wiki/Shrek_the_Third" title="Shrek the Third">Shrek the Third</a></i> (2007) with his former <i>Python</i> co-star John Cleese, who voiced <a href="/wiki/King_Harold_(Shrek)" class="mw-redirect" title="King Harold (Shrek)">King Harold</a>. He has also narrated the audiobook version of <i><a href="/wiki/Charlie_and_the_Chocolate_Factory" title="Charlie and the Chocolate Factory">Charlie and the Chocolate Factory</a></i> by <a href="/wiki/Roald_Dahl" title="Roald Dahl">Roald Dahl</a> and Spanque in an episode of <i><a href="/wiki/The_Angry_Beavers" title="The Angry Beavers">The Angry Beavers</a></i>.<sup id="cite_ref-21" class="reference"><a href="#cite_note-21">&#91;21&#93;</a></sup>
</p><p>In late 2003, Idle began a performing tour of several <a href="/wiki/North_America" title="North America">American and Canadian</a> cities entitled <i>The Greedy Bastard Tour</i>.<sup id="cite_ref-Eggers_2-2" class="reference"><a href="#cite_note-Eggers-2">&#91;2&#93;</a></sup> The stage performances consisted largely of music from Monty Python episodes and films, along with some original post-Python material. In 2005, Idle released <i>The Greedy Bastard Diary</i>, a book detailing the things the cast and crew encountered during the three-month tour.<sup id="cite_ref-Eggers_2-3" class="reference"><a href="#cite_note-Eggers-2">&#91;2&#93;</a></sup>
</p>
<div class="thumb tright"><div class="thumbinner" style="width:222px;"><a href="/wiki/File:Nudge,_Nudge_O2_Arena.jpg" class="image"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/95/Nudge%2C_Nudge_O2_Arena.jpg/220px-Nudge%2C_Nudge_O2_Arena.jpg" decoding="async" width="220" height="165" class="thumbimage" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/95/Nudge%2C_Nudge_O2_Arena.jpg/330px-Nudge%2C_Nudge_O2_Arena.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/95/Nudge%2C_Nudge_O2_Arena.jpg/440px-Nudge%2C_Nudge_O2_Arena.jpg 2x" data-file-width="2592" data-file-height="1944" /></a>  <div class="thumbcaption"><div class="magnify"><a href="/wiki/File:Nudge,_Nudge_O2_Arena.jpg" class="internal" title="Enlarge"></a></div>Idle (right) and <a href="/wiki/Terry_Jones" title="Terry Jones">Terry Jones</a> performing the “<a href="/wiki/Nudge_Nudge" title="Nudge Nudge">Nudge Nudge</a>” sketch at the Python reunion in 2014.</div></div></div>
<p>In 2004, Idle created <i><a href="/wiki/Spamalot" title="Spamalot">Spamalot</a>,</i> a <a href="/wiki/Comedy_music" title="Comedy music">musical comedy</a> based on the 1975 film <i>Monty Python and the Holy Grail</i>. The medieval production tells the story of <a href="/wiki/King_Arthur" title="King Arthur">King Arthur</a> and his Knights of the Round Table as they journey on their quest for the <a href="/wiki/Holy_Grail" title="Holy Grail">Holy Grail</a>.<sup id="cite_ref-Eggers_2-4" class="reference"><a href="#cite_note-Eggers-2">&#91;2&#93;</a></sup> <i>Spamalot</i> features a book and lyrics by Eric Idle, music by Idle and <a href="/wiki/John_Du_Prez" title="John Du Prez">John Du Prez</a>, direction by <a href="/wiki/Mike_Nichols" title="Mike Nichols">Mike Nichols</a>, and choreography by <a href="/wiki/Casey_Nicholaw" title="Casey Nicholaw">Casey Nicholaw</a>.<sup id="cite_ref-22" class="reference"><a href="#cite_note-22">&#91;22&#93;</a></sup>
</p><p>Idle's play <i>What About Dick?</i> was given a staged reading at two public performances in Hollywood on 10–11 November 2007. The cast included Idle, <a href="/wiki/Billy_Connolly" title="Billy Connolly">Billy Connolly</a>, <a href="/wiki/Tim_Curry" title="Tim Curry">Tim Curry</a>, <a href="/wiki/Eddie_Izzard" title="Eddie Izzard">Eddie Izzard</a>, <a href="/wiki/Jane_Leeves" title="Jane Leeves">Jane Leeves</a>, <a href="/wiki/Emily_Mortimer" title="Emily Mortimer">Emily Mortimer</a>, <a href="/wiki/Jim_Piddock" title="Jim Piddock">Jim Piddock</a> and <a href="/wiki/Tracey_Ullman" title="Tracey Ullman">Tracey Ullman</a>.<sup id="cite_ref-23" class="reference"><a href="#cite_note-23">&#91;23&#93;</a></sup> The play returned on 26–29 April 2012 in the <a href="/wiki/Orpheum_Theatre_(Los_Angeles)" title="Orpheum Theatre (Los Angeles)">Orpheum Theatre</a> with most of the cast returning with the exception of Emily Mortimer who was replaced by <a href="/wiki/Sophie_Winkleman" title="Sophie Winkleman">Sophie Winkleman</a>. <a href="/wiki/Russell_Brand" title="Russell Brand">Russell Brand</a> also joined the cast. The play was made available for digital download on 13 November 2012.
</p><p>Idle performed at the <a href="/wiki/2012_Summer_Olympics_closing_ceremony" title="2012 Summer Olympics closing ceremony">2012 Summer Olympics closing ceremony</a> at the <a href="/wiki/London_Stadium" title="London Stadium">Olympic Stadium</a> in London on 12 August, singing "<a href="/wiki/Always_Look_on_the_Bright_Side_of_Life" title="Always Look on the Bright Side of Life">Always Look on the Bright Side of Life</a>". He was the creator and director of the live show <i><a href="/wiki/Monty_Python_Live_(Mostly)" title="Monty Python Live (Mostly)">Monty Python Live (mostly)&#160;– One down, Five to go</a></i> which took place at <a href="/wiki/The_O2_Arena" title="The O2 Arena">the O2 Arena</a>, London between 1 and 20 July 2014.<sup id="cite_ref-24" class="reference"><a href="#cite_note-24">&#91;24&#93;</a></sup>
</p><p>In December 2016, Idle was the writer and co-presenter of <i>The Entire Universe</i>, a "comedy and musical extravaganza with the help of <a href="/wiki/Warwick_Davis" title="Warwick Davis">Warwick Davis</a>, <a href="/wiki/Noel_Fielding" title="Noel Fielding">Noel Fielding</a>, <a href="/wiki/Hannah_Waddingham" title="Hannah Waddingham">Hannah Waddingham</a> and <a href="/wiki/Robin_Ince" title="Robin Ince">Robin Ince</a>, alongside a chorus of singers and dancers," broadcast by BBC Two.<sup id="cite_ref-25" class="reference"><a href="#cite_note-25">&#91;25&#93;</a></sup>
</p>
<h2><span class="mw-headline" id="Other_credits">Other credits</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Eric_Idle&amp;action=edit&amp;section=6" title="Edit section: Other credits">edit</a><span class="mw-editsection-bracket">]</span></span></h2>
<h3><span class="mw-headline" id="Writing">Writing</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Eric_Idle&amp;action=edit&amp;section=7" title="Edit section: Writing">edit</a><span class="mw-editsection-bracket">]</span></span></h3>
<p>Idle has written several books, both fiction and non-fiction. His novels are <i><a href="/wiki/Hello_Sailor_(novel)" title="Hello Sailor (novel)">Hello Sailor</a></i> and <i><a href="/wiki/The_Road_to_Mars" title="The Road to Mars">The Road to Mars</a></i>. In 1976, he produced a spin-off book to <i><a href="/wiki/Rutland_Weekend_Television" title="Rutland Weekend Television">Rutland Weekend Television</a></i>, titled <i>The Rutland Dirty Weekend Book</i>. In 1982, he wrote a West End farce <i>Pass the Butler</i>, starring <a href="/wiki/Willie_Rushton" title="Willie Rushton">Willie Rushton</a>. During his Greedy Bastard Tour of 2003, he wrote the diaries that would be made into <i>The Greedy Bastard Diary: A Comic Tour of America</i>, published in February 2005.
</p><p>Idle also wrote the book and co-wrote the music and lyrics for the musical <i><a href="/wiki/Spamalot" title="Spamalot">Monty Python's Spamalot</a></i>, based on the film <i><a href="/wiki/Monty_Python_and_the_Holy_Grail" title="Monty Python and the Holy Grail">Monty Python and the Holy Grail</a></i>. It premiered in Chicago before moving to Broadway, where it received the <a href="/wiki/Tony_Award_for_Best_Musical" title="Tony Award for Best Musical">Tony Award for Best Musical</a> of the 2004–05 season. Idle won the <a href="/wiki/Drama_Desk_Award_for_Outstanding_Lyrics" title="Drama Desk Award for Outstanding Lyrics">Drama Desk Award for Outstanding Lyrics</a>.
</p><p>In a 2005 poll to find <i>"The Comedians' Comedian"</i> (UK), he was voted 21 in the top 50 greatest comedy acts ever by fellow comedians and comedy insiders.<sup id="cite_ref-26" class="reference"><a href="#cite_note-26">&#91;26&#93;</a></sup><sup id="cite_ref-27" class="reference"><a href="#cite_note-27">&#91;27&#93;</a></sup>
</p><p>An example of Idle's idiosyncratic writing is "Ants in Their Pants"&#160;– a poem about the sex life of <a href="/wiki/Ant" title="Ant">ants</a>. It starts as follows:
</p>
<dl><dd>'Where does an ant get its rocks off?</dd>
<dd>How does the ant get it on?</dd>
<dd>Do ants have it away, say three times a day,</dd>
<dd>Is it once a week sex, or p'raps none?'</dd></dl>
<h3><span class="mw-headline" id="Songwriting">Songwriting</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Eric_Idle&amp;action=edit&amp;section=8" title="Edit section: Songwriting">edit</a><span class="mw-editsection-bracket">]</span></span></h3>
<p>Idle is an accomplished songwriter, and has about 150 songs to his credit.<sup id="cite_ref-Eggers_2-5" class="reference"><a href="#cite_note-Eggers-2">&#91;2&#93;</a></sup> He composed and performed many of Pythons' most famous comic pieces, including "<a href="/wiki/Eric_the_Half-a-Bee" title="Eric the Half-a-Bee">Eric the Half-a-Bee</a>", "<a href="/wiki/The_Philosophers%27_Song" class="mw-redirect" title="The Philosophers&#39; Song">The Philosophers' Song</a>", "<a href="/wiki/Galaxy_Song" title="Galaxy Song">Galaxy Song</a>", "<a href="/wiki/Penis_Song_(Not_the_Noel_Coward_Song)" class="mw-redirect" title="Penis Song (Not the Noel Coward Song)">Penis Song</a>" and, probably his most recognised hit, "<a href="/wiki/Always_Look_on_the_Bright_Side_of_Life" title="Always Look on the Bright Side of Life">Always Look on the Bright Side of Life</a>", which was written for the closing scene of the Monty Python film <i><a href="/wiki/Life_of_Brian" class="mw-redirect" title="Life of Brian">Life of Brian</a></i>, and sung from the crosses during the mass <a href="/wiki/Crucifixion" title="Crucifixion">crucifixion</a>. The song has since been covered by <a href="/wiki/Harry_Nilsson" title="Harry Nilsson">Harry Nilsson</a>, <a href="/wiki/Bruce_Cockburn" title="Bruce Cockburn">Bruce Cockburn</a>, <a href="/wiki/Art_Garfunkel" title="Art Garfunkel">Art Garfunkel</a> and <a href="/wiki/Green_Day" title="Green Day">Green Day</a>. Idle, his fellow Pythons, and assorted family and friends performed the song at <a href="/wiki/Graham_Chapman" title="Graham Chapman">Graham Chapman</a>'s memorial service. Idle performed the song at the closing ceremony of the London 2012 Olympic Games on 12 August 2012 and as the farewell song of the last show of the <a href="/wiki/Monty_Python_Live_(Mostly)" title="Monty Python Live (Mostly)">Python's reunion at the O2 arena</a>, 20 July 2014.<sup id="cite_ref-28" class="reference"><a href="#cite_note-28">&#91;28&#93;</a></sup>
</p>
<div class="thumb tright"><div class="thumbinner" style="width:222px;"><a href="/wiki/File:Eric_Idle_Carol_Cleveland_Galaxy_Song.jpg" class="image"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/50/Eric_Idle_Carol_Cleveland_Galaxy_Song.jpg/220px-Eric_Idle_Carol_Cleveland_Galaxy_Song.jpg" decoding="async" width="220" height="165" class="thumbimage" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/50/Eric_Idle_Carol_Cleveland_Galaxy_Song.jpg/330px-Eric_Idle_Carol_Cleveland_Galaxy_Song.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/50/Eric_Idle_Carol_Cleveland_Galaxy_Song.jpg/440px-Eric_Idle_Carol_Cleveland_Galaxy_Song.jpg 2x" data-file-width="2592" data-file-height="1944" /></a>  <div class="thumbcaption"><div class="magnify"><a href="/wiki/File:Eric_Idle_Carol_Cleveland_Galaxy_Song.jpg" class="internal" title="Enlarge"></a></div>Idle (left) and <a href="/wiki/Carol_Cleveland" title="Carol Cleveland">Carol Cleveland</a> performing the “<a href="/wiki/Galaxy_Song" title="Galaxy Song">Galaxy Song</a>” (from <i>Monty Python's The Meaning of Life</i>) at <i><a href="/wiki/Monty_Python_Live_(Mostly)" title="Monty Python Live (Mostly)">Monty Python Live (Mostly)</a></i> in 2014</div></div></div>
<p>As Ko-Ko in the 1987 <a href="/wiki/English_National_Opera" title="English National Opera">English National Opera</a> production of <i><a href="/wiki/The_Mikado" title="The Mikado">The Mikado</a></i>, Idle wrote his own 'Little List' on "<a href="https://en.wikisource.org/wiki/The_Mikado/Act_I/Part_Va" class="extiw" title="s:The Mikado/Act I/Part Va">As some day it may happen</a>". In 1989, Idle co-wrote and sang the theme tune to the popular British sitcom <i><a href="/wiki/One_Foot_in_the_Grave" title="One Foot in the Grave">One Foot in the Grave</a></i> and although the series became immensely popular, the song did poorly in the charts. However, when "Always Look on the Bright Side of Life" was adopted as a <a href="/wiki/Association_football" title="Association football">football</a> chant in the late 1980s, Idle's then neighbour <a href="/wiki/Gary_Lineker" title="Gary Lineker">Gary Lineker</a> suggested Idle re-record and release the popular track. With help from <a href="/wiki/BBC_Radio_1" title="BBC Radio 1">Radio 1</a> breakfast show host <a href="/wiki/Simon_Mayo" title="Simon Mayo">Simon Mayo</a>, who gave the song regular airplay and also used the chorus within a jingle, it became a hit, some 12 years after the song's original appearance in <i>Life of Brian</i>, reaching number 3 in the UK charts and landing Idle a set on <i><a href="/wiki/Top_of_the_Pops" title="Top of the Pops">Top of the Pops</a></i> in October 1991.<sup id="cite_ref-29" class="reference"><a href="#cite_note-29">&#91;29&#93;</a></sup> The following month Idle, accompanied by opera singer <a href="/wiki/Ann_Howard_(mezzo-soprano)" title="Ann Howard (mezzo-soprano)">Ann Howard</a>, sang the song at the <a href="/wiki/Royal_Variety_Performance" title="Royal Variety Performance">Royal Variety Performance</a>.<sup id="cite_ref-30" class="reference"><a href="#cite_note-30">&#91;30&#93;</a></sup> He recorded a special version for Mayo's own use on air ("Come on Simon, get another song on now; why don't you put on a nice <a href="/wiki/Cliff_Richard" title="Cliff Richard">Cliff Richard</a> record?") and changed the line "life's a piece of shit" to "life's a piece of spit" in order to get daytime airplay on radio. Idle presented Mayo with a model human foot, akin to the one used in the <i>Monty Python</i> title sequence, as a thank you gift for promoting the song.
</p>
<div class="thumb tleft"><div class="thumbinner" style="width:222px;"><a href="/wiki/File:Monty_Python_Live_02-07-14_11_29_34_(14415367089).jpg" class="image"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Monty_Python_Live_02-07-14_11_29_34_%2814415367089%29.jpg/220px-Monty_Python_Live_02-07-14_11_29_34_%2814415367089%29.jpg" decoding="async" width="220" height="165" class="thumbimage" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Monty_Python_Live_02-07-14_11_29_34_%2814415367089%29.jpg/330px-Monty_Python_Live_02-07-14_11_29_34_%2814415367089%29.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Monty_Python_Live_02-07-14_11_29_34_%2814415367089%29.jpg/440px-Monty_Python_Live_02-07-14_11_29_34_%2814415367089%29.jpg 2x" data-file-width="2592" data-file-height="1944" /></a>  <div class="thumbcaption"><div class="magnify"><a href="/wiki/File:Monty_Python_Live_02-07-14_11_29_34_(14415367089).jpg" class="internal" title="Enlarge"></a></div>Idle performing “<a href="/wiki/Bruces_sketch" title="Bruces sketch">Bruces sketch</a>” in 2014. Involving stereotypical "<a href="/wiki/Ocker" title="Ocker">ocker</a>” Australians, Idle said he based it on his Australian friends from the 1960s "who always seemed to be called Bruce".<sup id="cite_ref-31" class="reference"><a href="#cite_note-31">&#91;31&#93;</a></sup></div></div></div>
<p>In 2004, Idle recorded a <a href="/wiki/Protest_song" title="Protest song">protest song</a> of sorts, the "<a href="/wiki/FCC_Song" title="FCC Song">FCC Song</a>", in which he lambasts the U.S. <a href="/wiki/Federal_Communications_Commission" title="Federal Communications Commission">FCC</a> for fining him $5,000 for saying "fuck" on national radio. The song contains 14 uses of the word. The song can be downloaded in MP3 and <a href="/wiki/OGG_Vorbis" class="mw-redirect" title="OGG Vorbis">OGG Vorbis</a> format at the <a href="/wiki/Internet_Archive" title="Internet Archive">Internet Archive</a>.<sup id="cite_ref-32" class="reference"><a href="#cite_note-32">&#91;32&#93;</a></sup>
</p><p>In 2004, the musical comedy <i><a href="/wiki/Spamalot" title="Spamalot">Spamalot</a></i> debuted in <a href="/wiki/Chicago" title="Chicago">Chicago</a> and opened in New York's <a href="/wiki/Shubert_Theatre_(New_York_City)" title="Shubert Theatre (New York City)">Shubert Theatre</a> on 14 February 2005. Idle wrote the lyrics and book for <i><a href="/wiki/Spamalot" title="Spamalot">Spamalot</a></i>, collaborating with <a href="/wiki/John_Du_Prez" title="John Du Prez">John Du Prez</a> on much of the music. The original 2005 Broadway theatre production was nominated for 14 <a href="/wiki/Tony_Awards" class="mw-redirect" title="Tony Awards">Tony Awards</a> and won three: <a href="/wiki/Tony_Award_for_Best_Musical" title="Tony Award for Best Musical">Best Musical</a>, <a href="/wiki/Tony_Award_for_Best_Featured_Actress_in_a_Musical" title="Tony Award for Best Featured Actress in a Musical">Best Performance by a Featured Actress in a Musical</a> (<a href="/wiki/Sara_Ramirez" title="Sara Ramirez">Sara Ramirez</a>), and <a href="/wiki/Tony_Award_for_Best_Direction_of_a_Musical" title="Tony Award for Best Direction of a Musical">Best Direction of a Musical</a> (<a href="/wiki/Mike_Nichols" title="Mike Nichols">Mike Nichols</a>). In 2006 he wrote, produced and performed the song "Really Nice Day" for the movie <i><a href="/wiki/The_Wild" title="The Wild">The Wild</a></i>.<sup id="cite_ref-33" class="reference"><a href="#cite_note-33">&#91;33&#93;</a></sup>
</p><p>In June 2007, "<a href="/wiki/Not_the_Messiah_(He%27s_a_Very_Naughty_Boy)" title="Not the Messiah (He&#39;s a Very Naughty Boy)">Not the Messiah</a>", a comic <a href="/wiki/Oratorio" title="Oratorio">oratorio</a> by Idle and <a href="/wiki/John_Du_Prez" title="John Du Prez">John Du Prez</a> premiered at the inaugural <a href="/wiki/Luminato" title="Luminato">Luminato</a> arts festival in <a href="/wiki/Toronto" title="Toronto">Toronto</a>. Idle performed live during this 50-minute oratorio, along with the <a href="/wiki/Toronto_Symphony_Orchestra" title="Toronto Symphony Orchestra">Toronto Symphony Orchestra</a> and members of the <a href="/wiki/Toronto_Mendelssohn_Choir" title="Toronto Mendelssohn Choir">Toronto Mendelssohn Choir</a>. The composer, <a href="/wiki/John_Du_Prez" title="John Du Prez">John Du Prez</a>, was also present. Shannon Mercer, Jean Stilwell, <a href="/wiki/Christopher_Sieber" title="Christopher Sieber">Christopher Sieber</a>, and Theodore Baerg sang the principal parts. The American premiere was at Caramoor (<a href="/wiki/Westchester_County,_New_York" title="Westchester County, New York">Westchester County, New York</a>) on 1 July 2007. Soloists were the same as in the Toronto performance, but the accompanying chorus was made up of members of New York City's Collegiate Chorale. The show was revised and expanded for a tour of Australia and New Zealand in 2007, including two sell-out nights at the <a href="/wiki/Sydney_Opera_House" title="Sydney Opera House">Sydney Opera House</a>.<sup id="cite_ref-34" class="reference"><a href="#cite_note-34">&#91;34&#93;</a></sup> A tour during the summer of 2008 included performances with the <a href="/wiki/National_Symphony_Orchestra_(United_States)" class="mw-redirect" title="National Symphony Orchestra (United States)">National Symphony Orchestra</a> at <a href="/wiki/Wolf_Trap_National_Park_for_the_Performing_Arts" title="Wolf Trap National Park for the Performing Arts">Wolf Trap National Park for the Performing Arts</a>, the <a href="/wiki/Los_Angeles_Philharmonic" title="Los Angeles Philharmonic">Los Angeles Philharmonic</a> at the <a href="/wiki/Hollywood_Bowl" title="Hollywood Bowl">Hollywood Bowl</a> in Los Angeles, and the <a href="/wiki/Delaware_Symphony_Orchestra" title="Delaware Symphony Orchestra">Delaware Symphony Orchestra</a> at the <a href="/wiki/Mann_Center_for_the_Performing_Arts" title="Mann Center for the Performing Arts">Mann Center for the Performing Arts</a> in Philadelphia.<sup id="cite_ref-35" class="reference"><a href="#cite_note-35">&#91;35&#93;</a></sup><sup id="cite_ref-36" class="reference"><a href="#cite_note-36">&#91;36&#93;</a></sup><sup id="cite_ref-37" class="reference"><a href="#cite_note-37">&#91;37&#93;</a></sup><sup id="cite_ref-38" class="reference"><a href="#cite_note-38">&#91;38&#93;</a></sup>
</p><p>Idle contributed a cover of <a href="/wiki/Buddy_Holly" title="Buddy Holly">Buddy Holly</a>'s "<a href="/wiki/Raining_in_My_Heart" title="Raining in My Heart">Raining in My Heart</a>" for the tribute album <i><a href="/wiki/Listen_to_Me:_Buddy_Holly" title="Listen to Me: Buddy Holly">Listen to Me: Buddy Holly</a></i>, released 6 September 2011. He also wrote and sang a variant of the galaxy song for <a href="/wiki/Brian_Cox_(physicist)" title="Brian Cox (physicist)">Professor Brian Cox</a>'s show, <i><a href="/wiki/Wonders_of_Life_(TV_series)" title="Wonders of Life (TV series)">Wonders of Life</a></i> as well as the new theme for Cox's radio show <i><a href="/wiki/The_Infinite_Monkey_Cage" title="The Infinite Monkey Cage">The Infinite Monkey Cage</a></i>.<sup id="cite_ref-39" class="reference"><a href="#cite_note-39">&#91;39&#93;</a></sup>
</p>
<h2><span class="mw-headline" id="Personal_life">Personal life</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Eric_Idle&amp;action=edit&amp;section=9" title="Edit section: Personal life">edit</a><span class="mw-editsection-bracket">]</span></span></h2>
<p>Idle has been married twice. His first marriage was in 1969 to actress <a href="/wiki/Lyn_Ashley" title="Lyn Ashley">Lyn Ashley</a>, with whom he had one son, Carey (b. 1973), before their <a href="/wiki/Divorce" title="Divorce">divorce</a> in 1975. He met Tania Kosevich, a former model, in 1977 and they married in 1981.<sup id="cite_ref-40" class="reference"><a href="#cite_note-40">&#91;40&#93;</a></sup> They have one daughter, Lily (b. 1990), and reside in <a href="/wiki/Studio_City,_Los_Angeles" title="Studio City, Los Angeles">Studio City, Los Angeles</a>.<sup id="cite_ref-41" class="reference"><a href="#cite_note-41">&#91;41&#93;</a></sup>
</p><p>He is a first cousin of Canadian conductor <a href="/wiki/Peter_Oundjian" title="Peter Oundjian">Peter Oundjian</a><sup id="cite_ref-42" class="reference"><a href="#cite_note-42">&#91;42&#93;</a></sup><sup id="cite_ref-43" class="reference"><a href="#cite_note-43">&#91;43&#93;</a></sup> and Nigel Wray, former Chairman of <a href="/wiki/Saracens_F.C." title="Saracens F.C.">Saracens</a> Rugby Club.<sup id="cite_ref-44" class="reference"><a href="#cite_note-44">&#91;44&#93;</a></sup>
</p><p>Idle holds <a href="/wiki/Atheism" title="Atheism">atheist</a> views, but does not like using the term.<sup id="cite_ref-45" class="reference"><a href="#cite_note-45">&#91;45&#93;</a></sup>
</p>
<h2><span class="mw-headline" id="Tributes">Tributes</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Eric_Idle&amp;action=edit&amp;section=10" title="Edit section: Tributes">edit</a><span class="mw-editsection-bracket">]</span></span></h2>
<ul><li>An <a href="/wiki/Asteroid" title="Asteroid">asteroid</a>, <a href="/wiki/9620_Ericidle" class="mw-redirect" title="9620 Ericidle">9620 Ericidle</a>, is named in his honour.<sup id="cite_ref-46" class="reference"><a href="#cite_note-46">&#91;46&#93;</a></sup></li>
<li>Idle was voted the 21st favourite comedian out of 50 in The Comedian's Comedian 2005 poll by comedians and comedy insiders.<sup id="cite_ref-47" class="reference"><a href="#cite_note-47">&#91;47&#93;</a></sup></li>
<li>The default <a href="/wiki/Integrated_development_environment" title="Integrated development environment">Integrated development environment (IDE)</a> of the <a href="/wiki/Programming_language" title="Programming language">programming language</a> <a href="/wiki/Python_(programming_language)" title="Python (programming language)">Python</a>, is called <a href="/wiki/IDLE_(Python)" class="mw-redirect" title="IDLE (Python)">IDLE</a>. Although officially IDLE stands for "Integrated DeveLopment Environment", the name has been chosen in allusion to Eric Idle, as the name of the programming language Python itself has been chosen in allusion to Monty Python.<sup id="cite_ref-48" class="reference"><a href="#cite_note-48">&#91;48&#93;</a></sup><sup id="cite_ref-49" class="reference"><a href="#cite_note-49">&#91;49&#93;</a></sup></li>
<li>The <a href="/wiki/Eric_(software)" title="Eric (software)">eric</a> IDE for the programming language Python is named in allusion to the aforementioned IDLE IDE and Eric Idle.</li></ul>
<h2><span class="mw-headline" id="Filmography">Filmography</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Eric_Idle&amp;action=edit&amp;section=11" title="Edit section: Filmography">edit</a><span class="mw-editsection-bracket">]</span></span></h2>
<h3><span class="mw-headline" id="Film">Film</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Eric_Idle&amp;action=edit&amp;section=12" title="Edit section: Film">edit</a><span class="mw-editsection-bracket">]</span></span></h3>
<table class="wikitable">

<tbody><tr style="background:#b0c4de; text-align:center;">
<th>Year
</th>
<th>Title
</th>
<th>Role
</th>
<th>Notes
</th></tr>
<tr>
<td>1971
</td>
<td><i><a href="/wiki/And_Now_for_Something_Completely_Different" title="And Now for Something Completely Different">And Now for Something Completely Different</a></i>
</td>
<td rowspan="5">Various roles
</td>
<td rowspan="3">Also writer
</td></tr>
<tr>
<td>1975
</td>
<td><i><a href="/wiki/Monty_Python_and_the_Holy_Grail" title="Monty Python and the Holy Grail">Monty Python and the Holy Grail</a></i>
</td></tr>
<tr>
<td>1979
</td>
<td><i><a href="/wiki/Monty_Python%27s_Life_of_Brian" title="Monty Python&#39;s Life of Brian">Monty Python's Life of Brian</a></i>
</td></tr>
<tr>
<td>1982
</td>
<td><i><a href="/wiki/Monty_Python_Live_at_the_Hollywood_Bowl" title="Monty Python Live at the Hollywood Bowl">Monty Python Live at the Hollywood Bowl</a></i>
</td>
<td>Concert film; also writer
</td></tr>
<tr>
<td rowspan="2">1983
</td>
<td><i><a href="/wiki/Monty_Python%27s_The_Meaning_of_Life" title="Monty Python&#39;s The Meaning of Life">Monty Python's The Meaning of Life</a></i>
</td>
<td>Also writer
</td></tr>
<tr>
<td><i><a href="/wiki/Yellowbeard" title="Yellowbeard">Yellowbeard</a></i>
</td>
<td>Commander Clement
</td>
<td>
</td></tr>
<tr>
<td>1985
</td>
<td><i><a href="/wiki/National_Lampoon%27s_European_Vacation" title="National Lampoon&#39;s European Vacation">National Lampoon's European Vacation</a></i>
</td>
<td>The Bike Rider
</td>
<td>
</td></tr>
<tr>
<td>1986
</td>
<td><i><a href="/wiki/The_Transformers:_The_Movie" title="The Transformers: The Movie">The Transformers: The Movie</a></i>
</td>
<td>Wreck-Gar (voice)
</td>
<td>
</td></tr>
<tr>
<td>1988
</td>
<td><i><a href="/wiki/The_Adventures_of_Baron_Munchausen" title="The Adventures of Baron Munchausen">The Adventures of Baron Munchausen</a></i>
</td>
<td>Berthold / Desmond
</td>
<td>
</td></tr>
<tr>
<td rowspan="2">1990
</td>
<td><i><a href="/wiki/Nuns_on_the_Run" title="Nuns on the Run">Nuns on the Run</a></i>
</td>
<td>Brian Hope
</td>
<td>
</td></tr>
<tr>
<td><i><a href="/wiki/Too_Much_Sun" title="Too Much Sun">Too Much Sun</a></i>
</td>
<td>Sonny
</td>
<td>
</td></tr>
<tr>
<td rowspan="2">1992
</td>
<td><i><a href="/wiki/Mom_and_Dad_Save_the_World" title="Mom and Dad Save the World">Mom and Dad Save the World</a></i>
</td>
<td>King Raff
</td>
<td>
</td></tr>
<tr>
<td><i><a href="/wiki/Missing_Pieces_(1992_film)" title="Missing Pieces (1992 film)">Missing Pieces</a></i>
</td>
<td>Wendel
</td>
<td>
</td></tr>
<tr>
<td>1993
</td>
<td><i><a href="/wiki/Splitting_Heirs" title="Splitting Heirs">Splitting Heirs</a></i>
</td>
<td>Tommy Butterfly Rainbow Peace Patel
</td>
<td>Also writer and executive producer
</td></tr>
<tr>
<td>1994
</td>
<td><i><a href="/wiki/Honey,_I_Shrunk_the_Audience!" title="Honey, I Shrunk the Audience!">Honey, I Shrunk the Audience!</a></i>
</td>
<td>Dr. Nigel Channing
</td>
<td>Short film
</td></tr>
<tr>
<td>1995
</td>
<td><i><a href="/wiki/Casper_(film)" title="Casper (film)">Casper</a></i>
</td>
<td>Paul "Dibs" Plutzker
</td>
<td>
</td></tr>
<tr>
<td>1996
</td>
<td><i><a href="/wiki/The_Wind_in_the_Willows_(1996_film)" title="The Wind in the Willows (1996 film)">The Wind in the Willows</a></i>
</td>
<td>Mr. Rat
</td>
<td>
</td></tr>
<tr>
<td>1997
</td>
<td><i><a href="/wiki/Pirates_4-D" title="Pirates 4-D">Pirates 4-D</a></i>
</td>
<td>Pierre
</td>
<td>Short film; also writer
</td></tr>
<tr>
<td rowspan="4">1998
</td>
<td><i><a href="/wiki/An_Alan_Smithee_Film:_Burn_Hollywood_Burn" title="An Alan Smithee Film: Burn Hollywood Burn">An Alan Smithee Film: Burn Hollywood Burn</a></i>
</td>
<td><a href="/wiki/Alan_Smithee" title="Alan Smithee">Alan Smithee</a>
</td>
<td>
</td></tr>
<tr>
<td><i><a href="/wiki/The_Secret_of_NIMH_2:_Timmy_to_the_Rescue" title="The Secret of NIMH 2: Timmy to the Rescue">The Secret of NIMH 2: Timmy to the Rescue</a></i>
</td>
<td>Evil Martin (voice)
</td>
<td>Direct-to-video
</td></tr>
<tr>
<td><i><a href="/wiki/Quest_for_Camelot" title="Quest for Camelot">Quest for Camelot</a></i>
</td>
<td>Devon (voice)
</td>
<td>
</td></tr>
<tr>
<td><i><a href="/wiki/Rudolph_the_Red-Nosed_Reindeer:_The_Movie" title="Rudolph the Red-Nosed Reindeer: The Movie">Rudolph the Red-Nosed Reindeer: The Movie</a></i>
</td>
<td>Slyly (voice)
</td>
<td>
</td></tr>
<tr>
<td rowspan="2">1999
</td>
<td><i><a href="/wiki/Dudley_Do-Right_(film)" title="Dudley Do-Right (film)">Dudley Do-Right</a></i>
</td>
<td>Prospector Kim J. Darling
</td>
<td>
</td></tr>
<tr>
<td><i><a href="/wiki/South_Park:_Bigger,_Longer_%26_Uncut" title="South Park: Bigger, Longer &amp; Uncut">South Park: Bigger, Longer &amp; Uncut</a></i>
</td>
<td>Dr. Vosnocker (voice)
</td>
<td>
</td></tr>
<tr>
<td>2000
</td>
<td><i><a href="/wiki/102_Dalmatians" title="102 Dalmatians">102 Dalmatians</a></i>
</td>
<td>Waddlesworth (voice)
</td>
<td>
</td></tr>
<tr>
<td>2002
</td>
<td><i><a href="/wiki/Pinocchio_(2002_film)" title="Pinocchio (2002 film)">Pinocchio</a></i>
</td>
<td>Medoro
</td>
<td>English dub
</td></tr>
<tr>
<td rowspan="2">2003
</td>
<td><i><a href="/wiki/Concert_for_George_(film)" title="Concert for George (film)">Concert for George</a></i>
</td>
<td>Himself / Barber / Mountie
</td>
<td>Documentary
</td></tr>
<tr>
<td><i><a href="/wiki/Hollywood_Homicide" title="Hollywood Homicide">Hollywood Homicide</a></i>
</td>
<td>The Celebrity
</td>
<td>Cameo
</td></tr>
<tr>
<td>2004
</td>
<td><i><a href="/wiki/Ella_Enchanted_(film)" title="Ella Enchanted (film)">Ella Enchanted</a></i>
</td>
<td>Narrator (voice)
</td>
<td>
</td></tr>
<tr>
<td>2005
</td>
<td><i><a href="/wiki/The_Aristocrats_(film)" title="The Aristocrats (film)">The Aristocrats</a></i>
</td>
<td>Himself
</td>
<td>Documentary
</td></tr>
<tr>
<td>2006
</td>
<td><i><a href="/wiki/The_Wild" title="The Wild">The Wild</a></i>
</td>
<td>
</td>
<td>Composer/performer: "Really Nice Day"
</td></tr>
<tr>
<td>2007
</td>
<td><i><a href="/wiki/Shrek_the_Third" title="Shrek the Third">Shrek the Third</a></i>
</td>
<td><a href="/wiki/Merlin" title="Merlin">Merlin</a> (voice)
</td>
<td>
</td></tr>
<tr>
<td>2008
</td>
<td><i><a href="/wiki/Delgo" title="Delgo">Delgo</a></i>
</td>
<td>Spig (voice)
</td>
<td>
</td></tr>
<tr>
<td rowspan="2">2014
</td>
<td><i><a href="/wiki/Monty_Python_Live_(Mostly)" title="Monty Python Live (Mostly)">Monty Python Live (Mostly)</a></i>
</td>
<td>Various roles
</td>
<td>Concert film; also writer and director<sup id="cite_ref-50" class="reference"><a href="#cite_note-50">&#91;50&#93;</a></sup>
</td></tr>
<tr>
<td><i><a href="/wiki/The_Boxtrolls" title="The Boxtrolls">The Boxtrolls</a></i>
</td>
<td>
</td>
<td>Composer: "The Boxtrolls Song"
</td></tr>
<tr>
<td>2015
</td>
<td><i><a href="/wiki/Absolutely_Anything" title="Absolutely Anything">Absolutely Anything</a></i>
</td>
<td>Salubrious Gat (voice)
</td>
<td>
</td></tr></tbody></table>
<h3><span class="mw-headline" id="Television">Television</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Eric_Idle&amp;action=edit&amp;section=13" title="Edit section: Television">edit</a><span class="mw-editsection-bracket">]</span></span></h3>
<table class="wikitable">

<tbody><tr style="background:#b0c4de; text-align:center;">
<th>Year
</th>
<th>Title
</th>
<th>Role
</th>
<th>Notes
</th></tr>
<tr>
<td>1967–1970
</td>
<td><i><a href="/wiki/No_%E2%80%93_That%27s_Me_Over_Here!" title="No – That&#39;s Me Over Here!">No&#160;– That's Me Over Here!</a></i>
</td>
<td>
</td>
<td>Co-creator and writer
</td></tr>
<tr>
<td>1967–1969
</td>
<td><i><a href="/wiki/Do_Not_Adjust_Your_Set" title="Do Not Adjust Your Set">Do Not Adjust Your Set</a></i>
</td>
<td rowspan="3">Various roles
</td>
<td>27 episodes; also writer
</td></tr>
<tr>
<td>1969–1974
</td>
<td><i><a href="/wiki/Monty_Python%27s_Flying_Circus" title="Monty Python&#39;s Flying Circus">Monty Python's Flying Circus</a></i>
</td>
<td>45 episodes; also co-creator and writer
</td></tr>
<tr>
<td>1972
</td>
<td><i><a href="/wiki/Monty_Python%27s_Fliegender_Zirkus" title="Monty Python&#39;s Fliegender Zirkus">Monty Python's Fliegender Zirkus</a></i>
</td>
<td>2 episodes; also co-creator and writer
</td></tr>
<tr>
<td>1975–1976
</td>
<td><i><a href="/wiki/Rutland_Weekend_Television" title="Rutland Weekend Television">Rutland Weekend Television</a></i>
</td>
<td>Dirk McQuickly / Various roles
</td>
<td>14 episodes; also co-creator and writer
</td></tr>
<tr>
<td>1976–1979
</td>
<td><i><a href="/wiki/Saturday_Night_Live" title="Saturday Night Live">Saturday Night Live</a></i>
</td>
<td>Himself
</td>
<td>6 Episodes
</td></tr>
<tr>
<td>1978
</td>
<td><i><a href="/wiki/All_You_Need_Is_Cash" title="All You Need Is Cash">All You Need Is Cash</a></i>
</td>
<td>Dirk McQuickly
</td>
<td>Television film; also writer and director
</td></tr>
<tr>
<td>1981
</td>
<td><i><a href="/wiki/Laverne_%26_Shirley" title="Laverne &amp; Shirley">Laverne &amp; Shirley</a></i>
</td>
<td>Derek DeWoods
</td>
<td>Episode: "I Do, I Do"
</td></tr>
<tr>
<td>1982
</td>
<td><i><a href="/wiki/Faerie_Tale_Theatre" title="Faerie Tale Theatre">Faerie Tale Theatre</a></i>
</td>
<td>Narrator
</td>
<td>Episode: "The Tale of the Frog Prince" <br />also director and writer
</td></tr>
<tr>
<td>1985
</td>
<td><i><a href="/wiki/Faerie_Tale_Theatre" title="Faerie Tale Theatre">Faerie Tale Theatre</a></i>
</td>
<td><a href="/wiki/The_Pied_Piper" class="mw-redirect" title="The Pied Piper">The Pied Piper</a>
</td>
<td>Episode: "The Pied Piper of Hamelin"
</td></tr>
<tr>
<td rowspan="2">1989
</td>
<td><i><a href="/wiki/Around_the_World_in_80_Days_(TV_miniseries)" class="mw-redirect" title="Around the World in 80 Days (TV miniseries)">Around the World in 80 Days</a></i>
</td>
<td>Jean Passepartout
</td>
<td>3 episodes
</td></tr>
<tr>
<td><i><a href="/wiki/Nearly_Departed" title="Nearly Departed">Nearly Departed</a></i>
</td>
<td>Grant Pritchard
</td>
<td>6 episodes
</td></tr>
<tr>
<td>1991
</td>
<td><i><a href="/wiki/One_Foot_in_the_Grave" title="One Foot in the Grave">One Foot in the Grave</a></i>
</td>
<td>Mervyn Whale
</td>
<td>Episode: "The Man in the Long Black Coat"
</td></tr>
<tr>
<td>1996
</td>
<td><i><a href="/wiki/Frasier" title="Frasier">Frasier</a></i>
</td>
<td>Chuck (voice)
</td>
<td>Episode: "High Crane Drifter"
</td></tr>
<tr>
<td>1998
</td>
<td><i><a href="/wiki/Pinky_and_the_Brain" title="Pinky and the Brain">Pinky and the Brain</a></i>
</td>
<td>Pinky's Mom and Dad (voice)
</td>
<td>Episode: "The Family That Poits Together, <br /> Narfs Together"
</td></tr>
<tr>
<td rowspan="2">1998–1999
</td>
<td><i><a href="/wiki/Hercules_(1998_TV_series)" title="Hercules (1998 TV series)">Hercules</a></i>
</td>
<td>Mr. Parentheses (voice)
</td>
<td>11 episodes
</td></tr>
<tr>
<td><i><a href="/wiki/Recess_(TV_series)" title="Recess (TV series)">Recess</a></i>
</td>
<td>Galileo (voice)
</td>
<td>2 episodes
</td></tr>
<tr>
<td>1998
</td>
<td><i><a href="/wiki/The_Angry_Beavers" title="The Angry Beavers">The Angry Beavers</a></i>
</td>
<td>Spanque (voice)
</td>
<td>Episode: "Open Wide for Zombies/Dumbwaiters"
</td></tr>
<tr>
<td>1999–2000
</td>
<td><i><a href="/wiki/Suddenly_Susan" title="Suddenly Susan">Suddenly Susan</a></i>
</td>
<td>Ian Maxtone-Graham
</td>
<td>22 episodes
</td></tr>
<tr>
<td>2000
</td>
<td><i><a href="/wiki/Buzz_Lightyear_of_Star_Command" title="Buzz Lightyear of Star Command">Buzz Lightyear of Star Command</a></i>
</td>
<td>Guzelian (voice)
</td>
<td>Episode: "War and Peace and War"
</td></tr>
<tr>
<td>2001–2002
</td>
<td><i><a href="/wiki/House_of_Mouse" title="House of Mouse">House of Mouse</a></i>
</td>
<td>Pluto Angel (voice)
</td>
<td>2 episodes
</td></tr>
<tr>
<td rowspan="3">2002
</td>
<td><i><a href="/wiki/MADtv" class="mw-redirect" title="MADtv">MADtv</a></i>
</td>
<td>Zookeeper
</td>
<td>Episode: "#8.18"
</td></tr>
<tr>
<td><i><a href="/wiki/The_Rutles_2:_Can%27t_Buy_Me_Lunch" title="The Rutles 2: Can&#39;t Buy Me Lunch">The Rutles 2: Can't Buy Me Lunch</a></i>
</td>
<td>Narrator / Various
</td>
<td>Television film; also writer, director and producer
</td></tr>
<tr>
<td><i><a href="/wiki/The_Scream_Team" title="The Scream Team">The Scream Team</a></i>
</td>
<td>Coffin Ed
</td>
<td>Television film
</td></tr>
<tr>
<td>2003–2012
</td>
<td><i><a href="/wiki/The_Simpsons" title="The Simpsons">The Simpsons</a></i>
</td>
<td>Declan Desmond (voice)
</td>
<td>4 episodes
</td></tr>
<tr>
<td>2003
</td>
<td><i><a href="/wiki/National_Lampoon%27s_Christmas_Vacation_2" title="National Lampoon&#39;s Christmas Vacation 2">National Lampoon's Christmas Vacation 2</a></i>
</td>
<td>Plane passenger
</td>
<td>Television film
</td></tr>
<tr>
<td>2004–2005
</td>
<td><i><a href="/wiki/Super_Robot_Monkey_Team_Hyperforce_Go!" title="Super Robot Monkey Team Hyperforce Go!">Super Robot Monkey Team Hyperforce Go!</a></i>
</td>
<td>Scrapperton (voice)
</td>
<td>3 episodes
</td></tr>
<tr>
<td>2016
</td>
<td><i>The Entire Universe</i>
</td>
<td>Himself (host)
</td>
<td>Television special; also writer
</td></tr>
</tbody></table>
<h3><span class="mw-headline" id="Video_games">Video games</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Eric_Idle&amp;action=edit&amp;section=14" title="Edit section: Video games">edit</a><span class="mw-editsection-bracket">]</span></span></h3>
<table class="wikitable">

<tbody><tr style="background:#b0c4de; text-align:center;">
<th>Year
</th>
<th>Title
</th>
<th>Role
</th>
<th>Notes
</th></tr>
<tr>
<td>1995
</td>
<td><i><a href="/wiki/Discworld_(video_game)" title="Discworld (video game)">Discworld</a></i>
</td>
<td rowspan="2"><a href="/wiki/Rincewind" title="Rincewind">Rincewind</a>
</td>
<td rowspan="2">Voice
</td></tr>
<tr>
<td rowspan="2">1996
</td>
<td><i><a href="/wiki/Discworld_II:_Missing_Presumed...!%3F" title="Discworld II: Missing Presumed...!?">Discworld II: Missing Presumed...!?</a></i>
</td></tr>
<tr>
<td><i><a href="/wiki/Monty_Python_%26_the_Quest_for_the_Holy_Grail" title="Monty Python &amp; the Quest for the Holy Grail">Monty Python &amp; the Quest for the Holy Grail</a></i>
</td>
<td rowspan="2">Various roles
</td>
<td>Voice<br />Also producer and writer
</td></tr>
<tr>
<td>1997
</td>
<td><i><a href="/wiki/Monty_Python%27s_The_Meaning_of_Life_(video_game)" title="Monty Python&#39;s The Meaning of Life (video game)">Monty Python's The Meaning of Life</a></i>
</td>
<td>Voice
</td></tr></tbody></table>
<h3><span class="mw-headline" id="Stage">Stage</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Eric_Idle&amp;action=edit&amp;section=15" title="Edit section: Stage">edit</a><span class="mw-editsection-bracket">]</span></span></h3>
<table class="wikitable">

<tbody><tr style="background:#b0c4de; text-align:center;">
<th>Year
</th>
<th>Title
</th>
<th>Role
</th>
<th>Notes
</th></tr>
<tr>
<td>2000
</td>
<td><i><a href="/wiki/Seussical" title="Seussical">Seussical</a></i>
</td>
<td>
</td>
<td>Co-conceiver
</td></tr>
<tr>
<td>2004
</td>
<td><i><a href="/wiki/Spamalot" title="Spamalot">Spamalot</a></i>
</td>
<td>
</td>
<td>Writer and co-lyricist<br /><a href="/wiki/Tony_Award_for_Best_Musical" title="Tony Award for Best Musical">Tony Award for Best Musical</a><br /><a href="/wiki/Drama_Desk_Award_for_Outstanding_Lyrics" title="Drama Desk Award for Outstanding Lyrics">Drama Desk Award for Outstanding Lyrics</a><br /><a href="/wiki/Grammy_Award_for_Best_Musical_Theater_Album" title="Grammy Award for Best Musical Theater Album">Grammy Award for Best Musical Theater Album</a><br />Nominated—<a href="/wiki/Tony_Award_for_Best_Book_of_a_Musical" title="Tony Award for Best Book of a Musical">Tony Award for Best Book of a Musical</a><br />Nominated—<a href="/wiki/Tony_Award_for_Best_Original_Score" title="Tony Award for Best Original Score">Tony Award for Best Original Score</a><br />Nominated—<a href="/wiki/Drama_Desk_Award_for_Outstanding_Book_of_a_Musical" title="Drama Desk Award for Outstanding Book of a Musical">Drama Desk Award for Outstanding Book of a Musical</a>
</td></tr>
<tr>
<td>2007
</td>
<td><i><a href="/wiki/Not_the_Messiah_(He%27s_a_Very_Naughty_Boy)" title="Not the Messiah (He&#39;s a Very Naughty Boy)">Not the Messiah</a></i>
</td>
<td>Various roles
</td>
<td>Also writer
</td></tr>
<tr>
<td>2009
</td>
<td><i>An Evening Without Monty Python</i>
</td>
<td>
</td>
<td>Director
</td></tr>
<tr>
<td>2012
</td>
<td><i>What About Dick?</i>
</td>
<td>Piano
</td>
<td>Also writer and co-director
</td></tr>
<tr>
<td>2014
</td>
<td><i><a href="/wiki/Monty_Python_Live_(Mostly)" title="Monty Python Live (Mostly)">Monty Python Live</a></i>
</td>
<td>Various roles
</td>
<td>Also co-writer and director
</td></tr></tbody></table>
<h3><span class="mw-headline" id="Bibliography">Bibliography</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Eric_Idle&amp;action=edit&amp;section=16" title="Edit section: Bibliography">edit</a><span class="mw-editsection-bracket">]</span></span></h3>
<ul><li><i><a href="/wiki/Hello_Sailor_(novel)" title="Hello Sailor (novel)">Hello Sailor</a></i>, novel, 1975, <a href="/wiki/Weidenfeld_%26_Nicolson" title="Weidenfeld &amp; Nicolson">Weidenfeld &amp; Nicolson</a>, <style data-mw-deduplicate="TemplateStyles:r951705291">.mw-parser-output cite.citation{font-style:inherit}.mw-parser-output .citation q{quotes:"\"""\"""'""'"}.mw-parser-output .id-lock-free a,.mw-parser-output .citation .cs1-lock-free a{background-image:url("//upload.wikimedia.org/wikipedia/commons/thumb/6/65/Lock-green.svg/9px-Lock-green.svg.png");background-image:linear-gradient(transparent,transparent),url("//upload.wikimedia.org/wikipedia/commons/6/65/Lock-green.svg");background-repeat:no-repeat;background-size:9px;background-position:right .1em center}.mw-parser-output .id-lock-limited a,.mw-parser-output .id-lock-registration a,.mw-parser-output .citation .cs1-lock-limited a,.mw-parser-output .citation .cs1-lock-registration a{background-image:url("//upload.wikimedia.org/wikipedia/commons/thumb/d/d6/Lock-gray-alt-2.svg/9px-Lock-gray-alt-2.svg.png");background-image:linear-gradient(transparent,transparent),url("//upload.wikimedia.org/wikipedia/commons/d/d6/Lock-gray-alt-2.svg");background-repeat:no-repeat;background-size:9px;background-position:right .1em center}.mw-parser-output .id-lock-subscription a,.mw-parser-output .citation .cs1-lock-subscription a{background-image:url("//upload.wikimedia.org/wikipedia/commons/thumb/a/aa/Lock-red-alt-2.svg/9px-Lock-red-alt-2.svg.png");background-image:linear-gradient(transparent,transparent),url("//upload.wikimedia.org/wikipedia/commons/a/aa/Lock-red-alt-2.svg");background-repeat:no-repeat;background-size:9px;background-position:right .1em center}.mw-parser-output .cs1-subscription,.mw-parser-output .cs1-registration{color:#555}.mw-parser-output .cs1-subscription span,.mw-parser-output .cs1-registration span{border-bottom:1px dotted;cursor:help}.mw-parser-output .cs1-ws-icon a{background-image:url("//upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Wikisource-logo.svg/12px-Wikisource-logo.svg.png");background-image:linear-gradient(transparent,transparent),url("//upload.wikimedia.org/wikipedia/commons/4/4c/Wikisource-logo.svg");background-repeat:no-repeat;background-size:12px;background-position:right .1em center}.mw-parser-output code.cs1-code{color:inherit;background:inherit;border:inherit;padding:inherit}.mw-parser-output .cs1-hidden-error{display:none;font-size:100%}.mw-parser-output .cs1-visible-error{font-size:100%}.mw-parser-output .cs1-maint{display:none;color:#33aa33;margin-left:0.3em}.mw-parser-output .cs1-subscription,.mw-parser-output .cs1-registration,.mw-parser-output .cs1-format{font-size:95%}.mw-parser-output .cs1-kern-left,.mw-parser-output .cs1-kern-wl-left{padding-left:0.2em}.mw-parser-output .cs1-kern-right,.mw-parser-output .cs1-kern-wl-right{padding-right:0.2em}.mw-parser-output .citation .mw-selflink{font-weight:inherit}</style><a href="/wiki/ISBN_(identifier)" class="mw-redirect" title="ISBN (identifier)">ISBN</a>&#160;<a href="/wiki/Special:BookSources/0-297-76929-4" title="Special:BookSources/0-297-76929-4">0-297-76929-4</a></li>
<li><i>The Rutland Dirty Weekend Book</i>, 1976, <a href="/wiki/Random_House" title="Random House">Mandarin</a> <link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r951705291"/><a href="/wiki/ISBN_(identifier)" class="mw-redirect" title="ISBN (identifier)">ISBN</a>&#160;<a href="/wiki/Special:BookSources/0-413-36570-0" title="Special:BookSources/0-413-36570-0">0-413-36570-0</a></li>
<li><i>Pass the Butler</i>, play script, 1982, <link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r951705291"/><a href="/wiki/ISBN_(identifier)" class="mw-redirect" title="ISBN (identifier)">ISBN</a>&#160;<a href="/wiki/Special:BookSources/0-413-49990-1" title="Special:BookSources/0-413-49990-1">0-413-49990-1</a></li>
<li><i>The Quite Remarkable Adventures of the Owl and the Pussycat</i>, children's book, 1996, Dove Books, <link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r951705291"/><a href="/wiki/ISBN_(identifier)" class="mw-redirect" title="ISBN (identifier)">ISBN</a>&#160;<a href="/wiki/Special:BookSources/0-7871-1042-6" title="Special:BookSources/0-7871-1042-6">0-7871-1042-6</a></li>
<li><i><a href="/wiki/The_Road_to_Mars" title="The Road to Mars">The Road to Mars</a></i>, novel, 1998, <link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r951705291"/><a href="/wiki/ISBN_(identifier)" class="mw-redirect" title="ISBN (identifier)">ISBN</a>&#160;<a href="/wiki/Special:BookSources/0-7522-2414-X" title="Special:BookSources/0-7522-2414-X">0-7522-2414-X</a>, <a href="/wiki/Macmillan_Publishers" title="Macmillan Publishers">Boxtree</a>, (hardcover), <link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r951705291"/><a href="/wiki/ISBN_(identifier)" class="mw-redirect" title="ISBN (identifier)">ISBN</a>&#160;<a href="/wiki/Special:BookSources/0-375-70312-8" title="Special:BookSources/0-375-70312-8">0-375-70312-8</a> (paperback)</li>
<li><i>Eric Idle Exploits Monty Python Souvenir Program</i>, Green Street Press (U.S.), 2000</li>
<li><i>The Greedy Bastard Tour Souvenir Program</i>, Green Street Press (U.S.), 2003</li>
<li><i>The Greedy Bastard Diary: A Comic Tour of America</i>, journal, 2005, <link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r951705291"/><a href="/wiki/ISBN_(identifier)" class="mw-redirect" title="ISBN (identifier)">ISBN</a>&#160;<a href="/wiki/Special:BookSources/0-06-075864-3" title="Special:BookSources/0-06-075864-3">0-06-075864-3</a></li>
<li><i>The Writer's Cut</i>, e-Book, 2015, <link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r951705291"/><a href="/wiki/ISBN_(identifier)" class="mw-redirect" title="ISBN (identifier)">ISBN</a>&#160;<a href="/wiki/Special:BookSources/9781910859247" title="Special:BookSources/9781910859247">9781910859247</a></li>
<li><i>Always Look on the Bright Side of Life: A Sortabiography</i>, memoir, 2018, <link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r951705291"/><a href="/wiki/ISBN_(identifier)" class="mw-redirect" title="ISBN (identifier)">ISBN</a>&#160;<a href="/wiki/Special:BookSources/9781984822581" title="Special:BookSources/9781984822581">9781984822581</a></li></ul>
<h2><span class="mw-headline" id="References">References</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Eric_Idle&amp;action=edit&amp;section=17" title="Edit section: References">edit</a><span class="mw-editsection-bracket">]</span></span></h2>
<div class="reflist columns references-column-width" style="-moz-column-width: 30em; -webkit-column-width: 30em; column-width: 30em; list-style-type: decimal;">
<ol class="references">
<li id="cite_note-1"><span class="mw-cite-backlink"><b><a href="#cite_ref-1">^</a></b></span> <span class="reference-text"><cite class="citation web cs1"><a rel="nofollow" class="external text" href="https://www.ukwhoswho.com/view/10.1093/ww/9780199540884.001.0001/ww-9780199540884-e-21409">"Who's Who"</a>. <i>www.ukwhoswho.com</i><span class="reference-accessdate">. Retrieved <span class="nowrap">30 August</span> 2019</span>.</cite><span title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=unknown&amp;rft.jtitle=www.ukwhoswho.com&amp;rft.atitle=Who%27s+Who&amp;rft_id=https%3A%2F%2Fwww.ukwhoswho.com%2Fview%2F10.1093%2Fww%2F9780199540884.001.0001%2Fww-9780199540884-e-21409&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AEric+Idle" class="Z3988"></span><link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r951705291"/></span>
</li>
<li id="cite_note-Eggers-2"><span class="mw-cite-backlink">^ <a href="#cite_ref-Eggers_2-0"><sup><i><b>a</b></i></sup></a> <a href="#cite_ref-Eggers_2-1"><sup><i><b>b</b></i></sup></a> <a href="#cite_ref-Eggers_2-2"><sup><i><b>c</b></i></sup></a> <a href="#cite_ref-Eggers_2-3"><sup><i><b>d</b></i></sup></a> <a href="#cite_ref-Eggers_2-4"><sup><i><b>e</b></i></sup></a> <a href="#cite_ref-Eggers_2-5"><sup><i><b>f</b></i></sup></a></span> <span class="reference-text"><cite class="citation news cs1"><a rel="nofollow" class="external text" href="https://www.theguardian.com/stage/2006/sep/13/theatre">"And now for something completely difficult ..."</a> <i>The Guardian</i><span class="reference-accessdate">. Retrieved <span class="nowrap">21 August</span> 2019</span>.</cite><span title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=article&amp;rft.jtitle=The+Guardian&amp;rft.atitle=And+now+for+something+completely+difficult+...&amp;rft_id=https%3A%2F%2Fwww.theguardian.com%2Fstage%2F2006%2Fsep%2F13%2Ftheatre&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AEric+Idle" class="Z3988"></span><link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r951705291"/></span>
</li>
<li id="cite_note-3"><span class="mw-cite-backlink"><b><a href="#cite_ref-3">^</a></b></span> <span class="reference-text">Eric Idle, [Email letter to] "The Pythons," 20 December 2006. Reprinted in Roy Thompson Hall Performance Program Insert, Summer 2007. p. 6.</span>
</li>
<li id="cite_note-4"><span class="mw-cite-backlink"><b><a href="#cite_ref-4">^</a></b></span> <span class="reference-text"><cite class="citation web cs1"><a rel="nofollow" class="external text" href="http://www.aljazeera.com/news/europe/2012/08/201281305330562117.html">"London ends Olympics on extravagant notes – Europe"</a>. <i>Al Jazeera English</i>. 12 August 2012<span class="reference-accessdate">. Retrieved <span class="nowrap">20 August</span> 2019</span>.</cite><span title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=unknown&amp;rft.jtitle=Al+Jazeera+English&amp;rft.atitle=London+ends+Olympics+on+extravagant+notes+%E2%80%93+Europe&amp;rft.date=2012-08-12&amp;rft_id=http%3A%2F%2Fwww.aljazeera.com%2Fnews%2Feurope%2F2012%2F08%2F201281305330562117.html&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AEric+Idle" class="Z3988"></span><link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r951705291"/></span>
</li>
<li id="cite_note-5"><span class="mw-cite-backlink"><b><a href="#cite_ref-5">^</a></b></span> <span class="reference-text"><cite class="citation web cs1"><a rel="nofollow" class="external text" href="https://archive.today/20141018115144/http://www.southtyneside.info/applications/2/registersearch/resultlist.aspx">"Search Register Office records&#160;– South Tyneside Council"</a>. <i>South Tyneside Birth death and Marriages</i>. Archived from <a rel="nofollow" class="external text" href="http://www.southtyneside.info/applications/2/registersearch/resultlist.aspx">the original</a> on 18 October 2014.</cite><span title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=unknown&amp;rft.jtitle=South+Tyneside+Birth+death+and+Marriages&amp;rft.atitle=Search+Register+Office+records+%E2%80%93+South+Tyneside+Council&amp;rft_id=http%3A%2F%2Fwww.southtyneside.info%2Fapplications%2F2%2Fregistersearch%2Fresultlist.aspx&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AEric+Idle" class="Z3988"></span><link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r951705291"/></span>
</li>
<li id="cite_note-Tel170207-6"><span class="mw-cite-backlink"><b><a href="#cite_ref-Tel170207_6-0">^</a></b></span> <span class="reference-text">Barratt, Nick; <a rel="nofollow" class="external text" href="https://www.telegraph.co.uk/news/features/3631569/Family-detective.html">"Family detective"</a> <i><a href="/wiki/The_Daily_Telegraph" title="The Daily Telegraph">The Daily Telegraph</a></i>, 17 February 2007 (Retrieved: 19 August 2009)</span>
</li>
<li id="cite_note-7"><span class="mw-cite-backlink"><b><a href="#cite_ref-7">^</a></b></span> <span class="reference-text"><a rel="nofollow" class="external text" href="http://www.filmreference.com/film/25/Eric-Idle.html">Eric Idle Biography (1943–)</a>, Theatre, Film, and Television Biographies</span>
</li>
<li id="cite_note-8"><span class="mw-cite-backlink"><b><a href="#cite_ref-8">^</a></b></span> <span class="reference-text"><cite class="citation web cs1"><a rel="nofollow" class="external text" href="http://www.cwgc.org/find-war-dead/casualty/2414186">"Casualty Details"</a>. CWGC. 24 December 1945<span class="reference-accessdate">. Retrieved <span class="nowrap">1 June</span> 2011</span>.</cite><span title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook&amp;rft.genre=unknown&amp;rft.btitle=Casualty+Details&amp;rft.pub=CWGC&amp;rft.date=1945-12-24&amp;rft_id=http%3A%2F%2Fwww.cwgc.org%2Ffind-war-dead%2Fcasualty%2F2414186&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AEric+Idle" class="Z3988"></span><link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r951705291"/></span>
</li>
<li id="cite_note-9"><span class="mw-cite-backlink"><b><a href="#cite_ref-9">^</a></b></span> <span class="reference-text">see also p. 4 of Idles autobiography.</span>
</li>
<li id="cite_note-10"><span class="mw-cite-backlink"><b><a href="#cite_ref-10">^</a></b></span> <span class="reference-text"><cite class="citation news cs1"><a rel="nofollow" class="external text" href="https://twitter.com/ericidle/status/650759410449518594">"Eric Idle on Twitter"</a>. <i>Twitter</i><span class="reference-accessdate">. Retrieved <span class="nowrap">10 July</span> 2018</span>.</cite><span title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=article&amp;rft.jtitle=Twitter&amp;rft.atitle=Eric+Idle+on+Twitter&amp;rft_id=https%3A%2F%2Ftwitter.com%2Fericidle%2Fstatus%2F650759410449518594&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AEric+Idle" class="Z3988"></span><link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r951705291"/></span>
</li>
<li id="cite_note-11"><span class="mw-cite-backlink"><b><a href="#cite_ref-11">^</a></b></span> <span class="reference-text"><cite id="CITEREFHughes2017" class="citation news cs1">Hughes, Lorna (26 December 2017). <a rel="nofollow" class="external text" href="https://www.liverpoolecho.co.uk/news/liverpool-news/65-famous-people-wirral-given-14061848">"65 famous people Wirral has given to the world"</a>. <i>liverpoolecho</i><span class="reference-accessdate">. Retrieved <span class="nowrap">10 July</span> 2018</span>.</cite><span title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=article&amp;rft.jtitle=liverpoolecho&amp;rft.atitle=65+famous+people+Wirral+has+given+to+the+world&amp;rft.date=2017-12-26&amp;rft.aulast=Hughes&amp;rft.aufirst=Lorna&amp;rft_id=https%3A%2F%2Fwww.liverpoolecho.co.uk%2Fnews%2Fliverpool-news%2F65-famous-people-wirral-given-14061848&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AEric+Idle" class="Z3988"></span><link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r951705291"/></span>
</li>
<li id="cite_note-McCabe-12"><span class="mw-cite-backlink">^ <a href="#cite_ref-McCabe_12-0"><sup><i><b>a</b></i></sup></a> <a href="#cite_ref-McCabe_12-1"><sup><i><b>b</b></i></sup></a> <a href="#cite_ref-McCabe_12-2"><sup><i><b>c</b></i></sup></a> <a href="#cite_ref-McCabe_12-3"><sup><i><b>d</b></i></sup></a></span> <span class="reference-text"><cite id="CITEREFMcCabe2005" class="citation book cs1">McCabe, Bob (2005). <i>The Pythons' Autobiography by the Pythons</i>. London, England: <a href="/wiki/Orion_Publishing_Group" title="Orion Publishing Group">Orion Publishing Group</a>. <a href="/wiki/ISBN_(identifier)" class="mw-redirect" title="ISBN (identifier)">ISBN</a>&#160;<a href="/wiki/Special:BookSources/978-0-7528-6425-9" title="Special:BookSources/978-0-7528-6425-9"><bdi>978-0-7528-6425-9</bdi></a>.</cite><span title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook&amp;rft.genre=book&amp;rft.btitle=The+Pythons%27+Autobiography+by+the+Pythons&amp;rft.place=London%2C+England&amp;rft.pub=Orion+Publishing+Group&amp;rft.date=2005&amp;rft.isbn=978-0-7528-6425-9&amp;rft.aulast=McCabe&amp;rft.aufirst=Bob&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AEric+Idle" class="Z3988"></span><link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r951705291"/></span>
</li>
<li id="cite_note-13"><span class="mw-cite-backlink"><b><a href="#cite_ref-13">^</a></b></span> <span class="reference-text"><cite class="citation web cs1"><a rel="nofollow" class="external text" href="https://www.expressandstar.com/editors-picks/2014/10/01/holy-grail-of-eric-idle-story/">"Holy grail of Eric Idle story"</a>. <i>www.expressandstar.com</i>.</cite><span title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=unknown&amp;rft.jtitle=www.expressandstar.com&amp;rft.atitle=Holy+grail+of+Eric+Idle+story&amp;rft_id=https%3A%2F%2Fwww.expressandstar.com%2Feditors-picks%2F2014%2F10%2F01%2Fholy-grail-of-eric-idle-story%2F&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AEric+Idle" class="Z3988"></span><link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r951705291"/></span>
</li>
<li id="cite_note-14"><span class="mw-cite-backlink"><b><a href="#cite_ref-14">^</a></b></span> <span class="reference-text"><cite id="CITEREFPerry1994" class="citation book cs1">Perry, George (1994). <i>The Life of Python</i>. London, England: <a href="/wiki/Pavilion_Books" title="Pavilion Books">Pavilion Books</a>. <a href="/wiki/ISBN_(identifier)" class="mw-redirect" title="ISBN (identifier)">ISBN</a>&#160;<a href="/wiki/Special:BookSources/978-1909815452" title="Special:BookSources/978-1909815452"><bdi>978-1909815452</bdi></a>.</cite><span title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook&amp;rft.genre=book&amp;rft.btitle=The+Life+of+Python&amp;rft.place=London%2C+England&amp;rft.pub=Pavilion+Books&amp;rft.date=1994&amp;rft.isbn=978-1909815452&amp;rft.aulast=Perry&amp;rft.aufirst=George&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AEric+Idle" class="Z3988"></span><link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r951705291"/></span>
</li>
<li id="cite_note-15"><span class="mw-cite-backlink"><b><a href="#cite_ref-15">^</a></b></span> <span class="reference-text"><cite id="CITEREFPython" class="citation web cs1">Python, Monty. <a rel="nofollow" class="external text" href="http://www.montypython.com/python_Eric_Idle/17">"Eric Idle"</a><span class="reference-accessdate">. Retrieved <span class="nowrap">27 December</span> 2016</span>.</cite><span title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook&amp;rft.genre=unknown&amp;rft.btitle=Eric+Idle&amp;rft.aulast=Python&amp;rft.aufirst=Monty&amp;rft_id=http%3A%2F%2Fwww.montypython.com%2Fpython_Eric_Idle%2F17&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AEric+Idle" class="Z3988"></span><link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r951705291"/></span>
</li>
<li id="cite_note-16"><span class="mw-cite-backlink"><b><a href="#cite_ref-16">^</a></b></span> <span class="reference-text"><a rel="nofollow" class="external text" href="https://www.theguardian.com/media/2015/sep/16/missing-episodes-of-monty-python-precursor-at-last-the-1948-show-found">"Missing episodes of Monty Python precursor At Last the 1948 Show found"</a>, <i>The Guardian</i>, 16 September 2015. Retrieved 16 September 2015.</span>
</li>
<li id="cite_note-17"><span class="mw-cite-backlink"><b><a href="#cite_ref-17">^</a></b></span> <span class="reference-text">Comment made by Eric Idle during an interview shown on the <a href="/wiki/Australian_Broadcasting_Corporation" title="Australian Broadcasting Corporation">ABC-TV</a> program "7.30 Report" on 28 November 2007.</span>
</li>
<li id="cite_note-18"><span class="mw-cite-backlink"><b><a href="#cite_ref-18">^</a></b></span> <span class="reference-text"><a rel="nofollow" class="external text" href="http://www.rutles.org/rnews301.html">Original Rutles reunite for 30th anniversary</a>, Vol 3 Issue 1, 3 March 2008, Rutles News</span>
</li>
<li id="cite_note-19"><span class="mw-cite-backlink"><b><a href="#cite_ref-19">^</a></b></span> <span class="reference-text"><cite class="citation web cs1"><a rel="nofollow" class="external text" href="https://web.archive.org/web/20080401011616/http://flavorpill.com/newyork/events/2008/3/26/the-rutles">"Rutlemania"</a>. Archived from <a rel="nofollow" class="external text" href="http://flavorpill.com/newyork/events/2008/3/26/the-rutles">the original</a> on 1 April 2008<span class="reference-accessdate">. Retrieved <span class="nowrap">4 November</span> 2008</span>.</cite><span title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook&amp;rft.genre=unknown&amp;rft.btitle=Rutlemania&amp;rft_id=http%3A%2F%2Fflavorpill.com%2Fnewyork%2Fevents%2F2008%2F3%2F26%2Fthe-rutles&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AEric+Idle" class="Z3988"></span><link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r951705291"/><sup class="noprint Inline-Template"><span style="white-space: nowrap;">&#91;<i><a href="/wiki/Wikipedia:Link_rot" title="Wikipedia:Link rot"><span title="&#160;Dead link since December 2013">dead link</span></a></i>&#93;</span></sup></span>
</li>
<li id="cite_note-20"><span class="mw-cite-backlink"><b><a href="#cite_ref-20">^</a></b></span> <span class="reference-text"><cite id="CITEREFStaff1997" class="citation web cs1">Staff, I. G. N. (24 September 1997). <a rel="nofollow" class="external text" href="https://www.ign.com/articles/1997/09/25/discworld-ii-mortality-bytes">"Discworld II: Mortality Bytes!"</a>.</cite><span title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook&amp;rft.genre=unknown&amp;rft.btitle=Discworld+II%3A+Mortality+Bytes%21&amp;rft.date=1997-09-24&amp;rft.aulast=Staff&amp;rft.aufirst=I.+G.+N.&amp;rft_id=https%3A%2F%2Fwww.ign.com%2Farticles%2F1997%2F09%2F25%2Fdiscworld-ii-mortality-bytes&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AEric+Idle" class="Z3988"></span><link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r951705291"/></span>
</li>
<li id="cite_note-21"><span class="mw-cite-backlink"><b><a href="#cite_ref-21">^</a></b></span> <span class="reference-text"><cite id="CITEREFMcCall2013" class="citation book cs1">McCall, Douglas (2013). <i>Monty Python: A Chronology, 1969-2012, 2d ed</i>. McFarland. p.&#160;166.</cite><span title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook&amp;rft.genre=book&amp;rft.btitle=Monty+Python%3A+A+Chronology%2C+1969-2012%2C+2d+ed.&amp;rft.pages=166&amp;rft.pub=McFarland&amp;rft.date=2013&amp;rft.aulast=McCall&amp;rft.aufirst=Douglas&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AEric+Idle" class="Z3988"></span><link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r951705291"/></span>
</li>
<li id="cite_note-22"><span class="mw-cite-backlink"><b><a href="#cite_ref-22">^</a></b></span> <span class="reference-text"><a rel="nofollow" class="external text" href="http://montypythonsspamalot.com/creators.php">ERIC IDLE</a>, Monty Python's <i>Spamalot</i> <a rel="nofollow" class="external text" href="https://web.archive.org/web/20130809122909/http://montypythonsspamalot.com/creators.php">Archived</a> 9 August 2013 at the <a href="/wiki/Wayback_Machine" title="Wayback Machine">Wayback Machine</a></span>
</li>
<li id="cite_note-23"><span class="mw-cite-backlink"><b><a href="#cite_ref-23">^</a></b></span> <span class="reference-text"><cite class="citation news cs1"><a rel="nofollow" class="external text" href="https://web.archive.org/web/20071024204345/http://www.variety.com/article/VR1117974601.html?categoryid=15&amp;cs=1">"Eric Idle asks 'What About Dick?<span class="cs1-kern-right">'</span>"</a>. <i>Variety</i>. 23 October 2007. Archived from <a rel="nofollow" class="external text" href="https://www.variety.com/article/VR1117974601.html?categoryid=15&amp;cs=1">the original</a> on 24 October 2007.</cite><span title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=article&amp;rft.jtitle=Variety&amp;rft.atitle=Eric+Idle+asks+%27What+About+Dick%3F%27&amp;rft.date=2007-10-23&amp;rft_id=https%3A%2F%2Fwww.variety.com%2Farticle%2FVR1117974601.html%3Fcategoryid%3D15%26cs%3D1&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AEric+Idle" class="Z3988"></span><link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r951705291"/></span>
</li>
<li id="cite_note-24"><span class="mw-cite-backlink"><b><a href="#cite_ref-24">^</a></b></span> <span class="reference-text"><cite id="CITEREFDominic_Cavendish" class="citation web cs1">Dominic Cavendish. <a rel="nofollow" class="external text" href="https://www.telegraph.co.uk/culture/comedy/10940401/The-almost-definitive-guide-to-Monty-Python-Live-Mostly.html">"The almost-definitive guide to Monty Python Live (Mostly)"</a>. <a href="/wiki/The_Daily_Telegraph" title="The Daily Telegraph">The Telegraph</a><span class="reference-accessdate">. Retrieved <span class="nowrap">21 July</span> 2014</span>.</cite><span title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook&amp;rft.genre=unknown&amp;rft.btitle=The+almost-definitive+guide+to+Monty+Python+Live+%28Mostly%29&amp;rft.pub=The+Telegraph&amp;rft.au=Dominic+Cavendish&amp;rft_id=https%3A%2F%2Fwww.telegraph.co.uk%2Fculture%2Fcomedy%2F10940401%2FThe-almost-definitive-guide-to-Monty-Python-Live-Mostly.html&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AEric+Idle" class="Z3988"></span><link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r951705291"/></span>
</li>
<li id="cite_note-25"><span class="mw-cite-backlink"><b><a href="#cite_ref-25">^</a></b></span> <span class="reference-text"><cite class="citation web cs1"><a rel="nofollow" class="external text" href="http://www.bbc.co.uk/programmes/b086kfbj">"The Entire Universe"</a>. BBC. 26 December 2017<span class="reference-accessdate">. Retrieved <span class="nowrap">27 December</span> 2016</span>.</cite><span title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook&amp;rft.genre=unknown&amp;rft.btitle=The+Entire+Universe&amp;rft.pub=BBC&amp;rft.date=2017-12-26&amp;rft_id=http%3A%2F%2Fwww.bbc.co.uk%2Fprogrammes%2Fb086kfbj&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AEric+Idle" class="Z3988"></span><link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r951705291"/></span>
</li>
<li id="cite_note-26"><span class="mw-cite-backlink"><b><a href="#cite_ref-26">^</a></b></span> <span class="reference-text"><cite class="citation news cs1"><a rel="nofollow" class="external text" href="https://www.theguardian.com/uk/2005/jan/02/arts.artsnews">"Cook tops poll of comedy greats"</a>. <i>The Guardian</i>. 2 January 2005.</cite><span title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=article&amp;rft.jtitle=The+Guardian&amp;rft.atitle=Cook+tops+poll+of+comedy+greats&amp;rft.date=2005-01-02&amp;rft_id=https%3A%2F%2Fwww.theguardian.com%2Fuk%2F2005%2Fjan%2F02%2Farts.artsnews&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AEric+Idle" class="Z3988"></span><link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r951705291"/></span>
</li>
<li id="cite_note-27"><span class="mw-cite-backlink"><b><a href="#cite_ref-27">^</a></b></span> <span class="reference-text"><cite class="citation news cs1"><a rel="nofollow" class="external text" href="http://news.bbc.co.uk/1/hi/entertainment/tv_and_radio/4141019.stm">"Cook voted 'comedians' comedian<span class="cs1-kern-right">'</span>"</a>. <i>BBC News</i>. 2 January 2005<span class="reference-accessdate">. Retrieved <span class="nowrap">21 September</span> 2008</span>.</cite><span title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=article&amp;rft.jtitle=BBC+News&amp;rft.atitle=Cook+voted+%27comedians%27+comedian%27&amp;rft.date=2005-01-02&amp;rft_id=http%3A%2F%2Fnews.bbc.co.uk%2F1%2Fhi%2Fentertainment%2Ftv_and_radio%2F4141019.stm&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AEric+Idle" class="Z3988"></span><link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r951705291"/></span>
</li>
<li id="cite_note-28"><span class="mw-cite-backlink"><b><a href="#cite_ref-28">^</a></b></span> <span class="reference-text"><cite id="CITEREFGoldsmith2012" class="citation web cs1">Goldsmith, Belinda (13 August 2012). <a rel="nofollow" class="external text" href="https://web.archive.org/web/20121023175728/https://www.reuters.com/london-olympics-2012/articles/2012/08/12/london-calling-games-end-music-extravaganza">"London says goodbye with musical extravaganza"</a>. Reuters. Archived from <a rel="nofollow" class="external text" href="https://www.reuters.com/london-olympics-2012/articles/2012/08/12/london-calling-games-end-music-extravaganza">the original</a> on 23 October 2012<span class="reference-accessdate">. Retrieved <span class="nowrap">13 August</span> 2012</span>.</cite><span title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook&amp;rft.genre=unknown&amp;rft.btitle=London+says+goodbye+with+musical+extravaganza&amp;rft.date=2012-08-13&amp;rft.aulast=Goldsmith&amp;rft.aufirst=Belinda&amp;rft_id=https%3A%2F%2Fwww.reuters.com%2Flondon-olympics-2012%2Farticles%2F2012%2F08%2F12%2Flondon-calling-games-end-music-extravaganza&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AEric+Idle" class="Z3988"></span><link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r951705291"/></span>
</li>
<li id="cite_note-29"><span class="mw-cite-backlink"><b><a href="#cite_ref-29">^</a></b></span> <span class="reference-text"><cite class="citation news cs1"><a rel="nofollow" class="external text" href="https://www.officialcharts.com/charts/singles-chart/19911013/7501/">"Official Singles Chart Top 75 (13 October 1991 - 19 October 1991)"</a>. <i>Official Charts Company</i><span class="reference-accessdate">. Retrieved <span class="nowrap">22 August</span> 2019</span>.</cite><span title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=article&amp;rft.jtitle=Official+Charts+Company&amp;rft.atitle=Official+Singles+Chart+Top+75+%2813+October+1991+-+19+October+1991%29&amp;rft_id=https%3A%2F%2Fwww.officialcharts.com%2Fcharts%2Fsingles-chart%2F19911013%2F7501%2F&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AEric+Idle" class="Z3988"></span><link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r951705291"/></span>
</li>
<li id="cite_note-30"><span class="mw-cite-backlink"><b><a href="#cite_ref-30">^</a></b></span> <span class="reference-text"><cite class="citation news cs1"><a rel="nofollow" class="external text" href="https://www.telegraph.co.uk/news/obituaries/10739966/Ann-Howard-obituary.html">"Ann Howard – obituary"</a>. <i><a href="/wiki/The_Daily_Telegraph" title="The Daily Telegraph">The Daily Telegraph</a></i>. 2 April 2014. <a href="/wiki/ISSN_(identifier)" class="mw-redirect" title="ISSN (identifier)">ISSN</a>&#160;<a rel="nofollow" class="external text" href="//www.worldcat.org/issn/0307-1235">0307-1235</a><span class="reference-accessdate">. Retrieved <span class="nowrap">26 June</span> 2020</span>.</cite><span title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=article&amp;rft.jtitle=The+Daily+Telegraph&amp;rft.atitle=Ann+Howard+%E2%80%93+obituary&amp;rft.date=2014-04-02&amp;rft.issn=0307-1235&amp;rft_id=https%3A%2F%2Fwww.telegraph.co.uk%2Fnews%2Fobituaries%2F10739966%2FAnn-Howard-obituary.html&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AEric+Idle" class="Z3988"></span><link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r951705291"/></span>
</li>
<li id="cite_note-31"><span class="mw-cite-backlink"><b><a href="#cite_ref-31">^</a></b></span> <span class="reference-text"><cite id="CITEREFJohnson1989" class="citation book cs1">Johnson, Kim "Howard" (1989). <span class="cs1-lock-registration" title="Free registration required"><a rel="nofollow" class="external text" href="https://archive.org/details/first200yearsofm00john"><i>The First 20 Years of Monty Python</i></a></span>. New York, NY: St. Martin's Press. p.&#160;<a rel="nofollow" class="external text" href="https://archive.org/details/first200yearsofm00john/page/107">107</a>. <a href="/wiki/ISBN_(identifier)" class="mw-redirect" title="ISBN (identifier)">ISBN</a>&#160;<a href="/wiki/Special:BookSources/0-312-03309-5" title="Special:BookSources/0-312-03309-5"><bdi>0-312-03309-5</bdi></a>.</cite><span title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook&amp;rft.genre=book&amp;rft.btitle=The+First+20+Years+of+Monty+Python&amp;rft.place=New+York%2C+NY&amp;rft.pages=107&amp;rft.pub=St.+Martin%27s+Press&amp;rft.date=1989&amp;rft.isbn=0-312-03309-5&amp;rft.aulast=Johnson&amp;rft.aufirst=Kim+%22Howard%22&amp;rft_id=https%3A%2F%2Farchive.org%2Fdetails%2Ffirst200yearsofm00john&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AEric+Idle" class="Z3988"></span><link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r951705291"/></span>
</li>
<li id="cite_note-32"><span class="mw-cite-backlink"><b><a href="#cite_ref-32">^</a></b></span> <span class="reference-text"><cite class="citation web cs1"><a rel="nofollow" class="external text" href="http://archive.org/details/Eric_Idle_The_FCC_Song">"The FCC Song"</a> &#8211; via Internet Archive.</cite><span title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook&amp;rft.genre=unknown&amp;rft.btitle=The+FCC+Song&amp;rft_id=http%3A%2F%2Farchive.org%2Fdetails%2FEric_Idle_The_FCC_Song&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AEric+Idle" class="Z3988"></span><link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r951705291"/></span>
</li>
<li id="cite_note-33"><span class="mw-cite-backlink"><b><a href="#cite_ref-33">^</a></b></span> <span class="reference-text"><cite class="citation web cs1"><a rel="nofollow" class="external text" href="http://www.imdb.com/name/nm0001385/">"Eric Idle"</a>. <i>IMDb</i>.</cite><span title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=unknown&amp;rft.jtitle=IMDb&amp;rft.atitle=Eric+Idle&amp;rft_id=http%3A%2F%2Fwww.imdb.com%2Fname%2Fnm0001385%2F&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AEric+Idle" class="Z3988"></span><link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r951705291"/></span>
</li>
<li id="cite_note-34"><span class="mw-cite-backlink"><b><a href="#cite_ref-34">^</a></b></span> <span class="reference-text"><cite class="citation web cs1"><a rel="nofollow" class="external text" href="https://web.archive.org/web/20090506030717/http://www.americanorchestras.org/symphony_magazine/something_completely_different.html">"Something Completely Different"</a>. Archived from <a rel="nofollow" class="external text" href="http://www.americanorchestras.org/symphony_magazine/something_completely_different.html">the original</a> on 6 May 2009<span class="reference-accessdate">. Retrieved <span class="nowrap">4 November</span> 2008</span>.</cite><span title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook&amp;rft.genre=unknown&amp;rft.btitle=Something+Completely+Different&amp;rft_id=http%3A%2F%2Fwww.americanorchestras.org%2Fsymphony_magazine%2Fsomething_completely_different.html&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AEric+Idle" class="Z3988"></span><link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r951705291"/></span>
</li>
<li id="cite_note-35"><span class="mw-cite-backlink"><b><a href="#cite_ref-35">^</a></b></span> <span class="reference-text"><cite class="citation news cs1"><a rel="nofollow" class="external text" href="https://www.washingtonpost.com/wp-dyn/content/article/2008/07/25/AR2008072502791.html">"<span class="cs1-kern-left">'</span>Not the Messiah': Eric Idle Revs Up"</a>. <i>The Washington Post</i>. 26 July 2008<span class="reference-accessdate">. Retrieved <span class="nowrap">4 November</span> 2008</span>.</cite><span title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=article&amp;rft.jtitle=The+Washington+Post&amp;rft.atitle=%27Not+the+Messiah%27%3A+Eric+Idle+Revs+Up&amp;rft.date=2008-07-26&amp;rft_id=https%3A%2F%2Fwww.washingtonpost.com%2Fwp-dyn%2Fcontent%2Farticle%2F2008%2F07%2F25%2FAR2008072502791.html&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AEric+Idle" class="Z3988"></span><link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r951705291"/></span>
</li>
<li id="cite_note-36"><span class="mw-cite-backlink"><b><a href="#cite_ref-36">^</a></b></span> <span class="reference-text"><cite class="citation web cs1"><a rel="nofollow" class="external text" href="https://www.npr.org/templates/story/story.php?storyId=92869664">"Monty Python's Eric Idle Resurrects 'Life of Brian<span class="cs1-kern-right">'</span>"</a><span class="reference-accessdate">. Retrieved <span class="nowrap">4 November</span> 2008</span>.</cite><span title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook&amp;rft.genre=unknown&amp;rft.btitle=Monty+Python%27s+Eric+Idle+Resurrects+%27Life+of+Brian%27&amp;rft_id=https%3A%2F%2Fwww.npr.org%2Ftemplates%2Fstory%2Fstory.php%3FstoryId%3D92869664&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AEric+Idle" class="Z3988"></span><link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r951705291"/></span>
</li>
<li id="cite_note-37"><span class="mw-cite-backlink"><b><a href="#cite_ref-37">^</a></b></span> <span class="reference-text"><cite class="citation web cs1"><a rel="nofollow" class="external text" href="http://blogs.houstonpress.com/rocks/2008/07/tonight_and_friday_eric_idle_w.php">"Tonight and Friday: Eric Idle with the Houston Symphony"</a><span class="reference-accessdate">. Retrieved <span class="nowrap">4 November</span> 2008</span>.</cite><span title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook&amp;rft.genre=unknown&amp;rft.btitle=Tonight+and+Friday%3A+Eric+Idle+with+the+Houston+Symphony&amp;rft_id=http%3A%2F%2Fblogs.houstonpress.com%2Frocks%2F2008%2F07%2Ftonight_and_friday_eric_idle_w.php&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AEric+Idle" class="Z3988"></span><link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r951705291"/></span>
</li>
<li id="cite_note-38"><span class="mw-cite-backlink"><b><a href="#cite_ref-38">^</a></b></span> <span class="reference-text"><cite id="CITEREFreports" class="citation web cs1">reports, Staff. <a rel="nofollow" class="external text" href="https://www.therecordherald.com/article/20080528/NEWS/305289903">"Amado returns to helm of Delaware Symphony Orchestra"</a>. <i>Waynesboro Record Herald - Waynesboro, PA</i><span class="reference-accessdate">. Retrieved <span class="nowrap">8 May</span> 2020</span>.</cite><span title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=unknown&amp;rft.jtitle=Waynesboro+Record+Herald+-+Waynesboro%2C+PA&amp;rft.atitle=Amado+returns+to+helm+of+Delaware+Symphony+Orchestra&amp;rft.aulast=reports&amp;rft.aufirst=Staff&amp;rft_id=https%3A%2F%2Fwww.therecordherald.com%2Farticle%2F20080528%2FNEWS%2F305289903&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AEric+Idle" class="Z3988"></span><link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r951705291"/></span>
</li>
<li id="cite_note-39"><span class="mw-cite-backlink"><b><a href="#cite_ref-39">^</a></b></span> <span class="reference-text"><cite class="citation web cs1"><a rel="nofollow" class="external text" href="http://www.bbc.co.uk/programmes/p021x88c">"Eric Idle performs theme song for The Infinite Monkey Cage, The Infinite Monkey Cage&#160;– BBC Radio 4"</a><span class="reference-accessdate">. Retrieved <span class="nowrap">27 December</span> 2016</span>.</cite><span title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook&amp;rft.genre=unknown&amp;rft.btitle=Eric+Idle+performs+theme+song+for+The+Infinite+Monkey+Cage%2C+The+Infinite+Monkey+Cage+%E2%80%93+BBC+Radio+4&amp;rft_id=http%3A%2F%2Fwww.bbc.co.uk%2Fprogrammes%2Fp021x88c&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AEric+Idle" class="Z3988"></span><link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r951705291"/></span>
</li>
<li id="cite_note-40"><span class="mw-cite-backlink"><b><a href="#cite_ref-40">^</a></b></span> <span class="reference-text"><cite class="citation news cs1"><a rel="nofollow" class="external text" href="https://www.theglobeandmail.com/arts/erics-naughty-bits/article1023519/">"Eric's naughty bits"</a><span class="reference-accessdate">. Retrieved <span class="nowrap">26 May</span> 2020</span>.</cite><span title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=article&amp;rft.atitle=Eric%27s+naughty+bits&amp;rft_id=https%3A%2F%2Fwww.theglobeandmail.com%2Farts%2Ferics-naughty-bits%2Farticle1023519%2F&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AEric+Idle" class="Z3988"></span><link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r951705291"/></span>
</li>
<li id="cite_note-41"><span class="mw-cite-backlink"><b><a href="#cite_ref-41">^</a></b></span> <span class="reference-text"><cite class="citation news cs1"><a rel="nofollow" class="external text" href="https://www.express.co.uk/expressyourself/98595/Marriage-is-no-laughing-matter-when-you-re-a-Python">"Marriage is no laughing matter when you're a Python"</a>. <i><a href="/wiki/Daily_Express" title="Daily Express">Daily Express</a></i>. 3 May 2009<span class="reference-accessdate">. Retrieved <span class="nowrap">17 July</span> 2018</span>.</cite><span title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=article&amp;rft.jtitle=Daily+Express&amp;rft.atitle=Marriage+is+no+laughing+matter+when+you%27re+a+Python&amp;rft.date=2009-05-03&amp;rft_id=https%3A%2F%2Fwww.express.co.uk%2Fexpressyourself%2F98595%2FMarriage-is-no-laughing-matter-when-you-re-a-Python&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AEric+Idle" class="Z3988"></span><link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r951705291"/></span>
</li>
<li id="cite_note-42"><span class="mw-cite-backlink"><b><a href="#cite_ref-42">^</a></b></span> <span class="reference-text"><cite id="CITEREFZekas2013" class="citation news cs1">Zekas, Rita (5 December 2013). <a rel="nofollow" class="external text" href="https://www.thestar.com/life/homes/2013/12/05/a_symphony_of_comfort_and_cheer.html">"A symphony of comfort and cheer"</a>. <i>Toronto Star</i><span class="reference-accessdate">. Retrieved <span class="nowrap">27 July</span> 2018</span>.</cite><span title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=article&amp;rft.jtitle=Toronto+Star&amp;rft.atitle=A+symphony+of+comfort+and+cheer&amp;rft.date=2013-12-05&amp;rft.aulast=Zekas&amp;rft.aufirst=Rita&amp;rft_id=https%3A%2F%2Fwww.thestar.com%2Flife%2Fhomes%2F2013%2F12%2F05%2Fa_symphony_of_comfort_and_cheer.html&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AEric+Idle" class="Z3988"></span><link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r951705291"/></span>
</li>
<li id="cite_note-43"><span class="mw-cite-backlink"><b><a href="#cite_ref-43">^</a></b></span> <span class="reference-text"><cite class="citation web cs1"><a rel="nofollow" class="external text" href="https://www.classicfm.com/music-news/pictures/artist/scotlands-finest/peter-oundjian/">"Peter Oundjian (b.1955)"</a>. <i>Classic FM</i><span class="reference-accessdate">. Retrieved <span class="nowrap">26 May</span> 2020</span>.</cite><span title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=unknown&amp;rft.jtitle=Classic+FM&amp;rft.atitle=Peter+Oundjian+%28b.1955%29&amp;rft_id=https%3A%2F%2Fwww.classicfm.com%2Fmusic-news%2Fpictures%2Fartist%2Fscotlands-finest%2Fpeter-oundjian%2F&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AEric+Idle" class="Z3988"></span><link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r951705291"/></span>
</li>
<li id="cite_note-44"><span class="mw-cite-backlink"><b><a href="#cite_ref-44">^</a></b></span> <span class="reference-text"><cite class="citation web cs1"><a rel="nofollow" class="external text" href="https://www.rugbypass.com/news/nigel-wray-receives-unlikely-backing-of-comedy-legend/">"Nigel Wray receives unlikely backing of comedy legend"</a>. <i>Rugby Pass</i>.</cite><span title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=unknown&amp;rft.jtitle=Rugby+Pass&amp;rft.atitle=Nigel+Wray+receives+unlikely+backing+of+comedy+legend&amp;rft_id=https%3A%2F%2Fwww.rugbypass.com%2Fnews%2Fnigel-wray-receives-unlikely-backing-of-comedy-legend%2F&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AEric+Idle" class="Z3988"></span><link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r951705291"/></span>
</li>
<li id="cite_note-45"><span class="mw-cite-backlink"><b><a href="#cite_ref-45">^</a></b></span> <span class="reference-text"><cite class="citation web cs1"><a rel="nofollow" class="external text" href="https://www.radiotimes.com/news/2016-12-26/eric-idle-on-terry-jones-brian-cox-religion-and-the-entire-universe/">"Eric Idle on Terry Jones, Brian Cox, religion and The Entire Universe"</a>. <i>Radio Times</i>.</cite><span title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=unknown&amp;rft.jtitle=Radio+Times&amp;rft.atitle=Eric+Idle+on+Terry+Jones%2C+Brian+Cox%2C+religion+and+The+Entire+Universe&amp;rft_id=https%3A%2F%2Fwww.radiotimes.com%2Fnews%2F2016-12-26%2Feric-idle-on-terry-jones-brian-cox-religion-and-the-entire-universe%2F&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AEric+Idle" class="Z3988"></span><link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r951705291"/></span>
</li>
<li id="cite_note-46"><span class="mw-cite-backlink"><b><a href="#cite_ref-46">^</a></b></span> <span class="reference-text"><cite class="citation web cs1"><a rel="nofollow" class="external text" href="https://web.archive.org/web/20120813034146/http://www.astro.uu.se/planet/asteroid/astdiv/9620.html">"(9620) Ericidle = 1993 FU13"</a>. 17 June 2007. Archived from <a rel="nofollow" class="external text" href="http://www.astro.uu.se/planet/asteroid/astdiv/9620.html">the original</a> on 13 August 2012.</cite><span title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook&amp;rft.genre=unknown&amp;rft.btitle=%289620%29+Ericidle+%3D+1993+FU13&amp;rft.date=2007-06-17&amp;rft_id=http%3A%2F%2Fwww.astro.uu.se%2Fplanet%2Fasteroid%2Fastdiv%2F9620.html&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AEric+Idle" class="Z3988"></span><link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r951705291"/></span>
</li>
<li id="cite_note-47"><span class="mw-cite-backlink"><b><a href="#cite_ref-47">^</a></b></span> <span class="reference-text">Hans ten Cate, <a rel="nofollow" class="external text" href="http://www.dailyllama.com/news/2005/llama270.html">"COMEDY EXPERTS SAY PYTHON MEMBERS AMONG GREATEST COMICS OF ALL TIME"</a>, 2 January 2005</span>
</li>
<li id="cite_note-48"><span class="mw-cite-backlink"><b><a href="#cite_ref-48">^</a></b></span> <span class="reference-text">Lutz, Mark &amp; Ascher, David (2004). <i>Learning Python</i>, p. 40. O'Reilly Media, Inc. <link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r951705291"/><a href="/wiki/ISBN_(identifier)" class="mw-redirect" title="ISBN (identifier)">ISBN</a>&#160;<a href="/wiki/Special:BookSources/0-596-00281-5" title="Special:BookSources/0-596-00281-5">0-596-00281-5</a>.</span>
</li>
<li id="cite_note-49"><span class="mw-cite-backlink"><b><a href="#cite_ref-49">^</a></b></span> <span class="reference-text">Hammond, Mark &amp; Robinson, Andy (2000). <i>Python Programming On Win32: Help for Windows Programmers</i>, p. 59. O'Reilly Media, Inc. <link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r951705291"/><a href="/wiki/ISBN_(identifier)" class="mw-redirect" title="ISBN (identifier)">ISBN</a>&#160;<a href="/wiki/Special:BookSources/978-1565926219" title="Special:BookSources/978-1565926219">978-1565926219</a>.</span>
</li>
<li id="cite_note-50"><span class="mw-cite-backlink"><b><a href="#cite_ref-50">^</a></b></span> <span class="reference-text"><cite class="citation web cs1"><a rel="nofollow" class="external text" href="https://www.imdb.com/title/tt3872778/">"Monty Python Live (Mostly)"</a>. 20 July 2014 &#8211; via www.imdb.com.</cite><span title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook&amp;rft.genre=unknown&amp;rft.btitle=Monty+Python+Live+%28Mostly%29&amp;rft.date=2014-07-20&amp;rft_id=https%3A%2F%2Fwww.imdb.com%2Ftitle%2Ftt3872778%2F&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AEric+Idle" class="Z3988"></span><link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r951705291"/></span>
</li>
</ol></div>
<h2><span class="mw-headline" id="External_links">External links</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Eric_Idle&amp;action=edit&amp;section=18" title="Edit section: External links">edit</a><span class="mw-editsection-bracket">]</span></span></h2>
<table role="presentation" class="mbox-small plainlinks sistersitebox" style="background-color:#f9f9f9;border:1px solid #aaa;color:#000">
<tbody><tr>
<td class="mbox-image"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Wikiquote-logo.svg/34px-Wikiquote-logo.svg.png" decoding="async" width="34" height="40" class="noviewer" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Wikiquote-logo.svg/51px-Wikiquote-logo.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Wikiquote-logo.svg/68px-Wikiquote-logo.svg.png 2x" data-file-width="300" data-file-height="355" /></td>
<td class="mbox-text plainlist">Wikiquote has quotations related to: <i><b><a href="https://en.wikiquote.org/wiki/Special:Search/Eric_Idle" class="extiw" title="q:Special:Search/Eric Idle">Eric Idle</a></b></i></td></tr>
</tbody></table>
<table role="presentation" class="mbox-small plainlinks sistersitebox" style="background-color:#f9f9f9;border:1px solid #aaa;color:#000">
<tbody><tr>
<td class="mbox-image"><img alt="" src="//upload.wikimedia.org/wikipedia/en/thumb/4/4a/Commons-logo.svg/30px-Commons-logo.svg.png" decoding="async" width="30" height="40" class="noviewer" srcset="//upload.wikimedia.org/wikipedia/en/thumb/4/4a/Commons-logo.svg/45px-Commons-logo.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/4/4a/Commons-logo.svg/59px-Commons-logo.svg.png 2x" data-file-width="1024" data-file-height="1376" /></td>
<td class="mbox-text plainlist">Wikimedia Commons has media related to <i><b><a href="https://commons.wikimedia.org/wiki/Special:Search/Eric_Idle" class="extiw" title="commons:Special:Search/Eric Idle">Eric Idle</a></b></i>.</td></tr>
</tbody></table>
<ul><li><a rel="nofollow" class="external text" href="http://www.montypython.com/python_Eric_Idle/17">Eric Idle's profile on Monty Python's official website</a></li>
<li><a rel="nofollow" class="external text" href="https://archive.org/details/Eric_Idle_The_FCC_Song">Eric Idle singing his "FCC Song" in MP3 format from Archive.org</a></li>
<li><a rel="nofollow" class="external text" href="https://www.imdb.com/name/nm0001385/">Eric Idle</a> on <a href="/wiki/IMDb" title="IMDb">IMDb</a></li>
<li><a rel="nofollow" class="external text" href="https://www.ibdb.com/broadway-cast-staff/76129">Eric Idle</a> at the <a href="/wiki/Internet_Broadway_Database" title="Internet Broadway Database">Internet Broadway Database</a> <a href="https://www.wikidata.org/wiki/Q210741#P1220" title="Edit this at Wikidata"><img alt="Edit this at Wikidata" src="//upload.wikimedia.org/wikipedia/en/thumb/8/8a/OOjs_UI_icon_edit-ltr-progressive.svg/10px-OOjs_UI_icon_edit-ltr-progressive.svg.png" decoding="async" width="10" height="10" style="vertical-align: text-top" srcset="//upload.wikimedia.org/wikipedia/en/thumb/8/8a/OOjs_UI_icon_edit-ltr-progressive.svg/15px-OOjs_UI_icon_edit-ltr-progressive.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/8/8a/OOjs_UI_icon_edit-ltr-progressive.svg/20px-OOjs_UI_icon_edit-ltr-progressive.svg.png 2x" data-file-width="20" data-file-height="20" /></a></li>
<li><a rel="nofollow" class="external text" href="http://www.lortel.org/Archives/CreditableEntity/35015">Eric Idle</a> at the <a href="/wiki/Lortel_Archives" title="Lortel Archives">Internet Off-Broadway Database</a></li>
<li><a rel="nofollow" class="external text" href="http://www.screenonline.org.uk/people/id/499808/">Eric Idle</a> at the <a href="/wiki/British_Film_Institute" title="British Film Institute">BFI</a>'s <a href="/wiki/Screenonline" title="Screenonline">Screenonline</a></li>
<li><a rel="nofollow" class="external text" href="https://www.comedy.co.uk/people/eric_idle/"><i>Eric Idle</i></a> at <a href="/wiki/British_Comedy_Guide" title="British Comedy Guide">British Comedy Guide</a></li>
<li><cite class="citation web cs1"><a rel="nofollow" class="external text" href="https://web.archive.org/web/20060104112941/http://www.footlights.org/past/1965">"<i>My Girl Herbert</i>"</a>. Archived from <a rel="nofollow" class="external text" href="http://www.footlights.org/past/1965">the original</a> on 4 January 2006<span class="reference-accessdate">. Retrieved <span class="nowrap">16 June</span> 2006</span>.</cite><span title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook&amp;rft.genre=unknown&amp;rft.btitle=My+Girl+Herbert&amp;rft_id=http%3A%2F%2Fwww.footlights.org%2Fpast%2F1965&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AEric+Idle" class="Z3988"></span><link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r951705291"/>&#160;– the 1965 Cambridge Footlights Club revue during the time when Eric Idle was President of the Footlights, as well as being a member of the revue cast</li></ul>
<div role="navigation" class="navbox" aria-labelledby="Monty_Python" style="padding:3px"><table class="nowraplinks hlist mw-collapsible autocollapse navbox-inner" style="border-spacing:0;background:transparent;color:inherit"><tbody><tr><th scope="col" class="navbox-title" colspan="2"><div class="plainlinks hlist navbar mini"><ul><li class="nv-view"><a href="/wiki/Template:Monty_Python" title="Template:Monty Python"><abbr title="View this template" style=";;background:none transparent;border:none;-moz-box-shadow:none;-webkit-box-shadow:none;box-shadow:none; padding:0;">v</abbr></a></li><li class="nv-talk"><a href="/wiki/Template_talk:Monty_Python" title="Template talk:Monty Python"><abbr title="Discuss this template" style=";;background:none transparent;border:none;-moz-box-shadow:none;-webkit-box-shadow:none;box-shadow:none; padding:0;">t</abbr></a></li><li class="nv-edit"><a class="external text" href="https://en.wikipedia.org/w/index.php?title=Template:Monty_Python&amp;action=edit"><abbr title="Edit this template" style=";;background:none transparent;border:none;-moz-box-shadow:none;-webkit-box-shadow:none;box-shadow:none; padding:0;">e</abbr></a></li></ul></div><div id="Monty_Python" style="font-size:114%;margin:0 4em"><a href="/wiki/Monty_Python" title="Monty Python">Monty Python</a></div></th></tr><tr><td class="navbox-abovebelow" colspan="2"><div id="*_Graham_Chapman_*_John_Cleese_*_Terry_Gilliam_*_Eric_Idle_*_Terry_Jones_*_Michael_Palin&amp;#95;_*_Carol_Cleveland_*_Neil_Innes">
<ul><li><b><a href="/wiki/Graham_Chapman" title="Graham Chapman">Graham Chapman</a></b></li>
<li><b><a href="/wiki/John_Cleese" title="John Cleese">John Cleese</a></b></li>
<li><b><a href="/wiki/Terry_Gilliam" title="Terry Gilliam">Terry Gilliam</a></b></li>
<li><b><a class="mw-selflink selflink">Eric Idle</a></b></li>
<li><b><a href="/wiki/Terry_Jones" title="Terry Jones">Terry Jones</a></b></li>
<li><b><a href="/wiki/Michael_Palin" title="Michael Palin">Michael Palin</a></b></li></ul>
<ul><li><a href="/wiki/Carol_Cleveland" title="Carol Cleveland">Carol Cleveland</a></li>
<li><a href="/wiki/Neil_Innes" title="Neil Innes">Neil Innes</a></li></ul>
</div></td></tr><tr><th scope="row" class="navbox-group" style="width:1%">Television series</th><td class="navbox-list navbox-odd" style="text-align:left;border-left-width:2px;border-left-style:solid;width:100%;padding:0px"><div style="padding:0em 0.25em">
<ul><li><i><a href="/wiki/Monty_Python%27s_Flying_Circus" title="Monty Python&#39;s Flying Circus">Flying Circus</a></i>
<ul><li><a href="/wiki/List_of_Monty_Python%27s_Flying_Circus_episodes" title="List of Monty Python&#39;s Flying Circus episodes">episodes</a></li></ul></li>
<li><i><a href="/wiki/Monty_Python%27s_Fliegender_Zirkus" title="Monty Python&#39;s Fliegender Zirkus">Fliegender Zirkus</a></i></li>
<li><i><a href="/wiki/Monty_Python%27s_Personal_Best" title="Monty Python&#39;s Personal Best">Personal Best</a></i></li></ul>
</div></td></tr><tr><th scope="row" class="navbox-group" style="width:1%">Films</th><td class="navbox-list navbox-even" style="text-align:left;border-left-width:2px;border-left-style:solid;width:100%;padding:0px"><div style="padding:0em 0.25em">
<ul><li><i><a href="/wiki/And_Now_for_Something_Completely_Different" title="And Now for Something Completely Different">And Now for Something Completely Different</a></i></li>
<li><i><a href="/wiki/Monty_Python_and_the_Holy_Grail" title="Monty Python and the Holy Grail">Holy Grail</a></i></li>
<li><i><a href="/wiki/Monty_Python%27s_Life_of_Brian" title="Monty Python&#39;s Life of Brian">Life of Brian</a></i></li>
<li><i><a href="/wiki/Monty_Python_Live_at_the_Hollywood_Bowl" title="Monty Python Live at the Hollywood Bowl">Live at the Hollywood Bowl</a></i></li>
<li><i><a href="/wiki/Monty_Python%27s_The_Meaning_of_Life" title="Monty Python&#39;s The Meaning of Life">The Meaning of Life</a></i>
<ul><li><i><a href="/wiki/The_Crimson_Permanent_Assurance" title="The Crimson Permanent Assurance">The Crimson Permanent Assurance</a></i></li></ul></li></ul>
</div></td></tr><tr><th scope="row" class="navbox-group" style="width:1%">Studio albums</th><td class="navbox-list navbox-odd" style="text-align:left;border-left-width:2px;border-left-style:solid;width:100%;padding:0px"><div style="padding:0em 0.25em">
<ul><li><i><a href="/wiki/Another_Monty_Python_Record" title="Another Monty Python Record">Another Record</a></i></li>
<li><i><a href="/wiki/Monty_Python%27s_Previous_Record" title="Monty Python&#39;s Previous Record">Previous Record</a></i></li>
<li><i><a href="/wiki/The_Monty_Python_Matching_Tie_and_Handkerchief" title="The Monty Python Matching Tie and Handkerchief">Matching Tie and Handkerchief</a></i></li>
<li><i><a href="/wiki/The_Album_of_the_Soundtrack_of_the_Trailer_of_the_Film_of_Monty_Python_and_the_Holy_Grail" title="The Album of the Soundtrack of the Trailer of the Film of Monty Python and the Holy Grail">Holy Grail</a></i></li>
<li><i><a href="/wiki/Monty_Python%27s_Life_of_Brian_(album)" title="Monty Python&#39;s Life of Brian (album)">Life of Brian</a></i></li>
<li><i><a href="/wiki/Monty_Python%27s_Contractual_Obligation_Album" title="Monty Python&#39;s Contractual Obligation Album">Contractual Obligation</a></i></li>
<li><i><a href="/wiki/Monty_Python%27s_The_Meaning_of_Life_(album)" title="Monty Python&#39;s The Meaning of Life (album)">The Meaning of Life</a></i></li></ul>
</div></td></tr><tr><th scope="row" class="navbox-group" style="width:1%">Compilation albums</th><td class="navbox-list navbox-even" style="text-align:left;border-left-width:2px;border-left-style:solid;width:100%;padding:0px"><div style="padding:0em 0.25em">
<ul><li><i><a href="/wiki/The_Monty_Python_Instant_Record_Collection" title="The Monty Python Instant Record Collection">Instant Record Collection</a></i></li>
<li><i><a href="/wiki/The_Final_Rip_Off" title="The Final Rip Off">Final Rip Off</a></i></li>
<li><i><a href="/wiki/Monty_Python_Sings" title="Monty Python Sings">Sings</a></i></li>
<li><i><a href="/wiki/The_Ultimate_Monty_Python_Rip_Off" title="The Ultimate Monty Python Rip Off">Ultimate Rip Off</a></i></li>
<li><i><a href="/wiki/The_Instant_Monty_Python_CD_Collection" title="The Instant Monty Python CD Collection">Instant CD Collection</a></i></li>
<li><i><a href="/wiki/Monty_Python%27s_Total_Rubbish" title="Monty Python&#39;s Total Rubbish">Total Rubbish</a></i></li></ul>
</div></td></tr><tr><th scope="row" class="navbox-group" style="width:1%">Live albums</th><td class="navbox-list navbox-odd" style="text-align:left;border-left-width:2px;border-left-style:solid;width:100%;padding:0px"><div style="padding:0em 0.25em">
<ul><li><i><a href="/wiki/Monty_Python%27s_Flying_Circus_(album)" title="Monty Python&#39;s Flying Circus (album)">Flying Circus</a></i></li>
<li><i><a href="/wiki/Live_at_Drury_Lane" title="Live at Drury Lane">Live at Drury Lane</a></i></li>
<li><i><a href="/wiki/Monty_Python_Live_at_City_Center" title="Monty Python Live at City Center">Live at City Center</a></i></li></ul>
</div></td></tr><tr><th scope="row" class="navbox-group" style="width:1%">Specials</th><td class="navbox-list navbox-even" style="text-align:left;border-left-width:2px;border-left-style:solid;width:100%;padding:0px"><div style="padding:0em 0.25em">
<ul><li><i><a href="/wiki/Parrot_Sketch_Not_Included_%E2%80%93_20_Years_of_Monty_Python" title="Parrot Sketch Not Included – 20 Years of Monty Python">Parrot Sketch Not Included</a></i></li>
<li><i><a href="/wiki/Monty_Python_Live_at_Aspen" title="Monty Python Live at Aspen">Live at Aspen</a></i></li>
<li><i><a href="/wiki/Python_Night_%E2%80%93_30_Years_of_Monty_Python" title="Python Night – 30 Years of Monty Python">Python Night</a></i></li></ul>
</div></td></tr><tr><th scope="row" class="navbox-group" style="width:1%">Documentaries</th><td class="navbox-list navbox-odd" style="text-align:left;border-left-width:2px;border-left-style:solid;width:100%;padding:0px"><div style="padding:0em 0.25em">
<ul><li><i><a href="/wiki/The_Pythons_(film)" title="The Pythons (film)">The Pythons</a></i></li>
<li><i><a href="/wiki/Life_of_Python" title="Life of Python">Life of Python</a></i></li>
<li><i><a href="/wiki/Monty_Python:_Almost_the_Truth_(Lawyers_Cut)" title="Monty Python: Almost the Truth (Lawyers Cut)">Almost the Truth (Lawyers Cut)</a></i></li>
<li><i><a href="/wiki/Monty_Python:_And_Now_for_Something_Rather_Similar" title="Monty Python: And Now for Something Rather Similar">And Now for Something Rather Similar</a></i></li>
<li><i><a href="/wiki/Monty_Python:_The_Meaning_of_Live" title="Monty Python: The Meaning of Live">The Meaning of Live</a></i></li></ul>
</div></td></tr><tr><th scope="row" class="navbox-group" style="width:1%">Stage productions</th><td class="navbox-list navbox-even" style="text-align:left;border-left-width:2px;border-left-style:solid;width:100%;padding:0px"><div style="padding:0em 0.25em">
<ul><li><i><a href="/wiki/Spamalot" title="Spamalot">Spamalot</a></i></li>
<li><i><a href="/wiki/Not_the_Messiah_(He%27s_a_Very_Naughty_Boy)" title="Not the Messiah (He&#39;s a Very Naughty Boy)">Not the Messiah (He's a Very Naughty Boy)</a></i></li>
<li><i><a href="/wiki/An_Evening_Without_Monty_Python" title="An Evening Without Monty Python">An Evening Without Monty Python</a></i></li>
<li><i><a href="/wiki/Monty_Python_Live_(Mostly)" title="Monty Python Live (Mostly)">Live (Mostly)</a></i></li></ul>
</div></td></tr><tr><th scope="row" class="navbox-group" style="width:1%">Literature</th><td class="navbox-list navbox-odd" style="text-align:left;border-left-width:2px;border-left-style:solid;width:100%;padding:0px"><div style="padding:0em 0.25em">
<ul><li><i><a href="/wiki/Monty_Python%27s_Big_Red_Book" title="Monty Python&#39;s Big Red Book">Big Red Book</a></i></li>
<li><i><a href="/wiki/The_Brand_New_Monty_Python_Bok" title="The Brand New Monty Python Bok">Brand New Bok</a></i></li>
<li><i><a href="/wiki/Monty_Python_and_the_Holy_Grail_(Book)" title="Monty Python and the Holy Grail (Book)">Holy Grail (Book)</a></i></li>
<li><i><a href="/wiki/Monty_Python%27s_The_Life_of_Brian_/_Monty_Python_Scrapbook" title="Monty Python&#39;s The Life of Brian / Monty Python Scrapbook">Life of Brian/SCRAPBOOK</a></i></li>
<li><i><a href="/wiki/Monty_Python%27s_The_Meaning_of_Life_(book)" title="Monty Python&#39;s The Meaning of Life (book)">The Meaning of Life</a></i></li>
<li><i><a href="/wiki/Monty_Python%27s_Flying_Circus:_Just_the_Words" title="Monty Python&#39;s Flying Circus: Just the Words">Just the Words</a></i></li>
<li><i><a href="/wiki/The_Fairly_Incomplete_%26_Rather_Badly_Illustrated_Monty_Python_Song_Book" title="The Fairly Incomplete &amp; Rather Badly Illustrated Monty Python Song Book">Song Book</a></i></li>
<li><i><a href="/wiki/A_Pocketful_of_Python" title="A Pocketful of Python">A Pocketful of Python</a></i></li>
<li><i><a href="/wiki/The_Pythons_Autobiography_by_The_Pythons" title="The Pythons Autobiography by The Pythons">The Pythons Autobiography</a></i></li>
<li><i><a href="/wiki/Monty_Python_Live!" title="Monty Python Live!">Live!</a></i></li></ul>
</div></td></tr><tr><th scope="row" class="navbox-group" style="width:1%">Video games</th><td class="navbox-list navbox-even" style="text-align:left;border-left-width:2px;border-left-style:solid;width:100%;padding:0px"><div style="padding:0em 0.25em">
<ul><li><i><a href="/wiki/Monty_Python%27s_Flying_Circus:_The_Computer_Game" title="Monty Python&#39;s Flying Circus: The Computer Game">Flying Circus</a></i></li>
<li><i><a href="/wiki/Monty_Python%27s_Complete_Waste_of_Time" title="Monty Python&#39;s Complete Waste of Time">Complete Waste of Time</a></i></li>
<li><i><a href="/wiki/Monty_Python_%26_the_Quest_for_the_Holy_Grail" title="Monty Python &amp; the Quest for the Holy Grail">Quest for the Holy Grail</a></i></li>
<li><i><a href="/wiki/Monty_Python%27s_The_Meaning_of_Life_(video_game)" title="Monty Python&#39;s The Meaning of Life (video game)">The Meaning of Life</a></i></li>
<li><i><a href="/wiki/Monty_Python%27s_Cow_Tossing" title="Monty Python&#39;s Cow Tossing">Cow Tossing</a></i></li></ul>
</div></td></tr><tr><th scope="row" class="navbox-group" style="width:1%">Characters</th><td class="navbox-list navbox-odd" style="text-align:left;border-left-width:2px;border-left-style:solid;width:100%;padding:0px"><div style="padding:0em 0.25em">
<ul><li><a href="/wiki/Mr_Praline" title="Mr Praline">Mr Praline</a></li>
<li><a href="/wiki/Gumbys" class="mw-redirect" title="Gumbys">Gumbys</a></li>
<li><a href="/wiki/The_Colonel_(Monty_Python)" title="The Colonel (Monty Python)">The Colonel</a></li>
<li><a href="/wiki/Mr_Creosote" title="Mr Creosote">Mr Creosote</a></li>
<li><a href="/wiki/Rabbit_of_Caerbannog" title="Rabbit of Caerbannog">Rabbit of Caerbannog</a></li>
<li><a href="/wiki/Ron_Obvious_(Monty_Python)" title="Ron Obvious (Monty Python)">Ron Obvious</a></li>
<li><a href="/wiki/List_of_recurring_Monty_Python%27s_Flying_Circus_characters" title="List of recurring Monty Python&#39;s Flying Circus characters">Other characters</a></li></ul>
</div></td></tr><tr><th scope="row" class="navbox-group" style="width:1%">Sketches</th><td class="navbox-list navbox-even" style="text-align:left;border-left-width:2px;border-left-style:solid;width:100%;padding:0px"><div style="padding:0em 0.25em">
<ul><li><a href="/wiki/Albatross_(Monty_Python_sketch)" title="Albatross (Monty Python sketch)">Albatross!</a></li>
<li><a href="/wiki/Anne_Elk%27s_Theory_on_Brontosauruses" title="Anne Elk&#39;s Theory on Brontosauruses">Anne Elk's Theory on Brontosauruses</a></li>
<li><a href="/wiki/Architects_Sketch" title="Architects Sketch">Architects</a></li>
<li><a href="/wiki/Argument_Clinic" title="Argument Clinic">Argument Clinic</a></li>
<li><a href="/wiki/The_Bishop_(Monty_Python)" class="mw-redirect" title="The Bishop (Monty Python)">Bishop</a></li>
<li><a href="/wiki/Bruces_sketch" title="Bruces sketch">Bruces</a></li>
<li><a href="/wiki/Cheese_Shop_sketch" title="Cheese Shop sketch">Cheese Shop</a></li>
<li><a href="/wiki/Colin_%22Bomber%22_Harris_vs_Colin_%22Bomber%22_Harris" title="Colin &quot;Bomber&quot; Harris vs Colin &quot;Bomber&quot; Harris">Colin "Bomber" Harris vs Colin "Bomber" Harris</a></li>
<li><a href="/wiki/Crunchy_Frog" title="Crunchy Frog">Crunchy Frog</a></li>
<li><a href="/wiki/Dead_Parrot_sketch" title="Dead Parrot sketch">Dead Parrot</a></li>
<li><a href="/wiki/The_Dirty_Fork" title="The Dirty Fork">Dirty Fork</a></li>
<li><a href="/wiki/Dirty_Hungarian_Phrasebook" title="Dirty Hungarian Phrasebook">Dirty Hungarian Phrasebook</a></li>
<li><a href="/wiki/Election_Night_Special" title="Election Night Special">Election Night Special</a></li>
<li><a href="/wiki/Fish_Licence" title="Fish Licence">Fish Licence</a></li>
<li><a href="/wiki/The_Fish-Slapping_Dance" title="The Fish-Slapping Dance">Fish-Slapping Dance</a></li>
<li><a href="/wiki/Four_Yorkshiremen_sketch" title="Four Yorkshiremen sketch">Four Yorkshiremen</a></li>
<li><a href="/wiki/The_Funniest_Joke_in_the_World" title="The Funniest Joke in the World">The Funniest Joke in the World</a></li>
<li><a href="/wiki/How_Not_to_Be_Seen" title="How Not to Be Seen">How Not to Be Seen</a></li>
<li><a href="/wiki/Kilimanjaro_Expedition" title="Kilimanjaro Expedition">Kilimanjaro Expedition</a></li>
<li><a href="/wiki/Lifeboat_sketch" title="Lifeboat sketch">Lifeboat</a></li>
<li><a href="/wiki/Marriage_Guidance_Counsellor" title="Marriage Guidance Counsellor">Marriage Guidance Counsellor</a></li>
<li><a href="/wiki/The_Ministry_of_Silly_Walks" title="The Ministry of Silly Walks">Ministry of Silly Walks</a></li>
<li><a href="/wiki/The_Mouse_Problem" title="The Mouse Problem">Mouse Problem</a></li>
<li><a href="/wiki/Nudge_Nudge" title="Nudge Nudge">Nudge Nudge</a></li>
<li><a href="/wiki/Patient_Abuse" title="Patient Abuse">Patient Abuse</a></li>
<li><a href="/wiki/The_Philosophers%27_Football_Match" title="The Philosophers&#39; Football Match">Philosophers' Football Match</a></li>
<li><a href="/wiki/Piranha_Brothers" title="Piranha Brothers">Piranha Brothers</a></li>
<li><a href="/wiki/Sam_Peckinpah%27s_%22Salad_Days%22" title="Sam Peckinpah&#39;s &quot;Salad Days&quot;">Sam Peckinpah's "Salad Days"</a></li>
<li><a href="/wiki/Seduced_Milkmen" title="Seduced Milkmen">Seduced Milkmen</a></li>
<li><a href="/wiki/Self_Defence_Against_Fresh_Fruit" title="Self Defence Against Fresh Fruit">Self Defence Against Fresh Fruit</a></li>
<li><a href="/wiki/Spam_(Monty_Python)" title="Spam (Monty Python)">Spam</a></li>
<li><a href="/wiki/The_Spanish_Inquisition_(Monty_Python)" title="The Spanish Inquisition (Monty Python)">Spanish Inquisition</a></li>
<li><a href="/wiki/Undertakers_sketch" title="Undertakers sketch">Undertakers</a></li>
<li><a href="/wiki/Upper_Class_Twit_of_the_Year" title="Upper Class Twit of the Year">Upper Class Twit of the Year</a></li>
<li><a href="/wiki/Vocational_Guidance_Counsellor" title="Vocational Guidance Counsellor">Vocational Guidance Counsellor</a></li>
<li><a href="/wiki/World_Forum/Communist_Quiz" title="World Forum/Communist Quiz">World Forum/Communist Quiz</a></li></ul>
</div></td></tr><tr><th scope="row" class="navbox-group" style="width:1%">Songs</th><td class="navbox-list navbox-odd" style="text-align:left;border-left-width:2px;border-left-style:solid;width:100%;padding:0px"><div style="padding:0em 0.25em">
<ul><li>"<a href="/wiki/Always_Look_on_the_Bright_Side_of_Life" title="Always Look on the Bright Side of Life">Always Look on the Bright Side of Life</a>"</li>
<li>"<a href="/wiki/Brian_Song" title="Brian Song">Brian Song</a>"</li>
<li>"<a href="/wiki/Bruces%27_Philosophers_Song" title="Bruces&#39; Philosophers Song">Bruces' Philosophers Song</a>"</li>
<li>"<a href="/wiki/Decomposing_Composers" title="Decomposing Composers">Decomposing Composers</a>"</li>
<li>"<a href="/wiki/Eric_the_Half-a-Bee" title="Eric the Half-a-Bee">Eric the Half-a-Bee</a>"</li>
<li>"<a href="/wiki/Every_Sperm_Is_Sacred" title="Every Sperm Is Sacred">Every Sperm Is Sacred</a>"</li>
<li>"<a href="/wiki/Finland_(song)" title="Finland (song)">Finland</a>"</li>
<li>"<a href="/wiki/Galaxy_Song" title="Galaxy Song">Galaxy Song</a>"</li>
<li>"<a href="/wiki/I_Bet_You_They_Won%27t_Play_This_Song_on_the_Radio" title="I Bet You They Won&#39;t Play This Song on the Radio">I Bet You They Won't Play This Song on the Radio</a>"</li>
<li>"<a href="/wiki/I_Like_Chinese" title="I Like Chinese">I Like Chinese</a>"</li>
<li>"<a href="/wiki/I%27ve_Got_Two_Legs" title="I&#39;ve Got Two Legs">I've Got Two Legs</a>"</li>
<li>"<a href="/wiki/The_Lumberjack_Song" title="The Lumberjack Song">The Lumberjack Song</a>"</li>
<li>"<a href="/wiki/Medical_Love_Song" title="Medical Love Song">Medical Love Song</a>"</li>
<li>"<a href="/wiki/Never_Be_Rude_to_an_Arab" title="Never Be Rude to an Arab">Never Be Rude to an Arab</a>"</li>
<li>"<a href="/wiki/Oliver_Cromwell_(song)" title="Oliver Cromwell (song)">Oliver Cromwell</a>"</li>
<li>"<a href="/wiki/Sit_on_My_Face" title="Sit on My Face">Sit on My Face</a>"</li></ul>
</div></td></tr><tr><th scope="row" class="navbox-group" style="width:1%">Related articles</th><td class="navbox-list navbox-even" style="text-align:left;border-left-width:2px;border-left-style:solid;width:100%;padding:0px"><div style="padding:0em 0.25em">
<ul><li><a href="/wiki/List_of_Monty_Python_projects" title="List of Monty Python projects">List of Monty Python projects</a></li>
<li><a href="/wiki/The_Foot_of_Cupid" title="The Foot of Cupid">The Foot of Cupid</a></li>
<li><i><a href="/wiki/Cambridge_Footlights_Revue#&quot;A_Clump_of_Plinths&quot;_—_&quot;Cambridge_Circus&quot;" title="Cambridge Footlights Revue">Cambridge Circus</a></i></li>
<li><i><a href="/wiki/I%27m_Sorry,_I%27ll_Read_That_Again" title="I&#39;m Sorry, I&#39;ll Read That Again">I'm Sorry, I'll Read That Again</a></i></li>
<li><i><a href="/wiki/The_Frost_Report" title="The Frost Report">The Frost Report</a></i></li>
<li><i><a href="/wiki/At_Last_the_1948_Show" title="At Last the 1948 Show">At Last the 1948 Show</a></i></li>
<li><i><a href="/wiki/Twice_a_Fortnight" title="Twice a Fortnight">Twice a Fortnight</a></i></li>
<li><i><a href="/wiki/Do_Not_Adjust_Your_Set" title="Do Not Adjust Your Set">Do Not Adjust Your Set</a></i></li>
<li><i><a href="/wiki/We_Have_Ways_of_Making_You_Laugh" title="We Have Ways of Making You Laugh">We Have Ways of Making You Laugh</a></i></li>
<li><i><a href="/wiki/Broaden_Your_Mind" title="Broaden Your Mind">Broaden Your Mind</a></i></li>
<li><i><a href="/wiki/How_to_Irritate_People" title="How to Irritate People">How to Irritate People</a></i></li>
<li><i><a href="/wiki/The_Complete_and_Utter_History_of_Britain" title="The Complete and Utter History of Britain">The Complete and Utter History of Britain</a></i></li>
<li><i><a href="/wiki/Teach_Yourself_Heath" title="Teach Yourself Heath">Teach Yourself Heath</a></i></li>
<li><i><a href="/wiki/Monty_Python%27s_Tiny_Black_Round_Thing" title="Monty Python&#39;s Tiny Black Round Thing">Tiny Black Round Thing</a></i></li>
<li><i><a href="/wiki/Bert_Fegg%27s_Nasty_Book_for_Boys_and_Girls" title="Bert Fegg&#39;s Nasty Book for Boys and Girls">Bert Fegg's Nasty Book for Boys and Girls</a></i></li>
<li><i><a href="/wiki/Rutland_Weekend_Television" title="Rutland Weekend Television">Rutland Weekend Television</a></i></li>
<li><i><a href="/wiki/Fawlty_Towers" title="Fawlty Towers">Fawlty Towers</a></i></li>
<li><i><a href="/wiki/Ripping_Yarns" title="Ripping Yarns">Ripping Yarns</a></i></li>
<li><i><a href="/wiki/Out_of_the_Trees" title="Out of the Trees">Out of the Trees</a></i></li>
<li><i><a href="/wiki/A_Poke_in_the_Eye_(With_a_Sharp_Stick)" title="A Poke in the Eye (With a Sharp Stick)">A Poke in the Eye (With a Sharp Stick)</a></i></li>
<li><i><a href="/wiki/Python_On_Song" title="Python On Song">Python On Song</a></i></li>
<li><i><a href="/wiki/All_You_Need_Is_Cash" title="All You Need Is Cash">All You Need Is Cash</a></i></li>
<li><i><a href="/wiki/The_Secret_Policeman%27s_Ball" title="The Secret Policeman&#39;s Ball">The Secret Policeman's Ball</a></i></li>
<li><i><a href="/wiki/The_Hastily_Cobbled_Together_for_a_Fast_Buck_Album" title="The Hastily Cobbled Together for a Fast Buck Album">The Hastily Cobbled Together for a Fast Buck Album</a></i></li>
<li><i><a href="/wiki/Monty_Python_Live" title="Monty Python Live">Monty Python Live</a></i></li>
<li><i><a href="/wiki/Concert_for_George" title="Concert for George">Concert for George</a></i></li>
<li><i><a href="/wiki/Diaries_1969%E2%80%931979:_The_Python_Years" title="Diaries 1969–1979: The Python Years">Diaries 1969–1979: The Python Years</a></i></li>
<li><i><a href="/wiki/The_Seventh_Python" title="The Seventh Python">The Seventh Python</a></i></li>
<li><i><a href="/wiki/Holy_Flying_Circus" title="Holy Flying Circus">Holy Flying Circus</a></i></li>
<li><i><a href="/wiki/A_Liar%27s_Autobiography:_The_Untrue_Story_of_Monty_Python%27s_Graham_Chapman" title="A Liar&#39;s Autobiography: The Untrue Story of Monty Python&#39;s Graham Chapman">A Liar's Autobiography: The Untrue Story of Monty Python's Graham Chapman</a></i></li></ul>
</div></td></tr></tbody></table></div>
<div role="navigation" class="navbox" aria-labelledby="The_Rutles" style="padding:3px"><table class="nowraplinks hlist mw-collapsible autocollapse navbox-inner" style="border-spacing:0;background:transparent;color:inherit"><tbody><tr><th scope="col" class="navbox-title" colspan="2"><div class="plainlinks hlist navbar mini"><ul><li class="nv-view"><a href="/wiki/Template:The_Rutles" title="Template:The Rutles"><abbr title="View this template" style=";;background:none transparent;border:none;-moz-box-shadow:none;-webkit-box-shadow:none;box-shadow:none; padding:0;">v</abbr></a></li><li class="nv-talk"><a href="/wiki/Template_talk:The_Rutles" title="Template talk:The Rutles"><abbr title="Discuss this template" style=";;background:none transparent;border:none;-moz-box-shadow:none;-webkit-box-shadow:none;box-shadow:none; padding:0;">t</abbr></a></li><li class="nv-edit"><a class="external text" href="https://en.wikipedia.org/w/index.php?title=Template:The_Rutles&amp;action=edit"><abbr title="Edit this template" style=";;background:none transparent;border:none;-moz-box-shadow:none;-webkit-box-shadow:none;box-shadow:none; padding:0;">e</abbr></a></li></ul></div><div id="The_Rutles" style="font-size:114%;margin:0 4em"><a href="/wiki/The_Rutles" title="The Rutles">The Rutles</a></div></th></tr><tr><td class="navbox-abovebelow" colspan="2"><div id="*_Neil_Innes_*_Eric_Idle_*_John_Halsey_*_Ricky_Fataar_*_Ollie_Halsall_*_David_Battley">
<ul><li><a href="/wiki/Neil_Innes" title="Neil Innes">Neil Innes</a></li>
<li><a class="mw-selflink selflink">Eric Idle</a></li>
<li><a href="/wiki/John_Halsey_(musician)" title="John Halsey (musician)">John Halsey</a></li>
<li><a href="/wiki/Ricky_Fataar" title="Ricky Fataar">Ricky Fataar</a></li>
<li><a href="/wiki/Ollie_Halsall" title="Ollie Halsall">Ollie Halsall</a></li>
<li><a href="/wiki/David_Battley" title="David Battley">David Battley</a></li></ul>
</div></td></tr><tr><th scope="row" class="navbox-group" style="width:1%">TV series</th><td class="navbox-list navbox-odd" style="text-align:left;border-left-width:2px;border-left-style:solid;width:100%;padding:0px"><div style="padding:0em 0.25em">
<ul><li><i><a href="/wiki/Rutland_Weekend_Television" title="Rutland Weekend Television">Rutland Weekend Television</a></i></li></ul>
</div></td></tr><tr><th scope="row" class="navbox-group" style="width:1%">Films</th><td class="navbox-list navbox-even" style="text-align:left;border-left-width:2px;border-left-style:solid;width:100%;padding:0px"><div style="padding:0em 0.25em">
<ul><li><i><a href="/wiki/All_You_Need_Is_Cash" title="All You Need Is Cash">All You Need Is Cash</a></i></li>
<li><i><a href="/wiki/The_Rutles_2:_Can%27t_Buy_Me_Lunch" title="The Rutles 2: Can&#39;t Buy Me Lunch">The Rutles 2: Can't Buy Me Lunch</a></i></li></ul>
</div></td></tr><tr><th scope="row" class="navbox-group" style="width:1%">Music</th><td class="navbox-list navbox-odd" style="text-align:left;border-left-width:2px;border-left-style:solid;width:100%;padding:0px"><div style="padding:0em 0.25em">
<ul><li><i><a href="/wiki/The_Rutland_Weekend_Songbook" title="The Rutland Weekend Songbook">The Rutland Weekend Songbook</a></i> (1976)</li>
<li><a href="/wiki/The_Rutles_(album)" title="The Rutles (album)"><i>The Rutles</i> OST</a> (1978)</li>
<li><a href="/wiki/The_Rutles#Rutles_Highway_Revisited_(A_tribute_to_The_Rutles)" title="The Rutles"><i>Rutles Highway Revisited</i></a> (1993)</li>
<li><i><a href="/wiki/Archaeology_(album)" title="Archaeology (album)">Archaeology</a></i> (1996)</li></ul>
</div></td></tr></tbody></table></div>
<div role="navigation" class="navbox" aria-labelledby="Drama_Desk_Award_for_Outstanding_Lyrics" style="padding:3px"><table class="nowraplinks hlist mw-collapsible autocollapse navbox-inner" style="border-spacing:0;background:transparent;color:inherit"><tbody><tr><th scope="col" class="navbox-title" colspan="2" style="background: #D7F1D7;"><div class="plainlinks hlist navbar mini"><ul><li class="nv-view"><a href="/wiki/Template:DramaDesk_Lyrics" title="Template:DramaDesk Lyrics"><abbr title="View this template" style="background: #D7F1D7;;;background:none transparent;border:none;-moz-box-shadow:none;-webkit-box-shadow:none;box-shadow:none; padding:0;">v</abbr></a></li><li class="nv-talk"><a href="/wiki/Template_talk:DramaDesk_Lyrics" title="Template talk:DramaDesk Lyrics"><abbr title="Discuss this template" style="background: #D7F1D7;;;background:none transparent;border:none;-moz-box-shadow:none;-webkit-box-shadow:none;box-shadow:none; padding:0;">t</abbr></a></li><li class="nv-edit"><a class="external text" href="https://en.wikipedia.org/w/index.php?title=Template:DramaDesk_Lyrics&amp;action=edit"><abbr title="Edit this template" style="background: #D7F1D7;;;background:none transparent;border:none;-moz-box-shadow:none;-webkit-box-shadow:none;box-shadow:none; padding:0;">e</abbr></a></li></ul></div><div id="Drama_Desk_Award_for_Outstanding_Lyrics" style="font-size:114%;margin:0 4em"><a href="/wiki/Drama_Desk_Award_for_Outstanding_Lyrics" title="Drama Desk Award for Outstanding Lyrics">Drama Desk Award for Outstanding Lyrics</a></div></th></tr><tr><td colspan="2" class="navbox-list navbox-odd" style="width:100%;padding:0px"><div style="padding:0em 0.25em">
<ul><li><a href="/wiki/Fred_Ebb" title="Fred Ebb">Fred Ebb</a> (1969)</li>
<li><a href="/wiki/Stephen_Sondheim" title="Stephen Sondheim">Stephen Sondheim</a>/<a href="/wiki/Bertolt_Brecht" title="Bertolt Brecht">Bertolt Brecht</a> (1970)</li>
<li><a href="/wiki/Stephen_Sondheim" title="Stephen Sondheim">Stephen Sondheim</a> (1971)</li>
<li><a href="/wiki/John_Guare" title="John Guare">John Guare</a> (1972)</li>
<li><a href="/wiki/Stephen_Sondheim" title="Stephen Sondheim">Stephen Sondheim</a> (1973)</li>
<li><a href="/wiki/Al_Carmines" title="Al Carmines">Al Carmines</a> (1974)</li>
<li><a href="/wiki/Charlie_Smalls" title="Charlie Smalls">Charlie Smalls</a> (1975)</li>
<li><a href="/wiki/Edward_Kleban" title="Edward Kleban">Edward Kleban</a> (1976)</li>
<li><a href="/wiki/Martin_Charnin" title="Martin Charnin">Martin Charnin</a> (1977)</li>
<li><a href="/wiki/Carol_Hall" title="Carol Hall">Carol Hall</a> (1978)</li>
<li><a href="/wiki/Stephen_Sondheim" title="Stephen Sondheim">Stephen Sondheim</a> (1979)</li>
<li><a href="/wiki/Tim_Rice" title="Tim Rice">Tim Rice</a> (1980)</li>
<li><a href="/wiki/Stephen_Sondheim" title="Stephen Sondheim">Stephen Sondheim</a>/<a href="/wiki/Maury_Yeston" title="Maury Yeston">Maury Yeston</a> (1982)</li>
<li><a href="/wiki/Howard_Ashman" title="Howard Ashman">Howard Ashman</a> (1983)</li>
<li><a href="/wiki/Stephen_Sondheim" title="Stephen Sondheim">Stephen Sondheim</a> (1984)</li>
<li><a href="/wiki/Roger_Miller" title="Roger Miller">Roger Miller</a> (1985)</li>
<li><a href="/wiki/Stephen_Sondheim" title="Stephen Sondheim">Stephen Sondheim</a> (1988)</li>
<li><a href="/wiki/David_Zippel" title="David Zippel">David Zippel</a> (1990)</li>
<li><a href="/wiki/William_Finn" title="William Finn">William Finn</a> (1991)</li>
<li><a href="/wiki/Susan_Birkenhead" title="Susan Birkenhead">Susan Birkenhead</a> (1992)</li>
<li>Denis Markell and Douglas Bernstein (1993)</li>
<li><a href="/wiki/Stephen_Sondheim" title="Stephen Sondheim">Stephen Sondheim</a> (1994)</li>
<li><a href="/wiki/Jonathan_Larson" title="Jonathan Larson">Jonathan Larson</a> (1996)</li>
<li><a href="/wiki/Gerard_Alessandrini" title="Gerard Alessandrini">Gerard Alessandrini</a> (1997)</li>
<li><a href="/wiki/Lynn_Ahrens" title="Lynn Ahrens">Lynn Ahrens</a> (1998)</li>
<li><a href="/wiki/Gerard_Alessandrini" title="Gerard Alessandrini">Gerard Alessandrini</a> (1999)</li>
<li><a href="/wiki/Stephen_Sondheim" title="Stephen Sondheim">Stephen Sondheim</a> (2000)</li>
<li><a href="/wiki/Mel_Brooks" title="Mel Brooks">Mel Brooks</a> (2001)</li>
<li><a href="/wiki/Jason_Robert_Brown" title="Jason Robert Brown">Jason Robert Brown</a> (2002)</li>
<li><a href="/wiki/Scott_Wittman" title="Scott Wittman">Scott Wittman</a> and <a href="/wiki/Marc_Shaiman" title="Marc Shaiman">Marc Shaiman</a> (2003)</li>
<li><a href="/wiki/Stephen_Schwartz_(composer)" title="Stephen Schwartz (composer)">Stephen Schwartz</a> (2004)</li>
<li><a class="mw-selflink selflink">Eric Idle</a> (2005)</li>
<li><a href="/wiki/Lisa_Lambert" title="Lisa Lambert">Lisa Lambert</a> and <a href="/wiki/Greg_Morrison" title="Greg Morrison">Greg Morrison</a> (2006)</li>
<li><a href="/wiki/Steven_Sater" title="Steven Sater">Steven Sater</a> (2007)</li>
<li><a href="/wiki/Stew_(musician)" title="Stew (musician)">Stew</a> (2008)</li>
<li><a href="/wiki/Stephen_Sondheim" title="Stephen Sondheim">Stephen Sondheim</a> (2009)</li>
<li><a href="/wiki/John_Kander" title="John Kander">John Kander</a> and <a href="/wiki/Fred_Ebb" title="Fred Ebb">Fred Ebb</a> (2010)</li>
<li><a href="/wiki/Trey_Parker" title="Trey Parker">Trey Parker</a>, <a href="/wiki/Robert_Lopez" title="Robert Lopez">Robert Lopez</a> and <a href="/wiki/Matt_Stone" title="Matt Stone">Matt Stone</a> (2011)</li>
<li><a href="/wiki/Glen_Hansard" title="Glen Hansard">Glen Hansard</a> and <a href="/wiki/Mark%C3%A9ta_Irglov%C3%A1" title="Markéta Irglová">Markéta Irglová</a> (2012)</li>
<li><a href="/wiki/Tim_Minchin" title="Tim Minchin">Tim Minchin</a> (2013)</li>
<li><a href="/wiki/Robert_L._Freedman" title="Robert L. Freedman">Robert L. Freedman</a> and <a href="/wiki/Steven_Lutvak" title="Steven Lutvak">Steven Lutvak</a> (2014)</li>
<li><a href="/wiki/Lin-Manuel_Miranda" title="Lin-Manuel Miranda">Lin-Manuel Miranda</a> (2015)</li>
<li><a href="/wiki/Pasek_and_Paul" title="Pasek and Paul">Benj Pasek</a> and <a href="/wiki/Justin_Paul" title="Justin Paul">Justin Paul</a> (2016)</li>
<li><a href="/wiki/David_Yazbek" title="David Yazbek">David Yazbek</a> (2017)</li>
<li><a href="/wiki/Peter_Kellogg_(writer)" title="Peter Kellogg (writer)">Peter Kellogg</a> (2018)</li>
<li><a href="/wiki/David_Yazbek" title="David Yazbek">David Yazbek</a> (2019)</li>
<li><a href="/wiki/Michael_R._Jackson" title="Michael R. Jackson">Michael R. Jackson</a> (2020)</li></ul>
</div></td></tr></tbody></table></div>
<div role="navigation" class="navbox authority-control" aria-labelledby="Authority_control_frameless_&amp;#124;text-top_&amp;#124;10px_&amp;#124;alt=Edit_this_at_Wikidata_&amp;#124;link=https&amp;#58;//www.wikidata.org/wiki/Q210741&amp;#124;Edit_this_at_Wikidata" style="padding:3px"><table class="nowraplinks hlist navbox-inner" style="border-spacing:0;background:transparent;color:inherit"><tbody><tr><th id="Authority_control_frameless_&amp;#124;text-top_&amp;#124;10px_&amp;#124;alt=Edit_this_at_Wikidata_&amp;#124;link=https&amp;#58;//www.wikidata.org/wiki/Q210741&amp;#124;Edit_this_at_Wikidata" scope="row" class="navbox-group" style="width:1%"><a href="/wiki/Help:Authority_control" title="Help:Authority control">Authority control</a> <a href="https://www.wikidata.org/wiki/Q210741" title="Edit this at Wikidata"><img alt="Edit this at Wikidata" src="//upload.wikimedia.org/wikipedia/en/thumb/8/8a/OOjs_UI_icon_edit-ltr-progressive.svg/10px-OOjs_UI_icon_edit-ltr-progressive.svg.png" decoding="async" width="10" height="10" style="vertical-align: text-top" srcset="//upload.wikimedia.org/wikipedia/en/thumb/8/8a/OOjs_UI_icon_edit-ltr-progressive.svg/15px-OOjs_UI_icon_edit-ltr-progressive.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/8/8a/OOjs_UI_icon_edit-ltr-progressive.svg/20px-OOjs_UI_icon_edit-ltr-progressive.svg.png 2x" data-file-width="20" data-file-height="20" /></a></th><td class="navbox-list navbox-odd" style="text-align:left;border-left-width:2px;border-left-style:solid;width:100%;padding:0px"><div style="padding:0em 0.25em">
<ul><li><span class="nowrap"><a href="/wiki/Biblioteca_Nacional_de_Espa%C3%B1a" title="Biblioteca Nacional de España">BNE</a>: <span class="uid"><a rel="nofollow" class="external text" href="http://catalogo.bne.es/uhtbin/authoritybrowse.cgi?action=display&amp;authority_id=XX1363725">XX1363725</a></span></span></li>
<li><span class="nowrap"><a href="/wiki/BNF_(identifier)" class="mw-redirect" title="BNF (identifier)">BNF</a>: <span class="uid"><a rel="nofollow" class="external text" href="https://catalogue.bnf.fr/ark:/12148/cb14031373m">cb14031373m</a> <a rel="nofollow" class="external text" href="https://data.bnf.fr/ark:/12148/cb14031373m">(data)</a></span></span></li>
<li><span class="nowrap"><a href="/wiki/GND_(identifier)" class="mw-redirect" title="GND (identifier)">GND</a>: <span class="uid"><a rel="nofollow" class="external text" href="https://d-nb.info/gnd/114797145">114797145</a></span></span></li>
<li><span class="nowrap"><a href="/wiki/ISNI_(identifier)" class="mw-redirect" title="ISNI (identifier)">ISNI</a>: <span class="uid"><a rel="nofollow" class="external text" href="http://isni.org/isni/0000000121367272">0000 0001 2136 7272</a></span></span></li>
<li><span class="nowrap"><a href="/wiki/LCCN_(identifier)" class="mw-redirect" title="LCCN (identifier)">LCCN</a>: <span class="uid"><a rel="nofollow" class="external text" href="https://id.loc.gov/authorities/names/n50031974">n50031974</a></span></span></li>
<li><span class="nowrap"><a href="/wiki/MusicBrainz" title="MusicBrainz">MusicBrainz</a>: <span class="uid"><a rel="nofollow" class="external text" href="https://musicbrainz.org/artist/c4b096cb-ffa2-48d2-81a2-04a498c7c5f8">c4b096cb-ffa2-48d2-81a2-04a498c7c5f8</a></span></span></li>
<li><span class="nowrap"><a href="/wiki/National_Library_of_the_Czech_Republic" title="National Library of the Czech Republic">NKC</a>: <span class="uid"><a rel="nofollow" class="external text" href="https://aleph.nkp.cz/F/?func=find-c&amp;local_base=aut&amp;ccl_term=ica=xx0004411&amp;CON_LNG=ENG">xx0004411</a></span></span></li>
<li><span class="nowrap"><a href="/wiki/Royal_Library_of_the_Netherlands" title="Royal Library of the Netherlands">NTA</a>: <span class="uid"><a rel="nofollow" class="external text" href="http://data.bibliotheken.nl/id/thes/p071593195">071593195</a></span></span></li>
<li><span class="nowrap"><a href="/wiki/SELIBR_(identifier)" class="mw-redirect" title="SELIBR (identifier)">SELIBR</a>: <span class="uid"><a rel="nofollow" class="external text" href="https://libris.kb.se/auth/331789">331789</a></span></span></li>
<li><span class="nowrap"><a href="/wiki/SUDOC_(identifier)" class="mw-redirect" title="SUDOC (identifier)">SUDOC</a>: <span class="uid"><a rel="nofollow" class="external text" href="https://www.idref.fr/055675735">055675735</a></span></span></li>
<li><span class="nowrap"><a href="/wiki/Trove" title="Trove">Trove</a>: <span class="uid"><a rel="nofollow" class="external text" href="https://trove.nla.gov.au/people/869805">869805</a></span></span></li>
<li><span class="nowrap"><a href="/wiki/VIAF_(identifier)" class="mw-redirect" title="VIAF (identifier)">VIAF</a>: <span class="uid"><a rel="nofollow" class="external text" href="https://viaf.org/viaf/64205965">64205965</a></span></span></li>
<li><span class="nowrap"> <a href="/wiki/WorldCat_Identities" class="mw-redirect" title="WorldCat Identities">WorldCat Identities</a>: <a rel="nofollow" class="external text" href="https://www.worldcat.org/identities/lccn-n50031974">lccn-n50031974</a></span></li></ul>
</div></td></tr></tbody></table></div>
<!-- 
NewPP limit report
Parsed by mw1391
Cached time: 20200721135736
Cache expiry: 2592000
Dynamic content: false
Complications: [vary‐revision‐sha1]
CPU time usage: 0.952 seconds
Real time usage: 1.442 seconds
Preprocessor visited node count: 7338/1000000
Post‐expand include size: 149364/2097152 bytes
Template argument size: 11297/2097152 bytes
Highest expansion depth: 17/40
Expensive parser function count: 15/500
Unstrip recursion depth: 1/20
Unstrip post‐expand size: 188600/5000000 bytes
Lua time usage: 0.370/10.000 seconds
Lua memory usage: 9.16 MB/50 MB
Number of Wikibase entities loaded: 1/400
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00% 1249.136      1 -total
 24.99%  312.176      1 Template:Reflist
 22.83%  285.202      1 Template:Infobox_person
 20.05%  250.465      1 Template:Infobox
 14.36%  179.326     11 Template:ISBN
 10.45%  130.574     24 Template:Cite_web
  8.98%  112.222      5 Template:Br_separated_entries
  8.07%  100.768     11 Template:Catalog_lookup_link
  6.32%   78.909      1 Template:Birth_date_and_age
  5.44%   67.922      2 Template:Marriage
-->

<!-- Saved in parser cache with key enwiki:pcache:idhash:52042-0!canonical and timestamp 20200721135734 and revision id 968641123
 -->
</div><noscript><img src="//en.wikipedia.org/wiki/Special:CentralAutoLogin/start?type=1x1" alt="" title="" width="1" height="1" style="border: none; position: absolute;" /></noscript></div><div class="printfooter">Retrieved from "<a dir="ltr" href="https://en.wikipedia.org/w/index.php?title=Eric_Idle&amp;oldid=968641123">https://en.wikipedia.org/w/index.php?title=Eric_Idle&amp;oldid=968641123</a>"</div>
		<div id="catlinks" class="catlinks" data-mw="interface"><div id="mw-normal-catlinks" class="mw-normal-catlinks"><a href="/wiki/Help:Category" title="Help:Category">Categories</a>: <ul><li><a href="/wiki/Category:1943_births" title="Category:1943 births">1943 births</a></li><li><a href="/wiki/Category:20th-century_English_comedians" title="Category:20th-century English comedians">20th-century English comedians</a></li><li><a href="/wiki/Category:20th-century_English_male_actors" title="Category:20th-century English male actors">20th-century English male actors</a></li><li><a href="/wiki/Category:20th-century_English_composers" title="Category:20th-century English composers">20th-century English composers</a></li><li><a href="/wiki/Category:20th-century_English_novelists" title="Category:20th-century English novelists">20th-century English novelists</a></li><li><a href="/wiki/Category:20th-century_English_singers" title="Category:20th-century English singers">20th-century English singers</a></li><li><a href="/wiki/Category:21st-century_English_comedians" title="Category:21st-century English comedians">21st-century English comedians</a></li><li><a href="/wiki/Category:21st-century_English_male_actors" title="Category:21st-century English male actors">21st-century English male actors</a></li><li><a href="/wiki/Category:21st-century_British_composers" title="Category:21st-century British composers">21st-century British composers</a></li><li><a href="/wiki/Category:21st-century_English_novelists" title="Category:21st-century English novelists">21st-century English novelists</a></li><li><a href="/wiki/Category:21st-century_English_singers" title="Category:21st-century English singers">21st-century English singers</a></li><li><a href="/wiki/Category:Actors_from_County_Durham" title="Category:Actors from County Durham">Actors from County Durham</a></li><li><a href="/wiki/Category:Alumni_of_Pembroke_College,_Cambridge" title="Category:Alumni of Pembroke College, Cambridge">Alumni of Pembroke College, Cambridge</a></li><li><a href="/wiki/Category:Drama_Desk_Award_winners" title="Category:Drama Desk Award winners">Drama Desk Award winners</a></li><li><a href="/wiki/Category:English_comedy_musicians" title="Category:English comedy musicians">English comedy musicians</a></li><li><a href="/wiki/Category:British_novelty_song_performers" title="Category:British novelty song performers">British novelty song performers</a></li><li><a href="/wiki/Category:British_surrealist_artists" title="Category:British surrealist artists">British surrealist artists</a></li><li><a href="/wiki/Category:English_comedy_writers" title="Category:English comedy writers">English comedy writers</a></li><li><a href="/wiki/Category:English_dramatists_and_playwrights" title="Category:English dramatists and playwrights">English dramatists and playwrights</a></li><li><a href="/wiki/Category:British_expatriate_male_actors_in_the_United_States" title="Category:British expatriate male actors in the United States">British expatriate male actors in the United States</a></li><li><a href="/wiki/Category:British_male_comedy_actors" title="Category:British male comedy actors">British male comedy actors</a></li><li><a href="/wiki/Category:English_male_comedians" title="Category:English male comedians">English male comedians</a></li><li><a href="/wiki/Category:English_male_composers" title="Category:English male composers">English male composers</a></li><li><a href="/wiki/Category:English_male_dramatists_and_playwrights" title="Category:English male dramatists and playwrights">English male dramatists and playwrights</a></li><li><a href="/wiki/Category:English_male_film_actors" title="Category:English male film actors">English male film actors</a></li><li><a href="/wiki/Category:English_male_novelists" title="Category:English male novelists">English male novelists</a></li><li><a href="/wiki/Category:English_male_radio_actors" title="Category:English male radio actors">English male radio actors</a></li><li><a href="/wiki/Category:English_male_television_actors" title="Category:English male television actors">English male television actors</a></li><li><a href="/wiki/Category:English_male_voice_actors" title="Category:English male voice actors">English male voice actors</a></li><li><a href="/wiki/Category:English_musical_theatre_composers" title="Category:English musical theatre composers">English musical theatre composers</a></li><li><a href="/wiki/Category:English_singer-songwriters" title="Category:English singer-songwriters">English singer-songwriters</a></li><li><a href="/wiki/Category:English_television_writers" title="Category:English television writers">English television writers</a></li><li><a href="/wiki/Category:Grammy_Award_winners" title="Category:Grammy Award winners">Grammy Award winners</a></li><li><a href="/wiki/Category:Living_people" title="Category:Living people">Living people</a></li><li><a href="/wiki/Category:Male_screenwriters" title="Category:Male screenwriters">Male screenwriters</a></li><li><a href="/wiki/Category:Monty_Python_members" title="Category:Monty Python members">Monty Python members</a></li><li><a href="/wiki/Category:Musicians_from_Tyne_and_Wear" title="Category:Musicians from Tyne and Wear">Musicians from Tyne and Wear</a></li><li><a href="/wiki/Category:People_educated_at_the_Royal_Wolverhampton_School" title="Category:People educated at the Royal Wolverhampton School">People educated at the Royal Wolverhampton School</a></li><li><a href="/wiki/Category:People_from_South_Shields" title="Category:People from South Shields">People from South Shields</a></li><li><a href="/wiki/Category:People_from_Wolverhampton" title="Category:People from Wolverhampton">People from Wolverhampton</a></li><li><a href="/wiki/Category:The_Rutles_members" title="Category:The Rutles members">The Rutles members</a></li><li><a href="/wiki/Category:Male_television_writers" title="Category:Male television writers">Male television writers</a></li><li><a href="/wiki/Category:English_atheists" title="Category:English atheists">English atheists</a></li><li><a href="/wiki/Category:English_agnostics" title="Category:English agnostics">English agnostics</a></li></ul></div><div id="mw-hidden-catlinks" class="mw-hidden-catlinks mw-hidden-cats-hidden">Hidden categories: <ul><li><a href="/wiki/Category:All_articles_with_dead_external_links" title="Category:All articles with dead external links">All articles with dead external links</a></li><li><a href="/wiki/Category:Articles_with_dead_external_links_from_December_2013" title="Category:Articles with dead external links from December 2013">Articles with dead external links from December 2013</a></li><li><a href="/wiki/Category:Webarchive_template_wayback_links" title="Category:Webarchive template wayback links">Webarchive template wayback links</a></li><li><a href="/wiki/Category:Use_British_English_from_November_2012" title="Category:Use British English from November 2012">Use British English from November 2012</a></li><li><a href="/wiki/Category:Use_dmy_dates_from_October_2017" title="Category:Use dmy dates from October 2017">Use dmy dates from October 2017</a></li><li><a href="/wiki/Category:Articles_with_hCards" title="Category:Articles with hCards">Articles with hCards</a></li><li><a href="/wiki/Category:Articles_with_IBDb_links" title="Category:Articles with IBDb links">Articles with IBDb links</a></li><li><a href="/wiki/Category:Internet_Off-Broadway_Database_person_ID_same_as_Wikidata" title="Category:Internet Off-Broadway Database person ID same as Wikidata">Internet Off-Broadway Database person ID same as Wikidata</a></li><li><a href="/wiki/Category:Wikipedia_articles_with_BNE_identifiers" title="Category:Wikipedia articles with BNE identifiers">Wikipedia articles with BNE identifiers</a></li><li><a href="/wiki/Category:Wikipedia_articles_with_BNF_identifiers" title="Category:Wikipedia articles with BNF identifiers">Wikipedia articles with BNF identifiers</a></li><li><a href="/wiki/Category:Wikipedia_articles_with_GND_identifiers" title="Category:Wikipedia articles with GND identifiers">Wikipedia articles with GND identifiers</a></li><li><a href="/wiki/Category:Wikipedia_articles_with_ISNI_identifiers" title="Category:Wikipedia articles with ISNI identifiers">Wikipedia articles with ISNI identifiers</a></li><li><a href="/wiki/Category:Wikipedia_articles_with_LCCN_identifiers" title="Category:Wikipedia articles with LCCN identifiers">Wikipedia articles with LCCN identifiers</a></li><li><a href="/wiki/Category:Wikipedia_articles_with_MusicBrainz_identifiers" title="Category:Wikipedia articles with MusicBrainz identifiers">Wikipedia articles with MusicBrainz identifiers</a></li><li><a href="/wiki/Category:Wikipedia_articles_with_NKC_identifiers" title="Category:Wikipedia articles with NKC identifiers">Wikipedia articles with NKC identifiers</a></li><li><a href="/wiki/Category:Wikipedia_articles_with_NTA_identifiers" title="Category:Wikipedia articles with NTA identifiers">Wikipedia articles with NTA identifiers</a></li><li><a href="/wiki/Category:Wikipedia_articles_with_SELIBR_identifiers" title="Category:Wikipedia articles with SELIBR identifiers">Wikipedia articles with SELIBR identifiers</a></li><li><a href="/wiki/Category:Wikipedia_articles_with_SUDOC_identifiers" title="Category:Wikipedia articles with SUDOC identifiers">Wikipedia articles with SUDOC identifiers</a></li><li><a href="/wiki/Category:Wikipedia_articles_with_Trove_identifiers" title="Category:Wikipedia articles with Trove identifiers">Wikipedia articles with Trove identifiers</a></li><li><a href="/wiki/Category:Wikipedia_articles_with_VIAF_identifiers" title="Category:Wikipedia articles with VIAF identifiers">Wikipedia articles with VIAF identifiers</a></li><li><a href="/wiki/Category:Wikipedia_articles_with_WorldCat_identifiers" title="Category:Wikipedia articles with WorldCat identifiers">Wikipedia articles with WorldCat identifiers</a></li></ul></div></div>
	</div>
</div>
<div id='mw-data-after-content'>
	<div class="read-more-container"></div>
</div>

<div id="mw-navigation">
	<h2>Navigation menu</h2>
	<div id="mw-head">
		<!-- Please do not use role attribute as CSS selector, it is deprecated. -->
<nav id="p-personal" class="vector-menu" aria-labelledby="p-personal-label" role="navigation" 
	 >
	<h3 id="p-personal-label">
		<span>Personal tools</span>
	</h3>
	<!-- Please do not use the .body class, it is deprecated. -->
	<div class="body vector-menu-content">
		<!-- Please do not use the .menu class, it is deprecated. -->
		<ul class="vector-menu-content-list"><li id="pt-anonuserpage">Not logged in</li><li id="pt-anontalk"><a href="/wiki/Special:MyTalk" title="Discussion about edits from this IP address [n]" accesskey="n">Talk</a></li><li id="pt-anoncontribs"><a href="/wiki/Special:MyContributions" title="A list of edits made from this IP address [y]" accesskey="y">Contributions</a></li><li id="pt-createaccount"><a href="/w/index.php?title=Special:CreateAccount&amp;returnto=Eric+Idle" title="You are encouraged to create an account and log in; however, it is not mandatory">Create account</a></li><li id="pt-login"><a href="/w/index.php?title=Special:UserLogin&amp;returnto=Eric+Idle" title="You&#039;re encouraged to log in; however, it&#039;s not mandatory. [o]" accesskey="o">Log in</a></li></ul>

	</div>
</nav>


		<div id="left-navigation">
			<!-- Please do not use role attribute as CSS selector, it is deprecated. -->
<nav id="p-namespaces" class="vector-menu vector-menu-tabs vectorTabs" aria-labelledby="p-namespaces-label" role="navigation" 
	 >
	<h3 id="p-namespaces-label">
		<span>Namespaces</span>
	</h3>
	<!-- Please do not use the .body class, it is deprecated. -->
	<div class="body vector-menu-content">
		<!-- Please do not use the .menu class, it is deprecated. -->
		<ul class="vector-menu-content-list"><li id="ca-nstab-main" class="selected"><a href="/wiki/Eric_Idle" title="View the content page [c]" accesskey="c">Article</a></li><li id="ca-talk"><a href="/wiki/Talk:Eric_Idle" rel="discussion" title="Discuss improvements to the content page [t]" accesskey="t">Talk</a></li></ul>

	</div>
</nav>


			<!-- Please do not use role attribute as CSS selector, it is deprecated. -->
<nav id="p-variants" class="vector-menu-empty emptyPortlet vector-menu vector-menu-dropdown vectorMenu" aria-labelledby="p-variants-label" role="navigation" 
	 >
	<input type="checkbox" class="vector-menu-checkbox vectorMenuCheckbox" aria-labelledby="p-variants-label" />
	<h3 id="p-variants-label">
		<span>Variants</span>
	</h3>
	<!-- Please do not use the .body class, it is deprecated. -->
	<div class="body vector-menu-content">
		<!-- Please do not use the .menu class, it is deprecated. -->
		<ul class="menu vector-menu-content-list"></ul>

	</div>
</nav>


		</div>
		<div id="right-navigation">
			<!-- Please do not use role attribute as CSS selector, it is deprecated. -->
<nav id="p-views" class="vector-menu vector-menu-tabs vectorTabs" aria-labelledby="p-views-label" role="navigation" 
	 >
	<h3 id="p-views-label">
		<span>Views</span>
	</h3>
	<!-- Please do not use the .body class, it is deprecated. -->
	<div class="body vector-menu-content">
		<!-- Please do not use the .menu class, it is deprecated. -->
		<ul class="vector-menu-content-list"><li id="ca-view" class="collapsible selected"><a href="/wiki/Eric_Idle">Read</a></li><li id="ca-edit" class="collapsible"><a href="/w/index.php?title=Eric_Idle&amp;action=edit" title="Edit this page [e]" accesskey="e">Edit</a></li><li id="ca-history" class="collapsible"><a href="/w/index.php?title=Eric_Idle&amp;action=history" title="Past revisions of this page [h]" accesskey="h">View history</a></li></ul>

	</div>
</nav>


			<!-- Please do not use role attribute as CSS selector, it is deprecated. -->
<nav id="p-cactions" class="vector-menu-empty emptyPortlet vector-menu vector-menu-dropdown vectorMenu" aria-labelledby="p-cactions-label" role="navigation" 
	 >
	<input type="checkbox" class="vector-menu-checkbox vectorMenuCheckbox" aria-labelledby="p-cactions-label" />
	<h3 id="p-cactions-label">
		<span>More</span>
	</h3>
	<!-- Please do not use the .body class, it is deprecated. -->
	<div class="body vector-menu-content">
		<!-- Please do not use the .menu class, it is deprecated. -->
		<ul class="menu vector-menu-content-list"></ul>

	</div>
</nav>


			<div id="p-search" role="search">
	<h3 >
		<label for="searchInput">Search</label>
	</h3>
	<form action="/w/index.php" id="searchform">
		<div id="simpleSearch">
			<input type="search" name="search" placeholder="Search Wikipedia" title="Search Wikipedia [f]" accesskey="f" id="searchInput"/>
			<input type="hidden" name="title" value="Special:Search">
			<input type="submit" name="fulltext" value="Search" title="Search Wikipedia for this text" id="mw-searchButton" class="searchButton mw-fallbackSearchButton"/>
			<input type="submit" name="go" value="Go" title="Go to a page with this exact name if it exists" id="searchButton" class="searchButton"/>
		</div>
	</form>
</div>

		</div>
	</div>

<div id="mw-panel">
	<div id="p-logo" role="banner">
		<a  title="Visit the main page" class="mw-wiki-logo" href="/wiki/Main_Page"></a>
	</div>
	<!-- Please do not use role attribute as CSS selector, it is deprecated. -->
<nav id="p-navigation" class="vector-menu vector-menu-portal portal portal-first" aria-labelledby="p-navigation-label" role="navigation" 
	 >
	<h3 id="p-navigation-label">
		<span>Navigation</span>
	</h3>
	<!-- Please do not use the .body class, it is deprecated. -->
	<div class="body vector-menu-content">
		<!-- Please do not use the .menu class, it is deprecated. -->
		<ul class="vector-menu-content-list"><li id="n-mainpage-description"><a href="/wiki/Main_Page" title="Visit the main page [z]" accesskey="z">Main page</a></li><li id="n-contents"><a href="/wiki/Wikipedia:Contents" title="Guides to browsing Wikipedia">Contents</a></li><li id="n-currentevents"><a href="/wiki/Portal:Current_events" title="Find background information on current events">Current events</a></li><li id="n-randompage"><a href="/wiki/Special:Random" title="Visit a randomly selected article [x]" accesskey="x">Random article</a></li><li id="n-aboutsite"><a href="/wiki/Wikipedia:About" title="Learn about Wikipedia and how it works">About Wikipedia</a></li><li id="n-contactpage"><a href="//en.wikipedia.org/wiki/Wikipedia:Contact_us" title="How to contact Wikipedia">Contact us</a></li><li id="n-sitesupport"><a href="https://donate.wikimedia.org/wiki/Special:FundraiserRedirector?utm_source=donate&amp;utm_medium=sidebar&amp;utm_campaign=C13_en.wikipedia.org&amp;uselang=en" title="Support us by donating to the Wikimedia Foundation">Donate</a></li><li id="n-shoplink"><a href="//shop.wikimedia.org" title="Visit the Wikipedia store">Wikipedia store</a></li></ul>

	</div>
</nav>


	<!-- Please do not use role attribute as CSS selector, it is deprecated. -->
<nav id="p-interaction" class="vector-menu vector-menu-portal portal" aria-labelledby="p-interaction-label" role="navigation" 
	 >
	<h3 id="p-interaction-label">
		<span>Contribute</span>
	</h3>
	<!-- Please do not use the .body class, it is deprecated. -->
	<div class="body vector-menu-content">
		<!-- Please do not use the .menu class, it is deprecated. -->
		<ul class="vector-menu-content-list"><li id="n-help"><a href="/wiki/Help:Contents" title="Guidance on how to use and edit Wikipedia">Help</a></li><li id="n-portal"><a href="/wiki/Wikipedia:Community_portal" title="About the project, what you can do, where to find things">Community portal</a></li><li id="n-recentchanges"><a href="/wiki/Special:RecentChanges" title="A list of recent changes to Wikipedia [r]" accesskey="r">Recent changes</a></li><li id="n-upload"><a href="/wiki/Wikipedia:File_Upload_Wizard" title="Add images or other media for use on Wikipedia">Upload file</a></li></ul>

	</div>
</nav>

<!-- Please do not use role attribute as CSS selector, it is deprecated. -->
<nav id="p-tb" class="vector-menu vector-menu-portal portal" aria-labelledby="p-tb-label" role="navigation" 
	 >
	<h3 id="p-tb-label">
		<span>Tools</span>
	</h3>
	<!-- Please do not use the .body class, it is deprecated. -->
	<div class="body vector-menu-content">
		<!-- Please do not use the .menu class, it is deprecated. -->
		<ul class="vector-menu-content-list"><li id="t-whatlinkshere"><a href="/wiki/Special:WhatLinksHere/Eric_Idle" title="List of all English Wikipedia pages containing links to this page [j]" accesskey="j">What links here</a></li><li id="t-recentchangeslinked"><a href="/wiki/Special:RecentChangesLinked/Eric_Idle" rel="nofollow" title="Recent changes in pages linked from this page [k]" accesskey="k">Related changes</a></li><li id="t-upload"><a href="/wiki/Wikipedia:File_Upload_Wizard" title="Upload files [u]" accesskey="u">Upload file</a></li><li id="t-specialpages"><a href="/wiki/Special:SpecialPages" title="A list of all special pages [q]" accesskey="q">Special pages</a></li><li id="t-permalink"><a href="/w/index.php?title=Eric_Idle&amp;oldid=968641123" title="Permanent link to this revision of this page">Permanent link</a></li><li id="t-info"><a href="/w/index.php?title=Eric_Idle&amp;action=info" title="More information about this page">Page information</a></li><li id="t-cite"><a href="/w/index.php?title=Special:CiteThisPage&amp;page=Eric_Idle&amp;id=968641123&amp;wpFormIdentifier=titleform" title="Information on how to cite this page">Cite this page</a></li><li id="t-wikibase"><a href="https://www.wikidata.org/wiki/Special:EntityPage/Q210741" title="Structured data on this page hosted by Wikidata [g]" accesskey="g">Wikidata item</a></li></ul>

	</div>
</nav>

<!-- Please do not use role attribute as CSS selector, it is deprecated. -->
<nav id="p-coll-print_export" class="vector-menu vector-menu-portal portal" aria-labelledby="p-coll-print_export-label" role="navigation" 
	 >
	<h3 id="p-coll-print_export-label">
		<span>Print/export</span>
	</h3>
	<!-- Please do not use the .body class, it is deprecated. -->
	<div class="body vector-menu-content">
		<!-- Please do not use the .menu class, it is deprecated. -->
		<ul class="vector-menu-content-list"><li id="coll-download-as-rl"><a href="/w/index.php?title=Special:ElectronPdf&amp;page=Eric+Idle&amp;action=show-download-screen" title="Download this page as a PDF file">Download as PDF</a></li><li id="t-print"><a href="/w/index.php?title=Eric_Idle&amp;printable=yes" title="Printable version of this page [p]" accesskey="p">Printable version</a></li></ul>

	</div>
</nav>

<!-- Please do not use role attribute as CSS selector, it is deprecated. -->
<nav id="p-wikibase-otherprojects" class="vector-menu vector-menu-portal portal" aria-labelledby="p-wikibase-otherprojects-label" role="navigation" 
	 >
	<h3 id="p-wikibase-otherprojects-label">
		<span>In other projects</span>
	</h3>
	<!-- Please do not use the .body class, it is deprecated. -->
	<div class="body vector-menu-content">
		<!-- Please do not use the .menu class, it is deprecated. -->
		<ul class="vector-menu-content-list"><li class="wb-otherproject-link wb-otherproject-commons"><a href="https://commons.wikimedia.org/wiki/Category:Eric_Idle" hreflang="en">Wikimedia Commons</a></li><li class="wb-otherproject-link wb-otherproject-wikiquote"><a href="https://en.wikiquote.org/wiki/Eric_Idle" hreflang="en">Wikiquote</a></li></ul>

	</div>
</nav>


	<!-- Please do not use role attribute as CSS selector, it is deprecated. -->
<nav id="p-lang" class="vector-menu vector-menu-portal portal" aria-labelledby="p-lang-label" role="navigation" 
	 >
	<h3 id="p-lang-label">
		<span>Languages</span>
	</h3>
	<!-- Please do not use the .body class, it is deprecated. -->
	<div class="body vector-menu-content">
		<!-- Please do not use the .menu class, it is deprecated. -->
		<ul class="vector-menu-content-list"><li class="interlanguage-link interwiki-de"><a href="https://de.wikipedia.org/wiki/Eric_Idle" title="Eric Idle – German" lang="de" hreflang="de" class="interlanguage-link-target">Deutsch</a></li><li class="interlanguage-link interwiki-fr"><a href="https://fr.wikipedia.org/wiki/Eric_Idle" title="Eric Idle – French" lang="fr" hreflang="fr" class="interlanguage-link-target">Français</a></li><li class="interlanguage-link interwiki-es"><a href="https://es.wikipedia.org/wiki/Eric_Idle" title="Eric Idle – Spanish" lang="es" hreflang="es" class="interlanguage-link-target">Español</a></li><li class="interlanguage-link interwiki-ru"><a href="https://ru.wikipedia.org/wiki/%D0%90%D0%B9%D0%B4%D0%BB,_%D0%AD%D1%80%D0%B8%D0%BA" title="Айдл, Эрик – Russian" lang="ru" hreflang="ru" class="interlanguage-link-target">Русский</a></li><li class="interlanguage-link interwiki-it"><a href="https://it.wikipedia.org/wiki/Eric_Idle" title="Eric Idle – Italian" lang="it" hreflang="it" class="interlanguage-link-target">Italiano</a></li><li class="interlanguage-link interwiki-ja"><a href="https://ja.wikipedia.org/wiki/%E3%82%A8%E3%83%AA%E3%83%83%E3%82%AF%E3%83%BB%E3%82%A2%E3%82%A4%E3%83%89%E3%83%AB" title="エリック・アイドル – Japanese" lang="ja" hreflang="ja" class="interlanguage-link-target">日本語</a></li><li class="interlanguage-link interwiki-nl"><a href="https://nl.wikipedia.org/wiki/Eric_Idle" title="Eric Idle – Dutch" lang="nl" hreflang="nl" class="interlanguage-link-target">Nederlands</a></li><li class="interlanguage-link interwiki-pl"><a href="https://pl.wikipedia.org/wiki/Eric_Idle" title="Eric Idle – Polish" lang="pl" hreflang="pl" class="interlanguage-link-target">Polski</a></li><li class="interlanguage-link interwiki-pt"><a href="https://pt.wikipedia.org/wiki/Eric_Idle" title="Eric Idle – Portuguese" lang="pt" hreflang="pt" class="interlanguage-link-target">Português</a></li><li class="interlanguage-link interwiki-zh"><a href="https://zh.wikipedia.org/wiki/%E5%9F%83%E9%87%8C%E5%85%8B%C2%B7%E8%89%BE%E5%BE%B7%E5%B0%94" title="埃里克·艾德尔 – Chinese" lang="zh" hreflang="zh" class="interlanguage-link-target">中文</a></li><li class="interlanguage-link interwiki-sv"><a href="https://sv.wikipedia.org/wiki/Eric_Idle" title="Eric Idle – Swedish" lang="sv" hreflang="sv" class="interlanguage-link-target">Svenska</a></li><li class="interlanguage-link interwiki-fa"><a href="https://fa.wikipedia.org/wiki/%D8%A7%D8%B1%DB%8C%DA%A9_%D8%A2%DB%8C%D8%AF%D9%84" title="اریک آیدل – Persian" lang="fa" hreflang="fa" class="interlanguage-link-target">فارسی</a></li><li class="interlanguage-link interwiki-he"><a href="https://he.wikipedia.org/wiki/%D7%90%D7%A8%D7%99%D7%A7_%D7%90%D7%99%D7%99%D7%93%D7%9C" title="אריק איידל – Hebrew" lang="he" hreflang="he" class="interlanguage-link-target">עברית</a></li><li class="interlanguage-link interwiki-tr"><a href="https://tr.wikipedia.org/wiki/Eric_Idle" title="Eric Idle – Turkish" lang="tr" hreflang="tr" class="interlanguage-link-target">Türkçe</a></li><li class="interlanguage-link interwiki-hu"><a href="https://hu.wikipedia.org/wiki/Eric_Idle" title="Eric Idle – Hungarian" lang="hu" hreflang="hu" class="interlanguage-link-target">Magyar</a></li><li class="interlanguage-link interwiki-fi"><a href="https://fi.wikipedia.org/wiki/Eric_Idle" title="Eric Idle – Finnish" lang="fi" hreflang="fi" class="interlanguage-link-target">Suomi</a></li><li class="interlanguage-link interwiki-no"><a href="https://no.wikipedia.org/wiki/Eric_Idle" title="Eric Idle – Norwegian Bokmål" lang="nb" hreflang="nb" class="interlanguage-link-target">Norsk bokmål</a></li><li class="interlanguage-link interwiki-uk"><a href="https://uk.wikipedia.org/wiki/%D0%95%D1%80%D1%96%D0%BA_%D0%90%D0%B9%D0%B4%D0%BB" title="Ерік Айдл – Ukrainian" lang="uk" hreflang="uk" class="interlanguage-link-target">Українська</a></li><li class="interlanguage-link interwiki-ko"><a href="https://ko.wikipedia.org/wiki/%EC%97%90%EB%A6%AD_%EC%95%84%EC%9D%B4%EB%93%A4" title="에릭 아이들 – Korean" lang="ko" hreflang="ko" class="interlanguage-link-target">한국어</a></li><li class="interlanguage-link interwiki-ca"><a href="https://ca.wikipedia.org/wiki/Eric_Idle" title="Eric Idle – Catalan" lang="ca" hreflang="ca" class="interlanguage-link-target">Català</a></li><li class="interlanguage-link interwiki-cs"><a href="https://cs.wikipedia.org/wiki/Eric_Idle" title="Eric Idle – Czech" lang="cs" hreflang="cs" class="interlanguage-link-target">Čeština</a></li><li class="interlanguage-link interwiki-sr"><a href="https://sr.wikipedia.org/wiki/%D0%95%D1%80%D0%B8%D0%BA_%D0%90%D1%98%D0%B4%D0%BB" title="Ерик Ајдл – Serbian" lang="sr" hreflang="sr" class="interlanguage-link-target">Српски / srpski</a></li><li class="interlanguage-link interwiki-ro"><a href="https://ro.wikipedia.org/wiki/Eric_Idle" title="Eric Idle – Romanian" lang="ro" hreflang="ro" class="interlanguage-link-target">Română</a></li><li class="interlanguage-link interwiki-id"><a href="https://id.wikipedia.org/wiki/Eric_Idle" title="Eric Idle – Indonesian" lang="id" hreflang="id" class="interlanguage-link-target">Bahasa Indonesia</a></li><li class="interlanguage-link interwiki-da"><a href="https://da.wikipedia.org/wiki/Eric_Idle" title="Eric Idle – Danish" lang="da" hreflang="da" class="interlanguage-link-target">Dansk</a></li><li class="interlanguage-link interwiki-simple"><a href="https://simple.wikipedia.org/wiki/Eric_Idle" title="Eric Idle – Simple English" lang="en-simple" hreflang="en-simple" class="interlanguage-link-target">Simple English</a></li><li class="interlanguage-link interwiki-bg"><a href="https://bg.wikipedia.org/wiki/%D0%95%D1%80%D0%B8%D0%BA_%D0%90%D0%B9%D0%B4%D1%8A%D0%BB" title="Ерик Айдъл – Bulgarian" lang="bg" hreflang="bg" class="interlanguage-link-target">Български</a></li><li class="interlanguage-link interwiki-an"><a href="https://an.wikipedia.org/wiki/Eric_Idle" title="Eric Idle – Aragonese" lang="an" hreflang="an" class="interlanguage-link-target">Aragonés</a></li><li class="interlanguage-link interwiki-azb"><a href="https://azb.wikipedia.org/wiki/%D8%A7%D8%B1%DB%8C%DA%A9_%D8%A2%DB%8C%D8%AF%D9%84" title="اریک آیدل – South Azerbaijani" lang="azb" hreflang="azb" class="interlanguage-link-target">تۆرکجه</a></li><li class="interlanguage-link interwiki-cy"><a href="https://cy.wikipedia.org/wiki/Eric_Idle" title="Eric Idle – Welsh" lang="cy" hreflang="cy" class="interlanguage-link-target">Cymraeg</a></li><li class="interlanguage-link interwiki-eu"><a href="https://eu.wikipedia.org/wiki/Eric_Idle" title="Eric Idle – Basque" lang="eu" hreflang="eu" class="interlanguage-link-target">Euskara</a></li><li class="interlanguage-link interwiki-ga"><a href="https://ga.wikipedia.org/wiki/Eric_Idle" title="Eric Idle – Irish" lang="ga" hreflang="ga" class="interlanguage-link-target">Gaeilge</a></li><li class="interlanguage-link interwiki-gl"><a href="https://gl.wikipedia.org/wiki/Eric_Idle" title="Eric Idle – Galician" lang="gl" hreflang="gl" class="interlanguage-link-target">Galego</a></li><li class="interlanguage-link interwiki-hr"><a href="https://hr.wikipedia.org/wiki/Eric_Idle" title="Eric Idle – Croatian" lang="hr" hreflang="hr" class="interlanguage-link-target">Hrvatski</a></li><li class="interlanguage-link interwiki-hy"><a href="https://hy.wikipedia.org/wiki/%D4%B7%D6%80%D5%AB%D5%AF_%D4%B1%D5%B5%D5%A4%D5%AC" title="Էրիկ Այդլ – Armenian" lang="hy" hreflang="hy" class="interlanguage-link-target">Հայերեն</a></li><li class="interlanguage-link interwiki-io"><a href="https://io.wikipedia.org/wiki/Eric_Idle" title="Eric Idle – Ido" lang="io" hreflang="io" class="interlanguage-link-target">Ido</a></li><li class="interlanguage-link interwiki-la"><a href="https://la.wikipedia.org/wiki/Ericus_Idle" title="Ericus Idle – Latin" lang="la" hreflang="la" class="interlanguage-link-target">Latina</a></li><li class="interlanguage-link interwiki-lv"><a href="https://lv.wikipedia.org/wiki/%C4%92riks_Aidls" title="Ēriks Aidls – Latvian" lang="lv" hreflang="lv" class="interlanguage-link-target">Latviešu</a></li><li class="interlanguage-link interwiki-mk"><a href="https://mk.wikipedia.org/wiki/%D0%95%D1%80%D0%B8%D0%BA_%D0%90%D1%98%D0%B4%D0%BB" title="Ерик Ајдл – Macedonian" lang="mk" hreflang="mk" class="interlanguage-link-target">Македонски</a></li><li class="interlanguage-link interwiki-sco"><a href="https://sco.wikipedia.org/wiki/Eric_Idle" title="Eric Idle – Scots" lang="sco" hreflang="sco" class="interlanguage-link-target">Scots</a></li><li class="interlanguage-link interwiki-sh"><a href="https://sh.wikipedia.org/wiki/Eric_Idle" title="Eric Idle – Serbo-Croatian" lang="sh" hreflang="sh" class="interlanguage-link-target">Srpskohrvatski / српскохрватски</a></li><li class="interlanguage-link interwiki-sk"><a href="https://sk.wikipedia.org/wiki/Eric_Idle" title="Eric Idle – Slovak" lang="sk" hreflang="sk" class="interlanguage-link-target">Slovenčina</a></li><li class="interlanguage-link interwiki-war"><a href="https://war.wikipedia.org/wiki/Eric_Idle" title="Eric Idle – Waray" lang="war" hreflang="war" class="interlanguage-link-target">Winaray</a></li><li class="interlanguage-link interwiki-zh-min-nan"><a href="https://zh-min-nan.wikipedia.org/wiki/Eric_Idle" title="Eric Idle – Chinese (Min Nan)" lang="nan" hreflang="nan" class="interlanguage-link-target">Bân-lâm-gú</a></li><li class="interlanguage-link interwiki-sl"><a href="https://sl.wikipedia.org/wiki/Eric_Idle" title="Eric Idle – Slovenian" lang="sl" hreflang="sl" class="interlanguage-link-target">Slovenščina</a></li><li class="interlanguage-link interwiki-ar"><a href="https://ar.wikipedia.org/wiki/%D8%A5%D9%8A%D8%B1%D9%8A%D9%83_%D8%A3%D9%8A%D8%AF%D9%84" title="إيريك أيدل – Arabic" lang="ar" hreflang="ar" class="interlanguage-link-target">العربية</a></li><li class="interlanguage-link interwiki-af"><a href="https://af.wikipedia.org/wiki/Eric_Idle" title="Eric Idle – Afrikaans" lang="af" hreflang="af" class="interlanguage-link-target">Afrikaans</a></li><li class="interlanguage-link interwiki-th"><a href="https://th.wikipedia.org/wiki/%E0%B9%80%E0%B8%AD%E0%B8%A3%E0%B8%B4%E0%B8%81_%E0%B9%84%E0%B8%AD%E0%B9%80%E0%B8%94%E0%B8%B4%E0%B8%A5" title="เอริก ไอเดิล – Thai" lang="th" hreflang="th" class="interlanguage-link-target">ไทย</a></li><li class="interlanguage-link interwiki-ia"><a href="https://ia.wikipedia.org/wiki/Eric_Idle" title="Eric Idle – Interlingua" lang="ia" hreflang="ia" class="interlanguage-link-target">Interlingua</a></li><li class="interlanguage-link interwiki-arz"><a href="https://arz.wikipedia.org/wiki/%D8%A7%D9%8A%D8%B1%D9%8A%D9%83_%D8%A7%D9%8A%D8%AF%D9%84" title="ايريك ايدل – Egyptian Arabic" lang="arz" hreflang="arz" class="interlanguage-link-target">مصرى</a></li></ul>
		<div class="after-portlet after-portlet-lang"><span class="wb-langlinks-edit wb-langlinks-link"><a href="https://www.wikidata.org/wiki/Special:EntityPage/Q210741#sitelinks-wikipedia" title="Edit interlanguage links" class="wbc-editpage">Edit links</a></span></div>
	</div>
</nav>


</div>

</div>

<footer id="footer" class="mw-footer" role="contentinfo" >
	<ul id="footer-info" >
		<li id="footer-info-lastmod"> This page was last edited on 20 July 2020, at 16:35<span class="anonymous-show">&#160;(UTC)</span>.</li>
		<li id="footer-info-copyright">Text is available under the <a rel="license" href="//en.wikipedia.org/wiki/Wikipedia:Text_of_Creative_Commons_Attribution-ShareAlike_3.0_Unported_License">Creative Commons Attribution-ShareAlike License</a><a rel="license" href="//creativecommons.org/licenses/by-sa/3.0/" style="display:none;"></a>;
additional terms may apply.  By using this site, you agree to the <a href="//foundation.wikimedia.org/wiki/Terms_of_Use">Terms of Use</a> and <a href="//foundation.wikimedia.org/wiki/Privacy_policy">Privacy Policy</a>. Wikipedia® is a registered trademark of the <a href="//www.wikimediafoundation.org/">Wikimedia Foundation, Inc.</a>, a non-profit organization.</li>
	</ul>
	<ul id="footer-places" >
		<li id="footer-places-privacy"><a href="https://foundation.wikimedia.org/wiki/Privacy_policy" class="extiw" title="wmf:Privacy policy">Privacy policy</a></li>
		<li id="footer-places-about"><a href="/wiki/Wikipedia:About" title="Wikipedia:About">About Wikipedia</a></li>
		<li id="footer-places-disclaimer"><a href="/wiki/Wikipedia:General_disclaimer" title="Wikipedia:General disclaimer">Disclaimers</a></li>
		<li id="footer-places-contact"><a href="//en.wikipedia.org/wiki/Wikipedia:Contact_us">Contact Wikipedia</a></li>
		<li id="footer-places-developers"><a href="https://www.mediawiki.org/wiki/Special:MyLanguage/How_to_contribute">Developers</a></li>
		<li id="footer-places-statslink"><a href="https://stats.wikimedia.org/#/en.wikipedia.org">Statistics</a></li>
		<li id="footer-places-cookiestatement"><a href="https://foundation.wikimedia.org/wiki/Cookie_statement">Cookie statement</a></li>
		<li id="footer-places-mobileview"><a href="//en.m.wikipedia.org/w/index.php?title=Eric_Idle&amp;mobileaction=toggle_view_mobile" class="noprint stopMobileRedirectToggle">Mobile view</a></li>
	</ul>
	<ul id="footer-icons" class="noprint">
		<li id="footer-copyrightico"><a href="https://wikimediafoundation.org/"><img src="/static/images/wikimedia-button.png" srcset="/static/images/wikimedia-button-1.5x.png 1.5x, /static/images/wikimedia-button-2x.png 2x" width="88" height="31" alt="Wikimedia Foundation" loading="lazy" /></a></li>
		<li id="footer-poweredbyico"><a href="https://www.mediawiki.org/"><img src="/static/images/poweredby_mediawiki_88x31.png" alt="Powered by MediaWiki" srcset="/static/images/poweredby_mediawiki_132x47.png 1.5x, /static/images/poweredby_mediawiki_176x62.png 2x" width="88" height="31" loading="lazy"/></a></li>
	</ul>
	<div style="clear: both;"></div>
</footer>



<script>(RLQ=window.RLQ||[]).push(function(){mw.config.set({"wgPageParseReport":{"limitreport":{"cputime":"0.952","walltime":"1.442","ppvisitednodes":{"value":7338,"limit":1000000},"postexpandincludesize":{"value":149364,"limit":2097152},"templateargumentsize":{"value":11297,"limit":2097152},"expansiondepth":{"value":17,"limit":40},"expensivefunctioncount":{"value":15,"limit":500},"unstrip-depth":{"value":1,"limit":20},"unstrip-size":{"value":188600,"limit":5000000},"entityaccesscount":{"value":1,"limit":400},"timingprofile":["100.00% 1249.136      1 -total"," 24.99%  312.176      1 Template:Reflist"," 22.83%  285.202      1 Template:Infobox_person"," 20.05%  250.465      1 Template:Infobox"," 14.36%  179.326     11 Template:ISBN"," 10.45%  130.574     24 Template:Cite_web","  8.98%  112.222      5 Template:Br_separated_entries","  8.07%  100.768     11 Template:Catalog_lookup_link","  6.32%   78.909      1 Template:Birth_date_and_age","  5.44%   67.922      2 Template:Marriage"]},"scribunto":{"limitreport-timeusage":{"value":"0.370","limit":"10.000"},"limitreport-memusage":{"value":9603892,"limit":52428800}},"cachereport":{"origin":"mw1391","timestamp":"20200721135736","ttl":2592000,"transientcontent":false}}});});</script>
<script type="application/ld+json">{"@context":"https:\/\/schema.org","@type":"Article","name":"Eric Idle","url":"https:\/\/en.wikipedia.org\/wiki\/Eric_Idle","sameAs":"http:\/\/www.wikidata.org\/entity\/Q210741","mainEntity":"http:\/\/www.wikidata.org\/entity\/Q210741","author":{"@type":"Organization","name":"Contributors to Wikimedia projects"},"publisher":{"@type":"Organization","name":"Wikimedia Foundation, Inc.","logo":{"@type":"ImageObject","url":"https:\/\/www.wikimedia.org\/static\/images\/wmf-hor-googpub.png"}},"datePublished":"2002-05-14T21:16:37Z","dateModified":"2020-07-20T16:35:05Z","image":"https:\/\/upload.wikimedia.org\/wikipedia\/commons\/6\/6f\/Eric_Idle_2014.jpg","headline":"English actor, comedian, and writer"}</script>
<script>(RLQ=window.RLQ||[]).push(function(){mw.config.set({"wgBackendResponseTime":168,"wgHostname":"mw1271"});});</script></body></html>
"""
getUrl(html_doc)