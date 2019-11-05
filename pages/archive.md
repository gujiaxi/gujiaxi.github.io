---
title: Archive
permalink: /archive.html
layout: default
---
<h1 class="post-title">{{ page.title }}</h1>

<div class="archive">
{% for post in site.posts %}
    {% assign currentDate = post.date | date: "%Y" %}
    {% if currentDate != myDate %}
        {% unless forloop.first %}</div>{% endunless %}
        <h2>{{ currentDate }}</h2>
        <div>
        {% assign myDate = currentDate %}
    {% endif %}
    <div class="archive-item">
    <a href="{{ post.url }}">{{ post.title }}</a>
    <span class="archive-date">{{ post.date | date: "%b %d, %Y" }}</span>
    </div>
    {% if forloop.last %}</div>{% endif %}
{% endfor %}
</div>
