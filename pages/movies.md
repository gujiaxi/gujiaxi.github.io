---
title: Watched Movies
permalink: /movies.html
layout: default
---
<h1 class="post-title">{{ page.title }}</h1>

<div class="post">
  <table class="play">
    <thead><tr><th class="play-date">Date</th><th>Title</th><th>Year</th><th class="play-rating">Rating</th></tr></thead>
    <tbody>
      {% for movie in site.data.movies %}
        <tr>
          <td class="play-date">{{ movie.Date }}</td>
          <td>{{ movie.Title }}</td>
          <td>{{ movie.Year }}</td>
          <td class="play-rating">{{ movie.Rating }}</td>
        </tr>
      {% endfor %}
    </tbody>
  </table>
</div>
