function search() {
  const target = document.getElementById('target-group').value;
  const location = document.getElementById('city-country').value;

  fetch('/search', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ target, location })
  })
  .then(response => response.text())
  .then(data => {
    document.getElementById('search-result').textContent = data;
  })
  .catch(error => {
    console.error('Error:', error);
  });
}
