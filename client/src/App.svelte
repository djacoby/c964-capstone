<script>
  import { onMount } from 'svelte';

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

  import Navbar from './Navbar.svelte';

  let storeList;
  let selectedStore;
  let forecast;
  let myChart;

  async function getStores() {
    const res = await fetch('http://localhost:5000/api/v1/store');
    return res.json();
  }

  async function getForecast(storeId) {
    const res = await fetch(
      `http://localhost:5000/api/v1/store/${storeId}/forecast?start_date=2022-04-21&end_date=2022-05-05`
    );
    return res.json();
  }

  function convertDate(date) {
    return new Date(date).toLocaleString('en-us', {
      month: '2-digit',
      day: '2-digit',
      year: 'numeric',
    });
  }

  function roundTrafficValue(trafficCount) {
    return Math.round(Math.abs(trafficCount));
  }

  onMount(async () => {
    getStores().then((stores) => {
      selectedStore = stores.result.shift();
      storeList = stores.result;
      getForecast(selectedStore.id)
        .then((fcast) => {
          forecast = fcast.result.map((f) => {
            return {
              ds: convertDate(f.ds),
              yhat1: roundTrafficValue(f.yhat1),
            };
          });
        })
        .then(() => {
          renderChart();
        });
    });
  });

  function updateForecast() {
    getForecast(selectedStore.id)
      .then((fcast) => {
        forecast = fcast.result.map((f) => {
          return {
            ds: convertDate(f.ds),
            yhat1: roundTrafficValue(f.yhat1),
          };
        });
      })
      .then(() => {
        renderChart();
      });
  }

  function renderChart() {
    const ctx = document.getElementById('myChart');
    if (myChart) {
      myChart.destroy();
    }

    myChart = new Chart(ctx, {
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
    });
  }
</script>

<main>
  <Navbar />
  <div class="container">
    <div class="row">
      <div class="col-lg-3">
        {#if storeList && selectedStore}
          <select
            class="form-select"
            aria-label="Default select example"
            bind:value={selectedStore}
          >
            <option selected value={selectedStore}>
              Store #{selectedStore.id}
              {selectedStore.city}, {selectedStore.state}
            </option>
            {#each storeList as store}
              <option value={store}
                >Store #{store.id} {store.city}, {store.state}
              </option>
            {/each}
          </select>
          <button
            type="button"
            class="btn btn-primary"
            on:click={() => updateForecast()}>Submit</button
          >
        {/if}
      </div>
    </div>

    <div
      class="chart-container"
      style="position: relative; height:40vh; width:80vw"
    >
      <canvas id="myChart" />
    </div>

    <!-- <div class="row">
      <div class="col-lg-12">
        {#if forecast}
          <table class="table table-striped">
            <thead>
              <tr>
                <th scope="col">Date</th>
                <th scope="col">Traffic</th>
              </tr>
            </thead>
            <tbody>
              {#each forecast as day}
                <tr>
                  <td
                    >{convertDate(day.ds)}</td
                  >
                  <td>{roundTrafficValue(day.yhat1)}</td>
                </tr>
              {/each}
            </tbody>
          </table>
        {/if}
      </div>
    </div> -->
  </div>
</main>

<style>
</style>
