import React from "react";
import styles from "@/app/ui/dashboard/products/addProduct/addProduct.module.css";

const AddProductVariantPage = () => {
  return (
    <div className={styles.container}>
      <form className={styles.form}>
        <input type="text" placeholder="name" name="name" required />
        <select name="product_id" id="product_id">
          <option value="general">Choose a Category</option>
          <option value="1">Kitchen</option>
          <option value="2">Phone</option>
          <option value="3">Computer</option>
        </select>
        <input type="number" placeholder="price" name="price" required />
        <input type="number" placeholder="stock" name="stock" required />
        <button type="submit">Submit</button>
      </form>
    </div>
  );
};

export default AddProductVariantPage;
