function register_employee(){
    emp_name = $('#emp_name').val()
    emp_phone = $('#phone').val()
    emp_email = $('#email').val()
    emp_dob = $('#dob').val()
    emp_address = $('#address').val()
    emp_idproof = $('#idproof').val()
    emp_idproofnum = $('#idproofnumber').val()
    emp_photo = $('#emp_photo').val()
    console.log(emp_name)
    console.log(emp_phone)
    console.log(emp_email)
    console.log(emp_dob)
    console.log(emp_address)
    console.log(emp_idproof)
    console.log(emp_idproofnum)
    console.log(emp_photo)

    if(emp_name==""){
        alert("Please Enter Employee Name")
        return false
    }
    if(emp_phone==""){
        alert("Please Enter Employee Phone Number")
        return false
    }
    if(emp_email==""){
        alert("Please Enter Employee E-Mail")
        return false
    }
    if(emp_dob==""){
        alert("Please Enter Employee Date of Birth")
        return false
    }
    if(emp_address==""){
        alert("Please Enter Employee Address")
        return false
    }
    
    if(emp_idproof==""){
        alert("Please Select Id Proof")
        return false
    }
    if(emp_idproofnum==""){
        alert("Please Enter ID Proof Number")
        return false
    }
    if(emp_photo==""){
        alert("Please upload Photo")
        return false
    }

    alert("Employee Registred Succesfully")
}