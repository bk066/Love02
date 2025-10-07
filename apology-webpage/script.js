// Listen for button click to display heart
document.getElementById("show-love-btn").addEventListener("click", function() {
    const container = document.getElementById("heart-display");
    container.innerHTML = ""; // Clear previous hearts

    // Simulate fetching heart HTML (could be replaced with an API call)
    const heartHTML = getHeartHTML();

    container.innerHTML = heartHTML;
});

// Placeholder function for heart structure
function getHeartHTML() {
    return `<div class="heart"></div>`;
}
