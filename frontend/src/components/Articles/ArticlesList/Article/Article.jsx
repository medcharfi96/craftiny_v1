import React from 'react';
import {Card, Row, Col, Avatar} from 'antd';
import { HeartOutlined, CommentOutlined } from '@ant-design/icons';
import './Article.css';

const { Meta } = Card;

const Article = (props) => {
    return (
        <Card
        hoverable
        style={{ width: 240 }}
        cover={<img alt="example" shape="circle" src={props.data.articlePicUrl} />}
        >
        <Meta style={{textAlign : 'left'}} title={props.data.title} description={props.data.description} />
        <Row  className="container " >
            <Col className=' heartComment' span={12} style={{color :'deeppink'}}>
                <HeartOutlined  /> {props.data.hearts}
            </Col>
            <Col className='heartComment' style={{color : 'steelblue'}} span={12}>
                <CommentOutlined /> {props.data.comments}
            </Col>
        </Row>

        <Row className="Infos" >
            <Col  className='gutter-row NameDate' span={4}>
                <Avatar  size="large" src={props.data.authorAvatar}/>
            </Col>
            <Col className='gutter-row NameDate container' span={20}>
                    <p> 
                        {props.data.authorName}
                            <br/>
                        {props.data.date}
                    </p>
            </Col>
        </Row>
      </Card>
    );

}

export default Article;