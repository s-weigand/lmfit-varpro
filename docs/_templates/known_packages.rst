..
    Don't change known_packages.rst since it changes will be overwritten.
    If you want to change known_packages.rst you have to make the changes in
    known_packages_template.rst and run `make api_docs` afterwards.
    For changes to take effect you might also have to run `make clean_all`
    afterwards.

{% set known_packages=[] %}
{% set child_modules=['lmfit_varpro.constraints', 'lmfit_varpro.qr_decomposition', 'lmfit_varpro.result', 'lmfit_varpro.separable_model', 'lmfit_varpro.util'] %}
{% block module %}

{% endblock %}