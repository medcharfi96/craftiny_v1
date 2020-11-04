import React from 'react';
import './App.css';

import {Layout, } from 'antd';


import BlogBuilder from './containers/BlogBuilder/BlogBuilder';
import ToolBar from './components/Navigation/Toolbar/Toolbar';

const { Header, Footer, Content } = Layout;
function App() {
  return (
    <div className="App">
      <Layout>
        <Header>
          <ToolBar/>
        </Header>
        <Layout className="Content">
          <Content className='site-layout '>
            <div className="site-layout-content">
              <BlogBuilder/>
            </div>
          </Content>
          
        </Layout>
        <Footer>Footer</Footer>
      </Layout>
      
    </div>
  );
}

export default App;
