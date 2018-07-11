---
layout: home
---
{% for image in site.static_files %}
{% if image.path contains 'historietas' %}
<img src="{{ image.path }}" alt="">
{% endif %}
{% endfor %}
