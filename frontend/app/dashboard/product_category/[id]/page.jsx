"use client";
import React, { useEffect, useState } from "react";
import styles from "@/app/ui/dashboard/products/singleProduct/singleProduct.module.css";

const SingleProductCategory = ({ params }) => {
  const { id } = params;
  const [category, setCategory] = useState([]);

  useEffect(() => {
    fetch("http://192.168.0.106:5358/category/" + id, {
      method: "GET",
      header: {
        "Content-Type": "application/json",
      },
    })
      .then((response) => response.json())
      .then((responseJson) => {
        setCategory(responseJson.data);
      });
  }, []);
  return (
    <div className={styles.container}>
      <div className={styles.infoContainer}>
        <div className={styles.imgContainer}>
          <Image src="/noproduct.png" alt="" fill />
        </div>
        {category.name}
      </div>
      <div className={styles.formContainer}>
        <form className={styles.form}>
          <input type="hidden" name="id" value={category.id} />
          <label>Name</label>
          <input type="text" name="name" placeholder={category.name} />
          <label>Active</label>
          <input type="text" name="active" placeholder={category.active} />
          <button>Update</button>
        </form>
      </div>
    </div>
  );
};

export default SingleProductCategory;
