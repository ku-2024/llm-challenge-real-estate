import React, { useEffect, useState } from "react";
import Sidebar from "../components/Sidebar";
import DetailInfo from "../components/DetailInfo";
import { useParams } from "react-router-dom";
import {
  env,
  community,
  attribute,
  traffic,
  infra,
  school,
  sound,
  parking,
} from "../icon";

const Apartment = () => {
  const info = `주소 : 서울시 송파구 신천동 17\n세대수 : 6864세대\n완공일자 : 2008-08-01\n시공사 : 현대건설(주) 외\n난방방식 : 지역난방, 열병합\n동 정보 : 52, 86A, 86B, 87C, 108B, 108A, 108B1, 109C, 149, 174`;
  const { apartmentId } = useParams();
  const [apt, setApt] = useState({});
  const [summaries, setSummaries] = useState({});
  const [reviewsArray, setReviewsArray] = useState([]); // New state to hold reviews
  const [error, setError] = useState(null);

  useEffect(() => {
    getData();
    getCategoryData();
  }, []);

  const getData = () => {
    fetch(`http://127.0.0.1:5000/getdata/${apartmentId}`)
      .then((response) => {
        if (!response.ok) {
          throw new Error("네트워크 응답에 문제가 있습니다.");
        }
        return response.json();
      })
      .then((data) => {
        setApt(data);
      })
      .catch((error) => {
        setError(error.message);
      });
  };

  const getCategoryData = () => {
    fetch(`http://127.0.0.1:5000/get/review_summary/db1e18fb`)
      .then((response) => {
        if (!response.ok) {
          throw new Error("네트워크 응답에 문제가 있습니다.");
        }
        return response.json();
      })
      .then((data) => {
        setSummaries(data.data || []);
        const reviews = data?.data?.map((summary) => summary.review) || [];
        setReviewsArray(reviews);
      })
      .catch((error) => {
        setError(error.message);
      });
  };

  return (
    <div className="bg-slate-100">
      <div className="flex">
        <Sidebar />
        <div className="mt-3 p-[2%] mx-[2vw] ml-[18vw] w-[78vw]">
          <div className="flex rounded-2xl p-3">
            <div className="w-[73%]">
              <h1 className="font-semibold text-3xl py-3 mb-4 flex justify-center">
                {apt?.data?.apt_name || "아파트 이름 없음"} 
              </h1>
              <ul className="list-disc pl-5 space-y-2">
                {info.split("\n").map((item, index) => (
                  <li key={index} className="text-xl">
                    {item.replace(" : ", ": ")}
                  </li>
                ))}
              </ul>
            </div>
            <img
              src="https://pds.joongang.co.kr/news/component/htmlphoto_mmdata/202409/04/db188d78-968d-4407-a75c-62dd5e79e852.jpg"
              class="w-[23vw] rounded-lg"
              alt="Apartment Image"
            />
          </div>
        </div>
      </div>

      <div className="ml-[18vw] px-[2%] mx-[2vw]">
        <div className="flex flex-wrap justify-between mb-4">
          {apt?.data?.trades?.length > 0 ? (
            apt.data.trades.slice(0, 4).map((element, index) => (
              <div
                key={index}
                className="border shadow-md rounded-xl p-3 mr-5 mt-5 w-[36vw]"
              >
                <div class = "font-bold">{element.apt_sq}평</div>
                <div>{element.avg_price}</div>
                <div>{element.top_avg_price}</div>
                <div>{element.bottom_avg_price}</div>
              </div>
            ))
          ) : (
            <div>No data available</div>
          )}
        </div>
        <DetailInfo id="A-env" title="환경(단지,조경)" info={reviewsArray[0]} icon={env} />
        <DetailInfo id="A-community" title="커뮤니티" info={reviewsArray[1]} icon={community} />
        <DetailInfo id="A-attribute" title="동별 특징" info={reviewsArray[2]} icon={attribute} />
        <DetailInfo id="A-infra" title="주변 상권" info={reviewsArray[3]} icon={infra} />
        <DetailInfo id="A-traffic" title="교통" info={reviewsArray[4]} icon={traffic} />
        <DetailInfo id="A-school" title="학군" info={reviewsArray[5]} icon={school} />
        <DetailInfo id="A-sound" title="소음" info={reviewsArray[6]} icon={sound} />
        <DetailInfo id="A-parking" title="주차" info={reviewsArray[7]} icon={parking} />
      </div>
    </div>
  );
};

export default Apartment;