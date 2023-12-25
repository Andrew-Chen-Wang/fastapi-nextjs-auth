import styles from './page.module.css'

function EmailLogin() {
  return (
    <div className={styles.container}>
      <main className={styles.main}>
        <h1 className={styles.title}>Login</h1>
        <form className={styles.form}>
          <label className={styles.label} htmlFor="username">
            Username
          </label>
          <input className={styles.input} id="username" type="text" />
          <label className={styles.label} htmlFor="password">
            Password
          </label>
          <input className={styles.input} id="password" type="password" />
          <button className={styles.button} type="submit">
            Login
          </button>
        </form>
      </main>
    </div>
  )
}

export default function Home() {
  return (
      <EmailLogin />
  )
}
