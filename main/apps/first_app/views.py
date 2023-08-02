from django.shortcuts import render, HttpResponse, redirect


def index(request):
	response = "First response"
	return HttpResponse(response)

def butt(requset):
	response = "Butt"
	return HttpResponse(response)