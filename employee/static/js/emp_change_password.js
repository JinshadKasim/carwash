function change_emp_password(){
    oldpassword = $("#oldpassword").val()
    newpassword = $("#newpassword").val()
    confirmnewpassword = $("#confirmnewpassword").val()

    if(oldpassword==""){
        alert("Please Enter Your Old Password")
        return false
    }

    if(newpassword==""){
        alert("Please Enter Your New Password")
        return false
    }
    if(confirmnewpassword==""){
        alert("Please Re-Enter Your New Password")
        return false
    }

    if(confirmnewpassword!=newpassword){
        alert("Password Does Not Match")
        return false
    }

    alert("Password Changed Successfully")
}