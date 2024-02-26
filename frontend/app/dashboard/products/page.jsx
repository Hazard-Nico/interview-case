"use client";
import React, { useState, useEffect } from "react";
import styles from "@/app/ui/dashboard/products/products.module.css";
import Search from "@/app/ui/dashboard/search/search";
import Image from "next/image";
import Link from "next/link";
import axios from "axios";

const ProductsPage = ({ searchParams }) => {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    fetch("http://192.168.0.106:5358/products", {
      method: "GET",
      header: {
        "Content-Type": "application/json",
      },
    })
      .then((response) => response.json())
      .then((responseJson) => {
        setProducts(responseJson.data);
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
            <td>PLU</td>
            <td>Name</td>
            <td>Product Category</td>
            <td>Active</td>
            <td>Created At</td>
            <td>Action</td>
          </tr>
        </thead>
        <tbody>
          {products.map((product) => (
            <tr key={product.id}>
              <td>{product.id}</td>
              <td>{product.plu}</td>
              <td>{product.name}</td>
              <td>{product.product_category === 1 ? "Makanan" : "Minuman"}</td>
              <td>{product.active === "true" ? "Active" : "Inactive"}</td>
              <td>{product.created_date?.toString().slice(4, 16)}</td>
              <td>
                <div className={styles.buttons}>
                  <Link href={`/dashboard/products/${product.id}`}>
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

export default ProductsPage;
