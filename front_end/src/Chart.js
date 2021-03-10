import { BarChart, Bar, CartesianGrid, XAxis, YAxis, Tooltip, Legend } from 'recharts';

// rechar library barchart to display bar chart 
export const Chart = ({data, barDataKey  }) => {
           
    return(
        <BarChart width={400} height={150} data={data}>
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="month" />
        <YAxis />
        <Tooltip />
        <Legend />
        <Bar dataKey={barDataKey} fill="#8884d8" />
    </BarChart>
    )
}