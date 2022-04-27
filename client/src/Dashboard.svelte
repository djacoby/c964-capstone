<script>
  import { onMount } from 'svelte';

  import SveltyPicker from 'svelty-picker';

  import Navbar from './Navbar.svelte';
  import Chart from './Chart.svelte';
  import Spinner from './Spinner.svelte';

  import {
    getAllStoresList,
    getForecast,
    getStoreById,
    getStoreListByDistrict,
    user,
  } from './api/api.service';

  import {
    MIN_START_DATE,
    END_DATE,
    validateStartDate,
    validateEndDate,
    convertDate,
    roundTrafficValue,
  } from './util';

  let storeList;
  let selectedStore;
  let forecast;
  let loading = true;

  let startDate = MIN_START_DATE;
  let endDate = END_DATE;

  let validStartDate = true;
  let validEndDate = true;

  onMount(async () => {
    if (user?.['store_id']) {
      return getStoresForManager();
    }
    if (user?.['district_id']) {
      return getStoresForDistrictManager();
    }

    return getAllStores();
  });

  function getAllStores() {
    getAllStoresList()
      .then((stores) => {
        selectedStore = stores.result[0];
        storeList = stores.result;
      })
      .then(() => getStoreForecast());
  }

  function getStoresForManager() {
    getStoreById(user['store_id'])
      .then((stores) => {
        selectedStore = stores.result[0];
        storeList = stores.result;
      })
      .then(() => getStoreForecast());
  }

  function getStoresForDistrictManager() {
    getStoreListByDistrict(user['district_id'])
      .then((stores) => {
        selectedStore = stores.result[0];
        storeList = stores.result;
      })
      .then(() => getStoreForecast());
  }

  function getStoreForecast() {
    getForecast(selectedStore.id, startDate, endDate).then((fcast) => {
      forecast = fcast.result.map((f) => {
        return {
          ds: convertDate(f.ds),
          yhat1: roundTrafficValue(f.yhat1),
        };
      });
    });
    loading = false;
  }

  function updateForecast() {
    loading = true;
    getForecast(selectedStore.id, startDate, endDate).then((fcast) => {
      forecast = fcast.result.map((f) => {
        return {
          ds: convertDate(f.ds),
          yhat1: roundTrafficValue(f.yhat1),
        };
      });
    });
    loading = false;
  }
</script>

<main>
  <Navbar />
  <div class="container">
    {#if storeList && selectedStore}
      <div class="row my-4 w-100">
        <div class="col-md-5">
          <label for="store-select" class="form-label pt-3">Store</label>
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
          <label for="start-picker" class="form-label pt-3">Start Date</label>
          <SveltyPicker
            id="start-picker"
            inputClasses="form-control form-select"
            format="yyyy-mm-dd"
            bind:value={startDate}
            on:input={() => {
              validStartDate = validateStartDate(startDate);
            }}
          />
          {#if !validStartDate}
            <div class="text-danger mt-1">
              Start Date can't be before tomorrow
            </div>
          {/if}
        </div>

        <div class="col-md-3">
          <label for="end-picker" class="form-label pt-3">End Date</label>
          <SveltyPicker
            id="end-picker"
            inputClasses="form-control form-select"
            format="yyyy-mm-dd"
            bind:value={endDate}
            on:input={() => {
              validEndDate = validateEndDate(startDate, endDate);
            }}
          />
          {#if !validEndDate}
            <div class="text-danger mt-1">
              End Date can't be before Start Date
            </div>
          {/if}
        </div>

        <div class="col-md-1 d-sm-none d-md-block mt-5">
          <button
            type="button"
            class="btn btn-primary"
            disabled={!validStartDate || !validEndDate}
            on:click={() => updateForecast()}>Submit</button
          >
        </div>

        <div class="d-grid d-block d-md-none mt-3">
          <button
            type="button"
            class="btn btn-primary"
            disabled={!validStartDate || !validEndDate}
            on:click={() => updateForecast()}>Submit</button
          >
        </div>
      </div>
    {/if}

    {#if loading}
      <Spinner />
    {:else}
      <Chart {forecast} />
    {/if}
  </div>
</main>

<style>
</style>
