import React, {useState} from 'react';
import { Comment, Avatar, Form, Button, List, Input } from 'antd';
import moment from 'moment';
import './CommentSection.css';

const { TextArea } = Input;

const CommentList = ({ comments }) => (
  <List
   className='CommentBox'
    dataSource={comments}
    header={`${comments.length} ${comments.length > 1 ? 'replies' : 'reply'}`}
    itemLayout="horizontal"
    renderItem={props => <Comment {...props} />}
  />
);

const Editor = ({ onChange, onSubmit, submitting, value }) => (
  <>
    <Form.Item>
      <TextArea rows={4} onChange={onChange} value={value} />
    </Form.Item>
    <Form.Item>
      <Button htmlType="submit" loading={submitting} onClick={onSubmit} type="primary">
        Add Comment
      </Button>
    </Form.Item>
  </>
);

const CommentSection = (props) => {

    const [Comments, setComments] = useState([]);
    const [Value, setValue] = useState ('');
    const [Submitting, setSubmitting] = useState(false);

    const handleSubmit = () => {
      if (!Value) {
        return;
      }

      setSubmitting(true);

      setTimeout(() => {
          setSubmitting(false);
          setValue('');
          setComments([
              {
                author: 'Han Solo',
                avatar: 'https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png',
                content: <p>{Value}</p>,
                datetime: moment().fromNow(),
              },
              ...Comments,
            ]);
      }, 1000);
    };

    const handleChange = e => {
        setValue(e.target.value);
    };

    const comments = Comments;
    const submitting = Submitting;
    const value = Value;

    return (
      <>
        {comments.length > 0 && <CommentList comments={comments} />}
        <Comment 
            className='CommentBox'
          avatar={
            <Avatar
              src="https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png"
              alt="Han Solo"
            />
          }
          content={
            <Editor
              onChange={handleChange}
              onSubmit={handleSubmit}
              submitting={submitting}
              value={value}
            />
          }
        />
      </>
    );
  
}
export default CommentSection;