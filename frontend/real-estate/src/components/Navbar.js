import React from 'react'

const Navbar = () => {
  return (
    <nav class="fixed top-0 left-0 right-0 border-gray-200 bg-gray-50 dark:bg-gray-300 dark:border-gray-700">
        <div class="max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4">
          <a href="/" class="flex items-center space-x-3 rtl:space-x-reverse">
            <svg
              class="w-6 h-6 text-gray-800 dark:text-black"
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
            <span class="self-center text-2xl font-semibold whitespace-nowrap dark:text-black">
              위키동산
            </span>
          </a>
        </div>
      </nav>
  )
}

export default Navbar