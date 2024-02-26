"use client";
import React, { useState, useEffect } from "react";
import styles from "@/app/ui/dashboard/products/products.module.css";
import Search from "@/app/ui/dashboard/search/search";
import Image from "next/image";
import Link from "next/link";

const ProductVariantPage = () => {
  const [variant, setVariants] = useState([]);

  useEffect(() => {
    fetch("http://192.168.0.106:5358/variants", {
      method: "GET",
      header: {
        "Content-Type": "application/json",
      },
    })
      .then((response) => response.json())
      .then((responseJson) => {
        setVariants(responseJson.data);
      });
  }, []);
  return (
    <div className={styles.container}>
      <div className={styles.top}>
        <Search placeholder="Search for a product..." />
        <Link href="/dashboard/products/add">
          <button className={styles.addButton}>Add New</button>
        </Link>
      </div>
      <table className={styles.table}>
        <thead>
          <tr>
            <td>ID</td>
            <td>Kode Produk Variant</td>
            <td>Name</td>
            <td>Image</td>
            <td>Active</td>
            <td>Created At</td>
            <td>Price</td>
            <td>Stock</td>
            <td>Action</td>
          </tr>
        </thead>
        <tbody>
          {variant.map((product) => (
            <tr key={product.id}>
              <td>{product.id}</td>
              <td>{product.code}</td>
              <td>{product.name}</td>
              <td>
                {product.image_location !== "" ? (
                  <Image
                    src={`/product_variant/${product.image_location}`}
                    alt=""
                    width={40}
                    height={40}
                    className={styles.productImage}
                  />
                ) : (
                  <Image
                    src={"/noproduct.png"}
                    alt=""
                    width={40}
                    height={40}
                    className={styles.productImage}
                  />
                )}
              </td>
              <td>{product.active === "true" ? "Active" : "Inactive"}</td>
              <td>{product.created_date?.toString().slice(4, 16)}</td>
              <td>{product.price}</td>
              <td>{product.qty}</td>
              <td>
                <div className={styles.buttons}>
                  <Link href={`/dashboard/product_variant/${product.id}`}>
                    <button className={`${styles.button} ${styles.view}`}>
                      View
                    </button>
                  </Link>
                  <form>
                    <input type="hidden" name="id" value={product.id} />
                    <button className={`${styles.button} ${styles.delete}`}>
                      Delete
                    </button>
                  </form>
                </div>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default ProductVariantPage;
