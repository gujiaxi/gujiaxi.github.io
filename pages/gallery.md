---
title: Gallery
permalink: /gallery.html
layout: default
images:
  - path: /assets/img/with_vincent.jpg
    title: With Vincent Cerf
    caption: With Vincent Cerf in Shanghai on May 19th, 2018.
  - path: /assets/img/with_alexander.jpg
    title: With Alexander Wolf
    caption: With Alexander Wolf in Shanghai on May 13th, 2017.
  - path: /assets/img/with_stonebraker.jpg
    title: With Michael Stonebraker
    caption: With Michael Stonebraker in Wuxi on October 21st, 2015.
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
