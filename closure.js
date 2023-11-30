(function() {
    var clickCount = 0; // This variable is enclosed within the closure

    // This is the closure function
    window.updateClickCount = function() {
        clickCount++; // Increment the click count
        console.log("Button clicked " + clickCount + " times."); // Log the current count
    };
})();