* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MaskField-ctor.html

# MaskField Constructor
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
public MaskField(List<string> choices, int defaultMask, Func<string,string> formatSelectedValueCallback, Func<string,string> formatListItemCallback); 
### Parameters
Parameter | Description  
---|---  
choices | A list of choices to populate the field.  
defaultValue | The initial mask value for this field.  
formatSelectedValueCallback | A callback to format the selected value. Unity calls this method automatically when a new value is selected in the field..  
formatListItemCallback | The initial mask value this field should use. Unity calls this method automatically when displaying choices for the field.  
### Description
Initializes and returns an instance of MaskField. 
* * *
## Declaration
public MaskField(string label, List<string> choices, int defaultMask, Func<string,string> formatSelectedValueCallback, Func<string,string> formatListItemCallback); 
### Parameters
Parameter | Description  
---|---  
label | The text to use as a label for the field.  
choices | A list of choices to populate the field.  
defaultValue | The initial mask value for this field.  
formatSelectedValueCallback | A callback to format the selected value. Unity calls this method automatically when a new value is selected in the field..  
formatListItemCallback | The initial mask value this field should use. Unity calls this method automatically when displaying choices for the field.  
### Description
Initializes and returns an instance of MaskField. 
* * *
## Declaration
public MaskField(); 
### Description
Initializes and returns an instance of MaskField. 
* * *
## Declaration
public MaskField(string label); 
### Parameters
Parameter | Description  
---|---  
label | The text to use as a label for the field.  
### Description
Initializes and returns an instance of MaskField. 
* * *
