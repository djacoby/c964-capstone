<script>
  import {
    Chart,
    BarElement,
    BarController,
    PointElement,
    CategoryScale,
    LinearScale,
    Legend,
    Title,
    Tooltip,
    SubTitle,
  } from 'chart.js';

  Chart.register(
    BarElement,
    BarController,
    PointElement,
    CategoryScale,
    LinearScale,
    Legend,
    Title,
    Tooltip,
    SubTitle
  );

  import { getBarChartConfig } from './chart-config';

  export let forecast;
  let chart;
  let ctx;

  $: {
    ctx = document.getElementById('barChart');

    if (ctx && forecast) {
      renderChart();
    }
  }

  function renderChart() {
    if (chart) {
      chart.destroy();
    }

    const chartConfig = getBarChartConfig(forecast, 'bar');

    chart = new Chart(ctx, chartConfig);
  }
</script>

<main>
  <div class="my-4 w-100">
    <canvas id="barChart" />
  </div>
</main>

<style></style>
