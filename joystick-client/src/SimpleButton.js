import React from "react";

const SimpleButton = ({ onClick, isOn, text }) => (
  <button
    onClick={onClick}
    style={{
      flex: 1,
      color: isOn ? "red" : "black"
    }}
  >
    {text}
  </button>
);

export default SimpleButton;
