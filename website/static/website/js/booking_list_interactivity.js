document.addEventListener("DOMContentLoaded", function () {
  // Select all rows with the class 'clickable-row' class
  const rows = document.querySelectorAll(".clickable-row");

  rows.forEach((row) => {
    row.addEventListener("click", function () {
      // Get the primary key from the data attribute
      const redirectUrl = this.dataset.href;

      if (redirectUrl) {
        // Navigate to the booking detail page
        // Ensure the URL structure matches your Django URL configuration
        window.location.href = redirectUrl;
      }
    });
  });
});
