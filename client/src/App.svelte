<script>
  import { onMount } from 'svelte';

  import Navbar from './Navbar.svelte';
  import Chart from './Chart.svelte';

  import { getAllStoresList, getForecast } from './api/api.service';
  import { convertDate, roundTrafficValue } from './util';

  let storeList;
  let selectedStore;
  let forecast;

  onMount(async () => {
    // const stores = await getAllStoresList();
    // storeList = stores.result;
    // selectedStore = storeList.result.shift();

    // const forecastData = await getForecast(
    //   selectedStore.id,
    //   '2022-05-01',
    //   '2022-05-08'
    // );

    // forecast = forecastData.result.map((f) => {
    //   return {
    //     ds: convertDate(f.ds),
    //     yhat1: roundTrafficValue(f.yhat1),
    //   };
    // });
    getAllStoresList().then((stores) => {
      selectedStore = stores.result.shift();
      storeList = stores.result;
      getForecast(selectedStore.id, '2022-05-01', '2022-05-08').then(
        (fcast) => {
          forecast = fcast.result.map((f) => {
            return {
              ds: convertDate(f.ds),
              yhat1: roundTrafficValue(f.yhat1),
            };
          });
        }
      );
    });
  });

  function updateForecast() {
    getForecast(selectedStore.id, '2022-05-01', '2022-05-08').then((fcast) => {
      forecast = fcast.result.map((f) => {
        return {
          ds: convertDate(f.ds),
          yhat1: roundTrafficValue(f.yhat1),
        };
      });
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

    <Chart {forecast} />

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
                  <td>{convertDate(day.ds)}</td>
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
