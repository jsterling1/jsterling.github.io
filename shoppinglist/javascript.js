$(document).ready(function(){
   $('button').on('click',function(){
    var input=$('input').val();
    $('#mydiv').append("<p>"+input+"</p>");
   });
});
