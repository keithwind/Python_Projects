const handleChange = (event) => {
    let text = event.target.value;
    let strength = 0;
    let length = text.length;
    let hasUpperCase = false;
    let hasLowerCase = false;
    let hasNumber = false;
    let hasSpecial = false;
    for(let i = 0; i < length; i++) {
        let char = text[i]
        if ([0,1,2,3,4,5,6,7,8,9].includes(parseInt(char))){
            hasNumber = true;
        }

        else if ('@#$&*!^_=-'.includes(char)){
            hasSpecial = true;
        }

        else if (char.toUpperCase()==char){
            hasUpperCase = true;
        }

        else if (char.toLowerCase()==char){
            hasLowerCase = true;
        }
    }
    if (hasUpperCase){
        strength++ ; 
    }
    if (hasLowerCase){
        strength++ ; 
    }
    if (hasNumber){
        strength++ ;
    }
    if (hasSpecial){
        strength++ ; 
    }
    if (length > 8){
        strength++ ;
    }
    if (strength < 5){
       let strengthDisplay = document.getElementById("strength")
       strengthDisplay.innerText = "Weak Password"
       strengthDisplay.classList.add('bad')
       strengthDisplay.classList.remove('good')

    }
    else {
        let strengthDisplay = document.getElementById("strength")
       strengthDisplay.innerText = "Strong Password"
       strengthDisplay.classList.add('good')
       strengthDisplay.classList.remove('bad')
    }
    console.log(strength);
}

$('document').ready(function(){
    passwordField = document.getElementById("InputPassword");
    passwordField.addEventListener("input", handleChange);
})
