$(document).ready(function () {

     $('.text').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "bounceIn",
        },
        out: {
            effect: "bounceOut",
        },

     })

     // Siri Voice Control
     var siriWave = new SiriWave({
        container: document.getElementById("siri-container"),
        width: 800,
        height: 200,
        style: "ios9",
        amplitude: "1",
        speed: "0.30",
        autostart: true
      });

    // siri Voice message
    $('.siri-message').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "fadeInUp",
            sync: true,
        },
        out: {
            effect: "fadeOutUp",
            sync: true,
        },

     })

     //mic button click

     $("#MicBtn").click(function () { 
        eel.playAssistantSound()
         $("#Oval").attr("hidden", true);
         $("#SiriWave").attr("hidden", false);
         eel.takecommand()()
     });

});