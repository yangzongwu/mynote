'''
how to use Django Forms to accept User Input and connect it to the database and retrieve it
Django Forms Advantages:
    --Quickly generate HTML form widgets
    --Validate data and process it into a Python data structure
    --Create form versions of our Models, quickly update models from Forms
step 1:
create a forms.py file inside the application

step 2:
call Django’s built in forms classes
Example inside of forms.py:
    from django import forms
    class FormName(forms.Form):
	      name = forms.CharField()
	      email = forms.EmailField()
	      text = forms.CharField(widget=forms.Textarea)

step 3:
show forms by using a view
inside our views.py file we need to import the forms (two ways to do this)
    from . import forms
    from forms import FormName
The . just indicates to import from the same directory as the current .py file
then create a new view for the form
    def form_name_view(request):
	      form = forms.FormName()
	      return render(request,’form_name.html’,
							      {‘form’:form})
step 4:
Then   add the view to the app’s urls, either directly or with include(). Directly:
    from basicapp import views
    urlpatterns = [
    url(r’formpage/’,views.form_name_view,
        name = ‘form_name’),
    ]

step 5:
create the templates folder along with the html file that will hold the template tagging for the form

There are several ways you can “inject” the form using template tagging. 
You can just pass in the key from the context dictionary:
    {{ form }}
    
Also added {% csrf_token %}
This is a Cross-Site Request Forgery (CSRF) token, which secures the HTTP POST action that is initiated 
on the subsequent submission of a form. 
The Django framework requires the CSRF token to be present. 
If it is not there, your form may not work!
It works by using a “hidden input” which is a random code and checking that it matches the user’s local site page.


HTTP stands for Hypertext Transfer Protocol and is designed to enable communication between a client and a server.
The client submits a request, the server then responds.
The most commonly used methods for this request/response protocol are GET and POST.
GET - requests data from a resource
POST - submits data to be process to a resource

step 6:
We need to inform the view that if we get a POST back, we should check if the data is valid and if so, grab that data.
We can do this by editing the view.
We will talk a lot more about form validation later on, but upon receiving a validated form, 
we can access a dictionary like attribute of the “cleaned_data”.
'''


# create templates/index.html
     <body>
         <h1>WELCOME TO HOME PAGE</h1>
         <h2>go to /formpage to fill our the form</h2>
     </body>
# create templates/form_page.html
    <body>
          {{form.as_p}}
    </body>
    
# change setting TEMPLATES_DIR
    TEMPLATES_DIR= os.path.join(BASE_DIR,'templates')
    
# create forms.py
    from django import forms
    class FormName(forms.Form):
        name=forms.CharField()
        email=forms.EmailField()
        text=forms.CharField(widget=forms.Textarea)

# change views.py
    from django.shortcuts import render
    from basicapp import forms
    # Create your views here.
    def index(request):
        return render(request,'basicapp/index.html')
    def form_name_view(request):
        form=forms.FormName()
        return render(request,'basicapp/form_page.html',{'form':form})

# change urls.py
    from basicapp import views
    urlpatterns = [
        url(r'^$',views.index,name='index'),
        url(r'^formpage/',views.form_name_view,name='form_name'),
        ]

#change templates/form_page.html
    <head>
        <meta charset="utf-8">
        <title>Forms</title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css" integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS" crossorigin="anonymous">
    </head>
    <body>
        <h1>Fill our the form!</h1>
        <div class="container">
            <form method="POST">
                {{form.as_p}}
                {% csrf_token %}
              <input type="submit" class="btn btn-primary" name="" value="submit">
            </form>
        </div>
    </body>

# views.py grab data
    def form_name_view(request):
        form=forms.FormName()
        if request.method == 'POST':
            form = forms.FormName(request.POST)
            if form.is_valid():
                #do something LANGUAGE_CODE
                print("validations success!")
                print("NAME:"+form.cleaned_data['name'])
                print("Email:"+form.cleaned_data['email'])
                print("Text:"+form.cleaned_data['text'])
        return render(request,'basicapp/form_page.html',{'form':form})

'''
Form Validation
Django has built-in validators you can conveniently use to validate your forms (or check for bots!)
We’ll use the basicapp from the previous lecture and work with the following:
    Adding a check for empty fields
    Adding a check for a “bot”
    Adding a clean method for the entire form.
'''

# check for a “bot”
    class FormName(forms.Form):
        botcatcher=forms.CharField(required=False,
                                widget=forms.HiddenInput,)
    def clean_botcatcher(self):
        botcatcher = self.cleaned_data['botcatcher']
        if len(botcatcher)>0:
            raise forms.ValidationError("gotcha got!")
        return botcatcher
        
    #method two
    from django.core import validators
    class FormName(forms.Form):
    botcatcher=forms.CharField(required=False,
                                widget=forms.HiddenInput,
                                validators=[validators.MaxLengthValidator(0)])

# check for name
    def check_for_z(value):
        if value[0].lower() != 'z':
            raise forms.ValidationError('NAME NEEDS TO START WITH Z')

    class FormName(forms.Form):
        name=forms.CharField(validators=[check_for_z])

#double check email
    class FormName(forms.Form):
        name=forms.CharField()
        email=forms.EmailField()
        verify_email=forms.EmailField(label='Enter your email again')
        text=forms.CharField(widget=forms.Textarea)
    
        def clean(self):
            all_clean_data=super().clean()
            email=all_clean_data['email']
            vmail=all_clean_data['verify_email']
            if email!=vmail:
                raise forms.ValidationError("make sure emails is match")

'''
So far we’ve only printed out that information, but what if we wanted to save it to a model?
Luckily Django makes accepting form input and passing it to a model very simple!
Instead of inheriting from the forms.Forms class, 
we will use forms.ModelForm in our forms.py file.

This helper class allows us to create a form from a pre-existing model
We then add an inline class (something we haven’t seen before) called Meta
This Meta class provides information connecting the model to the form.
    
Example:
    from django import forms
    from myapp.models import MyModel
    class MyNewForm(forms.ModelForm):
	      # Form Fields go here
		    class Meta:
			      model = MyModel
            fields = # Let’s see the options!
            
But if you want custom validators...
    from django import forms
    from myapp.models import MyModel
    class MyNewForm(forms.ModelForm):
		    # Form Fields go here with validators params
        class Meta:
			      model = MyModel
            fields = # Let’s see the options!

Option #1: Set it to “__all__”
    from django import forms
    from myapp.models import MyModel
    class MyNewForm(forms.ModelForm):
	      # Form Fields go here
		    class Meta:
			      model = MyModel
            fields = “__all__”
            
Option #2: exclude certain fields
    from django import forms
    from myapp.models import MyModel
    class MyNewForm(forms.ModelForm):
	      # Form Fields go here
		    class Meta:
			      model = MyModel
            exclude = [“field1”,“field2”]
            
Option #3: List included fields
    from django import forms
    from myapp.models import MyModel
    class MyNewForm(forms.ModelForm):
	      # Form Fields go here
		    class Meta:
			      model = MyModel
            fields = (“field1”,“field2”)
'''
    from AppTwo.models import User
    class FormName(forms.ModelForm):
    	class Meta():
        	model=User
        	fields = "__all__"
