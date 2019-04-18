import React, { Component } from "react";
import nipplejs from "nipplejs";
import JoyStick from "./Joystick";

// keep constant sending speed for webots
const SEND_GAP = 300;

const robots = [0, 1, 2, 3];

class App extends Component {
  state = {
    status: "connecting",
    robotId: robots[0]
  };

  componentDidMount() {
    // this.conn = new WebSocket("ws://192.168.43.54:9000");
    this.conn = new WebSocket("ws://" + window.location.hostname + ":9000");
    //this.conn = new WebSocket("wss://echo.websocket.org");

    this.conn.onopen = () => {
      this.setState({ status: "connected" });
    };

    this.conn.onclose = () => {
      this.setState({ status: "closed" });
    };
    this.conn.onerror = e => {
      this.setState({ status: "error" });
    };
  }

  sendDirection = direction => {
    const { robotId } = this.state;
    this.conn.send(`${robotId}:${direction}`);
  };

  listener = manager => {
    manager.on("dir", (e, stick) => {
      if (stick.direction && stick.direction.angle) {
        this.sendDirection(stick.direction.angle);
      }
    });
    manager.on("end", () => {
      this.sendDirection("stay");
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
      height: `${window.innerHeight}px`
    };

    return (
      <div>
        <div style={containerStyle}>
          <div style={menuStyle}>
            Status: {status}
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
