console.log('wtf')

function booking() {
    plan = document.getElementById('plan').value
    phone = document.getElementById('').value
    car_name = document.getElementById('car_name').value
    destination = document.getElementById('destination').value
    washing_date = document.getElementById('washing_date').value
    hour = document.getElementById('hour').value
    minute = document.getElementById('minute').value
    ampm = document.getElementById('ampm').value
    message = document.getElementById('message').value
    var number_pattern = /^[789]\d{9}$/

    if (plan == "") {
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

    if(hour ==""){
        alert("please select time")
        return false
    }

    if(minutes ==""){
        alert("please select time")
        return false
    }

    if(ampm ==""){
        alert("please select time")
        return false
    }

    


}