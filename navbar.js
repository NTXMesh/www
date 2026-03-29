// navbar.js
document.addEventListener("DOMContentLoaded", function () {
  const navContainer = document.getElementById("navbar-container");

  if (!navContainer) {
    console.error("Navbar container not found!");
    return;
  }

  fetch("/navbar.html")
    .then(response => {
      if (!response.ok) {
        throw new Error(`Failed to load navbar: ${response.status}`);
      }
      return response.text();
    })
    .then(data => {
      navContainer.innerHTML = data;
    })
    .catch(error => {
      console.error("Error loading navbar:", error);
    });
});
