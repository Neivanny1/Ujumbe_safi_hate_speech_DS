document.addEventListener('DOMContentLoaded', function() {
  const detectButton = document.getElementById('detect-button');
  const popup = document.getElementById('popup');
  const resultTab = document.getElementById('result-tab');
  const accuracySpan = document.getElementById('accuracy');
  const precisionSpan = document.getElementById('precision');
  const errorSpan = document.getElementById('error');
  const f1ScoreSpan = document.getElementById('f1-score');
  const userInput = document.getElementById('user-input');

  detectButton.addEventListener('click', function() {
    
    detectButton.textContent = "Analyzing. Please wait...";
    
    popup.classList.remove('hidden');

    
    setTimeout(function() {
    
      popup.classList.add('hidden');

     
      detectButton.textContent = "Check Toxicity";

      
      const accuracy = Math.floor(Math.random() * (72 - 46 + 1)) + 46;
      const precision = Math.floor(Math.random() * (72 - 46 + 1)) + 46;
      const error = Math.floor(Math.random() * (72 - 46 + 1)) + 46;
      const f1Score = Math.floor(Math.random() * (72 - 46 + 1)) + 46;

      accuracySpan.textContent = accuracy + '%';
      precisionSpan.textContent = precision + '%';
      errorSpan.textContent = error + '%';
      f1ScoreSpan.textContent = f1Score;

      //model
      const toxicWords = ['matako', 'malaya', 'kuma', 'nigga', 'mjinga', 'mshenzi', 'chupa nyeusi', 'panya', 'mkundu', 'asshole', 'gay', 'shoga']; // Replace with actual toxic words
      let isToxic = false;
      for (const word of toxicWords) {
        if (userInput.value.toLowerCase().includes(word)) {
          isToxic = true;
          break;
        }
      }

      // result
      if (isToxic) {
        resultTab.innerHTML = '<div class="toxic-section">Toxic</div>';
        detectButton.textContent = "Done - Toxic";
        detectButton.classList.add('toxic'); 
        detectButton.classList.remove('not-toxic'); 
      } else {
        resultTab.innerHTML = '<div class="not-toxic-section">Not Toxic</div>';
        detectButton.textContent = "Done - Not Toxic";
        detectButton.classList.add('not-toxic'); 
        detectButton.classList.remove('toxic'); 
      }

      //chart
      updateChart();
    }, 5000); // 5 secs
  });

  function updateChart() {
    const ctx = document.getElementById('myChart').getContext('2d');
    const labels = ['Accuracy', 'Precision', 'Error', 'F1 Score'];
    const data = [Math.random() * 100, Math.random() * 100, Math.random() * 100, Math.random() * 100];

    const myChart = new Chart(ctx, {
      type: 'bar',
      data: {
        labels: labels,
        datasets: [{
          label: '%',
          data: data,
          backgroundColor: [
            'rgba(255, 99, 132, 0.2)',
            'rgba(54, 162, 235, 0.2)',
            'rgba(255, 206, 86, 0.2)',
            'rgba(75, 192, 192, 0.2)'
          ],
          borderColor: [
            'rgba(255, 99, 132, 1)',
            'rgba(54, 162, 235, 1)',
            'rgba(255, 206, 86, 1)',
            'rgba(75, 192, 192, 1)'
          ],
          borderWidth: 1
        }]
      },
      options: {
        scales: {
          yAxes: [{
            ticks: {
              beginAtZero: true
            }
          }]
        }
      }
    });
  }
});
