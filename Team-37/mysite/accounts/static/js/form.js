// Function to dynamically create player name input fields based on the number of players
function createPlayerNameFields(numPlayers) {
    const container = document.getElementById('player-names-container');
    container.innerHTML = ''; // Clear the container

    for (let i = 1; i <= numPlayers; i++) {
        const label = document.createElement('label');
        label.textContent = `Player ${i} Name:`;

        const input = document.createElement('input');
        input.type = 'text';
        input.name = `player${i}`;
        input.required = true;

        container.appendChild(label);
        container.appendChild(input);
        container.appendChild(document.createElement('br'));
    }
}



// Event listener for form submission
const playerForm = document.getElementById('player-form');

// Event listener for number of players input change
const numPlayersInput = document.getElementById('num-players');
numPlayersInput.addEventListener('input', function () {
    createPlayerNameFields(numPlayersInput.value);
});
