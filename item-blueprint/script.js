let downloadUrl = ''; // To store the download URL

// Get the modal, close elements, and the OK button
const modal = document.getElementById('modal');
const closeModal = document.getElementById('closeModal');
const okBtn = document.getElementById('okBtn');

// Get all buttons with the "download-button" class
const downloadButtons = document.querySelectorAll('.download-button');

// Add event listener to each download button
downloadButtons.forEach(button => {
  button.addEventListener('click', (event) => {
    event.preventDefault(); // Prevent immediate download

    // Save the download URL (from the button's data attribute or href)
    downloadUrl = button.getAttribute('data-download-url');

    // Show modal
    modal.style.display = 'block';
  });
});

// Close modal when (X) or OK is clicked
closeModal.onclick = function() {
  modal.style.display = 'none';
};

window.onclick = function(event) {
  if (event.target === modal) {
    modal.style.display = 'none';
  }
};

// Trigger download when OK button is clicked
okBtn.onclick = function() {
  if (downloadUrl) {
    // Programmatically create an anchor element to trigger the download
    const link = document.createElement('a');
    link.href = downloadUrl;
    link.download = ''; // Optional: set the file name for the download
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link); // Clean up the element

    // Close the modal after download
    modal.style.display = 'none';
  }
};
