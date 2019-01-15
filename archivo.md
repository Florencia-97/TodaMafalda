---
layout: default
---

<ul class='archivo'>
  {% for image in site.static_files %}
    {% if image.path contains 'historietas' %}
      <li><a href="{{site.baseurl}}/{{image.path}}">{{image.basename}}</a></li>
    {% endif %}
  {% endfor %}
</ul>