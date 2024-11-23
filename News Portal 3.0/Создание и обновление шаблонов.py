Шаблон формы (news_form.html):
html
{% extends 'default.html' %}  

{% block content %}  
    <h2>{% if form.instance.pk %}Редактировать{% else %}Создать{% endif %} новость</h2>  
    <form method="POST">  
        {% csrf_token %}  
        {{ form.as_p }}  
        <button type="submit">Сохранить</button>  
    </form>  
{% endblock %} 
 
Шаблон подтверждения удаления (news_confirm_delete.html):
html
{% extends 'default.html' %}  

{% block content %}  
    <h2>Вы уверены, что хотите удалить "{{ post.title }}"?</h2>  
    <form method="POST">  
        {% csrf_token %}  
        <button type="submit">Удалить</button>  
        <a href="{% url 'news_list' %}">Отмена</a>  
    </form>  
{% endblock %} 