$(document).ready(function(){
    var name = item['name']
    if(name){
        $("#deleting option:selected").text(name)
        $("#deleting").prop('disabled', true)
    }


    $("#delete-form").submit(function(event){
        event.preventDefault();
        var deleted = $("#deleting option:selected").text()
        var comment = $("#input-comment").val();

        var item = {
            deleting: deleted,
            comment: comment
        };

        console.log(item)

        $.ajax({
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify(item),
            url: "/delete_item",
            success: function(data){
                console.log('success', data);
                $(".last").html("Item successfully Deleted.");
                window.location.href = "/delete/0"
            },
            error: function(data){
                console.log('Error', data);
                $(".last").html("Error occured. Please try again")
            }
        })
    })

    $(".undo").click(function(event){
        event.preventDefault();
        var id = $(this).parent().attr('id')

        var undo = {
            id: id
        }

        $.ajax({
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify(undo),
            url: "/undo_delete",
            success: function(data){
                console.log('success', data);
                window.location.href = "/delete/0"
            },
            error: function(data){
                console.log('Error', data);
                $(".last").html("Error occured. Please try again")
            }
        })
    })
})