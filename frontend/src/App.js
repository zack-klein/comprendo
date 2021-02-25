import "./App.css";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import { Home } from "./pages/Home";
import { Results } from "./pages/Results";
import { About } from "./pages/About";

function App() {
  return (
    <div className="App">
      <Router>
        <Switch>
          <Route path="/topic" component={Results} />
          <Route path="/about" component={About} />
          <Route path="/" component={Home} />
        </Switch>
      </Router>
    </div>
  );
}

export default App;
