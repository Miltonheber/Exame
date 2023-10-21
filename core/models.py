from django.db import models

# Create your models here.
anos = [(x,x) for x in range(2015,2024)]


classes = [
    ('10ª','10ª'),
    ('12ª','12ª')
]

#poderia ter aplicada compressão de listas
#para ia criar uma lista, com as disciplinas e depois fazer uma lista
#reflexiva com os elementos dessa mesma lista.
subjects = [
    ('Português', 'Português'),
    ('Matemática', 'Matemática'),
    ('DGD','DGD'),
    ('Física','Física'),
    ('Química','Química'),
    ('Hístoria','Hístoria'),
    ('Geografia','Geografia'),
    ('English','English'),
    ('Francês','Francês'),
    ('Filosofia','Filosofia'),
    ('Biologia','Biologia')
]

subjectsmed = [
    ('Português', 'Português'),
    ('Matemática', 'Matemática'),
    ('Física','Física'),
    ('Biologia','Biologia'),
    ('Química','Química')
]
nivelg = [
    ('Ensino Geral','Ensino Geral'),
]

nivels = [
    ('Ensino Superior', 'Ensino Superior')
]

nivelm = [
    ('Ensino Tecníco', 'Ensino Tecníco')
]

epocas = [
    ('1° época','1° época'),
    ('2° época','2° época')
]

universidades = [
    ('UEM','UEM'),
    ('UP','UP'),
    ('UJC','UJC'),
    ('ISISA','ISISA'),
    ('NÁUTICA', 'NÁUTICA')
    
]
entidades = [
    ('UEM','UEM'),
    ('UP','UP'),
    ('UJC','UJC'),
    ('ISISA','ISISA'),
    ('NÁUTICA', 'NÁUTICA'),
    ('INSTITUTO INDUSTRIAL','INSTITUTO INDUSTRIAL'),
    ('INSTITUTO COMERCIAL','INSTITUTO COMERCIAL'),
    
    
]

class Ano(models.Model):
    ano = models.CharField(
        null=False,
        max_length=4,
        
    )

    def __str__(self):
        return self.ano
class Editais(models.Model):
    ano = models.ForeignKey(Ano, on_delete=models.DO_NOTHING)
    tipo = models.CharField('tipo', null=False, max_length=10, default='edital')
    instituicao = models.CharField('instituicao',max_length=30, null=False, choices=entidades)
    pdf = models.FileField(null=False, upload_to='editais')
    
    def __str__(self):
        return f'Edital {self.instituicao} de {self.ano}'

    
class ExameSup(models.Model):

    disciplina = models.CharField(
                max_length=30,
                choices=subjects,
                null=False,
    )

    

    instituicao = models.CharField(
                'instituição',
                null=False,
                max_length=30,
                choices=universidades,
                
    )
    nivel = models.CharField(
        null=False,
        max_length=30,
        choices=nivels,
        default='Ensino Superior'
    )
    ano = models.ForeignKey(Ano, on_delete=models.DO_NOTHING)
    
    pdf = models.FileField(
        null=False,
        upload_to='sup'
    )

    def __str__(self):
        return f'{self.instituição}-{self.disciplina}-{self.ano}'


class ExameMed(models.Model):

    disciplina = models.CharField(
        null=False,
        max_length=30,
        choices=subjectsmed
    )



    nivel = models.CharField(
        null=False,
        max_length=30,
        choices=nivelm,
        default='Ensino Tecníco'
    )
    ano = models.ForeignKey(Ano,on_delete=models.DO_NOTHING
    )
    pdf = models.FileField(
        null=False,
        upload_to='med'
    )

    def __str__(self):
        return f'{self.disciplina}-{self.ano}'


class ExameGeral(models.Model):

    disciplina = models.CharField(
        null=False,
        choices=subjects,
        max_length=30
    )

    classe = models.CharField(
        null=False,
        max_length=4,
        choices=classes
        
    )
    epoca = models.CharField(
        'época',
        null=False,
        choices=epocas,
        max_length=10
    )
    nivel = models.CharField(
        null=False,
        max_length=30,
        choices=nivelg,
        default='Ensino Geral'
        
    )
    ano = models.ForeignKey(
        Ano, on_delete=models.DO_NOTHING
        
    )
    pdf = models.FileField(
        null=False,
        upload_to='geral'
    )

    def __str__(self):
        return f'{self.disciplina}-{self.ano}-{self.epoca}'
    
