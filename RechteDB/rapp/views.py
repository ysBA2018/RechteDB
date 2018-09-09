# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Create your views here.

from django.shortcuts import get_object_or_404
from django.views import generic, View

from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

# Imports für die Selektions-Views panel, selektion u.a.
from django.contrib.auth.models import User
from django.shortcuts import render
from django.core.paginator import Paginator
from .filters import PanelFilter, UseridRollenFilter, UseridFilter
from .forms import ShowGesamtForm, ShowUhRForm

# Zum Einlesen der csv
# import tablib
# from tablib import Dataset
# from import_export import resources
# from .resources import MyCSVImporterModel
from .models import TblUserIDundName, TblGesamt, TblOrga, TblPlattform, Tblrechteneuvonimport, \
						TblRollen, TblUserhatrolle, TblRollehataf

###################################################################
# RApp - erforderliche Sichten und Reports

# ToDo: Alle User und ihre Rollen für eine Selektion

# ToDo: Alle User und ihre Rollen sowie die daran hängenden AF für eine Selektion (nur zur Ansicht und Veränderung, kein PDF)
# Kombinieren UserundIhreRollen mit RollenundIhre AF


# ToDo: Alle Rollen sowie die daran hängenden AF für eine Selektion (gruppiert für PDF)

# ToDo: Alle TF / GF / AF / Rollen für selektierte User
# ToDo: - Evtl. gibt es das schon beim jetzigen Filterpanel

# ToDo: Abgleich vorhandener Rechte selektierter User mit Zertifizierungsliste

# ToDo: Abgleich vorhandener Rechte mit Rollenvorgaben
# ToDo: - Was fehlt?
# ToDo: - Was ist zu viel?
# ToDo: - Jeweils aufgeteilt für XV-, jeden vorhandenen AV/BV/CV und evtl. vorhandenen DV-User

# ToDo: Welche Direktzuordnungen hat eine UID schon über vorhandene AF?
# ToDo: - Welche Zuordnung ist damit doppelt?
# ToDo: - Welche TF fehlt als zugeordnete AF?
# ToDo: - Welche bekannten AFen würden hier helfen?

# ToDo: Importfunktion für "Alle meine TFen und die zugeordneten User"
# ToDo: Importfunktion für "Alle meine AFen und die zugeordneten User"

# ToDo: Alten "Finde Datei"-Dialog implemenieren

# ToDo: Hier werden sicherlich noch etliche Filterfunktionen benötigt:
# ToDo: Was passt eventuell nicht (welche Personen passen nicht in die erlaubten Orgabereiche)
# ToDo: Welche Rechte haben Ausschluss-/Einschlusskriterien und sind sie erfüllt?
# ToDo: Welche Rechte sind redundant, weil sie neu modelliert wurden und was ist die Alternativempfehlung?
# ToDo: Zu welchen Orgabereichen (Importfunktion dafür!) gehören die identifizierten User (Vorbereitung Mail an FK zum Prüfen und eventuellem Löschen

from django.http import HttpResponse

# Der Direkteinsteig für die gesamte Anwendung
def home(request):
	# Zeige ein paar Statistik-Infos über die RechteDB.
	# Das stellt sicher, dass die Anbidnung an die Datenbank funzt
	num_rights = TblGesamt.objects.all().count()
	num_userids = TblUserIDundName.objects.all().count
	num_active_userids = TblUserIDundName.objects.filter(geloescht=False).count
	num_plattforms = TblPlattform.objects.count
	num_iamba = TblGesamt.objects.filter(geloescht=False,
										 userid_name__abteilung__icontains='ZI-AI-BA',
										 userid_name__geloescht=False).count
	num_userids_in_department = TblUserIDundName.objects.filter(geloescht=False, abteilung__icontains='ZI-AI-BA').count
	num_teams = TblOrga.objects.all().count
	num_active_rights = TblGesamt.objects.filter(geloescht=False).count

	return render(
		request,
		'index.html',
		context={
			'num_rights': num_rights,
			'num_active_rights': num_active_rights,
			'num_userIDs': num_userids,
			'num_iam_ba': num_iamba,
			'num_activeUserIDs': num_active_userids,
			'num_plattforms': num_plattforms,
			'num_userIDsInDepartment': num_userids_in_department,
			'num_teams': num_teams,
			'num_users': User.objects.all().count,
		},
	)

###################################################################
# Die Gesamtliste der Rechte ungefiltert
class GesamtListView(generic.ListView):
	model = TblGesamt
	paginate_by = 50

# Die Detailsicht eines einzelnen Rechts

class GesamtDetailView(generic.DetailView):
	model = TblGesamt


###################################################################
# Die Gesamtliste der User ungefiltert
class UserIDundNameListView(generic.ListView):
	model = TblUserIDundName
	paginate_by = 50

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class TblUserIDundNameCreate(CreateView):
	model = TblUserIDundName
	fields = '__all__'
	initial = {'geloscht' : 'False',}

class TblUserIDundNameUpdate(UpdateView):
	model = TblUserIDundName
	fields = '__all__'

class TblUserIDundNameDelete(DeleteView):
	model = TblUserIDundName
	success_url = reverse_lazy('userliste')

def userToggleGeloescht(request, pk):
	# View function zum Togglen des Gelöscht-Flags in der DB für eine konkrete Instanz.
	# Dieser Aufruf wird nicht in zwei Schritten als GET / POST-Kombination durchgeführt.
	# sondern ausschließlich als GET.
	user_inst = get_object_or_404(TblUserIDundName, pk = pk)

	user_inst.geloescht = not user_inst.geloescht
	user_inst.save()

	# redirect to a new URL:
	return HttpResponseRedirect(reverse('userliste') )


###################################################################
# Die Gesamtliste der Teams (TblOrga)
class TeamListView(generic.ListView):
	model = TblOrga

class TblOrgaCreate(CreateView):
	model = TblOrga
	fields = '__all__'
	initial = {'geloscht' : 'False',}

class TblOrgaUpdate(UpdateView):
	model = TblOrga
	fields = '__all__'

class TblOrgaDelete(DeleteView):
	model = TblOrga
	success_url = reverse_lazy('teamliste')


###################################################################
# Die Ab hier kommen die Views für das Panel

"""
###################################################################
# Nur zum Zeigen, wie das mit den Panels gehen könnte....

def search(request):
	user_list = User.objects.all()
	user_filter = UserFilter(request.GET, queryset=user_list)
	return render(request, 'rapp/user_list.html', {'filter': user_filter})
"""

###################################################################
# Panel geht direkt auf die Gesamt-Datentabelle

def panel(request):
	panel_list = TblGesamt.objects.all()
	panel_filter = PanelFilter(request.GET, queryset=panel_list)
	panel_list = panel_filter.qs

	pagesize = request.GET.get('pagesize')

	if type(pagesize) == type(None) or int(pagesize) < 1:
		pagesize = 20
	else:
		pagesize = int(pagesize)

	paginator = Paginator(panel_list, pagesize)
	page = request.GET.get('page', 1)
	try:
		pages = paginator.page(page)
	except PageNotAnInteger:
		pages = paginator.page(1)
	except EmptyPage:
		pages = paginator.page(paginator.num_pages)

	args = {'paginator': paginator, 'filter': panel_filter, 'pages': pages, 'meineTabelle': panel_list, 'pagesize': pagesize}
	return render(request, 'rapp/panel_list.html', args)

###################################################################
# Finde alle relevanten Informationen zur aktuellen Selektion:
#
# Ausgangspunkt ist TblUseridUndName.
# Hierfür gibt es einen Filter, der per GET abgefragt wird.
# Geliefert werden nur die XV-Nummern zu den Namen (diese muss es je Namen zwingend geben)
#
# Die dort gefundene Treffermenge wird angereichert um die relevanten Daten aus TblUserHatRolle.
# Hier werden allerdings alle UserIDen zurückgeliefert je Name.
# Von dort aus gibt eine ForeignKey-Verbindung zu TblRollen.
#
# Problematisch ist noch die Verbindung zwischen TblRollen und TblRollaHatAf,
# Weil hier der Foreign Key Definition in TblRolleHatAf liegt.
# Das kann aber aufgelöst werden,
# sobald ein konkreter User betrachtet wird und nicht mehr eine Menge an Usern.

def panel_user_rolle_af(request, id = 0):
	panel_liste = TblUserIDundName.objects.filter(geloescht=False).order_by('name')
	panel_filter = UseridFilter(request.GET, queryset=panel_liste)
	namen_liste = panel_filter.qs.filter(userid__istartswith="xv")
	panel_liste = panel_filter.qs.select_related("orga")

	if request.method == 'POST':
		#form = ShowUhRForm(request.POST)
		if form.is_valid():
			return redirect('home')  # TODO: redirect ordentlich machen

	else:
		#form = ShowUhRForm()

		# Selektiere alle Userids und alle Namen in TblUserHatRolle, die auch in der Selektion vorkommen
		# Hier könnte man mal einen reverse lookup einbauen von TblUserUndName zu TblUserHatRolle
		#
		# Die Liste der disjunkten UserIDs wird später in der Anzeige benötigt (Welche UserID gehören zu einem Namen).
		# Hintergrund ist die Festlegung, dass die Rollen am UserNAMEN un dnicht an der UserID hängen.
		# Dennoch gibt es Rollen, die nur zu bestimmten Userid-Typen (also bspw. nur für XV-Nummer) sinnvoll
		# und gültig sind.
		usernamen = []
		userids = []
		for row in panel_liste:
			x = row.name
			try:
				usernamen.index(x)
			except ValueError:
				usernamen.append(x)

			x = row.userid
			try:
				userids.index(x)
			except ValueError:
				userids.append(x)

		if (id != 0):	# Dann wurde der ReST-Parameter 'id' mitgegeben
			userHatRolle_liste = TblUserhatrolle.objects.filter(userid__id=id).order_by('rollenname')
			selektierter_name = TblUserIDundName.objects.get(id=id).name
			"""
			print(userHatRolle_liste.count())
			print(userHatRolle_liste)
			for x in userHatRolle_liste:
				print (id, x.userid.id, x.userid, x.rollenname, x.rollenname.system, x.rollenname.datum)
			"""
		else:
			userHatRolle_liste = []
			selektierter_name = -1

		pagesize = request.GET.get('pagesize')
		if type(pagesize) == type(None) or pagesize == '' or int(pagesize) < 1:
			pagesize = 100	# Eigentlich sollte hier nie gepaget werden, dient nur dem Schutz vor Fehlabfragen
		else:
			pagesize = int(pagesize)
		paginator = Paginator(namen_liste, pagesize)
		page = request.GET.get('page', 1)
		try:
			pages = paginator.page(page)
		except PageNotAnInteger:
			pages = paginator.page(1)
		except EmptyPage:
			pages = paginator.page(paginator.num_pages)

	args = {
		'paginator': paginator,
		'pages': pages,
		'pagesize': pagesize,
		# 'form': form,
		'filter': panel_filter,
		'userids': userids,
		'usernamen': usernamen,
		'userHatRolle_liste': userHatRolle_liste,
		'id': id,
	}

	if id != 0:
		args['selektierter_name'] = selektierter_name
	return render(request, 'rapp/panel_user_rolle_af.html', args)
