window.settings = {
    MEDIA_URL: "{{ settings.MEDIA_URL }}",
    LANGUAGE_CODE: "{{ settings.LANGUAGE_CODE }}",
    DEBUG: {% if settings.DEBUG %}true{% else %}false{% endif %}
};
