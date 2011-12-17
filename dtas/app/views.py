# Create your views here.
from django.http import HttpResponse
from django.http import *
from django.shortcuts import render_to_response,render
import twitter #uses python-twitter library. In Mac OS-X: easy_install python-twitter
import oauth2 as oauth
import cgi
import urlparse
import urllib


#import Twitter related settings.
from dtas.settings import CONSUMER_KEY,CONSUMER_SECRET,REQUEST_TOKEN_URL,ACCESS_TOKEN_URL,AUTH_URL

def home(request):
	if('access_token' in request.session):
			#if logged in and authenticated

			t_api=twitter.Api(CONSUMER_KEY,CONSUMER_SECRET,request.session['access_token']['oauth_token'],request.session['access_token']['oauth_token_secret'])
			t_user = t_api.VerifyCredentials()

			#This is where you now do what you want to do.
			return render(request,'index.html',locals())

	elif(request.GET.get('oauth_token') != None):
			#authenticate if token is received from Twitter.	
			token = oauth.Token(request.session['request_token']['oauth_token'],request.session['request_token']['oauth_token_secret'])

			_consumer = oauth.Consumer(CONSUMER_KEY, CONSUMER_SECRET)

			client = oauth.Client(_consumer, token)

			resp, content = client.request(ACCESS_TOKEN_URL, 'POST')
			access_token = dict(urlparse.parse_qsl(content))

			request.session['access_token'] = dict(cgi.parse_qsl(content)) 
			
			t_api=twitter.Api(CONSUMER_KEY,CONSUMER_SECRET,access_token['oauth_token'],access_token['oauth_token_secret'])
			t_user = t_api.VerifyCredentials()
			
			return HttpResponseRedirect('/')
	else:
			#basic home page
			_consumer = oauth.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
			client = oauth.Client(_consumer)

			resp, content = client.request(REQUEST_TOKEN_URL, 'GET')
			if resp['status'] != '200':
					raise Exception('Invalid response %s', resp['status'])

			request_token = dict(urlparse.parse_qsl(content))
			request.session['request_token'] = dict(cgi.parse_qsl(content)) 

			#authentication url
			a_url = AUTH_URL + '?oauth_token=' + request_token['oauth_token']
			return render(request,"index.html",locals())

def t_logout(request):
	#delete session
	request.session.flush()
	return HttpResponseRedirect('/')
	#redirect
