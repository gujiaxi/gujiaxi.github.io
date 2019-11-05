---
title: Read Books
permalink: /books.html
layout: default
---
<h1 class="post-title">{{ page.title }}</h1>

<div class="post">
  <table class="play">
    <thead><tr><th class="play-date">Date</th><th>Title</th><th>Author</th><th class="play-rating">Rating</th></tr></thead>
    <tbody>
      {% for book in site.data.books %}
        <tr>
          <td class="play-date">{{ book.Date }}</td>
          <td>{{ book.Title }}</td>
          <td>{{ book.Author }}</td>
          <td class="play-rating">{{ book.Rating }}</td>
        </tr>
      {% endfor %}
    </tbody>
  </table>
</div>
