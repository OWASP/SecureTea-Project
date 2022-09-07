import React, { component } from "react";
import Dashboard from "views/Dashboard.js";
import Network from "views/Network.js";
import Security from "views/Security.js";
import Signin from "views/Signin.js";
import Process from "views/Process"
import Lastlogin from "views/Lastlogin";


const dashboardRoutes = [
  {
    path: "/dashboard",
    name: "Dashboard",
    icon: "nc-icon nc-layers-3",
    component: Dashboard,
    layout: "/admin"
  },
  {
    path: "/process",
    name: "Process Table",
    icon: "nc-icon nc-chart-bar-32",
    component: Process,
    layout: "/admin"
  },
  {
    path: "/last-login",
    name: "Last Login",
    icon: "nc-icon nc-badge",
    component: Lastlogin,
    layout: "/admin"
  },
  {
    path: "/network",
    name: "Network",
    icon: "nc-icon nc-vector",
    component: Network,
    layout: "/admin"
  },
  {
    path: "/security",
    name: "Security",
    icon: "nc-icon nc-lock-circle-open",
    component: Security,
    layout: "/admin"
  },
  {
    path: "/signin",
    name: "Sign in",
    icon: "nc-icon nc-circle-09",
    component: Signin,
    layout: "/admin"
  },
 

];

export default dashboardRoutes;