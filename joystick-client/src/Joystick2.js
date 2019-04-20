import React, { Component } from "react";

const radius = 75;

class JoyStick extends Component {
  state = {
    pressed: false,
    x: 0,
    y: 0
  };

  onMouseMove = e => {
    console.log(e);
    const { pressed } = this.state;
    if (pressed) {
      const bounds = e.target.getBoundingClientRect();
      let x = e.clientX - (bounds.left + bounds.right) / 2;
      let y = e.clientY - (bounds.bottom + bounds.top) / 2;

      const angle = Math.atan2(y, x);
      const maxX = Math.cos(angle) * radius;
      const maxY = Math.sin(angle) * radius;

      if (maxX > 0) x = Math.min(x, maxX);
      else x = Math.max(x, maxX);

      if (maxY > 0) y = Math.min(y, maxY);
      else y = Math.max(y, maxY);

      this.setState({ x, y });
      console.log(x, y, e.clientY);
    }
  };

  onPressDown = () => {
    this.setState({ pressed: true });
    console.log("pressed");
  };

  onRelease = () => {
    this.setState({ pressed: false });
    this.setState({ x: 0, y: 0 });
    console.log("release");
  };

  render() {
    const { x, y } = this.state;

    const transform = {
      transform: `translate(${x}px, ${y}px)`
    };

    return (
      <div
        onPointerDown={this.onPressDown}
        // onPointerUp={this.onRelease}
        // onPointerLeave={this.onRelease}
        onPointerMove={this.onMouseMove}
        style={wrapper}
      >
        <div style={cirle}>
          <div style={{ ...nipple, ...transform }} />
        </div>
      </div>
    );
  }
}

const wrapper = {
  display: "flex",
  justifyContent: "center",
  alignItems: "center",
  flex: 1,
  backgroundColor: "#000"
};

const cirle = {
  display: "flex",
  justifyContent: "center",
  alignItems: "center",
  borderRadius: "100%",
  width: radius * 2 + "px",
  height: radius * 2 + "px",
  backgroundColor: "#999",
  pointerEvents: "none"
};

const nipple = {
  display: "block",
  borderRadius: "100%",
  width: "30px",
  height: "30px",
  margin: "-15px",
  backgroundColor: "#ccc",
  pointerEvents: "none"
};

export default JoyStick;
