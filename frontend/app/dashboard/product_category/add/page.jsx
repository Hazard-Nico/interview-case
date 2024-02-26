import styles from "@/app/ui/dashboard/products/addProduct/addProduct.module.css";

const AddProductPage = () => {
  return (
    <div className={styles.container}>
      <form className={styles.form}>
        <input
          type="text"
          placeholder="Masukkan nama kategori"
          name="name"
          required
        />
        <select name="active" id="active">
          <option value="kitchen">Activate</option>
          <option value="phone">Inactivate</option>
        </select>
        <button type="submit">Submit</button>
      </form>
    </div>
  );
};

export default AddProductPage;
