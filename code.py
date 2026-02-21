# Get all items from the Aggregate node
items = _items

# Start building the HTML table
html_output = """
<p>Dear sir,</p>
<p>This is a reminder regarding your outstanding balance. Please see the details below:</p>

<table border="1" style="border-collapse: collapse; width: 100%; font-family: Arial, sans-serif;">
  <thead>
    <tr style="background-color: #f2f2f2;">
      <th style="padding: 10px; text-align: left;">Delivery Status</th>
      <th style="padding: 10px; text-align: left;">PO</th>
      <th style="padding: 10px; text-align: left;">Description</th>
      <th style="padding: 10px; text-align: left;">GRN</th>
      <th style="padding: 10px; text-align: left;">BILL</th>
      <th style="padding: 10px; text-align: left;">INVOICE</th>
      <th style="padding: 10px; text-align: left;">PAYMENT</th>
    </tr>
  </thead>
  <tbody>
"""

# Loop through all items and build table rows
for item in items:
    json_data = item['json']
    
    # Get the aggregated arrays
    po_list = json_data.get('PO#', [])
    des_list = json_data.get('Description', [])
    grn_list = json_data.get('GRN', [])
    bill_list = json_data.get('BILL', [])
    invoice_list = json_data.get('Invoice', [])
    payment_list = json_data.get('Payment', [])
    
    # Create rows for each item in the arrays
    max_length = max(len(po_list), len(des_list), len(grn_list), len(bill_list), len(invoice_list), len(payment_list))
    
    for i in range(max_length):
        pos = po_list[i] if i < len(po_list) else ''
        des = des_list[i] if i < len(des_list) else ''
        grn = grn_list[i] if i < len(grn_list) else ''
        bill = bill_list[i] if i < len(bill_list) else ''
        invoice = invoice_list[i] if i < len(invoice_list) else ''
        payment = payment_list[i] if i < len(payment_list) else ''

        
        
        html_output += f"""
        
    <tr>
      <td style="padding: 10px;">Delivered</td>
      <td style="padding: 10px; color: red; font-weight: bold;">{pos}</td>
      <td style="padding: 10px; color: red; font-weight: bold;">{des}</td>
      <td style="padding: 10px; color: red; font-weight: bold;">{grn}</td>
      <td style="padding: 10px; color: red; font-weight: bold;">{bill}</td>
      <td style="padding: 10px; color: red; font-weight: bold;">{invoice}</td>
      <td style="padding: 10px; color: red; font-weight: bold;">{payment}</td>
    </tr>
"""

# Close the table and add footer
html_output += """
  </tbody>
</table>
<p>Please settle this as soon as possible. Thank you!</p>
"""

# Return the HTML as email_body
return [{'json': {'email_body': html_output}}]