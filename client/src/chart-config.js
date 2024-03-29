/**
 * Get line chart config object
 * 
 * @param {Forecast} forecast 
 */
export const getLineChartConfig = (forecast) => {
  return {
    type: 'line',
    data: {
      datasets: [
        {
          data: forecast,
          backgroundColor: 'rgba(255, 99, 132, 0.2)',
          borderColor: [
            'rgba(54, 162, 235, 1)',
          ],
          borderWidth: 2,
        },
      ],
    },
    options: {
      responsive: true,
      maintainAspectRatio: true,
      scales: {
        x: {
          title: {
            display: true,
            text: 'Date',
          },
        },
        y: {
          title: {
            display: true,
            text: 'Traffic',
          },
        },
      },
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

/**
 * Get bar chart config object
 * 
 * @param {Forecast} forecast 
 */
export const getBarChartConfig = (forecast) => {
  return {
    type: 'bar',
    data: {
      datasets: [
        {
          data: forecast,
          backgroundColor: 'rgba(255, 99, 132, 0.2)',
          borderColor: [
            'rgb(255, 99, 132)',
          ],
          borderWidth: 2,
        },
      ],
    },
    options: {
      responsive: true,
      maintainAspectRatio: true,
      scales: {
        x: {
          title: {
            display: true,
            text: 'Date',
          },
        },
        y: {
          title: {
            display: true,
            text: 'Traffic',
          },
        },
      },
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
