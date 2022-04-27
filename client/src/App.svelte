<script>
  import { Router, Route } from 'svelte-routing';

  import Login from './Login.svelte';
  import Dashboard from './Dashboard.svelte';

  export let url;
</script>

<main>
  <Router {url}>
    <Route path="/" component={Login} />
    <Route path="/dashboard" component={Dashboard} />
  </Router>
</main>
