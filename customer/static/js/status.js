function editData(id) {
    $.ajax({
        url:"edit_data",
        type:"post",
        data: {
            'id': id,
            'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function(response) {
            console.log(response)
        }
    })
}