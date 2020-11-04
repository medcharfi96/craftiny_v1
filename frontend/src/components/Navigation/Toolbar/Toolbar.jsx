import React from 'react';
import {Menu, Input} from 'antd';


const ToolBar = (props) => {
    return (
        <Menu>
            <Menu theme="dark" mode="horizontal" defaultSelectedKeys={['2']}>
                <Menu.Item key="1">Logo</Menu.Item>
                <Menu.Item key="2">
                    <Input.Search/>
                </Menu.Item>
                <Menu.Item key="3">Shop</Menu.Item>
                <Menu.Item key="4">acount</Menu.Item>
            </Menu>
        </Menu>
        
    );
}


export default ToolBar;