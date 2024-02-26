"use client";
import React, { useEffect, useState } from "react";
import styles from "@/app/ui/dashboard/products/singleProduct/singleProduct.module.css";
import Image from "next/image";

const SingleProductVariantPage = ({ params }) => {
  const { id } = params;
  const [product, setProduct] = useState([]);

  useEffect(() => {
    fetch("http://192.168.0.106:5358/variant/" + id, {
      method: "GET",
      header: {
        "Content-Type": "application/json",
      },
    })
      .then((response) => response.json())
      .then((responseJson) => {
        setProduct(responseJson.data);
      });
  }, []);
  return (
    <div className={styles.container}>
      <div className={styles.infoContainer}>
        <div className={styles.imgContainer}>
          {product.image_location !== "" ? (
            <Image
              src={`/product_variant/${product.image_location}`}
              alt=""
              fill
            />
          ) : (
            <Image src={"/noproduct.png"} alt="" fill />
          )}
        </div>
        {product.title}
      </div>
      <div className={styles.formContainer}>
        <form className={styles.form}>
          <input type="hidden" name="id" value={product.id} />
          <label>Name</label>
          <input type="text" name="name" placeholder={product.name} />
          <label>Product Category</label>
          <input type="text" name="name" placeholder={product.product_id} />
          <label>Stock</label>
          <input type="text" name="name" placeholder={product.qty} />
          <label>Price</label>
          <input type="text" name="name" placeholder={product.price} />
          <label>Active</label>
          <input type="text" name="active" placeholder={product.active} />
          <button>Update</button>
        </form>
      </div>
    </div>
  );
};

export default SingleProductVariantPage;
