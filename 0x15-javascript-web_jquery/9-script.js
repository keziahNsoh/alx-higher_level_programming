$(document).ready(function() {
  // Perform an AJAX GET request to the provided URL
  $.getJSON('https://hellosalut.stefanbohacek.dev/?lang=fr', function(data) {
    // Extract the 'hello' translation from the response
    const helloTranslation = data.hello;
    
    // Update the content of the <div id="hello"> with the translation
    $('#hello').text(helloTranslation);
  });
});

