<script>
  import { onMount } from 'svelte';

  import SveltyPicker from 'svelty-picker';
  import { navigate } from 'svelte-routing';

  import Navbar from './Navbar.svelte';
  import Chart from './Chart.svelte';
  import Spinner from './Spinner.svelte';

  import {
    getAllStoresList,
    getForecast,
    getStoreById,
    getStoreListByDistrict,
  } from './api/api.service';

  import {
    MIN_START_DATE,
    END_DATE,
    validateStartDate,
    validateEndDate,
  } from './util';

  let user = JSON.parse(localStorage.getItem('user'))?.user;

  if (!user) {
    navigate('/', { replace: true });
  }

  let storeList;
  let selectedStore;
  let forecast;

  let startDate = MIN_START_DATE;
  let endDate = END_DATE;

  let validStartDate = true;
  let validEndDate = true;

  onMount(async () => {
    if (!user) {
      navigate('/', { replace: true });
    }
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

  async function getStoreForecast() {
    forecast = await getForecast(selectedStore.id, startDate, endDate);
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
            on:click={() => getStoreForecast()}>Submit</button
          >
        </div>

        <div class="d-grid d-block d-md-none mt-3">
          <button
            type="button"
            class="btn btn-primary"
            disabled={!validStartDate || !validEndDate}
            on:click={() => getStoreForecast()}>Submit</button
          >
        </div>
      </div>
    {/if}
    {#await forecast}
      <Spinner />
    {:then fcast}
      <Chart forecast={fcast} />
    {/await}
  </div>
</main>

<style>
</style>
