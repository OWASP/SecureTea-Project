import React, {useEffect, useState} from "react";
import ram_icon from "../assets/img/icons/ram.png"
import cpu_icon from "../assets/img/icons/cpu.png"
import swap_icon from "../assets/img/icons/swap-horizontal-orientation-arrows.png"
import cpu_icon_2 from "../assets/img/icons/cpu-tower.png"
import hdd_icon from "../assets/img/icons/harddisk.png"
import uptime_icon from "../assets/img/icons/time-left.png"

// react-bootstrap components
import {
  Badge,
  Button,
  Card,
  Navbar,
  Nav,
  Table,
  Container,
  Row,
  Col,
  Form,
  OverlayTrigger,
  Tooltip,
} from "react-bootstrap";

import Cookies from 'universal-cookie';

const cookies = new Cookies();

class Dashboard extends React.Component {


  // Constructor 
    constructor(props) {
        super(props);
   
        this.state = {
            cpu: [],
            ram: [],
            swap: [],
            device: [],
            diskio: [],
            uptime: [],
            processor: [],
            DataisLoaded: false
        };
    }
   
    // ComponentDidMount is used to
    // execute the code 
    componentDidMount() {

      const cookie_val = cookies.get('cookie');
      const server_url = cookies.get('url');
      console.log(cookie_val);

      const requestOptions = {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          "cookie": cookie_val
        })
      };

      fetch(
        server_url + "cpu/", requestOptions)
          .then((res) => res.json())
          .then((json) => {
              this.setState({
                  cpu: json,
                  DataisLoaded: true
              });
          })

      fetch(
        server_url + "ram/", requestOptions)
          .then((res) => res.json())
          .then((json) => {
              this.setState({
                  ram: json,
                  DataisLoaded: true
              });
          })

      fetch(
        server_url + "swap/", requestOptions)
          .then((res) => res.json())
          .then((json) => {
              this.setState({
                  swap: json,
                  DataisLoaded: true
              });
          })

      fetch(
        server_url + "uptime/", requestOptions)
          .then((res) => res.json())
          .then((json) => {
              this.setState({
                  uptime: json,
                  DataisLoaded: true
              });
          })

      fetch(
        server_url + "diskio/", requestOptions)
          .then((res) => res.json())
          .then((json) => {
              this.setState({
                  diskio: json,
                  DataisLoaded: true
              });
          })
      
      fetch(
        server_url + "uptime/", requestOptions)
          .then((res) => res.json())
          .then((json) => {
              this.setState({
                  uptime: json,
                  DataisLoaded: true
              });
          })

      fetch(
        server_url + "processor/", requestOptions)
          .then((res) => res.json())
          .then((json) => {
              this.setState({
                  processor: json,
                  DataisLoaded: true
              });
          })

    }

  render() {
    const { cpu, ram, swap, device, diskio, uptime, processor } = this.state;

    return (
      <>
        <Container fluid>
          <Row className="page-data">
          {/* RAM */}
          <Col lg="4" md="6" sm="6" >
              <Card className="card-stats css-card ">
                <Card.Body>
                  <Row>
                    <Col xs="5" >
                      <div className="icon-big text-center icon-warning card-icon-blue">
                      <img className="mb-4" src={ram_icon} alt="Cpu Tower" />
                      </div>
                    </Col>
                    <Col xs="7">
                      <div className="numbers">
                        <p className="card-category">RAM</p>
                        <Card.Title as="h4">{ram["percent"]} %</Card.Title>
                      </div>
                    </Col>
                  </Row>
                </Card.Body>
                <Card.Footer>
                  <hr></hr>
                  <div className="stats d-flex card-stats justify-content-between pt-1">
                    <p className="p-0 mb-0">Total</p>
                    <p className="p-0 mb-0">{ram["total"]}</p>
                  </div>
                  <div className="stats d-flex card-stats justify-content-between">
                    <p className="p-0 mb-0">Percent</p>
                    <p className="p-0 mb-0">{ram["percent"]} %</p>
                  </div>
                  <div className="stats d-flex card-stats justify-content-between">
                    <p className="p-0 mb-0">Used</p>
                    <p className="p-0 mb-0">{ram["used"]}</p>
                  </div>
                  <div className="stats d-flex card-stats justify-content-between">
                    <p className="p-0 mb-0">Free</p>
                    <p className="p-0 mb-0">{ram["free"]}</p>
                  </div>
                </Card.Footer>
              </Card>
            </Col>
          {/* SWAP */}
          <Col lg="4" md="6" sm="6">
              <Card className="card-stats css-card">
                <Card.Body>
                  <Row>
                    <Col xs="5">
                      <div className="icon-big text-center icon-warning card-icon-blue">
                      <img className="mb-4" src={swap_icon} alt="Swap Icon" />
                      </div>
                    </Col>
                    <Col xs="7">
                      <div className="numbers">
                        <p className="card-category">Swap</p>
                        <Card.Title as="h4">{swap["percent"]} %</Card.Title>
                      </div>
                    </Col>
                  </Row>
                </Card.Body>
                <Card.Footer>
                  <hr></hr>
                  <div className="stats d-flex card-stats justify-content-between pt-1">
                    <p className="p-0 mb-0">Total</p>
                    <p className="p-0 mb-0">{swap["total"]}</p>
                  </div>
                  <div className="stats d-flex card-stats justify-content-between">
                    <p className="p-0 mb-0">Percent</p>
                    <p className="p-0 mb-0">{swap["percent"]} %</p>
                  </div>
                  <div className="stats d-flex card-stats justify-content-between">
                    <p className="p-0 mb-0">Used</p>
                    <p className="p-0 mb-0">{swap["used"]} </p>
                  </div>
                  <div className="stats d-flex card-stats justify-content-between">
                    <p className="p-0 mb-0">Free</p>
                    <p className="p-0 mb-0">{swap["free"]}</p>
                  </div>
                </Card.Footer>
              </Card>
            </Col>
             {/* UPTIME */}
            <Col lg="4" md="6" sm="6">
              <Card className="card-stats css-card">
                <Card.Body>
                  <Row>
                    <Col xs="5">
                      <div className="icon-big text-center icon-warning card-icon-blue">
                      <img className="mb-4" src={uptime_icon} alt="uptime iconn" />
                      </div>
                    </Col>
                    <Col xs="7">
                      <div className="numbers">
                        <p className="card-category">UPTIME</p>
                        <Card.Title as="h4">{uptime["uptime"]}</Card.Title>
                      </div>
                    </Col>
                  </Row>
                </Card.Body>
                <Card.Footer>
                  <hr></hr>
                  <div className="stats d-flex card-stats justify-content-between pt-1">
                    <p className="p-0 mb-0">Net Up-time</p>
                    <p className="p-0 mb-0">{uptime["uptime"]}</p>
                  </div>
                </Card.Footer>
              </Card>
            </Col>
            {/* Processor */}
            <Col lg="8" md="6" sm="6">
              <Card className="card-stats css-card">
                <Card.Body>
                  <Row>
                    <Col xs="5">
                      <div className="icon-big text-center icon-warning card-icon-blue">
                      <img className="mb-4" src={cpu_icon} alt="CPU" />
                      </div>
                    </Col>
                    <Col xs="7">
                      <div className="numbers">
                        <p className="card-category">PROCESSOR</p>
                        <Card.Title as="h4">{cpu["percentage"]} %</Card.Title>
                      </div>
                    </Col>
                  </Row>
                </Card.Body>
                <Card.Footer>
                  <hr></hr>
                  <div className="stats d-flex card-stats justify-content-between pt-1">
                    <p className="p-0 mb-0">No of processors</p>
                    <p className="p-0 mb-0">{cpu["count"]}</p>
                  </div>
                  <div className="stats d-flex card-stats justify-content-between">
                    <p className="p-0 mb-0">Bits</p>
                    <p className="p-0 mb-0">{processor["bits"]}</p>
                  </div>
                  <div className="stats d-flex card-stats justify-content-between">
                    <p className="p-0 mb-0">Brand</p>
                    <p className="p-0 mb-0">{processor["brand"]}</p>
                  </div>
                  <div className="stats d-flex card-stats justify-content-between">
                    <p className="p-0 mb-0">Hz as Advertised</p>
                    <p className="p-0 mb-0">{processor["hz_advertised"]}</p>
                  </div>
                  <div className="stats d-flex card-stats justify-content-between">
                    <p className="p-0 mb-0">l3 cache size</p>
                    <p className="p-0 mb-0">{processor["l3_cache_size"]}</p>
                  </div>
                  <div className="stats d-flex card-stats justify-content-between">
                    <p className="p-0 mb-0">l2 cache size</p>
                    <p className="p-0 mb-0">{processor["l2_cache_size"]}</p>
                  </div>
                  <div className="stats d-flex card-stats justify-content-between">
                    <p className="p-0 mb-0">l1 data cache size</p>
                    <p className="p-0 mb-0">{processor["l1_data_cache_size"]} </p>
                  </div>
                  <div className="stats d-flex card-stats justify-content-between">
                    <p className="p-0 mb-0">l1 instruction cache size</p>
                    <p className="p-0 mb-0">{processor["l1_instruction_cache_size"]}</p>
                  </div>
                  <div className="stats d-flex card-stats justify-content-between">
                    <p className="p-0 mb-0">Vendor ID</p>
                    <p className="p-0 mb-0">{processor["vendor_id"]}</p>
                  </div>
                </Card.Footer>
              </Card>
            </Col>
              {/* Diskio */}
              <Col lg="4" md="6" sm="6">
              <Card className="card-stats css-card">
                <Card.Body>
                  <Row>
                    <Col xs="5">
                      <div className="icon-big text-center icon-warning card-icon-blue">
                        <img className="mb-4" src={hdd_icon} alt="Hard Disk" />
                      </div>
                    </Col>
                    <Col xs="7">
                      <div className="numbers">
                        <p className="card-category">Diskio</p>
                        <Card.Title as="h4">DISK READ WRITE</Card.Title>
                      </div>
                    </Col>
                  </Row>
                </Card.Body>
                <Card.Footer>
                  <hr></hr>
                  <div className="stats d-flex card-stats justify-content-between pt-1">
                    <p className="p-0 mb-0">Read Speed</p>
                    <p className="p-0 mb-0">{diskio["read"]}</p>
                  </div>
                  <div className="stats d-flex card-stats justify-content-between">
                    <p className="p-0 mb-0">Write Speed</p>
                    <p className="p-0 mb-0">{diskio["write"]}</p>
                  </div>
                </Card.Footer>
              </Card>
            </Col>
          </Row>
         
        </Container>
      </>
    );
  
  }
}

export default Dashboard;
