
$(document).ready(function(){
  //when page loads, show the contents of the keylogger
  $('.container > #keylogView').show();
  showKeys();
    

  })

// request and display all the keys collected
function showKeys() {
  $.ajax({
    url: "./showKeylog",
    method: "GET",
    dataType: 'json',
    success: showKeyTable,
    fail: console.log("FAILED")
  });
}

function showKeyTable(keys){
  $('#keylogView > table > tbody').empty();

  for (const [key,value] of Object.entries(keys)){
    var k = JSON.parse(value);
    $('#keylogView > table > tbody').append(
      '<tr><td>'
      + k.user
      +'</td><td>'
      + k.session
      +'</td><td>'
      + k.time
      +'</td><td>'
      + k.key_down
      +'</td><td>'
      + k.key
      +'</td></tr>'
    );
  }
}