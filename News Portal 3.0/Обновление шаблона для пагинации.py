news_list.html
html
{% extends 'default.html' %}  

{% block content %}  
    <h2>Новости</h2>  
    
    <form method="GET">  
        {{ filter.form.as_p }}  
        <button type="submit">Фильтровать</button>  
    </form>  

    <ul>  
        {% for article in news %}  
            <li>  
                <a href="{% url 'news_detail' article.id %}">{{ article.title|censor }}</a>  
                <p>Дата публикации: {{ article.created_at|date:"d.m.Y" }}</p>  
                <p>{{ article.content|censor|truncatechars:20 }}</p>  
            </li>  
        {% endfor %}  
    </ul>  

    <div class="pagination">  
        <span class="step-links">  
            {% if news.has_previous %}  
                <a href="?page=1">Первая</a>  
                <a href="?page={{ news.previous_page_number }}">« Предыдущая</a>  
            {% endif %}  

            <span class="current">  
                Страница {{ news.number }} из {{ news.paginator.num_pages }}.  
            </span>  

            {% if news.has_next %}  
                <a href="?page={{ news.next_page_number }}">Следующая »</a>  
                <a href="?page={{ news.paginator.num_pages }}">Последняя</a>  
            {% endif %}  
        </span>  
    </div>  
{% endblock %}  