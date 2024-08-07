// Ensure the DOM is fully loaded before running the script
$(document).ready(function() {
  // Attach a click event handler to the <div> with ID #red_header
  $('#red_header').click(function() {
    // Add the class 'red' to the <header> element
    $('header').addClass('red');
  });
});

