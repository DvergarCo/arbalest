import React, { Component } from "react";
import nipplejs from "nipplejs";

class JoyStick extends Component {
  constructor(props) {
    super(props);
    this.nippleRef = React.createRef();
  }

  componentDidMount() {
    this.manager = nipplejs.create({
      mode: "dynamic",
      maxNumberOfNipples: 1,
      color: "#fff",
      zone: this.nippleRef.current
    });
    this.props.listener(this.manager);
  }

  render() {
    return <div ref={this.nippleRef} style={joyStyle} />;
  }
}

const joyStyle = {
  flex: 1,
  background: "#000",
  borderRadius: "12px"
};

export default JoyStick;
