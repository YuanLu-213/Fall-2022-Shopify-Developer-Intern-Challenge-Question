$(document).ready(function(){

    $("#edit-form").submit(function(event){
        event.preventDefault();
        var name = $("#input-name").val();
        var category = $("#category option:selected").text();

        var item = {
            name: name,
            category: category
        };

        console.log(item)

        $.ajax({
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify(item),
            url: "/add_item",
            success: function(data){
                console.log('success', data);
                $(".last").html("Item successfully added to inventory.")
            },
            error: function(data){
                console.log('Error', data);
                $(".last").html("Error occured. Please try again")
            }
        })
    })
})
