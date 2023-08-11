function redirectToBooking() {
    window.location.href = "#booking";
}
window.onload = function() {
    if (window.location.hash === "#booking") {
        history.replaceState({}, document.title, window.location.pathname);
    }
};

const buttons = document.querySelectorAll('.btn-blue');
buttons.forEach(button => {
    button.addEventListener('click', redirectToBooking);
 });
