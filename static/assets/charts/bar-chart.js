// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Bar Chart Example
var ctx = document.getElementById("cdfhKent");
var myLineChart = new Chart(ctx, {
  type: 'bar',
  data: {
    labels: ["Authorised", "Processing", "Holding", "Completed"],
    datasets: [{
      label: "Stats",
      backgroundColor: "rgba(2,117,216,1)",
      borderColor: "rgba(2,117,216,1)",
      data: [10, 0, 0, 0],
    }],
  },
  options: {
    legend: {display: false},
    title: {
      display: true,
      text: "Monthly Stats"
    }
  }
});
