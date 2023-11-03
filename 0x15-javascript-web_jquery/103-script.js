#!/usr/bin/node

function translate () {
  const language = $('INPUT#language_code').val();
  const apiUrl = `https://fourtonfish.com/hellosalut/?lang=${language}`;

  $.ajax({
    url: apiUrl,
    type: 'GET',
    dataType: 'json',
    success: function (data) {
      $('DIV#hello').text(data.hello);
    }
  });
}
$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    translate();
  }
  );
  $('INPUT#language_code').keypress(function (e) {
    if (e.which === 13) {
      translate();
    }
  }
  );
}
);
