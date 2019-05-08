import React from "react";

const SimpleButton = ({ onClick, isOn, text }) => (
  <button
    onClick={onClick}
    style={{
      color: isOn ? "red" : "black"
    }}
  >
    {text}
  </button>
);

export default SimpleButton;
