"""Handlers for {% if database_type == "postgresql" %}postgresql{%endif%} queries.

- Collect response
- Handle exceptions
    - If {% if database_type == "postgresql" %}postgresql{%endif%} query have empty result, raises ``EmptyResult``
"""
