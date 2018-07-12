$(document).ready(function(){
    $('#button1').click(function() { // all trs with level-1 class inside abc table
        if($('#button1').attr('value') == 'Edit'){
            $('#button1').attr('value', 'Add');
        }
        else{
            $('#button1').attr('value', 'Edit');
        }
        $('#new_f').toggle();
        $('#edit_f').toggle();
    });
});