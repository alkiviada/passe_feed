import React from "react";
import { render } from "react-dom";
import {Provider} from "react-redux";

import Feed from "./Feed";

import store from "./store";

class App extends React.Component {
  render() {
    return <Provider store={store}><Feed /></Provider>
  }
}

render(<App />, document.getElementById("app"));

