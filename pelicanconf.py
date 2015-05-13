#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'DIANA HEP'
SITENAME = u'DIANA HEP'
SITEURL = ''

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DISPLAY_PAGES_ON_MENU =False
MENUITEMS = (
			('About','pages/about.html'),
			('Job Opportunities','pages/jobs.html')
			)

# Blogroll
LINKS =  (('ROOT', 'https://root.cern.ch/drupal/'),
		  ('RIO','/'),
		  ('NSF SI2','http://www.nsf.gov/funding/pgm_summ.jsp?pims_id=504817'),
		  ('RooStats','https://twiki.cern.ch/twiki/bin/view/RooStats/WebHome'),
		  ('GooFit','https://github.com/GooFit/GooFit'),
		  ('RootPy','http://www.rootpy.org'),
		  ('AstroPy','http://www.astropy.org'),
		  ('scikit-learn','http://scikit-learn.org/stable/'),
		  )

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/diana_hep'),
          ('github', 'http://github.com/diana-hep'),)

CC_LICENSE="CC-BY"


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DIRECT_TEMPLATES=('search',) 

STATIC_PATHS = ['images', 'downloads', 'downloads/notebooks',
                'downloads/files','downloads/code', 'favicon.png']

CODE_DIR = 'downloads/code'
NOTEBOOK_DIR = 'downloads/notebooks'


PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['summary', 'liquid_tags.img', 'liquid_tags.video',
			'liquid_tags.youtube', 'render_math',
           'liquid_tags.include_code', 'liquid_tags.notebook',
           'liquid_tags.literal', 'tipue_search']

DISPLAY_TAGS_ON_SIDEBAR=False
DISPLAY_RECENT_POSTS_ON_SIDEBAR=True

THEME = 'pelican-bootstrap3'
#THEME = 'notmyidea'
PYGMENTS_STYLE='default'
#PYGMENTS_STYLE='friendly'
#THEME = '../pelican-bootstrap3'
#THEME = '/Users/cranmer/virtualenvs/pelican/lib/python2.7/site-packages/pelican/themes/pelican-bootstrap3'
# This requires Pelican 3.3+

#For pelican-ootstrap3
BOOTSTRAP_THEME='simplex'
#BOOTSTRAP_THEME='yeti'
#BOOTSTRAP_THEME='superhero' #nice but, background doesn't work well with code as is
BOOTSTRAP_THEME='cosmo'
#BOOTSTRAP_THEME='paper'
DISPLAY_BREADCRUMBS=False

# comments
DISQUS_SITENAME="diana-hep"

''' For reference, this code
<div id="disqus_thread"></div>
<script type="text/javascript">
    /* * * CONFIGURATION VARIABLES * * */
    var disqus_shortname = 'diana-hep';
    
    /* * * DON'T EDIT BELOW THIS LINE * * */
    (function() {
        var dsq = document.createElement('script'); dsq.type = 'text/javascript'; dsq.async = true;
        dsq.src = '//' + disqus_shortname + '.disqus.com/embed.js';
        (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(dsq);
    })();
</script>
<noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript" rel="nofollow">comments powered by Disqus.</a></noscript>
'''

