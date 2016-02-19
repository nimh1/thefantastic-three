# thefantastic-three
Building frameworks and developing code for use in the upcoming event.

#strategy

my plan of attack is- attack!

I believe libraries exist for each one of these steps, through step 5. Step 6 is where we as students actually add value.  We're coming up with a unique way to look at the world, and using a dashboard system they may or may not have heard of.
- 1. first thing to do is get the dashboard display (method for displaying our pretty charts) working.  
- 2. second thing is to get the data analysis and chart generation working; this is where we use R or python data processing or matlab or octave.  (see folder with dashboard info for a conceptual template of what it should look like)
- 3. then tie the two pieces together.  Make the dashboard software display the charts we produce.  We'll need to coordinate the chart formats.  Maybe a simple .jpg
- 4. figure out where we're getting the data from.  This is last, because it's something that might change once we get to the event.  We probably want to create a python package for each data collection system, and make sure there's a standard input and output format.
- 5. tie everything together.  Use one of our potential concepts and see if the implementation works.
- 6. think about what we want to analyze.  we have one idea with the 'access', but we can come up with something for HIV, too.

Hopefully we can make it through step 5 before the hackathon.  If we don't, we probably won't make it.  We have three critical pieces, at steps 1,2, and 4, and they need to be successfully integrated before we can rest easy.

# Team Roles
- Sam: you're our salesman, moral support, and resident entrepreneur.  Mona and I are building a pair of binoculars; how do you want to look at the world with them?  Help us come up with ways to apply this dashboard.  If we have lots of ideas, then if Mona and I do our job right we could implement all of them easily.
- Mona: help me build this, and come up with ways to use it.  Claim one of the first few steps (1 or 2) and blow it out of the water.  I'll take the other one.
- me: build this, and come up with ways to use it.  I'll take whichever step you don't, do it, and then we'll both work on what's left when those are done.  

# Resources: 

Looks like we're gonna want to use python - Anaconda for python 2.7 looks like the best bet.

Part 1 - Building Dashboards
- dashboard + localhost web server: https://pypi.python.org/pypi/django-dash
- simple python web server: https://fragments.turtlemeat.com/pythonwebserver.php
- simple python web server: http://www.cherrypy.org/
- Django local website (this is what I used so far): http://blogs.msdn.com/b/cdndevs/archive/2014/10/27/part-6-get-started-with-python-build-your-first-django-application-in-ptvs.aspx

Part 2 - Analyzing and Plotting Data
- this is an even better control chart (I think): https://github.com/bwghughes/controlchart
- Control Chart (almost exactly what we need for the first quadrant): http://stackoverflow.com/questions/9962114/control-charts-in-python
- data plotting: http://stackoverflow.com/questions/915940/python-plotting-libraries (see all answers)
- data plotting: http://matplotlib.org/
- similar question asked here: http://stackoverflow.com/questions/7822064/creating-charts-graphs-with-python

Part 4 - Data Collection
 - Web Scraping: http://scrapy.org/
 - Twitter Datamining: http://marcobonzanini.com/2015/03/02/mining-twitter-data-with-python-part-1/
