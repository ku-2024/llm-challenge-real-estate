import React from 'react'

const DetailInfo = ({title,info,id,}) => {
  return (
    <div id = {id} title = {title} class = "mb-6 rounded-2xl p-3 border shadow-md">
        <h1 class="font-semibold text-2xl py-2">{title}</h1>
        <p>{info}</p>
    </div>
  )
}

export default DetailInfo