import React, { useEffect, useState } from "react";

const Card = ({ name, code }) => {
  let aptCodeList1 = {
    "3ae33ebe": [
      "3ae33ebe",
      "서울시 송파구 송파대로 345",
      "9510세대 (장기전세 1401세대 포함)",
      "2018-12-01",
    ],
    "79e9ff17": [
      "79e9ff17",
      "서울시 중구 다산로 32",
      "5150세대 (장기전세 2034세대 포함)",
      "2002-05-01",
    ],
    "93c2b21f": [
      "93c2b21f",
      "서울시 송파구 올림픽로 99",
      "5678세대",
      "2008-09-01",
    ],
    "1493f266": [
      "1493f266",
      "서울시 송파구 문정동 150",
      "4494세대",
      "1988-12-01",
    ],
    "4139b5cd": [
      "4139b5cd",
      "서울시 송파구 올림픽로 135",
      "5563세대",
      "2008-07-01",
    ],
    a32c5888: [
      "a32c5888",
      "서울시 송파구 양재대로 1218",
      "5540세대",
      "1988-06-01",
    ],
    ac976530: [
      "ac976530",
      "서울시 강동구 고덕동 693",
      "4932세대 (장기전세 140세대 포함)",
      "2019-09-01",
    ],
    b1b4b365: [
      "b1b4b365",
      "서울시 강남구 개포로 310",
      "5040세대",
      "1982-11-01",
    ],
    db1e18fb: [
      "db1e18fb",
      "서울시 송파구 올림픽로 435",
      "6864세대",
      "2008-08-01",
    ],
  };

  const [apartmentInfo, setApartmentInfo] = useState([]);

  useEffect(() => {
    setApartmentInfo(checkCodeList(code));
  }, [code]);

  const checkCodeList = (code) => {
    if (code in aptCodeList1) {
      return aptCodeList1[code];
    } else {
      let keys = Object.keys(aptCodeList1);
      let randomIndex = Math.floor(Math.random() * keys.length);
      return aptCodeList1[keys[randomIndex]];
    }
  };

  return (
    <div className="max-w-sm border rounded-lg shadow bg-gray-800 border-gray-700">
      <a href="#">
        <img
          className="rounded-t-lg h-[55%] w-[100%] object-cover"
          src={`/image/${apartmentInfo[0]}.jpeg`}
          alt={name}
        />
      </a>

      <div className="px-5 pt-5">
        <h5 className="mb-2 text-2xl font-bold tracking-tight text-white">
          {name}
        </h5>
        <p className="font-normal text-gray-400">주소: {apartmentInfo[1]}</p>
        <p className="font-normal text-gray-400">세대수: {apartmentInfo[2]}</p>
        <p className="font-normal text-gray-400">
          완공일자: {apartmentInfo[3]}
        </p>

        <div className="flex justify-end">
          <a
            href={`/apartment/${code}`}
            className="inline-flex items-center px-3 py-2 text-sm font-medium text-center text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
          >
            더 보기
            <svg
              className="rtl:rotate-180 w-3.5 h-3.5 ms-2"
              aria-hidden="true"
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 14 10"
            >
              <path
                stroke="currentColor"
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth="2"
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
