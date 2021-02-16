from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def home(request):
	if request.method == "POST":
		name = request.POST['name']
		Subject = request.POST['Subject']
		_replyto = request.POST['_replyto']
		message = request.POST['message']

		# send an email
		send_mail(
			'Message trough the website from ' + name, # subject
			'from: ' + _replyto + ' \n Subject: ' + Subject + '\n Message: ' + message, # message
			_replyto, # from email
			['kayran.ugur@gmail.com'], # to email
			)

		return render(request, 'home.html')

	else:
		return render(request, 'home.html')
