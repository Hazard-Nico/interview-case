import styles from "../ui/dashboard/dashboard.module.css";

const Dashboard = () => {
  return (
    <div>
      <div className={styles.wrapper}>
        <div className={styles.main}>
          <div className={styles.cards}></div>
        </div>
      </div>
      <div className={styles.side}></div>
    </div>
  );
};

export default Dashboard;
