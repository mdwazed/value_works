import { fetchWrapper } from './fetch-wrapper';
import { useState, useEffect } from 'react';
import './ChartWrapper.css';


function Summary(props) {
    
    const [data, setData] = useState({});

    useEffect(() => {
        fetchWrapper.get(props.resource)
            .then(resp => {
                setData(resp);
            })
    },[]);

    return (
        <div className="summary">
            <h4 className="title">{props.name}</h4>
            {
                props.dataKeys.map(item => {
                    return (
                        <div key={item.value}>
                            <p><strong>{item.value}:</strong> {data[item.key]} {item.unit}</p>
                        </div>
                    )
                })
            }
        </div>
    );
  }
export default Summary