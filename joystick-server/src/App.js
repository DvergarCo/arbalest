import React, { Component } from "react";
import nipplejs from "nipplejs";
import JoyStick from "./Joystick";

// keep constant sending speed for webots
const SEND_GAP = 100;

class App extends Component {
  state = {
    direction: "stay", // (stay, up, right, down, left)
    status: "connecting"
  };

  sendInterval = null;

  sendActions = () => {
    const { direction } = this.state;
    this.conn.send(direction);
    console.log("send", direction);
  };

  componentDidMount() {
    this.conn = new WebSocket("ws://" + window.location.hostname + ":9000");

    this.conn.onopen = () => {
      this.setState({ status: "connected" });
      this.sendInterval = setInterval(this.sendActions, SEND_GAP);
    };

    this.conn.onclose = () => {
      this.setState({ status: "closed" });
      clearInterval(this.sendInterval);
    };
    this.conn.onerror = e => {
      this.setState({ status: "error" });
      clearInterval(this.sendInterval);
    };
  }

  listener = manager => {
    manager.on("dir", (e, stick) => {
      if (stick.direction && stick.direction.angle) {
        const direction = stick.direction.angle;
        this.setState({ direction });
      }
    });
    manager.on("end", () => {
      const direction = "stay";
      this.setState({ direction });
    });
  };

  render() {
    const { status } = this.state;

    const containerStyle = {
      display: "flex",
      flexDirection: "column",
      position: "relative",
      width: "100%",
      height: `${window.innerHeight}px`
    };

    return (
      <div>
        <div style={containerStyle}>
          <div style={menuStyle}>{status}</div>
          {status === "connected" && <JoyStick listener={this.listener} />}
        </div>
      </div>
    );
  }
}

const joyOptions = {
  mode: "semi",
  catchDistance: 150,
  color: "#fff"
};

const joyStyle = {
  flex: 1
};

const menuStyle = {
  flex: 0,
  margin: "0.5em",
  background: "#fff"
};

export default App;
