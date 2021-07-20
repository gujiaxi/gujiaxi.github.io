---
title: Gallery
permalink: /gallery.html
layout: default
images:
  - path: /assets/img/20180522-3.jpg
    title: In Hawaii
    caption: In Hawaii (2018)
  - path: /assets/img/20120917-2.jpg
    title: In Taiwan
    caption: In Taiwan (2012)
---
<h1 class="post-title">{{ page.title }}</h1>

<div class="gallery">
    {% for image in page.images %}
    <div>
      <p><img src="{{ image.path }}" alt="{{ image.title }}" /></p>
      <p>{{ image.caption }}</p>
    </div>
    <hr>
    {% endfor %}
</div>
