from django.shortcuts import render

from channels import Channel


def home(request, template="home.html"):
    message = {}
    Channel('background-hello').send(message)

    return render(
        request,
        template,
        dict(),
    )
