import React, { Component } from "react";
import JoyStick from "./Joystick";
import TankContorl from "./TankControl";
import SimpleButton from "./SimpleButton";

// keep constant sending speed for webots
// webots lags, if interval is too high
const SEND_INTERVAL = 150;
const RECONNECT_TIMEOUT = 5000;

const robots = [0, 1, 2, 3];

document.body.style.margin = "0px";

class App extends Component { 
  state = {
    status: "connecting",
    robotId: robots[0],
    tankControls: true
  };

  left = 0;
  right = 0;
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
    const { left, right } = this;
    if (this.conn) this.conn.send(`${robotId}:${left}|${right}`);
  };

  joystickListener = manager => {
    manager.on("move", (e, stick) => {
      if (stick.angle) {
        const angle = stick.angle.radian;
        const force = Math.min(stick.force, 1);
        const forward = Math.sin(angle);
        const turn = Math.cos(angle);

        this.right = Math.min(0.8 * forward - 0.6 * turn, 1);
        this.left = Math.min(force * (0.8 * forward + 0.6 * turn), 1);
      }
    });
    manager.on("end", () => {
      this.left = 0;
      this.right = 0;
    });
  };

  tankListener = ({ left, right }) => {
    this.left = left;
    this.right = right;
  };

  onRobotSelection = robotId => {
    this.setState({ robotId });
  };

  onTankControlPress = () => {
    this.setState({ tankControls: true });
  };

  onJoystickControlPress = () => {
    this.setState({ tankControls: false });
  };

  render() {
    const { status, robotId, tankControls } = this.state;

    return (
      <div style={mainContainer}>
        <div style={menuStyle}>
          {robots.map(id => (
            <SimpleButton
              onClick={() => this.onRobotSelection(id)}
              key={id}
              isOn={id === robotId}
              text={`Robot ${id}`}
            />
          ))}
          <SimpleButton
            onClick={this.onTankControlPress}
            isOn={tankControls}
            text="Tank"
          />
          <SimpleButton
            onClick={this.onJoystickControlPress}
            isOn={!tankControls}
            text="Joystick"
          />
        </div>
        <div style={joystickContainer}>
          {status === "connected" ? (
            tankControls ? (
              <TankContorl listener={this.tankListener} />
            ) : (
              <JoyStick listener={this.joystickListener} />
            )
          ) : (
            <div style={statusContainer}>
              <div style={statusText}>{status}</div>
            </div>
          )}
        </div>
      </div>
    );
  }
}

const mainContainer = {
  display: "flex",
  flexDirection: "column",
  position: "relative",
  width: "100%",
  height: "100vh",
  boxSizing: "border-box",
  padding: "0.5em"
};

const statusText = {
  flex: 1,
  fontSize: 12,
  textAlign: "center",
  margin: "auto"
};

const statusContainer = {
  flex: 1,
  display: "flex",
  marginLeft: "1em",
  marginRight: "1em"
};

const joystickContainer = {
  flex: 1,
  display: "flex",
  flexDirection: "column",
  position: "relative"
};

const menuStyle = {
  flex: 0,
  display: "flex",
  flexWrap: "wrap",
  margin: "0.5em",
  background: "#fff"
};

export default App;
