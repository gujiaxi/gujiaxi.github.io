---
layout: default
permalink: /index.html
---
<div class="index">
  <section class="about">
    <h2>about</h2>
    <p>Hi &#x1f44b;, I’m Isaac or you can call me Jiaxi. This is my personal website and here I share my thoughts about my life or the world from time to time. Conventionally, any and all opinions listed here are my own and not representative of my employers; future, past and present. When not changing the world, I love <a href="/books.html">&#x0001f4d6;</a>, <a href="/games.html">&#x0001f3ae;</a> and <a href="/movies.html">&#x0001f3ac;</a>. The best way to reach me is by <a href="mailto:imjiaxi@gmail.com">Email</a> but you can also find me on <a href="https://twitter.com/gujiaxi" target="_blank">Twitter</a> and <a href="https://instagram.com/jiaxigu" target="_blank">Instagram</a>.
    </p>
  </section>
  <section class="posts">
  <h2>posts</h2>
    <ul>
      {% for post in site.posts limit:5 %}
        <li>
        <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%Y-%m-%d" }} &#187; </time><a href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a>
        </li>
      {% endfor %}
    </ul>
    <p>&#x203a;&#x203a;&#x203a; <a href="/archive.html">More...</a></p>
  </section>
  <section class="publication">
    <h2>publications</h2>
      <ul>
        <li><b>Jiaxi Gu</b>, et al. “Wukong: A 100 Million Large-scale Chinese Cross-modal Pre-training Benchmark.” In <i>Advances in Neural Information Processing Systems (NeurIPS)</i>, 2022.</li>
        <li><b>Jiaxi Gu</b>, et al. “Alohomora: Motion-based Hotword Detection in Head-Mounted Displays.” In <i>IEEE Internet of Things Journal</i>, 2019. [<a href="https://doi.org/10.1109/JIOT.2019.2946593">DOI</a>]</li>
        <li><b>Jiaxi Gu</b>, et al. “Traffic-based Side-channel Attack in Video Streaming.” In <i>IEEE/ACM Transactions on Networking</i>, 2019. [<a href="https://doi.org/10.1109/TNET.2019.2906568">DOI</a>]</li>
        <li><b>Jiaxi Gu</b>, et al. “Spotlight: Hot Target Discovery and Localization with Crowdsourced Photos” In <i>Tsinghua Science and Technology</i>, 2020. [<a href="https://doi.org/10.26599/TST.2019.9010004">DOI</a>]</li>
        <li><b>Jiaxi Gu</b>, et al. “Spotlight: Multiple-object Localization by Mobile Photo Fusion.” In <i>International Conference on Big Data Computing and Communications</i>, 2018. [<a href="https://doi.org/10.1109/BIGCOM.2018.00044">DOI</a>]</li>
        <li><b>Jiaxi Gu</b>, et al. “NASR: NonAuditory Speech Recognition with Motion Sensors in Head-mounted Displays.” In <i>International Conference on Wireless Algorithms, Systems, and Applications</i>, 2018. [<a href="https://doi.org/10.1007/978-3-319-94268-1_63">DOI</a>]</li>
        <li><b>Jiaxi Gu</b>, et al. “Walls Have Ears: Traffic-based Side-channel Attack in Video Streaming.” In <i>IEEE International Conference on Computer Communications</i>, 2018. [<a href="https://doi.org/10.1109/INFOCOM.2018.8486211">DOI</a>]</li>
      </ul>
  </section>
</div>
