import React from 'react';
import  {Tag, Typography,Row, Col, Badge}  from 'antd';
import { HeartOutlined, CommentOutlined } from '@ant-design/icons';
import './ShowArticle.css';
import CommentSection from './CommentSection/CommentSection';

const {Title} = Typography
const ShowArticle = (props) =>{
    return (
        <>
            <div className="ImageShow" style={{backgroundImage: `url(${props.data.articlePicUrl})`}}>
                <Row className='LikeCmntBox' justify='end'>
                    <div lg={24} >
                        <div className=' heartComment' span={12} style={{color :'deeppink'}}>
                                
                            <Badge size="small" count={props.data.hearts}>
                                <a><HeartOutlined   style={{color :'deeppink', fontSize: '2rem' }} />  </a>
                            </Badge>
                            
                        </div>
                    </div>
                </Row>
            </div>
                <Title className="Title">{props.data.title}</Title>
            <div dangerouslySetInnerHTML={{__html: props.data.content}} className="content" >
            </div>
            


            {props.data.tag.map((key) =>( <Tag key={key} color={key}>{key}</Tag> ))}


            <CommentSection/>
            
        


        </>
    );
}

export default ShowArticle;