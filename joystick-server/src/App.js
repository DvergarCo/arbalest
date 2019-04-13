import React, { Component } from "react";
import nipplejs from "nipplejs";

const joyOptions = {
  mode: "semi",
  catchDistance: 150,
  color: "#fff"
};

class App extends Component {
  constructor(props) {
    super(props);
    this.nippleRef = React.createRef();
  }

  componentDidMount() {
    this.manager = nipplejs.create({
      ...joyOptions,
      zone: this.nippleRef.current
    });
    this.listener(this.manager);
  }

  listener = manager => {
    manager.on("move", (e, stick) => {
      console.log("Moved", e, stick);
    });
    manager.on("end", () => {
      console.log("I ended!");
    });
  };

  render() {
    const containerStyle = {
      position: "relative",
      width: "100%",
      height: `${window.innerHeight}px`,
      background: "#000"
    };

    return (
      <div>
        <div ref={this.nippleRef} style={containerStyle} />
      </div>
    );
  }
}

export default App;
