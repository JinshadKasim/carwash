document.addEventListener("DOMContentLoaded", function(event) {
   
    const showNavbar = (toggleId, navId, bodyId, headerId) => {
        const toggle = document.getElementById(toggleId),
        nav = document.getElementById(navId),
        bodypd = document.getElementById(bodyId),
        headerpd = document.getElementById(headerId)
        
        // Validate that all variables exist
        if(toggle && nav && bodypd && headerpd){
        toggle.addEventListener('click', ()=>{
        // show navbar
        nav.classList.toggle('show')
        // change icon
        toggle.classList.toggle('bx-x')
        // add padding to body
        bodypd.classList.toggle('body-pd')
        // add padding to header
        headerpd.classList.toggle('body-pd')
        })
        }
    }
    
    showNavbar('header-toggle','nav-bar','body-pd','header')
    
    /*===== LINK ACTIVE =====*/
    const linkColor = document.querySelectorAll('.nav_link')
    
    function colorLink(){
    if(linkColor){
    linkColor.forEach(l=> l.classList.remove('active'))
    this.classList.add('active')
    }
    }
    linkColor.forEach(l=> l.addEventListener('click', colorLink))
    
     // Your code to run since DOM is loaded and ready
    });


function edit_employee_details(id){
    console.log(id)

    $.ajax({
        url:"edit_employee_data",
        type:"post",
        data: {
            'id': id,
            'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function(response) {
            console.log(response.data)
            document.getElementById('delete_url').href='delete_employee_data/'+response.data.id
            $("#manage_emp").css("display", "none")
            $("#edit_emp").css("display", "block")

            $('#emp_id').val(response.data.id)
            $('#id').val(response.data.id)
            $('#emp_name').val(response.data.name)
            $('#phone').val(response.data.phone)
            $('#email').val(response.data.email)
            $('#dob').val(response.data.dob)
            $('#address').val(response.data.address)
            $('#idproof').val(response.data.idproof)
            $('#idproofnum').val(response.data.idproofnum)
            $('#photo').val(response.data.photo)
            $('#password').val(response.data.password)
        }
    })
}