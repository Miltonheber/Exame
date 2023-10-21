from django.forms import ModelForm, TextInput
from .models import *



class ExameSupForm(ModelForm):
    class Meta:
        model = ExameSup
        fields = '__all__'
        exclude = ('pdf',)

        

class ExameMedForm(ModelForm):
    class Meta:
        model = ExameMed
        fields = '__all__'
        exclude = ('pdf',)

        widgets = {
            
        }

class ExameGeralForm(ModelForm):
    class Meta:
        model = ExameGeral
        fields = '__all__'
        exclude = ('pdf',)

class Editaisform(ModelForm):
    class Meta:
        model = Editais
        fields = '__all__'
        exclude = ['pdf','tipo']

