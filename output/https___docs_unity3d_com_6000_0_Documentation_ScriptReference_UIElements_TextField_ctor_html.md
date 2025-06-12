* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextField-ctor.html

# TextField Constructor
Leave feedback
Suggest a change
## Success!
Thank you for helping us improve the quality of Unity Documentation. Although we cannot accept all submissions, we do read each suggested change from our users and will make updates where applicable.
Close
## Submission failed
For some reason your suggested change could not be submitted. Please <a>try again</a> in a few minutes. And thank you for taking the time to help us improve the quality of Unity Documentation.
Close
Your name Your email Suggestion* Submit suggestion
Cancel
## Declaration
public TextField(); 
### Description
Creates a new textfield. 
* * *
## Declaration
public TextField(int maxLength, bool multiline, bool isPasswordField, char maskChar); 
### Parameters
Parameter | Description  
---|---  
maxLength | The maximum number of characters this textfield can hold. If -1, there is no limit.  
multiline | Set this to true to allow multiple lines in the textfield and false if otherwise.  
isPasswordField | Set this to true to mask the characters and false if otherwise.  
maskChar | The character used for masking in a password field.  
### Description
Creates a new textfield. 
* * *
## Declaration
public TextField(string label); 
### Description
Creates a new textfield. 
* * *
## Declaration
public TextField(string label, int maxLength, bool multiline, bool isPasswordField, char maskChar); 
### Parameters
Parameter | Description  
---|---  
maxLength | The maximum number of characters this textfield can hold. If 0, there is no limit.  
multiline | Set this to true to allow multiple lines in the textfield and false if otherwise.  
isPassword | Set this to true to mask the characters and false if otherwise.  
maskChar | The character used for masking in a password field.  
### Description
Creates a new textfield. 
* * *
