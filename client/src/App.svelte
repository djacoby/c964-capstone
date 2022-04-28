<script>
  import { Router, Route } from 'svelte-routing';

  import Login from './Login.svelte';
  import Dashboard from './Dashboard.svelte';

  export let url = '';
</script>

<main>
  <Router {url}>
    <Route path="/dashboard" component={Dashboard} />
    <Route path="/" component={Login} />
  </Router>
</main>
