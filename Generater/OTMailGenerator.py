import win32com.client as win32

def generateLeaveMail(formDict):
    # Create outlook application object
    outlook = win32.Dispatch('Outlook.Application')

    # Create mail iteam object
    mail = outlook.CreateItem(0)

    # Add recipient
    to_recipient = mail.Recipients.Add("Mark@qq.com")
    to_recipient.Type = 1

    # Add carbon copy
    cc_recipient = mail.Recipients.Add("Cindy@qq.com;Mary@qq.com")
    cc_recipient.Type = 2

    # Set subject
    mail.Subject = 'OT Application - ' + formDict['Name'] + ' from ' + formDict['Start Date'] + ' to ' + formDict['End Date']
    # mail.body = '''
    # Hi Mark,
    #
    # Would you please kindly review and approve my extended service requests below? Please let me know if any concern. Thanks!'''

    mail.HTMLBody = """
<style type="text/css">
table.tftable {font-size:12px;color:#333333;width:100%;border-width: 1px;border-color: #729ea5;border-collapse: collapse;}
table.tftable th {font-size:12px;background-color:#acc8cc;border-width: 1px;padding: 8px;border-style: solid;border-color: #729ea5;text-align:left;}
table.tftable tr {background-color:#ffffff;}
table.tftable td {font-size:12px;border-width: 1px;padding: 8px;border-style: solid;border-color: #729ea5;}
</style>

    <p>Hi Mark,</p>
    <p>Would you please kindly review and approve my extended service requests below? Please let me know if any concern. Thanks!</p>


<table id="tfhover" class="tftable" border="1">
<tr><th>Header 1</th><th>Header 2</th><th>Header 3</th><th>Header 4</th><th>Header 5</th><th>Header 6</th><th>Header 7</th></tr>
<tr><td>Row:1 Cell:1</td><td>Row:1 Cell:2</td><td>Row:1 Cell:3</td><td>Row:1 Cell:4</td><td>Row:1 Cell:5</td><td>Row:1 Cell:6</td><td>Row:1 Cell:7</td></tr>
</table>
"""

    mail.save()

    mail.Display()