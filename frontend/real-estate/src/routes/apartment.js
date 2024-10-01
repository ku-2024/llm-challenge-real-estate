import React from "react";
import Navbar from "../components/Navbar";

const Apartment = () => {
  return (
    <div class="">
      <Navbar />
      <div>
        <div class=" p-[2%] mx-[7vw]">
          <div class="flex">
            <div>
            <h1 class="font-semibold text-2xl py-3">호반 베르디움</h1>
            <p class="mr-8">
              Lorem Ipsum is simply dummy text of the printing and typesetting
              industry. Lorem Ipsum has been the industry's standard dummy text
              ever since the 1500s, when an unknown printer took a galley of
              type and scrambled it to make a type specimen book. It has
              survived not only five centuries, but also the leap into
              electronic typesetting, remaining essentially unchanged. It was
              popularised in the 1960s with the release of Letraset sheets
              containing Lorem Ipsum passages, and more recently with desktop
              publishing software like Aldus PageMaker including versions of
              Lorem Ipsum.
            </p>
            </div>
            <img
              src="https://pds.joongang.co.kr/news/component/htmlphoto_mmdata/202409/04/db188d78-968d-4407-a75c-62dd5e79e852.jpg"
              class="w-[20vw]"
            ></img>
          </div>
        </div>
      </div>
      
    </div>
  );
};

export default Apartment;
