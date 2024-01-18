function playSong(songUrl) {
            var audioPlayer = document.getElementById('audioPlayer');
            var audioSource = document.getElementById('audioSource');
            audioSource.src = songUrl;
            audioPlayer.load();
            audioPlayer.play();
        }