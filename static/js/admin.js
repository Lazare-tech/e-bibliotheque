// Graph
var ctx = document.getElementById("myChart");

var myChart = new Chart(ctx, {
  type: "line",
  data: {
    labels: [
      "Chemises",
      "Chaussures",
      "Sacs-à-main",
      "Bijoux",
      "Mèches",
      "Perruques",
      "Maquillages",
    ],
    datasets: [
      {
        data: [8, 4, 1, 24, 29, 92, 34],
        lineTension: 0,
        backgroundColor: "transparent",
        borderColor: "#007bff",
        borderWidth: 4,
        pointBackgroundColor: "#007bff",
      },
    ],
  },
  options: {
    scales: {
      yAxes: [
        {
          ticks: {
            beginAtZero: false,
          },
        },
      ],
    },
    legend: {
      display: false,
    },
  },
});
    // Cacher automatiquement les alertes après 5 secondes (5000 ms)
    setTimeout(function () {
      let alerts = document.querySelectorAll('.alert');
      alerts.forEach(function (alert) {
        alert.classList.remove('show');
        alert.classList.add('fade');
      });
    }, 5000);
  
  
    document.addEventListener("DOMContentLoaded", function () {
      // Automatically close the alert after 5 seconds
      setTimeout(function () {
        var alertMessage = document.getElementById("alertMessage");
        if (alertMessage) {
          alertMessage.style.transition = "opacity 1s ease";
          alertMessage.style.opacity = "0";

          setTimeout(function () {
            alertMessage.remove(); // Removes the alert from the DOM after fade out
          }, 1000); // Match this time with the fade-out time
        }
      }, 5000); // 5 seconds
    });
