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
    editais = Editaisform()
    
    contexto = {
        'id':id,
        'superior':examesup,
        'medio':examemed,
        'geral':examegeral,
        'editais':editais
    }

    if request.method == 'POST':
        d = request.POST
        nivel = d.get('nivel')
        if nivel == 'Ensino Superior':
            return redirect(f"/download/?nivel={nivel}&ano={d.get('ano')}&instituicao={d.get('instituicao')}&disciplina={d.get('disciplina')}")
        elif nivel == 'Ensino Tecníco':
            return redirect(f"/download/?nivel={nivel}&ano={d.get('ano')}&disciplina={d.get('disciplina')}")
        elif nivel == 'Ensino Geral':
            return redirect(f"/download/?nivel={nivel}&ano={d.get('ano')}&epoca={d.get('epoca')}&disciplina={d.get('disciplina')}&classe={d.get('classe')}")
        else:
            tipo = 'edital'
            return redirect(f"/download/?tipo={tipo}&ano={d.get('ano')}&instituicao={d.get('instituicao')}")
        print(d.get('tipo'))

        print(nivel)
    return render(request, 'form.html', contexto)

def download(request):
    dados = request.GET
    ano = dados.get('ano')
    disciplina = dados.get('disciplina')
    nivel = dados.get('nivel')
    instituicao = dados.get('instituicao')
    tipo = dados.get('tipo')
    if tipo == 'edital':
        try:
            edital = Editais.objects.get(
                ano = ano,
                instituicao = instituicao
            )
            contexto = {'edital':edital}
        except:
            contexto ={'erro':'Edital Indisponível!'}
        
    elif nivel == 'Ensino Superior':
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
   
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        msg = request.POST.get('msg')
        assunto = request.POST.get('assunto')
        
        
        print(request.POST)
        print(f" NOVO EMAIL:\nNome: {nome}\nEmail: {email}\nMensagem: {msg}")
    else:
        contexto = {}
        return render(request, 'contacto.html', contexto)


def sobre(request):
    print('ENTROU')
    return render(request, 'sobre.html')
