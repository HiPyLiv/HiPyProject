import Container from "react-bootstrap/Container"
import Tabs from "react-bootstrap/Tabs"
import Tab from "react-bootstrap/Tab"

import Resources from "../Resources/Resources"

import resource_data from "../resource_data"

function ResourceList() {

    return (
        <Container>
            <Tabs defaultActiveKey="Python">
                <Tab eventKey="Python" title="Python">
                    <br/>
                    <Resources data={resource_data.python}/>
                </Tab>
                <Tab eventKey="R" title="R" disabled>
                    <br/>
                    {/* <Resources data={resource_data.R}/> */}
                </Tab>
                <Tab eventKey="JavaScript" title="JavaScript" disabled>
                    <br/>
                    {/* <Resources data={resource_data.Javascript}/> */}
                </Tab>
            </Tabs>
        </Container>
    )
}

export default ResourceList
