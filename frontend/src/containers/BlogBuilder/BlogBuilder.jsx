import React, {useState} from 'react';
import {Row, Select} from 'antd';
import ArticlesList from '../../components/Articles/ArticlesList/ArticlesList';
import CreateArticle from './../../components/Articles/CreateArticle/CreateArticle';
import ShowArticle from './../../components/Articles/ShowArticle/ShowArticle';
import Artiles from './../../Service/data/ArticleData';


const {Option} = Select;

const BlogBuilder = () =>
{
  const [ArticleIndex, setArticleIndex] = useState(Artiles);
  const [Category, setCategory] = useState({
    used : false ,
    category : null,

  });
    

  // Index
  const ArticlesShow = (
      <>
          <Row>
          <Select placeholder="Sort Order" style={{ width: 200 }}>
            <Option value="Most popular">Most popular</Option>
            <Option value="Less popular">Less popular</Option>
            <Option value="New">New</Option>
            <Option value="Old">Old</Option>
          </Select>

          <Select placeholder="Categories" name="category" style={{ width: 200 }} onChange={(e) => SelectCategory(e)}>
            <Option value="House">House</Option>
            <Option value="Teck">Teck</Option>
            <Option value="Hobbies">Hobbies</Option>
          </Select>
        </Row>

        <ArticlesList
          data={ArticleIndex}
          category={Category} 
        />
      </>
  );

  //Index Function
  const SelectCategory = (cat) =>
  {
    console.log (cat);
    setCategory({used : true , category : cat});
  }

  // Create Article Functions
  const CreateArticleHandler = (data) =>
  {
    // setArticleIndex()
    const oldstate = [...ArticleIndex];
    oldstate.push(data);
    setArticleIndex(oldstate);
    console.log(ArticleIndex);
    
  }

  // Create Aritilce [Post ]
  const CreateARticle = ( <CreateArticle save = {CreateArticleHandler}/>);

  // Show Article
  const showarticle = ( 
      <ShowArticle
        data={ArticleIndex[0]}
       />
  );

  // Return
    return(
        <>
        {showarticle}
        </>
    );
}

export default BlogBuilder;