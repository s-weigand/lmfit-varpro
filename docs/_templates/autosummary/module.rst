{% extends "known_packages.rst" %}
{% block module %}
{{ fullname | replace("lmfit_varpro.", "") | escape | underline}}
{#{% set reduced_name={child_modules} %}#}

.. currentmodule:: {{ module }}

.. automodule:: {{ fullname }}

    {% if fullname in known_packages %}
    .. rubric:: Submodules

    .. autosummary::
        {% for item in child_modules %}
            {% if item.startswith( fullname + ".") %}
                {{ item }}
            {% endif %}
        {%- endfor %}
    {% endif %}

    {% block functions %}
    {% if functions %}

Functions
---------

    .. rubric:: Summary

    .. autosummary::
        :toctree: {{ fullname | replace("lmfit_varpro.", "") | replace(".", "/") }}/functions
        :nosignatures:
        {% for item in functions %}
        {{ item }}
        {%- endfor %}
    {% endif %}
    {% endblock %}

    {% block classes %}
    {% if classes %}

Classes
-------

    .. rubric:: Summary

    .. autosummary::
        :toctree: {{ fullname | replace("lmfit_varpro.", "") | replace(".", "/") }}/classes
        :nosignatures:
    {% for item in classes %}
        {{ item }}
    {%- endfor %}
    {% endif %}
    {% endblock %}

    {% block exceptions %}
    {% if exceptions %}

Exceptions
----------

    .. rubric:: Exception Summary

    .. autosummary::
        :toctree: {{ fullname | replace("lmfit_varpro.", "") | replace(".", "/") }}/exceptions
    {% for item in exceptions %}
        {{ item }}
    {%- endfor %}
    {% endif %}
    {% endblock %}


{% endblock %}