import React from "react";
import { env, community, attribute, infra, traffic, school, sound, parking } from "../icon";

const Sidebar = () => {
  return (
    <div class="z-20 border-t-4 border-white shadow-md ">
      <aside
        id="logo-sidebar"
        class="fixed top-0 left-0 z-40 w-[16vw] h-screen transition-transform -translate-x-full sm:translate-x-0"
        aria-label="Sidebar"
      >
        <div class=" flex flex-wrap  items-center justify-start mx-auto bg-gray-800">
          {" "}
          <a href="/" class="flex items-center space-x-3 rtl:space-x-reverse">
            <div class="flex justify-center">
              <img src="/Logo2.png" class="w-[63%]"></img>
            </div>
          </a>
        </div>
        <div class="h-full px-3  overflow-y-auto bg-gray-50 bg-gray-800">
          <ul class="space-y-2 font-medium">
            <li>
              <a
                href="#A-env"
                class="flex items-center p-2 rounded-lg text-white hover:bg-gray-700 group"
              >
                {env}
                <div title="환경" class="ms-3">
                  환경(단지,조경)
                </div>
              </a>
            </li>
            <li>
              <a
                href="#A-community"
                class="flex items-center p-2 rounded-lg text-white hover:bg-gray-700 group"
              >
                {community}
                <div title="커뮤니티" class="flex-1 ms-3 whitespace-nowrap">
                  커뮤니티
                </div>
              </a>
            </li>
            <li>
              <a
                href="#A-attribute"
                class="flex items-center p-2 rounded-lg text-white hover:bg-gray-700 group"
              >
                {attribute}
                <div title="동별 특징" class="flex-1 ms-3 whitespace-nowrap">
                  동별 특징
                </div>
              </a>
            </li>
            <li>
              <a
                href="#A-infra"
                class="flex items-center p-2 rounded-lg text-white hover:bg-gray-700 group"
              >
                {infra}
                <div title="주변 상권" class="flex-1 ms-3 whitespace-nowrap">
                  주변 상권
                </div>
              </a>
            </li>
            <li>
              <a
                href="#A-traffic"
                class="flex items-center p-2 rounded-lg text-white hover:bg-gray-700 group"
              >
                {traffic}
                <div class="flex-1 ms-3 whitespace-nowrap">교통</div>
              </a>
            </li>
            <li>
              <a
                href="#A-school"
                class="flex items-center p-2 rounded-lg text-white hover:bg-gray-700 group"
              >
                {school}
                <div class="flex-1 ms-3 whitespace-nowrap">학군</div>
              </a>
            </li>
            <li>
              <a
                href="#A-sound"
                class="flex items-center p-2 rounded-lg text-white hover:bg-gray-700 group"
              >
                {sound}
                <div class="flex-1 ms-3 whitespace-nowrap">소음</div>
              </a>
            </li>
            <li>
              <a
                href="#A-parking"
                class="flex items-center p-2 rounded-lg text-white hover:bg-gray-700 group"
              >
                {parking}
                <div class="flex-1 ms-3 whitespace-nowrap">주차</div>
              </a>
            </li>
          </ul>
        </div>
      </aside>
    </div>
  );
};

export default Sidebar;
