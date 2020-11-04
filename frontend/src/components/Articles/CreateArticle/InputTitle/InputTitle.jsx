import React from 'react'
import {Row, Col} from 'antd';
import './InputTitle.css'

const InputTitle = (props) =>
{
    return (
        <Row>
            <Col style={{margin : 'auto'}}>
                <input placeholder="Article title here" name="title" className="TitleInput" onChange={(e)=>props.getTitle(e.target.value)}/>
            </Col>
        </Row>
    );

}

export default InputTitle ;