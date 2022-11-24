function loadDoc()
{   
    var data = document.getElementById("submit").value

    $.ajax({
        type: "POST",
        url: "/first_post",
        data: JSON.stringify(data),
        contentType: "application/json",
        dataType: 'json',
        success: function(result) 
        {
            const object = document.getElementById("choose")
            object.innerHTML = ""
            for (var i in result) {
                const newDiv = document.createElement("button")
                newDiv.innerHTML = result[i]
                object.appendChild(newDiv)
            }
        }
    });
}