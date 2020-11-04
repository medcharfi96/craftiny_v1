import React from 'react';
import { Row, Col, } from 'antd';
import Lottie from 'react-lottie';
import NotFound from '../../../assets/lotties/404.json';
import Article from './Article/Article';

const ArticlesList = (props) => {
    const defaultOptions = {
        loop: true,
        autoplay: true,
        animationData: NotFound,
        rendererSettings: {
          preserveAspectRatio: "xMidYMid slice"
        }
      };
    
    const showArticles =  ()=> {
        if (Object.keys(props.data).length > 0  )
        {
            return ( 
                <>
                    {
                        props.data.map(data => {
                            if (data.category === props.category.category || !props.category.used)
                            {
                                return (<Col style={{padding : '1.5rem 0 0 0'}} sm={22}  md={12} lg={6}  >
                                    <Article data={data} />
                                </Col>)
                            }

                        })
                    }    
                </>
            ); 
        }
        else{
                return (
                    <div  style={{ margin:'auto', color: 'black'}}>
                             <Lottie 
                                options={defaultOptions}
                                height={400}
                                width={400}
                            />

                    </div>
                );
            }
    }
    return (
        <div>
        <Row>
            {showArticles()}
        </Row>
            
        </div>

    );

}

export default ArticlesList;