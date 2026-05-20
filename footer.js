// footer.js
document.addEventListener("DOMContentLoaded", function () {
  const footerContainer = document.getElementById("footer-container");

  if (!footerContainer) {
    console.error("Footer container not found!");
    return;
  }

  fetch("/footer.html")
    .then(response => {
      if (!response.ok) {
        throw new Error(`Failed to load footer: ${response.status}`);
      }
      return response.text();
    })
    .then(data => {
      footerContainer.innerHTML = data;
    })
    .catch(error => {
      console.error("Error loading footer:", error);
    });
});