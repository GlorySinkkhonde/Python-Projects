const registerBtn = document.querySelector(".reg-btn")

registerBtn.addEventListener("click", async () =>{

    let usernameInput = document.querySelector("#username")
    let emailInput = document.querySelector("#email")
    let passwordInput = document.querySelector("#password")

    let username = usernameInput.value
    let email = emailInput.value
    let password = passwordInput.value

    console.log("Here are the details")

    try{

        const response = await fetch("http://127.0.0.1:5000/", {
            method: 'POST',
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ username, email, password })
        })

        if(response.ok){
            const data = await response.json()
            console.log("Data sent successfully")
            window.location.href = "http://127.0.0.1:5000/login";
            
        }else {
            console.log("Failed to send data:", response.status)
        }


    }catch(error) {

        console.error("Error:", error)

    }

        usernameInput.value = ""
        emailInput.value = ""
        passwordInput.value = ""

    // console.log(username.value)
    // console.log(email.value)
    // console.log(password.value)

})

