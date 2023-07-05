// Add click event listener to the logout button
document.getElementById('logout-btn').addEventListener('click', function() {
    // Perform logout logic here, such as clearing session/local storage, redirecting, etc.
    
    // Example: Clear session storage and redirect to the login page
    sessionStorage.clear();
    window.location.href = '/'; // Replace with the actual login page URL
  });
  