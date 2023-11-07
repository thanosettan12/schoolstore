 // JavaScript to show the pop-up and overlay after form submission
    const form = document.getElementById('sampleForm');
    const popup = document.getElementById('popup');
    const overlay = document.getElementById('overlay');
    const closePopup = document.getElementById('closePopup');

    form.addEventListener('submit', function (event) {
        event.preventDefault(); // Prevent the form from actually submitting

        // Display the popup and overlay
        popup.style.display = 'block';
        overlay.style.display = 'block';
    });

    closePopup.addEventListener('click', function () {
        // Close the popup and overlay
        popup.style.display = 'none';
        overlay.style.display = 'none';
    });