import './ChartWrapper.css';
import { fetchWrapper } from './fetch-wrapper';
import { useState, useEffect } from 'react';
import { Chart } from './Chart'

export const ChartWrapper = ({ resource, label, dataKeys = [] }) => {

    const [data, setData] = useState([]);

    useEffect(() => {
        fetchWrapper.get(resource)
            .then(resp => {
                setData(resp);
            })
    },[]);

    return (
        <div>
            <div className="chartWrapperLabel">{label}</div>
            <div className="chartWrapper">
                {
                    dataKeys.map(key=>(
                        <Chart key={key.key}
                            data={ data.map(item=>{
                                return {
                                    month: item.month,
                                    [key.label]: item[key.key]
                                }
                            })}
                            barDataKey={key.label}
                        />
                    ))
                }
            </div>
        </div>
    );
}