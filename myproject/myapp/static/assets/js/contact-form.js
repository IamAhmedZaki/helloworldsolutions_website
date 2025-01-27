const form = document.querySelector('#contact-form');
const spinner = document.querySelector('#form-spinner');

form.addEventListener('submit', async (e) => {
  e.preventDefault();

  // Show loading spinner and hide messages
  spinner.style.display = 'inline-block';
  document.querySelector('.success-message').style.display = 'none';
  document.querySelector('.error-message').style.display = 'none';

  const formData = {
    name: document.querySelector('#name-field').value,
    email: document.querySelector('#email-field').value,
    subject: document.querySelector('#subject-field').value,
    message: document.querySelector('#message-field').value,
  };

  try {
    const response = await fetch('/api/contact/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
      },
      body: JSON.stringify(formData),
    });

    if (response.ok) {
      // Show success message and reset form
      document.querySelector('.success-message').style.display = 'block';
      form.reset();
    } else {
      // Show error message with details if available
      const errorData = await response.json();
      document.querySelector('.error-message').textContent =
        errorData.message || 'An error occurred.';
      document.querySelector('.error-message').style.display = 'block';
    }
  } catch (error) {
    console.error('Error:', error);
    document.querySelector('.error-message').textContent =
      'Failed to send your message. Please try again later.';
    document.querySelector('.error-message').style.display = 'block';
  } finally {
    spinner.style.display = 'none'; // Hide spinner after processing
  }
});
