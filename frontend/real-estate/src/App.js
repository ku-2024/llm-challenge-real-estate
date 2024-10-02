import "./App.css";
import React, { useEffect, useState } from 'react';
import { useNavigate } from "react-router-dom";
import Card from "./components/Card";
import logo from "./dongsan.png"

function App() {
  const navigate = useNavigate();

  const [data, setData] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    // FastAPI에서 데이터 가져오기
    fetch('http://127.0.0.1:5000/get/all-name-code')
      .then((response) => {
        if (!response.ok) {
          throw new Error('네트워크 응답에 문제가 있습니다.');
        }
        return response.json();
      })
      .then((data) => {
        setData(data); // 데이터를 state에 저장
      })
      .catch((error) => {
        setError(error.message); // 에러 메시지 저장
      });
      console.log(data)
    }, [data]);

  const handleSearch = () => {
    navigate("/apartment/1");
  };
  const handleHome = () => {
    navigate("/");
  };


  return (

    <div>
      <div class = "flex justify-center items-center h-[10vh] bg-blue-100">
      <img src={logo} width='100' onClick={handleHome}></img>
      <form class="max-w-md mx-auto">
        <label
          for="default-search"
          class="mb-2 text-sm font-medium text-gray-900 sr-only dark:text-white"
        >
          Search
        </label>
        <div class="relative w-[30vw]">
          <div class="absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none">
            <svg
              class="w-4 h-4 text-gray-500 dark:text-gray-400"
              aria-hidden="true"
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 20 20"
            >
              <path
                stroke="currentColor"
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z"
              />
            </svg>
          </div>
          <input
            type="search"
            id="default-search"
            class="block w-full p-4 ps-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
            placeholder="아파트 검색"
            required
          />
          <button
            type="submit"
            class="text-white absolute end-2.5 bottom-2.5 bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-4 py-2 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
            onClick={handleSearch}
          >
            검색
          </button>
        </div>
      </form>
      </div>
      <div>
        <h1>데이터 목록</h1>
        <ul>
          {data.map((item) => (
            <li key={item.apt_code}>{item.apt_name} - {item.apt_code}</li>
          ))}
        </ul>
      </div>
      <div class = "flex justify-around gap-y-8 flex-wrap">
        <Card name = {data[0].apt_name} code={data[0].apt_code}></Card>
        <Card name = {data[1].apt_name} code={data[1].apt_code}></Card>
        <Card name = {data[7].apt_name} code={data[7].apt_code}></Card>

        <Card name = {data[3].apt_name} code={data[3].apt_code}></Card>
        <Card name = {data[4].apt_name} code={data[4].apt_code}></Card>
        <Card name = {data[5].apt_name} code={data[5].apt_code}></Card>
      </div>
      
    </div>
  );
}

export default App;
