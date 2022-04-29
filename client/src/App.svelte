<script>
  import { Router, Route, navigate } from 'svelte-routing';

  import Login from './Login.svelte';
  import Dashboard from './Dashboard.svelte';

  export let url = '';

  let token = JSON.parse(localStorage.getItem('user'))?.token;

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
