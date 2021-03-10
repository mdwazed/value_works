import './App.css';
import {ChartWrapper} from './ChartWrapper';
import {SummaryWrapper} from './SummaryWrapper';

function App() {
  return (
    
    <div className="App">
      <div>
        {/* dashboard title */}
        <h1>Valueworks Dashboard</h1>
      </div>
      {/* aggregation panel  */}
      <SummaryWrapper />
      {/* marketing charts wrapper */}
      <ChartWrapper
          label="Marketing"
          resource="marketing"
          dataKeys = {[
            {key:'social_media_follower', label:'Social Media Follower (Count)' },
             {key:'website_visitors', label:'Website Visitor (Count)'},
             {key:'lead_ratio', label:'Lead Ratio (%)'},
            ]}
        />
        {/* customer charts wrapper */}
        <ChartWrapper
          label="Customer"
          resource="customer"
          dataKeys = {[
            { key:'net_promoter_score', label:'Net Promoter Score (out of 5)'}, 
            { key:'net_new_customer', label:'Net New Customer (Count)'}, 
            { key:'num_of_customer', label:'Number of Customer (Count)'} 
            ]}
        />
        {/* product development chart wrapper */}
       <ChartWrapper
          label="Product development"
          resource="product-development"
          dataKeys = {[
            { key:'dev_freq', label:'Development Frequency'}, 
            { key:'test_accuracy', label:'Test Accuracy (%)'}, 
            { key:'test_coverage', label:'Test Coverage (%)'}, 
          ]}
        />
        {/* product operation chart wrapper */}
         <ChartWrapper
          label="Product Operartion"
          resource="product-operation"
          dataKeys = {[
            { key:'sp_avg_reaction_time', label:'Avg Reaction Time in Sec (Support)'}, 
            { key:'sp_avg_resolution_time', label:'Avg Reaction Time in Sec (Resolution)'}, 
            { key:'customer_escalation', label:'Customer Escalation (Count)'}, 
            { key:'availability', label:'Availability (%)'}, 
            { key:'open_support_ticket', label:'open Support Ticket (Count)'}, 
          ]}
        />
        {/* hr chart wrapper */}
        <ChartWrapper
          label="HR"
          resource="hr"
          dataKeys = {[
            { key:'num_of_employee', label:'Number of Employee'}, 
            { key:'num_of_open_position', label:'Number of Open Position'}, 
            { key:'time_to_hire', label:'Time to Hire (Days)'}, 
            { key:'attrition', label:'Attrition (%)'}, 
          ]}
        />
        {/* profit loss chart wrapper */}
        <ChartWrapper
          label="Profit Loss"
          resource="profit-loss"
          dataKeys = {[
            { key:'software_revenue', label:'Software Revenue (€)'}, 
            { key:'other_revenue', label:'Other Revenue (€)'}, 
            { key:'professional_service_revenue', label:'Professional Service Revenue (€)'}, 
          ]}
        />
    </div>
  );
}

export default App;
