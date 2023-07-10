// Add click event listener to the logout button
document.getElementById('logout-btn').addEventListener('click', function() {
    sessionStorage.clear();
    window.location.href = '/';
  });
  