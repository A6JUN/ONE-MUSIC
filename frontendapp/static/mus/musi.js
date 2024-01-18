    document.addEventListener('DOMContentLoaded', function () {
        var audioPlayers = document.querySelectorAll('.audio-player');

        audioPlayers.forEach(function (player) {
            player.addEventListener('play', function (event) {
                // Pause all other audio players when one starts playing
                audioPlayers.forEach(function (otherPlayer) {
                    if (otherPlayer !== event.target) {
                        otherPlayer.pause();
                    }
                });
            });
        });
    });
