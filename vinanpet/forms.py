from django import forms
import calculation
from .models import VinanPetLtd

class ReportForm(forms.ModelForm):
    class Meta:
        model = VinanPetLtd
        fields = "__all__"
        widgets = {

            'entry_Date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'tank_Difference': calculation.FormulaInput('tank_Opening-tank_Closing'),
            'pump_Difference': calculation.FormulaInput('pump_Closing-pump_Opening'),
            'amount': calculation.FormulaInput('pump_Difference*price'),
            'balance': calculation.FormulaInput('cash-expenses'),

        }
    def __init__(self, *args, **kwargs):
        super(ReportForm, self).__init__(*args, **kwargs)
        self.fields["tank_Difference"].widget.attrs['readonly'] = True
        self.fields["pump_Difference"].widget.attrs['readonly'] = True
        self.fields["amount"].widget.attrs['readonly'] = True
        self.fields["balance"].widget.attrs['readonly'] = True

