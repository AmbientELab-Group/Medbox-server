import React from "react";
import {
  	Switch,
	Route,
	BrowserRouter as Router,
	Redirect
} from "react-router-dom";

import HomeView from "./views/HomeView";
import SignInView from "./views/SignInView";
import SingUpView from	"./views/SignUpView";
import DashboardView from "./views/DashboardView";


const App = props => {
	return (
		<Router>
			<Switch>
				<Route path="/" exact>
					<HomeView/>
				</Route>
				<Route path="/dashboard">
					<DashboardView/>
				</Route>
				<Route path="/signin">
					<SignInView/>
				</Route>
				<Route path="/signup">
					<SingUpView/>
				</Route>
				<Route path="*">
					<Redirect to="/"/>
				</Route>
			</Switch>
		</Router>
	);
}

export default App;
