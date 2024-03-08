const loginBtn = document.querySelector(".login-btn")

loginBtn.addEventListener("click", async () =>{

    let usernameInput = document.querySelector("#login-username")
    let passwordInput = document.querySelector("#login-password")

    let username = usernameInput.value
    let password = passwordInput.value

    console.log("login btn works")

    try{

        const response = await fetch("http://127.0.0.1:5000/login", {
            method: 'POST',
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ username, password })
        })

        if(response.ok){
            const data = await response.json()
            console.log("Data sent successfully")
            
        }else {
            console.log("Failed to send data:", response.status)
        }


    }catch(error) {

        console.error("Error:", error)

    }

        usernameInput.value = ""
        passwordInput.value = ""

})