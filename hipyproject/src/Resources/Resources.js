import Container from  "react-bootstrap/Container"
import Card from "react-bootstrap/Card"
import Accordion from "react-bootstrap/Accordion"

import CardList from "../CardList/CardList"

function Resources({ data }){

    console.log(data)

    Object.keys(data).map((keyName, i) => (
        console.log(data[keyName])
    )) 
    return (
        <Container>
            <Accordion defaultActiveKey="0">
                {Object.keys(data).map((keyName, i) => (
                    <Card key={i}>
                        <Accordion.Toggle as={Card.Header} eventKey={i.toString()}>
                            {data[keyName].name}
                        </Accordion.Toggle>
                        <Accordion.Collapse eventKey={i.toString()}>
                            <CardList data={data[keyName].cards}/>
                        </Accordion.Collapse>
                    </Card>
                    ))
                }
            </Accordion>
        </Container>
    )
}

export default Resources
