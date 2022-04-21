<script>
  import Navbar from './Navbar.svelte';

  const data = fetch(
    'http://localhost:5000/api/v1/store/1/forecast?start_date=2022-04-20&end_date=2022-04-25'
  )
    .then((response) => response.json())
    .then((data) => {
      console.log(JSON.stringify(data, null, 2));
    })
    .catch((error) => {
      console.log(error);
    });
</script>

<main>
  <Navbar />
  <div class="container">
    <h1>hello</h1>
  </div>
</main>

<style>
</style>
