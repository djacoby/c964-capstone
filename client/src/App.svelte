<script>
  import { onMount } from 'svelte';

  import SveltyPicker from 'svelty-picker';

  import Navbar from './Navbar.svelte';
  import Chart from './Chart.svelte';

  import { getAllStoresList, getForecast } from './api/api.service';

  import {
    getStartDate,
    getEndDate,
    convertDate,
    roundTrafficValue,
  } from './util';

  let storeList;
  let selectedStore;
  let forecast;

  let startDate = getStartDate();
  let endDate = getEndDate();

  let invalidInput = false;

  onMount(async () => {
    getAllStoresList().then((stores) => {
      selectedStore = stores.result[0];
      storeList = stores.result;

      getForecast(selectedStore.id, startDate, endDate).then((fcast) => {
        forecast = fcast.result.map((f) => {
          return {
            ds: convertDate(f.ds),
            yhat1: roundTrafficValue(f.yhat1),
          };
        });
      });
    });
  });

  function updateForecast() {
    getForecast(selectedStore.id, startDate, endDate).then((fcast) => {
      forecast = fcast.result.map((f) => {
        return {
          ds: convertDate(f.ds),
          yhat1: roundTrafficValue(f.yhat1),
        };
      });
    });
  }
</script>

<main class="bg-light">
  <Navbar />
  <div class="container">
    {#if storeList && selectedStore}
      <div class="row mb-5">
        <div class="col-md-3">
          <label for="store-select" class="form-label">Store</label>
          <select
            class="form-select"
            id="store-picker"
            bind:value={selectedStore}
          >
            <option selected value={selectedStore}>
              Store #{selectedStore.id}
              {selectedStore.city}, {selectedStore.state}
            </option>
            {#each storeList as store}
              {#if store.id !== selectedStore.id}
                <option value={store}
                  >Store #{store.id} {store.city}, {store.state}
                </option>
              {/if}
            {/each}
          </select>
        </div>

        <div class="col-md-3">
          <label for="start-picker" class="form-label">Start Date</label>
          <SveltyPicker
            id="start-picker"
            inputClasses="form-control form-select"
            format="yyyy-mm-dd"
            bind:value={startDate}
          />
        </div>

        <div class="col-md-3">
          <label for="end-picker" class="form-label">End Date</label>
          <SveltyPicker
            id="end-picker"
            inputClasses="form-control form-select"
            format="yyyy-mm-dd"
            bind:value={endDate}
          />
        </div>

        <div class="col-md-3 d-flex align-items-end">
          <button
            type="button"
            class="btn btn-primary"
            on:click={() => updateForecast()}>Submit</button
          >
        </div>
      </div>
    {/if}

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
