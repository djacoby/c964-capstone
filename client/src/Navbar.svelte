<script>
  import { logout } from './api/api.service';

  function logoutUser() {
    logout();
  }
</script>

<main>
  <div class="container">
    <header
      class="d-flex flex-wrap align-items-center justify-content-center justify-content-md-between mb-4 border-bottom"
    >
      <span
        class="d-flex align-items-center col-md-3 mb-2 mb-md-0 me-3 text-dark text-decoration-none"
      >
        <img src="/images/logo.png" alt="" width="100" height="100" />
      </span>

      <div class="col-md-3 text-end">
        <button
          type="button"
          class="btn btn-outline-secondary"
          on:click={() => logoutUser()}>Logout</button
        >
      </div>
    </header>
  </div>
</main>
