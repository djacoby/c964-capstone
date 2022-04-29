<script>
  export let forecast;
</script>

<main>
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
              <td>{day.ds}</td>
              <td>{day.yhat1}</td>
            </tr>
          {/each}
        </tbody>
      </table>
    {/if}
  </div>
</main>
