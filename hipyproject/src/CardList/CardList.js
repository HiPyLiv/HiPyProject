import Card from "react-bootstrap/Card"
import Container from "react-bootstrap/Container"
import Row from "react-bootstrap/Row"
import Col from "react-bootstrap/Col"
import Button from "react-bootstrap/Button"

import "./CardList.css"

function CardList({ data }){

    console.log(data)
    return (
        <Container>
            <Row>
                {Object.keys(data).map((keyName, i) => (
                    
                    <Col md={6} lg={4}>
                        <Card key={i} className="resource-card">
                            <Card.Body>
                                <Card.Title>{data[keyName].title}</Card.Title>
                                <Card.Text>{data[keyName].description}</Card.Text>
                            </Card.Body>
                            <Card.Body className="resource-button">
                                <Card.Link href={data[keyName].link}><Button>Get Started</Button></Card.Link>
                            </Card.Body>
                        </Card>
                    </Col>
                    
                ))}
            </Row>
        </Container>
    )
}


export default CardList
