 msg=document.getElementById('message');

function getQuote(){
fetch('/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    // No need to pass any body for a simple POST request
})
.then(response => {
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
    return response.json(); // Parse the JSON response
})
.then(data => {
    msg.innerHTML=`${data.Quote} : ${data.Character}`;
    
    console.log(data);
})
.catch(error => {
    // Handle errors
    console.error('There was a problem with the fetch operation:', error);
});

}