$(document).ready(function () {

    $('.editTask').click(function(){
       var id = $(this).val();
       window.location.href="/tasks/" + id + "/edit_task";
    });

    function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
        }
        return cookieValue;
    }
    $('.deleteTask').click(function(){
       var delete_task = confirm("Are you sure you want to delete this task?");
       if (delete_task == true){
           console.log("Here");
           csrf = getCookie("csrftoken");
           console.log(csrf);
           var id = $(this).val();
           $.ajax({
                type : "DELETE",
                url : "/tasks/" + id + "/delete_task",
                beforeSend: function(xhr) {
                    xhr.setRequestHeader("X-CSRFToken", csrf);
                  },
                success: function(result) {
                location.reload();
                }
            });
       }

    });

});
