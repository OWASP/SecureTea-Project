import React from "react";

export default function SideNavbar(){
    return(
        <div class="sidenavbar">
            <nav id="sidebarMenu" class="collapse d-lg-block sidebar collapse bg-white">
              <div class="position-sticky">
                <div class="list-group list-group-flush mx-3 mt-4">
                  <a href="#test" class="list-group-item list-group-item-action py-2 ripple" aria-current="true">
                    <i class="fas fa-tachometer-alt fa-fw me-3"></i><span>Main dashboard</span>
                  </a>
                  <a href="#test" class="list-group-item list-group-item-action py-2 ripple active">
                    <i class="fas fa-chart-area fa-fw me-3"></i><span>Webiste traffic</span>
                  </a>
                  <a href="#test" class="list-group-item list-group-item-action py-2 ripple"><i
                      class="fas fa-lock fa-fw me-3"></i><span>Password</span></a>
                  <a href="#test" class="list-group-item list-group-item-action py-2 ripple"><i
                      class="fas fa-chart-line fa-fw me-3"></i><span>Analytics</span></a>
                  <a href="#test" class="list-group-item list-group-item-action py-2 ripple">
                    <i class="fas fa-chart-pie fa-fw me-3"></i><span>SEO</span>
                  </a>
                  <a href="#test" class="list-group-item list-group-item-action py-2 ripple"><i
                      class="fas fa-chart-bar fa-fw me-3"></i><span>Orders</span></a>
                  <a href="#test" class="list-group-item list-group-item-action py-2 ripple"><i
                      class="fas fa-globe fa-fw me-3"></i><span>International</span></a>
                  <a href="#test" class="list-group-item list-group-item-action py-2 ripple"><i
                      class="fas fa-building fa-fw me-3"></i><span>Partners</span></a>
                  <a href="#test" class="list-group-item list-group-item-action py-2 ripple"><i
                      class="fas fa-calendar fa-fw me-3"></i><span>Calendar</span></a>
                  <a href="#test" class="list-group-item list-group-item-action py-2 ripple"><i
                      class="fas fa-users fa-fw me-3"></i><span>Users</span></a>
                  <a href="#test" class="list-group-item list-group-item-action py-2 ripple"><i
                      class="fas fa-money-bill fa-fw me-3"></i><span>Sales</span></a>
                </div>
              </div>
            </nav>
        </div>
    )
}
