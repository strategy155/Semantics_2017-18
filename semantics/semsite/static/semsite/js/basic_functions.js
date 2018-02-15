function showMenu() {
    $('#menu-column2').toggleClass('non-visible visible');
    $('#menu-column').toggleClass('visible non-visible');
    $('#content-column').toggleClass('s11 s9');
}

function changeData(title, text) {
    $('#article-title').text(title);
    $('#article-text').html(text);
}

$(document).ready(function(){  
    function setEqualHeight(columns){
        var tallestcolumn = 0;
        columns.each(function(){
            currentHeight = $(this).height();
            if(currentHeight > tallestcolumn){
               tallestcolumn  = currentHeight;
            }
        });
        $('#menu-column').height(tallestcolumn - 100);
        $('#menu-column2').height(tallestcolumn + 150); 
        $('#content-column').height(tallestcolumn);

    }
        
    setEqualHeight($('#menu-column, #content-column'));
});