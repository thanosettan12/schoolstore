
document.addEventListener('DOMContentLoaded', function() {
  const form = document.getElementById('sampleForm');
  const submitButton = document.getElementById('submitButton');
  const warningMessage = document.getElementById('warningMessage');

  form.addEventListener('submit', function(event) {
    // Check if any required field is empty
    const requiredFields = form.querySelectorAll('[required]');
    let isFormValid = true;

    requiredFields.forEach(function(field) {
      if (!field.value) {
        isFormValid = false;
      }
    });

    // If the form is not valid, prevent submission and show the warning message
    if (!isFormValid) {
      event.preventDefault();
      warningMessage.style.display = 'block';
    } else {
      warningMessage.style.display = 'none';
    }
  });
});


