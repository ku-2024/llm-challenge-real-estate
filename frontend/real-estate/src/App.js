import "./App.css";
import React, { useEffect, useState } from "react";
import Card from "./components/Card";
import Map from "./components/Maps";
import { Container as MapDiv, NaverMap, Marker, useNavermaps } from 'react-naver-maps'
// import { NavermapsProvider } from 'react-naver-maps';x

function App() {
  const [data, setData] = useState([]);
  const [dataToShow, setDataToShow] = useState([]);
  const [error, setError] = useState(null);
  const [searchTerm, setSearchTerm] = useState("");

  useEffect(() => {
    fetchData();
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
        setData(data.data); 
        setDataToShow(data.data.slice(0, 3));
      })
      .catch((error) => {
        setError(error.message);
      });
  };

  const handleSearch = (event) => {
    event.preventDefault();
    const newData = data.filter((element) =>
      element.apt_name.includes(searchTerm)
    );
    setDataToShow(newData);
  };

  return (
    <div className="bg-gray-600 min-h-screen flex-col items-center justify-center ">
      <div className="w-[100vw] flex flex-col items-center justify-center pt-5  ">
        <img src="/Logo2.png" className="w-[25%] m-[-3%]" alt="Logo"></img>
      </div>
      <div className="flex justify-center items-center h-[10vh] mb-4">
        <form className=" mx-auto" onSubmit={handleSearch}>
          <label
            htmlFor="default-search"
            className="mb-2 text-sm font-medium sr-only text-white"
          >
            Search
          </label>
          <div className="relative w-[50vw]">
            <div className="absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none">
              <svg
                className="w-4 h-4 text-gray-400"
                aria-hidden="true"
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 20 20"
              >
                <path
                  stroke="currentColor"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth="2"
                  d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z"
                />
              </svg>
            </div>
            <input
              type="search"
              id="default-search"
              className="block w-full p-4 ps-10 text-sm border rounded-lg bg-gray-700 border-gray-600 placeholder-gray-400 text-white focus:ring-blue-500 focus:border-blue-500"
              placeholder="아파트 검색"
              value={searchTerm} 
              onChange={(e) => setSearchTerm(e.target.value)} // Handle search input correctly
              required
            />
            <button
              type="submit"
              className="text-white absolute end-2.5 bottom-2.5 focus:ring-4 focus:outline-none font-medium rounded-lg text-sm px-4 py-2 bg-blue-600 hover:bg-blue-700 focus:ring-blue-800"
            >
              검색
            </button>
          </div>
        </form>
      </div>
      <div>
        <MapDiv
        style={{
          width: '80%',
          height: '600px',
        }}
      >
          <Map/>
        </MapDiv>
      </div>
      <div className="mx-20 pb-20">
        <div className="flex justify-around gap-y-5 flex-wrap">
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