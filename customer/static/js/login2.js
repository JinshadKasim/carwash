console.log("hello")

function signUp() {
    username = document.getElementById('name').value
    useremail = document.getElementById('email').value
    phone = document.getElementById('phone').value
    password = document.getElementById('password').value
    confirmPassword = document.getElementById('confirmPassword').value
    var email_pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
    var number_pattern = /^[789]\d{9}$/
    var username_pattern = /^[a-zA-Z\-]+$/

    if (username == "") {
        alert("Enter Your Name")
        return false
    }

    if (useremail == "") {
        alert("Email Field Should not be Empty")
        return false
    }

    if (useremail.match(email_pattern) == null) {
        alert("Email Is Invalid")
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
    
    if(password == ""){
        alert('Enter a Password')
        return false
    }

    if(password.length<3){
        alert('Enter at least 3 Charecters')
        return false
    }

    if(confirmPassword ==""){
        alert("Enter Password")
        return false
    }

    if(confirmPassword != password){
        alert("Password Does not Match")
        return false
    }

    


}
function checkEmailExist(){
    // console.log("function called")
    // console.log($('#email').val())
    $.ajax({
        url:"email_check",
        type:"post",
        data: {
            'email':$('#email').val()
        },
        success:function(response){
            if(response.message){
                $('#emailError').html("Email Alredy Exist")
                $('#submit').prop('disabled',true)
                
            }
            else{
                $('#emailError').html(" ")
                $('#submit').prop('disabled',false)


            }
        }
    })
}
