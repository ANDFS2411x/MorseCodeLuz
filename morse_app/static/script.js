document.addEventListener('DOMContentLoaded', function() {
    const morseCode = document.querySelector('#morseCode').innerText;
    const speed = 200; // velocidad del flash en milisegundos

    function flashDot() {
        console.log('dot');
        // Aquí iría el código para activar el flash brevemente
    }

    function flashDash() {
        console.log('dash');
        // Aquí iría el código para activar el flash más tiempo
    }

    for (const symbol of morseCode) {
        setTimeout(() => {
            if (symbol === '.') {
                flashDot();
            } else if (symbol === '-') {
                flashDash();
            }
        }, speed);
        speed += 200;
    }
});
