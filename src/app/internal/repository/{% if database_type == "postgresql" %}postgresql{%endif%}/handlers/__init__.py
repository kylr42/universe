"""Handlers for {% if database_type == "{% if database_type == "postgresql"%}postgresql{% endif %}" %}{% if database_type == "postgresql"%}postgresql{% endif %}{%endif%} queries.

- Collect response
- Handle exceptions
    - If {% if database_type == "{% if database_type == "postgresql"%}postgresql{% endif %}" %}{% if database_type == "postgresql"%}postgresql{% endif %}{%endif%} query have empty result, raises ``EmptyResult``
"""
