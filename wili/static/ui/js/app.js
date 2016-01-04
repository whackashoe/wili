$(function() {
    // initialization
    $('head').append(
        $('<link rel="stylesheet" type="text/css" />')
            .attr('href', '/static/ui/css/themes/' + data.customization.theme + '.css')
    );
    $('title, .navbar-brand').text(data.customization.title);
    $('#intro_text').text(data.customization.intro_text);
    $('#intro_subtext').text(data.customization.intro_subtext);



    // menu setup
    $('#main-navbar .nav').append($('<li><a href="/">Home</a></li>'));
    if(data.modules.library == 'enabled') $('#main-navbar .nav').append($('<li><a href="/library">Library</a></li>'));
});