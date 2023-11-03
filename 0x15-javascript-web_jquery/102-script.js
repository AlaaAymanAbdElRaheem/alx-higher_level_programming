#!/usr/bin/node

$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
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
  );
}
);
