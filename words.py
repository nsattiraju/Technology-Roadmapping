import pandas as pd
import json
from flask import Flask, render_template, request, flash, redirect, url_for
from bs4 import BeautifulSoup
import urllib, random, re, string, stopwords
import io
import random
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

app = Flask(__name__)
app.secret_key = 'You will never guess'
tweets = {'atomtronics':'Honduras Tech support are Teaching Mandrills Atomtronics', 'crispr': 'CRISPR fixes disease gene in viable human embryos', 'cuda': 'i do not know what CUDA cores are, but i really love saying CUDA cores. Cuda coressssssss', 'e-textile': 'e-textile cuff creation - Let us get started making some awesomely e-textile bracelets! Gather your materials', 'lidar': 'New LIDAR systems steal the headlines at CES 2017', 'mmwave': 'ETSI mmWave group produces first standard -- on use cases. Nice high-level look at mmWave practicalities.', 'nanofiber': 'Nanofiber coating prevents infections in artificial joints'}
sentiment = {'atomtronics':{'positive': 72, 'negative': 28}, 'crispr' : {'positive': 64, 'negative': 36}, 'cuda' : {'positive': 91, 'negative': 9}, 'e-textile': {'positive': 45, 'negative': 55}, 'lidar' : {'positive': 76, 'negative': 24}, 'mmwave' : {'positive': 67, 'negative': 33}, 'nanofiber' : {'positive': 88, 'negative': 12}}
global ur

@app.route('/', methods = ['GET','POST'])

@app.route('/index', methods = ['GET','POST'])
def index():
	global ur

	if request.method == 'POST':
		
		''' Store post variables '''
		ur = request.form['urllink']
		case = request.form['case']
		show_freq = request.form['show_freq']
		
		path = 'C:/Users/pavan/Desktop/pywordcloud-flask-master/wordcloud/'
		extension = '.json'


		with open(path+ur+extension) as f:
			m = json.load(f)
		
		a = m
		b = [x['size'] for x in m]
		minFreq = min(b)
		maxFreq = max(b)
        
		#Create html span tags and corresponding css
		span = ""
		css  = """#box{font-family:'calibri';border:2px solid black;}
		#box a{text-decoration : none}
		"""
		
		''' Colors for words in wordcloud '''
		colors = ['#607ec5','#002a8b','#86a0dc','#4c6db9']
		colsize = len(colors)
		k = 0
		for index, item in enumerate(a):
			index += 1
			tag = (item['text'])
			link=item['href']
			s=link.split()
			link='+'.join(s)
         
			          
            
			if show_freq == "yes":
				span += '<a href= '+link+'><span class="word'+str(index)+'" id="tag'+str(index)+'">&nbsp;' + tag + " (" + str(int(item['size'])) + ") " + "&nbsp;</span></a>\n"
			else:
				span += '<a href= '+link+'><span class="word'+str(index)+'" id="tag'+str(index)+'">&nbsp;' + tag + "&nbsp;</span></a>\n"	
			
			''' Algorithm to scale sizes'''
			
			freqTag = int(item['size'])
			fontMax = 5.5
			fontMin = 1.5
			K = (freqTag - minFreq)/(maxFreq - minFreq)
			frange = fontMax - fontMin
			C = 4
			
			K = float(freqTag - minFreq)/(maxFreq - minFreq)
			size = fontMin + (C*float(K*frange/C))

			css += '#tag'+str(index)+'{font-size: '+ str(size) +'em;color: '+colors[int(k%colsize)]+'}\n'
			css += '#tag'+str(index)+':hover{color: red}\n'
			k += 1
		    

		''' Write the HTML and CSS into seperate files ''' 


		
		f = open('templates/wordcloud.html', 'w')
		sp = '<a class="twitter-timeline" href="https://twitter.com/search?q=%23'+str(ur)+'&src=typed_query">Tweets about selected Technology</a> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>'
		message = """
		<style type="text/css">
		""" + css +"""
		</style>
		<div id='box'>
			""" + span +  """
		</div>
		<!DOCTYPE html>
<html lang="en">
<head>
  
	<link href="//netdna.bootstrapcdn.com/bootstrap/3.0.3/css/bootstrap.min.css" rel="stylesheet">
    <link href='http://fonts.googleapis.com/css?family=Lato:100,300,400,700,900,100italic,300italic,400italic,700italic,900italic' rel='stylesheet' type='text/css'>
    <link href="static/css/landing-page.css" rel="stylesheet">

</head>

<body>
    <nav class="navbar navbar-default" role="navigation">
        <div class="container">          
            <div class="collapse navbar-collapse navbar-right navbar-ex1-collapse">
                <ul class="nav navbar-nav">
     
                </ul>
            </div>
        </div>
    </nav>
	<div class="navbar-header">
                <h3>Sentiment Analysis on this technology</h3>
            </div>
	<p>{{ name }}</p>
	<img title="Sentiment on this technology" src="/plot.png" alt="my plot">
	<div id='box'>
	""" + sp + """
	</div>
		"""
		f.write(message)
		f.close
		f.flush()
    
		return render_template('index.html')



	startover()
	return render_template('index.html')


'''
Function to find twitter tweets about this tech
'''

@app.route('/twitter analysis')
def twitter():
	global ur
	f = open('templates/twitter.html', 'w')
	sp = '<a class="twitter-timeline" href="https://twitter.com/search?q=%23'+str(ur)+'&src=typed_query">Tweets about selected Technology</a> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>'
	
	message = """
	<!DOCTYPE html>
<html lang="en">
<head>
  
	<link href="//netdna.bootstrapcdn.com/bootstrap/3.0.3/css/bootstrap.min.css" rel="stylesheet">
    <link href='http://fonts.googleapis.com/css?family=Lato:100,300,400,700,900,100italic,300italic,400italic,700italic,900italic' rel='stylesheet' type='text/css'>
    <link href="static/css/landing-page.css" rel="stylesheet">

</head>

<body>
    <nav class="navbar navbar-default" role="navigation">
        <div class="container">
            <div class="navbar-header">
                <a class="navbar-brand" href="http://startbootstrap.com">Sentiment Analysis</a>
            </div>
            <div class="collapse navbar-collapse navbar-right navbar-ex1-collapse">
                <ul class="nav navbar-nav">
     
                </ul>
            </div>
        </div>
    </nav>
	<div id='box'>
	""" + sp + """
	</div>
	<p>{{ name }}</p>
	<img src="/plot.png" alt="my plot">
	"""
	
	f.write(message)
	f.close
	f.flush()
	return render_template('twitter.html')

@app.route('/plot.png')
def plot_png():
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


def create_figure():
	global ur
	fig = Figure()
	axis = fig.add_subplot(1, 1, 1)
	labels = ['positive', 'negative']
	sizes = [sentiment[ur]['positive'], sentiment[ur]['negative']]
	xs = range(100)
	ys = [random.randint(1, 50) for x in xs]
	explode = (0, 0.1)#add colors
	colors = ['#ff9999','#66b3ff']
	axis.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
	return fig

@app.route('/startover')
def startover():
	f = open("templates/wordcloud.html",'w')
	f.write("")
	f.close
	return redirect(url_for('index'))

def visible(element):
		    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
		        return False
		    elif re.match('<!--.*-->', str(element)):
		        return False
		    return True

'''
Run the Flask Application
'''
if __name__ == '__main__':
	app.run(debug = True)