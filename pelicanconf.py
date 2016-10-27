#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'S2I2 HEP'
SITENAME = u'S2I2 HEP'
SITEURL = ''

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DISPLAY_PAGES_ON_MENU =False
MENUITEMS = (
			('About','/pages/about.html'),
			('Documents','/pages/documents.html'),
			)
#            ('Blog','/category/blog.html')

# Blogroll
LINKS =  (('NSF SI2','http://www.nsf.gov/funding/pgm_summ.jsp?pims_id=504817'),
		  ('DIANA/HEP','http://diana-hep.org'),
		  ('HEP Software Foundation','http://hepsoftwarefoundation.org'),
		  ('Community White Paper','http://hepsoftwarefoundation.org/cwp.html'),
		  ('Molecular Sciences Software Institute','http://molssi.org/'),
		  ('Science Gateways Community Institute','http://sciencegateways.org/'),
                  ('S2I2-HEP Google Group', 'https://groups.google.com/forum/#!forum/s2i2-hep'),
                  ('Indico', 'https://indico.cern.ch/category/7971/'),
                  ('Vidyo Room', 'https://vidyoportal.cern.ch/flex.html?roomdirect.html&key=g24IFWEdhejzHVy851PztEh82e4'),
		  ('S2I2-HEP github', 'http://github.com/s2i2-hep'),
		  )

# Social widget
# Do not set for now, include these links in LINKS above
#SOCIAL = (('github', 'http://github.com/s2i2-hep'),
#          ('Indico', 'http://indico.cern.ch/category/5816/'),
#          ('Vidyo Room', 'https://vidyoportal.cern.ch/flex.html?roomdirect.html&key=g24IFWEdhejzHVy851PztEh82e4'),)
CC_LICENSE="CC-BY"

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
RELATIVE_URLS = False

DISPLAY_TAGS_ON_SIDEBAR=False
DISPLAY_RECENT_POSTS_ON_SIDEBAR=False
#DISPLAY_ARTICLE_INFO_ON_INDEX=False

THEME = 'pelican-themes/pelican-bootstrap3'
#THEME = 'pelican-themes/backdrop'
PYGMENTS_STYLE='default'
#PYGMENTS_STYLE='friendly'

BOOTSTRAP_THEME='spacelab'
#BOOTSTRAP_THEME='yeti'
#BOOTSTRAP_THEME='superhero' #nice but, background doesn't work well with code as is
#BOOTSTRAP_THEME='cosmo'
#BOOTSTRAP_THEME='paper'
DISPLAY_BREADCRUMBS=False

BOOTSTRAP_NAVBAR_INVERSE =True
BANNER="images/s2i2-banner.jpg"
BANNER_TITLE=None
#BANNER_SUBTITLE = None
BANNER_SUBTITLE="Conceptualization of an NSF Scientific Software Innovation Institute (S2I2) for High Energy Physics"
BANNER_ALL_PAGES = False

#custom CSS
CUSTOM_CSS = 'static/custom.css'


#DIRECT_TEMPLATES = ('index', 'categories', 'authors', 'archives', 'search')
DIRECT_TEMPLATES = ('index', 'categories', 'authors', 'archives')

STATIC_PATHS = ['images','css', 'downloads', 'downloads/notebooks',
                'downloads/files','downloads/code', 'favicon.png']

# Tell Pelican to change the path to 'static/custom.css' in the output dir
EXTRA_PATH_METADATA = {
    'css/custom.css': {'path': 'static/custom.css'}
}

CODE_DIR = 'downloads/code'
NOTEBOOK_DIR = 'downloads/notebooks'
FAVICON= "images/favicon.ico"

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['summary', 'liquid_tags.img', 'liquid_tags.video',
			'liquid_tags.youtube', 'render_math',
           'liquid_tags.include_code', 'liquid_tags.notebook',
           'liquid_tags.literal', 'tipue_search']


# comments
DISQUS_SITENAME="s2i2-hep"

''' For reference, this code
<div id="disqus_thread"></div>
<script type="text/javascript">
    /* * * CONFIGURATION VARIABLES * * */
    var disqus_shortname = 's2i2-hep';
    
    /* * * DON'T EDIT BELOW THIS LINE * * */
    (function() {
        var dsq = document.createElement('script'); dsq.type = 'text/javascript'; dsq.async = true;
        dsq.src = '//' + disqus_shortname + '.disqus.com/embed.js';
        (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(dsq);
    })();
</script>
<noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript" rel="nofollow">comments powered by Disqus.</a></noscript>
'''

