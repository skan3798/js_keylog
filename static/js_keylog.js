
$(document).ready(function(){
    //when page loads, show the contents of the keylogger
    $('.container > #KeylogView').show();
    showKeys();

  })

  // request and display all the keys collected
  function showKeys() {
    $.ajax({
      url: "./js_keylog",
      method: "GET",
      dataType: 'json',
      success: showKeyTable
    });
  }

  function showKeyTable(){
    print("here")
    for (const [key,value] of Object.entries(keys)){
      var k = JSON.parse(value);
      $('#KeylogView > table > tbody').append(
        '<tr><td>'
        + k.time
        +'</td><td>'
        + k.key-up
        +'</td><td>'
        + k.key
        +'</td></tr>'
      );
    }
  }