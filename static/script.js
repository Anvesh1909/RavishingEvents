

const scriptURL = 'https://script.google.com/macros/s/AKfycbzwRfhmbCmq6Zw-cWLDZPl06nUFWeCqHpLuo226Fj0bpq4fiwRoodKfS2Tc1E_X3kU/exec'
const form = document.forms['submit-to-google-sheet']



form.addEventListener('submit', e => {
  e.preventDefault()
  fetch(scriptURL, { method: 'POST', body: new FormData(form)})
    .then(response => console.log('Success!', response))
    .catch(error => console.error('Error!', error.message))
})


document.addEventListener("DOMContentLoaded", function() {
  

  setTimeout(function() {
    document.getElementById("popupForm").style.display = "block";
  }, 5000); // 5 seconds in milliseconds


  

  // Close the pop-up form when the close button is clicked
  document.getElementById("closeForm").addEventListener("click", function() {
    document.getElementById("popupForm").style.display = "none";
  });

  // Add event listener for form submission
  document.forms["submit-to-google-sheet"].addEventListener('submit', function() {
    // Hide the pop-up form when the form is submitted
    document.getElementById("popupForm").style.display = "none";
  });
  
});

// Prevent closing the pop-up form when clicking inside it
document.getElementById("popupForm").addEventListener("click", function(event) {
  event.stopPropagation();
});



document.addEventListener('DOMContentLoaded', function () {
  // Find the close button by its ID
  var closeButton = document.getElementById('close');

  // Add a click event listener to the close button
  closeButton.addEventListener('click', function () {
    // Find the popup by its ID
    var popup = document.getElementById('popup');

    // Hide the popup by changing its style display property
    popup.style.display = 'none';
  });

  // Add event listener for opening the form
  document.getElementById('openForm').addEventListener('click', function () {
    document.getElementById('popup').style.display = 'block';
  });
});