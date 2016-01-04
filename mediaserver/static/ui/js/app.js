$(function() {
    $('head').append(
        $('<link rel="stylesheet" type="text/css" />')
            .attr('href', '/static/ui/css/themes/' + data.customization.theme + '.css')
    );
    $('title, .navbar-brand').text(data.customization.title);
    $('#intro_text').text(data.customization.intro_text);
});