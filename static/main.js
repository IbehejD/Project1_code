function loadMessageAndCode()
{   
    var message = document.getElementById("message").value
    var code = document.getElementById("code").value
    var data = [message, code]

    $.ajax({
        type: "POST",
        url: "/first_post",
        data: JSON.stringify(data),
        contentType: "application/json",
        dataType: 'json',
        success: function(result) 
        {
            var object = document.getElementById("choose")
            object.innerHTML = ""
            for (var i in result) {
                var newDiv = document.createElement("button")
                newDiv.setAttribute("type", "button");
                newDiv.setAttribute("onClick", "sendPolynom(this.value)");
                newDiv.setAttribute("value", i);
                newDiv.innerHTML = result[i].join('')
                object.appendChild(newDiv)
            }
        }
    });
}

function sendPolynom(choice)
{   
    $.ajax({
        type: "POST",
        url: "/second_post",
        data: JSON.stringify(choice),
        contentType: "application/json",
        dataType: 'json',
        success: function(result) 
        {
            var cipher = document.getElementById("cipher")
            cipher.setAttribute("value", result[0].join(''))
            var polynom = document.getElementById("polynom")
            polynom.setAttribute("value", result[1].join(''))
        }
    });
}

function sendToDecode()
{   
    var message = document.getElementById("cipher").value
    var polynom = document.getElementById("polynom").value
    var data = [message, polynom]

    $.ajax({
        type: "POST",
        url: "/third_post",
        data: JSON.stringify(data),
        contentType: "application/json",
        dataType: 'json',
        success: function(result) 
        {
            var results = document.getElementById("results")
            results.innerHTML = ""

            console.log(result)
            
            for (let i = 0; i < result.length; i++){
                switch(i) {
                    case 0:
                        var newDiv = document.createElement("p")
                        newDiv.innerHTML = "Doručeno: "  + result[i]  
                        results.appendChild(newDiv)
                        break
                    
                    case 1:
                        var newDiv = document.createElement("p")
                        if (result[i] == true){
                            newDiv.innerHTML = "Zpráva byla úspěšně doručena"
                        }
                        else {
                            newDiv.innerHTML = "Zpráva byla doručena s chybou"
                        }

                        results.appendChild(newDiv)
                        break

                    case 2: 
                        var error = result[i]
                        console.log(error)
                        for (let p = 0; p < error.length; p++){
                            var newDiv = document.createElement("p")

                            console.log(p)
                            switch(p) {
                                case 0:
                                    newDiv.innerHTML = "Chyba se nachází: " + error[p]
                                    break

                                case 1:
                                    newDiv.innerHTML = "Opravená zpráva: " + error[p].join("")
                                    break

                                case 2:
                                    newDiv.innerHTML = "Opravená zpráva ve formě polynomu: " + error[p]
                                    break

                                default:
                                    //ds
                            }

                            results.appendChild(newDiv)

                        }
                        break
                    
                    default:
                        //dsf
                }
            }   

        }
    });
}
