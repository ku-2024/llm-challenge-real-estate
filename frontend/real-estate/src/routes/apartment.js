import React, { useEffect, useState } from "react";
import Sidebar from "../components/Sidebar";
import DetailInfo from "../components/DetailInfo";
import { useParams } from "react-router-dom";
import { env, community, attribute, traffic,infra, school, sound, parking } from "../icon";

const Apartment = () => {
  // const icons = [env, community, attribute, infra, traffic, school, sound, parking];
  const info = `Lorem Ipsum은 인쇄 및 조판 산업에서 단순한 더미 텍스트입니다. Lorem Ipsum은 1500년대에 한 무명의 인쇄공이 활자 배열을 뒤섞어 본보기 서적을 만들면서부터 업계 표준 더미 텍스트로 자리 잡았습니다. 이 텍스트는 5세기 동안 변함없이 살아남았을 뿐만 아니라 전자 조판으로의 도약도 이루었습니다. 1960년대에는 Lorem Ipsum 구절이 담긴 Letraset 시트가 출시되면서 널리 알려졌으며, 최근에는 Aldus PageMaker와 같은 데스크톱 출판 소프트웨어에도 Lorem Ipsum의 다양한 버전이 포함되었습니다.`;
  const { apartmentId } = useParams();
  const [apt, setApt] = useState({});
  const [error, setError] = useState(null);

  useEffect(() => {
    getData();
    console.log(apartmentId);
    console.log(apt);
  }, [apartmentId]);

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

  return (
    <div className="bg-slate-100">
      <div class="flex">
        <Sidebar />
        <div className="mt-3 p-[2%] mx-[2vw] ml-[18vw]">
          <div className="flex rounded-2xl p-3">
            <div>
              <h1 className="font-semibold text-3xl py-3 mb-4 flex justify-center">
                {apt?.data?.apt_name || "아파트 이름 없음"}
              </h1>
              <p className="mr-8 text-xl">{info}</p>
            </div>
            <img
              src="https://pds.joongang.co.kr/news/component/htmlphoto_mmdata/202409/04/db188d78-968d-4407-a75c-62dd5e79e852.jpg"
              class="w-[20vw]"
              alt="Apartment Image"
            />
          </div>
        </div>
      </div>

      <div class="ml-[18vw] px-[2%] mx-[2vw]">
        <div class="flex flex-wrap  justify-between mb-4">
          {apt?.data?.trades?.length > 0 ? (
            apt.data.trades.map((element) => (
              <div class="border shadow-md rounded-xl p-3 mr-5 mt-5 w-[36vw]">
                <div>{element.apt_sq}평</div>
                <div>{element.avg_price}</div>
                <div>{element.top_avg_price}</div>
                <div>{element.bottom_avg_price}</div>
              </div>
            ))
          ) : (
            <div>No data available</div>
          )}
        </div>
        <DetailInfo id="A-env" title="환경(단지,조경)" info={info} icon={env} />
        <DetailInfo
          id="A-community"
          title="커뮤니티"
          info={info}
          icon={community}
        />
        <DetailInfo id="A-attribute" title="동별 특징" info={info} icon={attribute} />
        <DetailInfo id="A-infra" title="주변 상권" info={info} icon={infra} />
        <DetailInfo id="A-traffic" title="교통" info={info} icon={traffic} />
        <DetailInfo id="A-school" title="학군" info={info} icon={school} />
        <DetailInfo id="A-sound" title="소음" info={info} icon={sound} />
        <DetailInfo id="A-parking" title="주차" info={info} icon={parking} />
      </div>
    </div>
  );
};

export default Apartment;
