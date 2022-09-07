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

class Precess extends React.Component {

      // Constructor 
      constructor(props) {
        super(props);
   
        this.state = {
            processes: [],
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
        "http://127.0.0.1:8000/process/", requestOptions
        )
          .then((res) => res.json())
          .then((json) => {
              this.setState({
                  processes: json,
                  DataisLoaded: true
              });
              console.log("Workingg");
              console.log(json);
              console.log("Workingg");
          })
    }




  render () {
    const { processes } = this.state;


    return(
      <>

      <Container fluid>
        <Row>
          <Col md="12" className="page-data">
            <Card className="strpied-tabled-with-hover table-main">
              <Card.Header className="box-header">
                <Card.Title as="h4" className="text-white text-bold pb-3 pt-1">Process Table</Card.Title>
              </Card.Header>
              <Card.Body className="table-full-width table-responsive px-0 ">
                <Table className="table-hover table-striped table-scroll">
                  <thead>
                    <tr>
                      <th className="border-0">PID</th>
                      <th className="border-0">Process Name</th>
                      <th className="border-0">CPU</th>
                      <th className="border-0">RAM</th>
                      <th className="border-0">Status</th>
                      <th className="border-0">User</th>
                      <th className="border-0">Create Time</th>
                    </tr>
                  </thead>
                  <tbody>
                    {
                      processes.map((process) => ( 
                        
                        <tr key = { process.pid } >
                            <td>{ process.pid }</td>
                            <td>{ process.name }</td>
                            <td>{ process.cpu }</td>
                            <td>{ process.memory }</td>
                            <td>{ process.status }</td>
                            <td>{ process.username }</td>
                            <td>{ process.createTime }</td>
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
    )
  }
}


export default Precess

/*
function Precess() {
  return (
    <>
      <Container fluid>
        <Row>
          <Col md="12" className="page-data">
            <Card className="strpied-tabled-with-hover table-main">
              <Card.Header className="box-header">
                <Card.Title as="h4" className="text-white text-bold pb-3 pt-1">Process Table</Card.Title>
              </Card.Header>
              <Card.Body className="table-full-width table-responsive px-0 ">
                <Table className="table-hover table-striped table-scroll">
                  <thead>
                    <tr>
                      <th className="border-0">PID</th>
                      <th className="border-0">Process Name</th>
                      <th className="border-0">CPU</th>
                      <th className="border-0">RAM</th>
                      <th className="border-0">Status</th>
                      <th className="border-0">User</th>
                      <th className="border-0">Create Time</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>1</td>
                      <td>Dakota Rice</td>
                      <td>$36,738</td>
                      <td>Niger</td>
                      <td>Oud-Turnhout</td>
                      <td>Niger</td>
                      <td>Oud-Turnhout</td>
                    </tr>
                    <tr>
                      <td>2</td>
                      <td>Minerva Hooper</td>
                      <td>$23,789</td>
                      <td>Curaçao</td>
                      <td>Sinaai-Waas</td>
                      <td>Niger</td>
                      <td>Oud-Turnhout</td>
                    </tr>
                    <tr>
                      <td>3</td>
                      <td>Sage Rodriguez</td>
                      <td>$56,142</td>
                      <td>Netherlands</td>
                      <td>Baileux</td>
                      <td>Niger</td>
                      <td>Oud-Turnhout</td>
                    </tr>
                    <tr>
                      <td>4</td>
                      <td>Philip Chaney</td>
                      <td>$38,735</td>
                      <td>Korea, South</td>
                      <td>Overland Park</td>
                      <td>Niger</td>
                      <td>Oud-Turnhout</td>
                    </tr>
                    <tr>
                      <td>5</td>
                      <td>Doris Greene</td>
                      <td>$63,542</td>
                      <td>Malawi</td>
                      <td>Feldkirchen in Kärnten</td>
                      <td>Niger</td>
                      <td>Oud-Turnhout</td>
                    </tr>
                    <tr>
                      <td>6</td>
                      <td>Mason Porter</td>
                      <td>$78,615</td>
                      <td>Chile</td>
                      <td>Gloucester</td>
                      <td>Niger</td>
                      <td>Oud-Turnhout</td>
                    </tr>
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
*/
