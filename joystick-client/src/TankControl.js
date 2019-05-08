import React, { Component } from "react";

class TankContorl extends Component {
  left = 0;
  right = 0;

  constructor(props) {
    super(props);
    this.leftRef = React.createRef();
  }

  onTouchLeft = e => this.onTouch(e, "left");
  onTouchRight = e => this.onTouch(e, "right");

  onTouch = (e, side) => {
    const bounds = e.target.getBoundingClientRect();

    const touch = e.targetTouches[0];

    const x = touch.clientX;
    const l = bounds.left;
    const r = bounds.right;

    if (x >= l && x <= r) {
      const height = bounds.bottom - bounds.top;
      const pos = Math.max(
        Math.min(((bounds.top - touch.clientY) / height + 0.5) * 2, 1),
        -1
      );
      this[side] = pos;
    }

    this.props.listener({ left: this.left, right: this.right });
  };

  onTouchEndLeft = () => this.onTouchEnd("left");
  onTouchEndRight = () => this.onTouchEnd("right");

  onTouchEnd = side => {
    this[side] = 0;
    this.props.listener({ left: this.left, right: this.right });
  };

  render() {
    return (
      <div style={container}>
        <div
          onTouchStart={this.onTouchLeft}
          onTouchMove={this.onTouchLeft}
          onTouchEnd={this.onTouchEndLeft}
          ref={this.leftRef}
          style={joyStyle}
        />
        <div
          onTouchStart={this.onToucRight}
          onTouchMove={this.onTouchRight}
          onTouchEnd={this.onTouchEndRight}
          ref={this.leftRef}
          style={joyStyle}
        />
      </div>
    );
  }
}

const container = {
  flex: 1,
  display: "flex"
};

const joyStyle = {
  flex: 1,
  background: "#000",
  borderRadius: "12px",
  margin: "5px"
};

export default TankContorl;
