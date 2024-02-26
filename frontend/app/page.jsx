"use client";

import React, { useState, useEffect } from "react";
import styles from "@/app/ui/index2.module.css";
import Image from "next/image";

const ECommerceHomepage = ({ match }) => {
  const [variants, setVariants] = useState([]);

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
    <div>
      <h1>Products</h1>
      <div className={styles.product_grid}>
        {variants.map((variant) => (
          <div className={styles.product_card} key={variant.id}>
            {variant.image_location !== "" ? (
              <Image
                src={`/product_variant/${variant.image_location}`}
                alt=""
                width={120}
                height={120}
              />
            ) : (
              <Image src={"/noproduct.png"} alt="" width={120} height={120} />
            )}
            <h2>{variant.name}</h2>
            <p>Rp.{variant.price}</p>
            <div className={styles.button_container}>
              <button className={styles.button}>Add to Cart</button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default ECommerceHomepage;
