from django.shortcuts import render, redirect
from django.contrib import messages
from .models 	import Tienda
from .forms 	import TiendaForm, ProductoForm


def tiendadd(request):
	if request.method == 'POST':
		form = TiendaForm(request.POST)
		if form.is_valid():
			try:
				tienda = form.save(commit=False)
				tienda.usuario = request.user
				tienda.save()
				messages.success(request, 'Se ha realizado con éxito!')
				return redirect('/')
			except Exception as e:
				messages.error(request, e)
	else:
		form = TiendaForm()
	return render(request, 'tienda/tiendadd.html', {'form': form})



def prodadd(request, url):
	if request.method == 'POST':
		form = ProductoForm(request.POST)
		if form.is_valid():
			try:
				prod = form.save(commit=False)
				prod.tienda = Tienda.objects.get(usuario=request.user)
				prod.shortcode = url
				prod.save()
				form.save_m2m()#save the many-to-many data for the form.
				messages.success(request, 'Se ha realizado con éxito!')
				return redirect('/')
			except Exception as e:
				messages.error(request, e)
	else:
		form = ProductoForm()
	return render(request, 'tienda/prodadd.html', {'form': form})

