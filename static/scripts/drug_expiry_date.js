// Function to check expiration date and generate warranty notification
function checkExpiration() {
    var expirationDate = document.getElementById("expirydate").value;
    var currentDate = new Date();

    var diffMilliseconds = new Date(expirationDate) - currentDate;
    var diffDays = Math.floor(diffMilliseconds / (1000 * 60 * 60 * 24));

    if (diffDays <= 90) {
        var warranty = "Your drug is expiring soon. Warranty remaining: ";
        if (diffDays <= 0) {
            warranty += "Expired";
        } else {
            warranty += diffDays + " days";
        }
        document.getElementById("warrantyNotification").innerHTML = warranty;
        return false; // Prevent form submission
    } else {
        document.getElementById("warrantyNotification").innerHTML = "Your drug is still within the warranty period.";
        return true; // Allow form submission
    }
}

// Add event listener to the form submission
document.getElementById("drug_reg_Form").addEventListener("submit", function(event) {
    var shouldSubmit = checkExpiration(); // Call the expiration check function
    if (!shouldSubmit) {
        event.preventDefault(); // Prevent default form submission
    }
});
