// let passwordLength = document.querySelector('.passLen')
const generateBtn = document.querySelector('.gen__btn')
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

