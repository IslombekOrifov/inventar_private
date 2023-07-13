from django import forms
from index.models import Category, Model, Product, Group
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UsernameField, AuthenticationForm
from django.utils.text import capfirst
from django.contrib.auth import authenticate, get_user_model
from django.db.models import Q

from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

from accounts.models import CustomUser, Department


UserModel = get_user_model()


class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name_en', 'name_ru', 'name_uz', 'image']
        labels = {
            'name': 'Kategoriya nomi ',
            'image': 'Kategoriya rasmi ',
        }


class DepartmentCreateForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name',]
        labels = {
            'name': "Bo'lim nomi ",
        }


class ResponsibleCreateForm(forms.ModelForm):
    password2 = forms.CharField(widget=forms.PasswordInput)
    description = forms.CharField(required=False, label='Xulosa', widget=forms.Textarea(attrs={'class': "form-control"}))

    class Meta:
        model = CustomUser
        fields = [
            'first_name', 'last_name', 'email', 
            'status_member', 'department', 
            'password', 'password2', 'description'
        ]
        labels = {
            'first_name': 'Javobgar shaxs ism ',
            'last_name': 'Javobgar shaxs familyasi ',
            'email': 'Javobgar shaxs elektron pochtasi ',
            'description': 'Shaxs haqida izoh ',
        }

    def clean_email(self):
        data = self.cleaned_data['email']
        if CustomUser.objects.filter(Q(email=data) | Q(username=data)).exists():
            raise forms.ValidationError('Email already in use.')
        return data

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']
    
    def save(self, commit=True):
        if self.errors:
            raise ValueError(
                "The %s could not be %s because the data didn't validate."
                % (
                    self.instance._meta.object_name,
                    "created" if self.instance._state.adding else "changed",
                )
            )

        user = CustomUser.objects.create_user(
            username=self.instance.email,
            first_name=self.instance.first_name,
            last_name=self.instance.last_name,
            email=self.instance.email,
            status_member=self.instance.status_member,
            department=self.instance.department,
            description=self.instance.description,
            password=self.instance.password
        )
        return user


class ResponsibleEditForm(forms.ModelForm):
    description = forms.CharField(label='Izoh', required=False, widget=forms.Textarea(attrs={'class': "form-control"}))
    email = forms.EmailField(max_length=128, label='Izoh', required=False, widget=forms.EmailInput(attrs={'class': "form-control"}))
    class Meta:
        model = CustomUser
        fields = [
            'first_name', 'last_name', 'email', 
            'status_member', 'department', 
            'description'
        ]

    def clean_email(self):
        data = self.cleaned_data['email']
        qs = CustomUser.objects.exclude(id=self.instance.id)\
        .filter(Q(email=data) | Q(username=data))
        if qs.exists():
            raise forms.ValidationError(' Email already in use.')
        return data



class ModelCreateForm(forms.ModelForm):
    class Meta:
        model = Model
        fields = ['name', 'description', 'image']
        labels = {
            'name': 'Jihoz modeli nomi ',
            'image': 'Jihoz modeli rasmi ',
            'description': 'Izoh ',
        }
        print(labels)


status_choices = (
    (1, _('Ishlatilmoqda')),
    (3, _('Olib ketilgan')),
    (0, _('Yaroqsiz')),
    (2, _('Zahirada')),
)


class EquipmentCreateForm(forms.Form):
    name = forms.CharField(max_length=100, label='Nomi', required=False,
                                   widget=forms.TextInput(attrs={'class': 'form-control', 'maxlength': '100'}))
    schet = forms.CharField(max_length=100, label='Schet', required=False,
                                   widget=forms.TextInput(attrs={'class': 'form-control', 'maxlength': '100'}))
    room_number = forms.CharField(max_length=30, label='Xona raqami',
                                    widget=forms.TextInput(attrs={'class': "form-control", 'maxlength': '30'}))
    inventar_number = forms.CharField(required=True, label='Inventar raqami',
                                         widget=forms.TextInput(attrs={'class': "form-control"}))
    model_id = forms.ModelChoiceField(queryset=Model.objects.none(), label='Modeli',
                                      widget=forms.Select(attrs={'class': "form-control"}))
    responsible = forms.ModelChoiceField(queryset=CustomUser.objects.none(), label='Javobgar shaxs',
                                            widget=forms.Select(attrs={'class': "form-control"}))
    image = forms.FileField(label='Rasm yuklang', required=False, widget=forms.ClearableFileInput(attrs={'class': "form-control"}))
    seria_number = forms.CharField(max_length=70, label='Seria raqami', required=False,
                                   widget=forms.TextInput(attrs={'class': 'form-control', 'maxlength': '25', 'id': "alloptions"}))
    year_of_manufacture = forms.CharField(max_length=50, label='Ishlab chiqarilgan yili', required=False,
                                   widget=forms.TextInput(attrs={'class': 'form-control', 'maxlength': '50'}))
    unit_of_measurement = forms.CharField(max_length=50, label='O\'lchov birligi', required=False,
                                   widget=forms.TextInput(attrs={'class': 'form-control', 'maxlength': '50'}))
    description = forms.CharField(required=False, label='Xulosa', widget=forms.Textarea(attrs={'class': "form-control"}))

    def clean_inventar_number(self):
        inventar_number = self.cleaned_data['inventar_number']
        qs = Product.objects.filter(inventar_number=inventar_number)
        if qs:
            raise ValidationError('Bu inventar raqam boshqa jihozga berilgan')
        return inventar_number

    def __init__(self, user, *args, **kwargs):
        super(EquipmentCreateForm, self).__init__(*args, **kwargs)
        self.fields['responsible'].queryset = CustomUser.objects.filter(groups=user.groups.first(), is_superuser=False)
        self.fields['model_id'].queryset = Model.objects.filter(group=user.groups.first())

    


class ProductUpdateForm(forms.ModelForm):
    name = forms.CharField(max_length=100, label='Nomi', required=False,
                                   widget=forms.TextInput(attrs={'class': 'form-control', 'maxlength': '100'}))
    schet = forms.CharField(max_length=100, label='Schet', required=False,
                                   widget=forms.TextInput(attrs={'class': 'form-control', 'maxlength': '100'}))
    category_id = forms.ModelChoiceField(queryset=Category.objects.none(), label='Kategoriyasi', widget=forms.Select(attrs={'class': "form-control"}))
    room_number = forms.CharField(max_length=30, label='Xona raqami',
                                    widget=forms.TextInput(attrs={'class': "form-control", 'maxlength': '30'}))
    inventar_number = forms.CharField(label='Inventar raqami',
                                         widget=forms.TextInput(attrs={'class': "form-control"}))
    model_id = forms.ModelChoiceField(queryset=Model.objects.all(), label='Modeli',
                                      widget=forms.Select(attrs={'class': "form-control"}))
    responsible = forms.ModelChoiceField(queryset=CustomUser.objects.none(), label='Javobgar shaxs',
                                            widget=forms.Select(attrs={'class': "form-control"}))
    images = forms.FileField(label='Rasm yuklang', required=False, widget=forms.ClearableFileInput(attrs={'class': "form-control"}))
    seria_number = forms.CharField(max_length=70, label='Seria raqami', required=False,
                                   widget=forms.TextInput(attrs={'class': 'form-control', 'maxlength': "25"}))
    year_of_manufacture = forms.CharField(max_length=50, label='Ishlab chiqarilgan yili', required=False,
                                   widget=forms.TextInput(attrs={'class': 'form-control', 'maxlength': '50'}))
    unit_of_measurement = forms.CharField(max_length=50, label='O\'lchov birligi', required=False,
                                   widget=forms.TextInput(attrs={'class': 'form-control', 'maxlength': '50'}))
    description = forms.CharField(label='Xulosa', required=False, widget=forms.Textarea(attrs={'class': "form-control", 'rows':3}))
    status = forms.IntegerField(widget=forms.NumberInput(attrs={'class': "form-control"}))

    class Meta:
        model = Product
        exclude = ('qr_code', 'group')

    def __init__(self, user, *args, **kwargs):
        super(ProductUpdateForm, self).__init__(*args, **kwargs)
        self.fields['responsible'].queryset = CustomUser.objects.filter(groups=user.groups.first(), is_superuser=False)
        self.fields['category_id'].queryset = Category.objects.filter(group=user.groups.first())
        self.fields['model_id'].queryset = Model.objects.filter(group=user.groups.first())

    # def clean_inventar_number(self):
    #     inventar_number = self.cleaned_data['inventar_number']
    #     qs = Product.objects.filter(inventar_number=inventar_number)
    #     if qs:
    #         raise ValidationError('Bu inventar raqam boshqa jihozga berilgan')
    #     return inventar_number


class ProductDetailUpdateForm(forms.ModelForm):
    # status = forms.TypedChoiceField(choices=status_choices, label='', widget=forms.Select(attrs={'class': "form-control"}))
    status = forms.IntegerField(label='', widget=forms.NumberInput(attrs={'class': "form-control"}))
    responsible = forms.ModelChoiceField(queryset=CustomUser.objects.none(), label="Mas'ul shaxs",
                                            widget=forms.Select(attrs={'class': "form-control"}))
    class Meta:
        model = Product
        fields = ['status', 'responsible']

    def __init__(self, user, *args, **kwargs):
        super(ProductDetailUpdateForm, self).__init__(*args, **kwargs)
        self.fields['responsible'].queryset = CustomUser.objects.filter(groups=user.groups.first(), is_superuser=False)
       
# CATEGORIES Forms
        
class CategoryEditForm(forms.ModelForm):

    name = forms.CharField(max_length=70, label='Nomi', required=True,
                           widget=forms.TextInput(attrs={'class': "form-control"}))
    image = forms.ImageField(label='Rasm yuklang', widget=forms.ClearableFileInput(attrs={'class': "form-control"}))

    class Meta:
        model = Category
        fields = ['name', 'image']


class UploadExcelFileForm(forms.Form):
    excel_file_cat = forms.FileField(required=False)
    excel_file_pro = forms.FileField(required=False)
    excel_file_mod = forms.FileField(required=False)
    excel_file_depart = forms.FileField(required=False)


class ModelEditForm(forms.ModelForm):
    name = forms.CharField(max_length=70, label='Nomi', required=True,
                           widget=forms.TextInput(attrs={'class': "form-control"}))
    image = forms.ImageField(label='Rasm yuklang', widget=forms.ClearableFileInput(attrs={'class': "form-control"}))
    description = forms.CharField(label='Xulosa', widget=forms.Textarea(attrs={'class': "form-control"}))

    class Meta:
        model = Model
        fields = ['name', 'image', 'description']





class CustomAuthenticationForm(AuthenticationForm):
    """
    Base class for authenticating users. Extend this to get a form that accepts
    username/password logins.
    """
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)


class ProfileEditForm(forms.ModelForm):
    first_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email']

    def clean_email(self):
        data = self.cleaned_data['email']
        qs = CustomUser.objects.exclude(id=self.instance.id)\
        .filter(Q(email=data) | Q(username=data))
        if qs.exists():
            raise forms.ValidationError(' Email already in use.')
        return data
    

