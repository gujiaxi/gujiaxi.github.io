---
title: Played Games
permalink: /games.html
layout: default
---
<h1 class="post-title">{{ page.title }}</h1>

<div class="post">
  <table class="play">
    <thead><tr><th class="play-date">Date</th><th>Title</th><th>Platform</th><th class="play-rating">Rating</th></tr></thead>
    <tbody>
      {% for game in site.data.games %}
        <tr>
          <td class="play-date">{{ game.Date }}</td>
          <td>{{ game.Title }}</td>
          <td>{{ game.Platform }}</td>
          <td class="play-rating">{{ game.Rating }}</td>
        </tr>
      {% endfor %}
    </tbody>
  </table>
</div>
