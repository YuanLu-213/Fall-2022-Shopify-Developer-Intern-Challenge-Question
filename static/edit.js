$(document).ready(function(){
    var name = item['name']
    if(name){
        $("#editing option:selected").text(name)
        $("#editing").prop('disabled', true)
    }


    $("#edit-form").submit(function(event){
        event.preventDefault();
        var edited = $("#editing option:selected").text()
        var name = $("#input-name").val();
        var category = $("#category option:selected").text();

        var item = {
            editing: edited,
            name: name,
            category: category
        };

        console.log(item)

        $.ajax({
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify(item),
            url: "/edit_item",
            success: function(data){
                console.log('success', data);
                $(".last").html("Item successfully Edited.");
                window.location.href = "/";
            },
            error: function(data){
                console.log('Error', data);
                $(".last").html("Error occured. Please try again")
            }
        })
    })
})