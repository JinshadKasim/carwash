// console.log('wtf')

// function booking() {

    


// }

function insert_data() {

    plan = document.getElementById('plan').value
    phone = document.getElementById('phone').value
    car_name = document.getElementById('car_name').value
    destination = document.getElementById('destination').value
    washing_date = document.getElementById('washing_date').value
    hour = document.getElementById('hour').value
    minute = document.getElementById('minute').value
    ampm = document.getElementById('ampm').value
    message = document.getElementById('message').value
    var number_pattern = /^[789]\d{9}$/

    if (plan == "Select a plan") {
        alert("Select Your Plan")
        return false
    }

    if (phone == "") {
       alert("Phone Field Should Not be Empty")
        return false
    }
    if (phone.match(number_pattern) == null) {
        alert("Not a Valid Number")
        return false
    }
    
    if(car_name == ""){
        alert('Enter the Name of the Vehicle')
        return false
    }

    if(destination ==""){
        alert("please Enter Your Destination")
        return false
    }

    if(washing_date ==""){
        alert("please select a date")
        return false
    }

    if(hour =="Hour"){
        alert("please select time")
        return false
    }

    if(minute =="Min"){
        alert("please select time")
        return false
    }

    if(ampm =="AM/PM"){
        alert("please select time")
        return false
    }


    $.ajax({
        url: "insert_data",
        type: "post",
        data: {
            'plan': $('#plan').val(),
            'phone': $('#phone').val(),
            'car_name': $('#car_name').val(),
            'destination': $('#destination').val(),
            'washing_date': $('#washing_date').val(),
            'hour': $('#hour').val(),
            'minute': $('#minute').val(),
            'ampm': $('#ampm').val(),
            'message': $('#message').val(),
        },
        success: function (response) {
            alert(response.message)
            location.reload()  
        }
    })
    // view_data()
     

}


