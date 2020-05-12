'''
how to connect Models-Templates-Views we call "MTV"
1.In the views.py file we import any models that we will need to use
2.Use the view to query the model for data that we will need
3.Pass results from the model to the template
4.Edit the template so that it is ready to accept and display the data from the model
5.Map a URL to the view
'''
#first_project/first_app/views.py
    from first_app.models import Topic,Webpage,AccessRecord
    def index(request):
        webpages_list=AccessRecord.objects.order_by('date')
        date_dict={'access_records':webpages_list}
        return render(request,'first_app/index.html',context=date_dict)

#template/first_app/index.html
    <!DOCTYPE html>
    {% load staticfiles %}
    <html lang="en" dir="ltr">
    
    <head>
        <meta charset="utf-8">
        <title>Django Level Two</title>
        <link rel="stylesheet" href="{% static "css/style.css" %}"/>
    </head>
    
    <body>
        <h1>Hi welcome to Django level 2</h1>
        <h2>Here are your access records:</h2>
        <div class="djangtwo">
            {% if access_records %}
                <table>
                    <thead>
                        <th>site name</th>
                        <th>data accessed</th>
                    </thead>
                    {% for acc in access_records %}
                    <tr>
                        <td>{{ acc.name }}</td>
                        <td>{{ acc.date }}</td>
                    </tr>
                    {% endfor %}
                </table>
            {% else %}
                <p>NO ACCESS RECORDS FOUND!</p>
            {% endif %}
        </div>
    </body>
    </html>
    
# check URL connecting

#static/css/style.css
    h1{
        color: red
    }

    table,td,tr{
        border: 2px solid black
    }

