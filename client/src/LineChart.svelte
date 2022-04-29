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

  import Spinner from './Spinner.svelte';
  import { getLineChartConfig } from './chart-config';

  export let forecast;
  let chart;
  let ctx;

  $: {
    ctx = document.getElementById('lineChart');

    if (ctx && forecast) {
      renderChart();
    }
  }

  function renderChart() {
    if (chart) {
      chart.destroy();
    }

    const chartConfig = getLineChartConfig(forecast, 'line');

    chart = new Chart(ctx, chartConfig);
  }
</script>

<main>
  {#if !forecast}
    <Spinner />
  {/if}
  <div class="my-4 w-100">
    <canvas id="lineChart" />
  </div>
</main>

<style></style>
