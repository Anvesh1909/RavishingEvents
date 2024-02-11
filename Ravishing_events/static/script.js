document.addEventListener("DOMContentLoaded", function() {
  setTimeout(function() {
    document.getElementById("popupForm").style.display = "block";
  }, 5000); // 10 seconds in milliseconds

  // Close the pop-up form when the close button is clicked
  document.getElementById("closeForm").addEventListener("click", function() {
    document.getElementById("popupForm").style.display = "none";
  });
});

// Prevent closing the pop-up form when clicking inside it
document.getElementById("popupForm").addEventListener("click", function(event) {
  event.stopPropagation();
});

