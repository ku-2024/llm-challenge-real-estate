import React from "react";
import Navbar from "../components/Navbar";
import Sidebar from "../components/Sidebar";
import DetailInfo from "../components/DetailInfo";

const Apartment = () => {
  let info = `Lorem Ipsum은 인쇄 및 조판 산업에서 단순한 더미 텍스트입니다. Lorem Ipsum은 1500년대에 한 무명의 인쇄공이 활자 배열을 뒤섞어 본보기 서적을 만들면서부터 업계 표준 더미 텍스트로 자리 잡았습니다. 이 텍스트는 5세기 동안 변함없이 살아남았을 뿐만 아니라 전자 조판으로의 도약도 이루었습니다. 1960년대에는 Lorem Ipsum 구절이 담긴 Letraset 시트가 출시되면서 널리 알려졌으며, 최근에는 Aldus PageMaker와 같은 데스크톱 출판 소프트웨어에도 Lorem Ipsum의 다양한 버전이 포함되었습니다.`;

  return (
    <div class = "bg-slate-100">
      {/* <Navbar /> */}
      <Sidebar />
      <div class="mt-3 p-[2%] mx-[2vw] ml-[18vw]">
        <div class="flex rounded-2xl p-3">
          <div>
            <h1 class="font-semibold text-3xl py-3 mb-4 flex justify-center">호반 베르디움</h1>
            <p class="mr-8 text-xl">{info}</p>
          </div>
          <img
            src="https://pds.joongang.co.kr/news/component/htmlphoto_mmdata/202409/04/db188d78-968d-4407-a75c-62dd5e79e852.jpg"
            class="w-[20vw]"
          ></img>
        </div>
      </div>
      <div class="ml-[18vw] px-[2%] mx-[2vw]">
        <DetailInfo id="A-env" title="환경(단지,조경)" info={info}></DetailInfo>
        <DetailInfo id="A-community" title="커뮤니티" info={info}></DetailInfo>
        <DetailInfo id="A-attribute" title="동별 특징" info={info}></DetailInfo>
        <DetailInfo id="A-infra" title="주변 상권" info={info}></DetailInfo>
        <DetailInfo id="A-traffic" title="교통" info={info}></DetailInfo>
        <DetailInfo id="A-school" title="학군" info={info}></DetailInfo>
        <DetailInfo id="A-sound" title="소음" info={info}></DetailInfo>
        <DetailInfo id="A-parking" title="주차" info={info}></DetailInfo>
      </div>
    </div>
  );
};

export default Apartment;
