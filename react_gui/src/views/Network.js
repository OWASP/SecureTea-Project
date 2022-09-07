import React from "react";

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
} from "react-bootstrap";

import Cookies from 'universal-cookie';

const cookies = new Cookies();

class Network extends React.Component {

    // Constructor 
    constructor(props) {
      super(props);
  
      this.state = {
          network_devices: [],
          DataisLoaded: false
      };
    }
   
    // ComponentDidMount is used to
    // execute the code 
    componentDidMount() {

      const cookie_val = cookies.get('cookie');
      console.log(cookie_val);

      const requestOptions = {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          "cookie": cookie_val
        })
      };

      fetch(
        "http://127.0.0.1:8000/netio/", requestOptions
        )
          .then((res) => res.json())
          .then((json) => {
              this.setState({
                network_devices: json,
                DataisLoaded: true
              });
              console.log("Workingg");
              console.log(json);
              console.log("Workingg");
          })
    }




  render () {

    const { network_devices } = this.state;

      return (
      <>
        <Container fluid>
          <Row>
            <Col md="12" className="page-data">
              <Card className="strpied-tabled-with-hover table-main">
                <Card.Header className="box-header">
                  <Card.Title as="h4" className="text-white text-bold pb-3 pt-1">Network Table</Card.Title>
                </Card.Header>
                <Card.Body className="table-full-width table-responsive px-0 ">
                  <Table className="table-hover table-striped table-scroll">
                    <thead>
                      <tr>
                        <th className="border-0">Wifi Device</th>
                        <th className="border-0">Send</th>
                        <th className="border-0">Recieve</th>
                        <th className="border-0">Isup</th>
                        <th className="border-0">ipv4</th>
                        <th className="border-0">ipv6</th>
                      </tr>
                    </thead>
                    <tbody>
                      {
                        network_devices.map((network_device) => ( 
                          
                          <tr key = { network_device.name } >
                            <td>{ network_device.name }</td>
                            <td>{ network_device.sent }</td>
                            <td>{ network_device.receive}</td>
                            <td>{ network_device.isup }</td>
                            <td>{ network_device.ipv4}</td>
                            <td>{ network_device.ipv6 }</td>
                          </tr>
                        ))
                      }
                    </tbody>
                  </Table>
                </Card.Body>
              </Card>
            </Col>
          </Row>
      </Container>
    </>
    );
  }
}

export default Network;
