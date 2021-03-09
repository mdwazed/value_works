import './ChartWrapper.css';
import Summary from './Summary';

export const SummaryWrapper = () => {
    
    return (
        <div>
            
            <div className="summaryWrapper">
                <Summary 
                    name='Marketing'
                    resource='marketing/aggregate'
                    dataKeys = {[{ key:'total_followers', value: 'Total Followers'},
                                { key:'total_visitors', value: 'Total Visitors'}]}
                />
                <Summary 
                    name='Customer'
                    resource='customer/aggregate'
                    dataKeys = {[{ key:'total_new_customer', value: 'Total New Customer'},
                                { key:'total_customer', value: 'Total Customer'}]}
                />
                <Summary 
                    name='Product Development'
                    resource='product-development/aggregate'
                    dataKeys = {[{ key:'avg_test_accuracy', value: 'Avg Test Accuracy', unit:'%'},
                                { key:'avg_test_coverage', value: 'Avg Test Coverage', unit:'%'}]}
                />
                <Summary 
                    name='Profit Loss'
                    resource='profit-loss/aggregate'
                    dataKeys = {[
                        { key:'avg_software_rev', value: 'Avg Software Revenue', unit:'€'},
                        { key:'avg_other_rev', value: 'Avg Other Revenue', unit:'€'},
                        { key:'avg_svc_rev', value: 'Avg Service Revenue', unit:'€'},
                    ]}
                />
                
            </div>
        </div>
    );
}