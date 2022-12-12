console.log("Hello")

function insert_feedback() {
    console.log("Go in")
    const date = new Date();

let day = date.getDate();
let month = date.getMonth() + 1;
let year = date.getFullYear();
let currentDate = `${year}-${month}-${day}`;
console.log(currentDate); // "17-6-2022"
      $.ajax({
        url: "insert_feedback",
        type: "post",
        data: {
            'feedback': $('#feedback').val(),
            'date': currentDate
        },
        success: function (response) {
            alert(response.message)
            location.reload()  
        }
    })
    }

