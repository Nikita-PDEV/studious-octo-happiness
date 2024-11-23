articles_list.html
html
{% extends 'default.html' %}  

{% block content %}  
    <h2>Статьи</h2>  
    <a href="{% url 'articles_create' %}">Создать новую статью</a>  
    
    <ul>  
        {% for article in articles %}  
            <li>  
                <a href="{% url 'article_detail' article.id %}">{{ article.title }}</a>  
                <p>Дата публикации: {{ article.created_at|date:"d.m.Y" }}</p>  
                <p>{{ article.content|truncatechars:100 }}</p>  
                <a href="{% url 'articles_edit' article.id %}">Редактировать</a>  
                <a href="{% url 'articles_delete' article.id %}">Удалить</a>  
            </li>  
        {% endfor %}  
    </ul>  

    <div class="pagination">  
        <span class="step-links">  
            {% if articles.has_previous %}  
                <a href="?page=1">Первая</a>  
                <a href="?page={{ articles.previous_page_number }}">« Предыдущая</a>  
            {% endif %}  
            <span class="current">Страница {{ articles.number }} из {{ articles.paginator.num_pages }}.</span>  
            {% if articles.has_next %}  
                <a href="?page={{ articles.next_page_number }}">Следующая »</a>  
                <a href="?page={{ articles.paginator.num_pages }}">Последняя</a>  
            {% endif %}  
        </span>  
    </div>  
{% endblock %}  
article_form.html
html
{% extends 'default.html' %}  

{% block content %}  
    <h2>{% if form.instance.pk %}Редактировать{% else %}Создать{% endif %} статью</h2>  
    <form method="POST">  
        {% csrf_token %}  
        {{ form.as_p }}  
        <button type="submit">Сохранить</button>  
    </form>  
{% endblock %}  
article_confirm_delete.html
html
{% extends 'default.html' %}  

{% block content %}  
    <h2>Вы уверены, что хотите удалить "{{ article.title }}"?</h2>  
    <form method="POST">  
        {% csrf_token %}  
        <button type="submit">Удалить</button>  
        <a href="{% url 'articles_list' %}">Отмена</a>  
    </form>  
{% endblock %}  