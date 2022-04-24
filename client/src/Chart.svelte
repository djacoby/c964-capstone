<script>
  import {
    Chart,
    LineElement,
    PointElement,
    LineController,
    CategoryScale,
    LinearScale,
    Legend,
    Title,
    Tooltip,
    SubTitle,
  } from 'chart.js';

  import { onMount } from 'svelte';

  Chart.register(
    LineElement,
    PointElement,
    LineController,
    CategoryScale,
    LinearScale,
    Legend,
    Title,
    Tooltip,
    SubTitle
  );

  import { getChartConfig } from './chart-config';

  export let forecast;
  let chart;
  let ctx;

  $: {
    ctx = document.getElementById('myChart');

    if (ctx && forecast) {
      renderChart();
    }
  }

  function renderChart() {
    if (chart) {
      chart.destroy();
    }

    const chartConfig = getChartConfig(forecast);

    chart = new Chart(ctx, chartConfig);
  }
</script>

<main>
  <div class="my-4 w-100">
    <canvas id="myChart" />
  </div>
</main>

<style></style>
