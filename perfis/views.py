from django.shortcuts import render, redirect
from perfis.models import Perfil, Convite
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required 
#import json
from django.http import JsonResponse



# Create your views here.
@login_required
def index(request):
	#print Perfil.objects.all()
	#return HttpResponse(Perfil.objects.all().values()) #retornar como json
	#return JsonResponse({"perfis": Perfil.objects.all().values()})
	return render(request, 'index.html', {"perfis" : Perfil.objects.all(), 
		"perfil_logado":get_perfil_logado(request)})
@login_required
def exibir(request, perfil_id):
	#print 'aaaaaaaaaa %s' %(perfil_id)
	#perfil = Perfil()
	#resp = {}
	#if perfil_id == '1':
	#	perfil = Perfil('thiago dantas', 'thiago@thiago.com', '7777', 'bioME')
	#	print perfil
	perfil = Perfil.objects.get(id = perfil_id)

	perfil_logado = get_perfil_logado(request)
	ja_eh_contato = perfil in perfil_logado.contatos.all()
	#return JsonResponse(perfil.__dict__.values() ,safe = False)
	return render(request, 'perfil.html',{"perfil": perfil, "ja_eh_contato": ja_eh_contato})
@login_required
def convidar(request, perfil_id):

	perfil_a_convidar = Perfil.objects.get( id = perfil_id)
	perfil_logado = get_perfil_logado(request)
	perfil_logado.convidar(perfil_a_convidar)	
	#return render(request, 'index.html', {"perfis" : Perfil.objects.all()})
	return redirect('index')
@login_required
def get_perfil_logado(request):
	return request.user.perfil


@login_required
def aceitar(request, convite_id):
	convite = Convite.objects.get(id = convite_id)
	convite.aceitar()
	return redirect('index')