// Handle form submission on the index page
document.getElementById('upload-form').addEventListener('submit', function (event) {
  event.preventDefault();
  const fileInput = document.getElementById('image-upload');

  if (fileInput.files.length > 0) {
    // Redirect to the result page (simulate processing)
    window.location.href = "/result";
  } else {
    alert("Please upload an image first.");
  }
});


const sidebar = document.querySelector('.sidebar');
const toggleButton = document.getElementById('sidebar-toggle');

toggleButton.addEventListener('click', () => {
  sidebar.classList.toggle('visible');
});

// Optional: Hide sidebar when clicking outside
document.addEventListener('click', (event) => {
  if (!sidebar.contains(event.target) && !toggleButton.contains(event.target)) {
    sidebar.classList.remove('visible');
  }
});




// Chart.js for defect trends (Dashboard)
if (document.getElementById('defectChart')) {
  const defectChartCanvas = document.getElementById('defectChart').getContext('2d');
  new Chart(defectChartCanvas, {
    type: 'bar',
    data: {
      labels: ['Printing Errors', 'Stains', 'Structural Flaws'],
      datasets: [{
        label: 'Defect Count',
        data: [12, 8, 5], // Replace with actual data
        backgroundColor: ['#a14aff', '#f79e3f', '#d5c0f5'],
        borderWidth: 1
      }]
    },
    options: {
      responsive: true,
      scales: {
        y: {
          beginAtZero: true
        }
      },
      onClick: (event, elements) => {
        if (elements.length > 0) {
          const index = elements[0].index;
          alert(`You clicked on ${this.data.labels[index]}`);
        }
      }
    }
  });
}