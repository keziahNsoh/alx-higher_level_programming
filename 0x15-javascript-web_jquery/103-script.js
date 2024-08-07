$(document).ready(function() {
  function fetchTranslation() {
    const langCode = $('#language_code').val();
    $.getJSON(`https://www.fourtonfish.com/hellosalut/hello/?lang=${langCode}`, function(data) {
      $('#hello').text(data.hello);
    });
  }

  $('#btn_translate').click(fetchTranslation);

  $('#language_code').keypress(function(event) {
    if (event.which === 13) {  // Enter key pressed
      fetchTranslation();
    }
  });
});

