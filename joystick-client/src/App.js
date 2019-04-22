import React, { Component } from "react";
import nipplejs from "nipplejs";
import JoyStick from "./Joystick";

// keep constant sending speed for webots
const SEND_INTERVAL = 150;
const RECONNECT_TIMEOUT = 5000;

const robots = [0, 1, 2, 3];

document.body.style.margin = "0px";

class App extends Component {
  state = {
    status: "connecting",
    robotId: robots[0]
  };

  angle = 0;
  force = 0;
  sender = null;
  connecter = null;

  componentDidMount() {
    this.connect();
  }

  connect = () => {
    this.conn = new WebSocket("ws://" + window.location.hostname + ":9000");

    this.conn.onopen = () => {
      this.setState({ status: "connected" });
      clearTimeout(this.connecter);
      this.sender = setInterval(this.sendDirection, SEND_INTERVAL);
    };

    this.conn.onclose = () => {
      this.setState({ status: "closed" });
      clearInterval(this.sender);
      this.connecter = setTimeout(this.connect, RECONNECT_TIMEOUT);
    };

    this.conn.onerror = e => {
      this.setState({ status: "error" });
      clearInterval(this.sender);
      this.connecter = setTimeout(this.connect, RECONNECT_TIMEOUT);
    };
  };

  sendDirection = () => {
    const { robotId } = this.state;
    const { angle, force } = this;
    if (this.conn) this.conn.send(`${robotId}:${angle}|${force}`);
  };

  listener = manager => {
    manager.on("move", (e, stick) => {
      if (stick.angle) {
        this.angle = stick.angle.radian;
        this.force = stick.force;
      }
    });
    manager.on("end", () => {
      this.angle = 0;
      this.force = 0;
    });
  };

  onRobotSelection = robotId => {
    this.setState({ robotId });
  };

  render() {
    const { status, robotId } = this.state;

    const containerStyle = {
      display: "flex",
      flexDirection: "column",
      position: "relative",
      width: "100%",
      height: "100vh",
      boxSizing: "border-box",
      padding: "0.5em"
    };

    return (
      <div style={containerStyle}>
        <div style={menuStyle}>
          <div>
            <div>Status: {status}</div>
          </div>
          {robots.map(id => (
            <button
              onClick={() => this.onRobotSelection(id)}
              key={id}
              style={{
                margin: "1em",
                color: id === robotId ? "red" : "black"
              }}
            >
              Robot {id}
            </button>
          ))}
        </div>
        <div style={joystickContainer}>
          {status === "connected" && <JoyStick listener={this.listener} />}
        </div>
      </div>
    );
  }
}

const joystickContainer = {
  flex: 1,
  display: "flex",
  flexDirection: "column",
  position: "relative"
};

const menuStyle = {
  flex: 0,
  margin: "0.5em",
  background: "#fff"
};

export default App;
