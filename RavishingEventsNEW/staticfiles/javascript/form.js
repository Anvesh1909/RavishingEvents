

const scriptURL = 'https://script.google.com/macros/s/AKfycbzwRfhmbCmq6Zw-cWLDZPl06nUFWeCqHpLuo226Fj0bpq4fiwRoodKfS2Tc1E_X3kU/exec'
const form = document.forms['submit-to-google-sheet']



form.addEventListener('submit', e => {
  e.preventDefault()
  fetch(scriptURL, { method: 'POST', body: new FormData(form)})
    .then(response => console.log('Success!', response))
    .catch(error => console.error('Error!', error.message))
})


document.addEventListener("DOMContentLoaded", function() {

    document.getElementById("openForm").addEventListener("click", function() {
        document.getElementById("popup").style.display = "block";
    });
  
  document.getElementById("close").addEventListener("click", function() {
    document.getElementById("popup").style.display = "none";
  });

  document.forms["submit-to-google-sheet"].addEventListener('submit', function() {
    
    document.getElementById("popup").style.display = "none";
  });
  
});

document.getElementById("popup").addEventListener("click", function(event) {
  event.stopPropagation();
});



