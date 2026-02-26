---
layout: page
permalink: /repositories/
title: repositories
description:
nav: true
nav_order: 4
---

{% for repo in site.data.repositories.github_repos %}
- [{{ repo.name }}]({{ repo.url }}) — {{ repo.description }}
{% endfor %}
