document.addEventListener('DOMContentLoaded', function() {
    console.log("JavaScript is executed");
    var messages = document.querySelectorAll('.messages');
    
    if (messages.length > 0) {
        messages.forEach(function(message) {
            message.classList.add('fade-in');

            // Attendez la fin de l'animation fade-in avant d'ajouter fade-out
            setTimeout(function() {
                message.classList.add('fade-out');
                message.classList.remove('fade-in'); // Supprimer la classe fade-in
            }, 1000);

            // Supprimez le message après l'animation fade-out
            message.addEventListener('transitionend', function(event) {
                if (event.propertyName === 'opacity' && message.classList.contains('fade-out')) {
                    message.remove();
                }
            });
        });
    }
});
