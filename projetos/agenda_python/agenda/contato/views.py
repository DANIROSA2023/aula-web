from django.shortcuts import render
from django.http import HttpResponse

def index(request):

    dados = {
        1: {
            "nome": "wesley bezerra",
            "fone": "99675-3679",
            "email": "wesley@xpto.com"

        },
        2: {
            "nome": "filipe oliveira",
            "fone": "98787-5972",
            "email": "filipe@xpto.com"
        },

        3: {
             "nome": "adriana silva",
            "fone": "98595-5684",
            "email": "adriana@xpto.com"
        }
    }

    return render(request, "index.html", {"contatos": dados})

