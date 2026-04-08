async function checkSpam(){

let email = document.getElementById("email").value;

if(!email){
alert("Enter email text");
return;
}

let response = await fetch("http://127.0.0.1:5000/detect",{

method:"POST",
headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({
email:email
})

});

let data = await response.json();

document.getElementById("result").innerHTML =
"Prediction: " + data.prediction;

}