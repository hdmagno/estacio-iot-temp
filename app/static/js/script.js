const socket = io.connect('http://' + window.location.hostname + ':' + location.port);

const temperatureDisplay = document.getElementById('temperature-display');

socket.on('connect', function() {
    console.log('Conectado ao servidor WebSocket');
});

socket.on('new_temperature', function(data) {
    const temperature = data.temperature;
    temperatureDisplay.textContent = `${temperature}°C`;

    if (temperature > 30) {
        temperatureDisplay.classList.remove('temperature-normal');
        temperatureDisplay.classList.add('temperature-high');
    } else {
        temperatureDisplay.classList.remove('temperature-high');
        temperatureDisplay.classList.add('temperature-normal');
    }
});
