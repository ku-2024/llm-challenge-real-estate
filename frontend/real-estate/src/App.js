import "./App.css";
import React, { useEffect, useState } from "react";
import Card from "./components/Card";

function App() {
  const [data, setData] = useState([]);
  const [dataToShow, setDataToShow] = useState([]);
  const [error, setError] = useState(null);
  const [searchTerm, setSearchTerm] = useState("");

  useEffect(() => {
    // FastAPI에서 데이터 가져오기
    fetchData();
    setDataToShow(data)
  }, []);

  const fetchData = () => {
    fetch("http://127.0.0.1:5000/get/all-name-code")
      .then((response) => {
        if (!response.ok) {
          throw new Error("네트워크 응답에 문제가 있습니다.");
        }
        return response.json();
      })
      .then((data) => {
        setData(data); // 데이터를 state에 저장
        setDataToShow(data.slice(0, 3));
      })
      .catch((error) => {
        setError(error.message); // 에러 메시지 저장
      });
  };
  const handleSearch = (event) => {
    event.preventDefault();

    setSearchTerm(searchTerm);
    const newData = data.filter((element) =>
      element.apt_name.includes(searchTerm)
    );
    setDataToShow(newData);
  };

  return (
    <div class="bg-gray-600 min-h-screen flex-col items-center justify-center ">
      <div class="w-[100vw] flex flex-col items-center justify-center pt-5  ">
        <img src="/wikiDSLogo.png" class="w-[20%] m-[-3%]"></img>
      </div>
      <div class="flex justify-center items-center h-[10vh] mb-4">
        <form class=" mx-auto">
          <label
            for="default-search"
            class="mb-2 text-sm font-medium text-gray-900 sr-only dark:text-white"
          >
            Search
          </label>
          <div class="relative w-[50vw]">
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
              value={searchTerm} // Set the input's value to the state
              onChange={(e) => setSearchTerm(e.target.value)} //
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
      <div class="mx-20 pb-20">
        <div class="flex justify-around gap-y-5 flex-wrap">
          {dataToShow.map((item) => (
            <Card
              key={item.apt_code}
              name={item.apt_name}
              code={item.apt_code}
            />
          ))}
        </div>
      </div>
    </div>
  );
}

export default App;
