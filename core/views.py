from django.shortcuts import render,redirect
from .forms import *
from .models import *


def home(request):
    return render(request, 'home.html')


def options(request):
    return render(request, 'options.html')

def form(request, id):


    examesup = ExameSupForm()
    examemed = ExameMedForm()
    examegeral = ExameGeralForm()
    
    contexto = {
        'id':id,
        'superior':examesup,
        'medio':examemed,
        'geral':examegeral,
    }

    if request.method == 'POST':
        d = request.POST
        nivel = d.get('nivel')
        if nivel == 'Ensino Superior':
            return redirect(f"/download/?nivel={nivel}&ano={d.get('ano')}&instituicao={d.get('instituicao')}&disciplina={d.get('disciplina')}")
        elif nivel == 'Ensino Tecníco':
            return redirect(f"/download/?nivel={nivel}&ano={d.get('ano')}&disciplina={d.get('disciplina')}")
        else:
            return redirect(f"/download/?nivel={nivel}&ano={d.get('ano')}&epoca={d.get('epoca')}&disciplina={d.get('disciplina')}&classe={d.get('classe')}")
        print(nivel)
    return render(request, 'form.html', contexto)

def download(request):


    dados = request.GET
    ano = dados['ano']
    disciplina = dados['disciplina']
    nivel = dados['nivel']
    
    if nivel == 'Ensino Superior':
        instituicao = dados['instituicao']
        try:
            exame = ExameSup.objects.get(
                ano = ano,
                disciplina = disciplina,
                nivel = nivel,
                instituicao = instituicao
            )
            contexto = {'exame':exame}
        except:
            contexto = {'erro':'Exame Indisponível! :('}
        
    elif nivel == 'Ensino Tecníco':
        try:
            exame = ExameMed.objects.get(
                nivel = nivel,
                ano = ano,
                disciplina = disciplina
            )
            contexto = {'exame':exame}
        except:
            contexto = {'erro':'Exame Indisponível! :('}
    else:
        epoca = dados['epoca']
        classe = dados['classe']
        try:
            exame = ExameGeral.objects.get(
                epoca = epoca,
                classe = classe,
                ano = ano,
                disciplina = disciplina,
                nivel = nivel
            )
            contexto = {'exame':exame}
        except:
            contexto = {'erro':'Exame Indisponível! :('}
        

    return render(request, 'download.html', contexto)

def contacto(request):
    contexto = {}
    return render(request, 'contacto.html', contexto)


def sobre(request):
    return render(request, 'sobre.html')
