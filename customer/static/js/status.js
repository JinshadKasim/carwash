function editData(id) {
    $.ajax({
        url:"edit_data",
        type:"post",
        data: {
            'id': id,
            'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
        },            

        success: function(response) {
            console.log(response.data)
            $('#id').val(response.data.id)
            $('#e_id').val(response.data.id)
            $('#plan').val(response.data.plan)
            $('#phone').val(response.data.phone)
            $('#car_name').val(response.data.car_name)
            $('#destination').val(response.data.destination)
            $('#washing_date').val(response.data.washing_date)
            $('#hour').val(response.data.hour)
            $('#minute').val(response.data.minute)
            $('#ampm').val(response.data.ampm)
            $('#message').val(response.data.message)
            $('#status').val(response.data.status)

        }
    })
}

function delete_booking(id){
    $.ajax({
        url:"delete_booking",
        type:"post",
        data: {
            'id': id,
            'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
        },            

        success: function(response) {
            console.log(response.data)
            document.getElementById('cancel_booking_btn').href='cancel_booking/'+response.data.id

        }
    })    

}