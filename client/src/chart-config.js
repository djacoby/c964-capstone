/**
 * Get line chart config object
 * 
 * @param {Forecast} forecast 
 */
export const getChartConfig = (forecast) => {
  return {
    type: 'line',
    data: {
      datasets: [
        {
          data: forecast,
          backgroundColor: 'rgba(255, 99, 132, 0.2)',
          borderColor: [
            'rgba(255, 99, 132, 1)',
            // 'rgba(54, 162, 235, 1)',
            // 'rgba(255, 206, 86, 1)',
            // 'rgba(75, 192, 192, 1)',
            // 'rgba(153, 102, 255, 1)',
            // 'rgba(255, 159, 64, 1)',
          ],
          borderWidth: 1,
        },
      ],
    },
    options: {
      responsive: true,
      maintainAspectRatio: true,
      parsing: {
        xAxisKey: 'ds',
        yAxisKey: 'yhat1',
      },
      plugins: {
        legend: {
          display: false,
        },
        title: {
          display: true,
          text: 'Traffic Forecast',
        },
      },
    },
  };
}
