import React from 'react';
import {Button,message, Select,Tag, Row, Col} from 'antd';
import CKEditor from '@ckeditor/ckeditor5-react';
import ClassicEditor from '@ckeditor/ckeditor5-build-classic';
import './CreateArticle.css';
import CoverPhotoUploader from './CoverPhotoUploader/CoverPhotoUploader';
import InputTitle from './InputTitle/InputTitle';


const options = [{ value: 'gold' }, { value: 'lime' }, { value: 'green' }, { value: 'cyan' }];

const ARTICLE = {
        id : 43,
        articlePicUrl : null,
        title : null,
        hearts  : null,
        comments : null,
        authorName : null,
        date : null,
        authorAvatar:   null ,
        category : null,
        tag : null,
        content: null,
};

function tagRender(props) {
  const { label, value, closable, onClose } = props;

  return (
    <Tag color={value} closable={closable} onClose={onClose} style={{ marginRight: 3 }}>
      {label}
    </Tag>
  );
}


const getTags = (tag) =>
{
    ARTICLE.Tag = tag;
}


const getTitle = (title)=>
{
    ARTICLE.title = title;


}
const getCategory = (cat) =>{
    ARTICLE.category= cat;
}
const getImage = (img) =>
{
   ARTICLE.articlePicUrl = img;
}

const {Option} = Select;
const CreateArticle = (props) => {
    const success = () => {
        props.save(ARTICLE);
        message.success('Your article was saved succeflys!!');
      };
    
    return(
        <>

            <CoverPhotoUploader getImage={getImage}/>
            <InputTitle
                getTitle={getTitle}
            /> 
            {/* <Button type="primary">Save</Button> */}

            <CKEditor
                    editor={ ClassicEditor }
                    data=""
                    onInit={ editor => {
                        // You can store the "editor" and use when it is needed.
                        console.log( '', editor );
                    } }
                    onChange={ ( event, editor ) => {
                        const data = editor.getData();
                        ARTICLE.content = data;
                        // console.log(ARTICLE);
                    } }
                    onBlur={ ( event, editor ) => {
                       
                    } }
                    onFocus={ ( event, editor ) => {
                      
                    } }
            />
            <Row className='Selects' justify="center">

                <Col lg={10}>
                    <Select
                        className='TagSelect'
                        width={10}
                        mode="multiple"
                        showArrow
                        tagRender={tagRender}
                        style={{ width: '100%' }}
                        options={options}
                        placeholder='Select your Tags'
                        onChange = {(e) => getTags(e)}
                    />
                </Col>
                <Col lg={8}>
                    <Select  placeholder="Categories" name="category" style={{ width: 200 }} onChange={(e)=>getCategory(e)}>
                        <Option value="House">House</Option>
                        <Option value="Teck">Teck</Option>
                        <Option value="Hobbies">Hobbies</Option>
                    </Select>
                </Col>
            </Row>

            <Button className="SaveBtn" type="primary" onClick={success}>
            Save
            </Button>
        </>
    );
}

 export default CreateArticle;