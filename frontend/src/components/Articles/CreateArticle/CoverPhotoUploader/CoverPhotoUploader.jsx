import React, {useState, useRef} from 'react';
import { Tooltip  } from 'antd';
import './CoverPhotoUploader.css';
import Lottie from 'react-lottie';
import uploadImg from  './../../../../assets/lotties/uploadImg.json';
// import { render } from '@testing-library/react';

const CoverPhotoUploader = (props) =>
{
    const [Image, setImage] = useState({file: '',imagePreviewUrl: '', updated : false});

    const btnupload = useRef(null);
    const defaultOptions = {
        loop: true,
        autoplay: true,
        animationData: uploadImg,
        rendererSettings: {
          preserveAspectRatio: "xMidYMid slice"
        }
    };
    

    const imageUploadHandler = e =>
    {
        console.log(e.target.files[0]);
        let render = new FileReader();
       

        e.preventDefault();
        let reader = new FileReader();
        let file = e.target.files[0];
    
        reader.onloadend = () => {
            setImage({
            file: file,
            imagePreviewUrl: reader.result,
            updated : true
          });
        }
        reader.readAsDataURL(file);
        props.getImage(Image.file);

    }
  
    const clickedImage = ()=>{
        btnupload.current.click();
        // uploadBtn.onChange() 
    }  
    const uploadBtn = (<input ref={btnupload} type='file' onChange={imageUploadHandler} style={{display : 'none'}}/>);
    return (
        <Tooltip  placement="right"  title="Select you cover" color="pink" key="pink">
             <div  className="ImageShow" style={{backgroundImage: `url(${Image.imagePreviewUrl})`}} onClick={clickedImage}>
                { !Image.updated ?
                    <Lottie options={defaultOptions} width={250}/> :null
                }
                
                {uploadBtn}
                
            </div>
        </Tooltip>

    );
}

export default CoverPhotoUploader