import React, { useEffect, useState } from "react";

const Card = ({name, code}) => {
  let aptCodeList = ['3ae33ebe', '79e9ff17','93c2b21f','1493f266','4139b5cd','a32c5888','ac976530','b1b4b365','db1e18fb']
  let [imgCode, setImgCode] = useState("3ae33ebe")

  useEffect (()=>{
    setImgCode(checkCodeList(code))
  })

  let checkCodeList = (code) => {
    if (aptCodeList.includes(code)) {
      return code;
    } else {
      // 이미지가 없으면 랜덤으로 imgList 중 하나를 반환
      let randomIndex = Math.floor(Math.random() * aptCodeList.length);
      return aptCodeList[randomIndex];
    }

  }

  return (
    <div class="max-w-sm border rounded-lg shadow bg-gray-800 border-gray-700">
        <a href="#">
          <img class="rounded-t-lg h-[50%] w-[100%] object-cover" src={`/image/${imgCode}.jpeg`} alt="" />
        </a>

      <div class="p-5">
        <a href="#">
          <h5 class="mb-2 text-2xl font-bold tracking-tight text-white">
           {name}
          </h5>
        </a>
        <p class="mb-3 font-normal text-gray-400">
          Here are the biggest enterprise technology acquisitions of 2021 so
          far, in reverse chronological order.
        </p>
        <div class="flex justify-end">
          <a
        href={`/apartment/${code}`}
            class="inline-flex items-center px-3 py-2 text-sm font-medium text-center text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
          >
            Read more
            <svg
              class="rtl:rotate-180 w-3.5 h-3.5 ms-2"
              aria-hidden="true"
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 14 10"
            >
              <path
                stroke="currentColor"
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M1 5h12m0 0L9 1m4 4L9 9"
              />
            </svg>
          </a>
        </div>
        
      </div>
    </div>
  );
};

export default Card;
