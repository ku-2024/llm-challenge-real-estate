import React from "react";

const Navbar = () => {
  return (
    <nav class="fixed top-0 left-0 right-0 bg-gray-800 shadow-lg">
      <div class=" flex flex-wrap  items-center justify-start mx-auto p-4">
        {" "}
        <a href="/" class="flex items-center space-x-3 rtl:space-x-reverse">
          <svg
            class="w-6 h-6 text-yellow-500"
            aria-hidden="true"
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 14 8"
          >
            <path
              stroke="currentColor"
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M13 7 7.674 1.3a.91.91 0 0 0-1.348 0L1 7"
            />
          </svg>
          <span class="text-2xl font-semibold whitespace-nowrap text-gray-300">
            위키동산
          </span>
        </a>
      </div>
    </nav>
  );
};

export default Navbar;
