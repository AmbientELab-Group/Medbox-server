import React, { lazy, Suspense } from "react";
import {
  	Switch,
	Route,
	BrowserRouter as Router,
	Redirect
} from "react-router-dom";
import { useAuth } from "./contexts/AuthContext";
import HomeView from "./views/HomeView";
import SignInView from "./views/SignInView";
import SignUpView from	"./views/SignUpView";
const DashboardView = lazy(() => import("./views/DashboardView"));


const App = props => {
	const [ ,, isAuthenticated ] = useAuth();

	return (
		<Router>
			<Suspense fallback={<div>Lazy loading...</div>}>
				<Switch>
					<Route path="/" exact>
						<HomeView/>
					</Route>
					<Route path="/dashboard" render={() => (
						isAuthenticated() ? 
						<DashboardView/>
							:
						<Redirect to="/signin"/>
					)}/>
					<Route path="/signin" component={SignInView}/>
					<Route path="/signup" component={SignUpView}/>
					<Route path="*">
						<Redirect to="/"/>
					</Route>
				</Switch>
			</Suspense>
		</Router>
	);
}

export default App;
