const generateBtn = document.querySelector('.gen__btn')
const acceptBtn = document.querySelector('.accept__btn')
let finalPassword = document.querySelector('.final_password')

generateBtn.addEventListener("click", async () =>{
    
    
    try{
        const passwordLength = document.querySelector('.passLen').value

        const response = await fetch('http://127.0.0.1:5000/generator', {
            method: 'POST',
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ passwordLength })
        })

        if (response.ok){
            const data = await response.json()
            finalPassword.value = data
            console.log("Data sent successfully")
        }else {
            console.log("Failed to send data:", response.status)
        }
    } catch(error){
        console.error("Error sending data:", error)
    }

  
})

// Once password is accepted, copy to clipboard (use JS)

acceptBtn.addEventListener("click", () =>{

    const generatedPassword = document.querySelector('.final_password').value
    console.log("hello word")

    navigator.clipboard.writeText(generatedPassword)
    .then(() => { 
        window.alert("Password copied to clipboard: " + generatedPassword);
    })
    .catch((error) => {
        console.error('Unable to copy text to clipboard:', error);
    });
})



