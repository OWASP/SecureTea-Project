import React from "react";

export default function SideNavbar(){
    return(
        <div class="sidenavbar">
            <nav id="sidebarMenu" class="collapse d-lg-block sidebar collapse bg-white">
              <div class="position-sticky">
                <div class="list-group list-group-flush mx-3 mt-4">
                  <a href="#test" class="list-group-item list-group-item-action py-2 ripple" aria-current="true">
                    <span>Main dashboard</span>
                  </a>
                  <a href="#test" class="list-group-item list-group-item-action py-2 ripple">
                    <span>Storage</span></a>
                  <a href="#test" class="list-group-item list-group-item-action py-2 ripple">
                    <span>Processes</span></a>
                  <a href="#test" class="list-group-item list-group-item-action py-2 ripple">
                    <span>Last Login</span></a>
                  <a href="#test" class="list-group-item list-group-item-action py-2 ripple">
                    <span>Network</span></a>
                  <a href="#test" class="list-group-item list-group-item-action py-2 ripple">
                    <span>Secrity</span></a>
                  <a href="#test" class="list-group-item list-group-item-action py-2 ripple">
                    <span>Logout</span></a>
                </div>
              </div>
            </nav>
        </div>
    )
}
