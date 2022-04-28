<script>
  import { beforeUpdate } from 'svelte';
  import { Router, Route, navigate } from 'svelte-routing';

  import Login from './Login.svelte';
  import Dashboard from './Dashboard.svelte';

  import { token } from './api/api.service';

  export let url = '';

  $: if (token) {
    navigate('/dashboard', { replace: true });
  } else {
    navigate('/', { replace: true });
  }
</script>

<main>
  <Router {url}>
    <Route path="/" component={Login} />
    <Route path="/dashboard" component={Dashboard} />
  </Router>
</main>
