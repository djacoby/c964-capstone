<script>
  import { navigate } from 'svelte-routing';
  import { login } from './api/api.service';

  let email;
  let password;
  let error = false;

  async function loginUser() {
    error = await login(email, password);
    if (!error) {
      navigate('/dashboard');
    }
  }
</script>

<body class="text-center">
  <main class="form-signin">
    <form>
      <img src="/images/logo.png" alt="" width="200" height="200" />
      <h1 class="h3 mb-3 fw-normal">Please sign in</h1>

      <div class="form-floating">
        <input
          type="email"
          class="form-control"
          id="floatingInput"
          bind:value={email}
          placeholder="name@example.com"
        />
        <label for="floatingInput">Email address</label>
      </div>
      <div class="form-floating">
        <input
          type="password"
          class="form-control"
          id="floatingPassword"
          bind:value={password}
          placeholder="Password"
        />
        <label for="floatingPassword">Password</label>
      </div>

      {#if error}
        <div class="text-danger my-1">Invalid email or password</div>
      {/if}

      <button
        class="w-100 btn btn-lg btn-primary"
        type="submit"
        on:click|preventDefault={() => loginUser()}>Sign in</button
      >
      <p class="mt-5 mb-3 text-muted">&copy; 2022 Acme Grocery INC.</p>
    </form>
  </main>
</body>

<style>
  body {
    display: flex;
    align-items: center;
    padding-top: 40px;
    padding-bottom: 40px;
    background-color: #f5f5f5;
  }

  .form-signin {
    width: 100%;
    max-width: 330px;
    padding: 15px;
    margin: auto;
  }

  .form-signin .form-floating:focus-within {
    z-index: 2;
  }

  .form-signin input[type='email'] {
    margin-bottom: -1px;
    border-bottom-right-radius: 0;
    border-bottom-left-radius: 0;
  }

  .form-signin input[type='password'] {
    margin-bottom: 10px;
    border-top-left-radius: 0;
    border-top-right-radius: 0;
  }
</style>
