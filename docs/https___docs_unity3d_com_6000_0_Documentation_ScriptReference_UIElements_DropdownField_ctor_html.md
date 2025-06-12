* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DropdownField-ctor.html

# DropdownField Constructor
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
public DropdownField(); 
### Description
Construct an empty DropdownField. 
* * *
## Declaration
public DropdownField(string label); 
### Parameters
Parameter | Description  
---|---  
label | The label to display in front of the field.  
### Description
Construct a DropdownField with a Label in front. 
* * *
## Declaration
public DropdownField(List<string> choices, string defaultValue, Func<string,string> formatSelectedValueCallback, Func<string,string> formatListItemCallback); 
### Parameters
Parameter | Description  
---|---  
choices | The list of choices to display in the dropdown.  
defaultValue | The default value selected from the dropdown.  
formatSelectedValueCallback | Callback to format the selected value.  
formatListItemCallback | Callback to format the list items displayed in the dropdown.  
### Description
Construct a DropdownField. 
* * *
## Declaration
public DropdownField(string label, List<string> choices, string defaultValue, Func<string,string> formatSelectedValueCallback, Func<string,string> formatListItemCallback); 
### Parameters
Parameter | Description  
---|---  
label | The label to display in front of the field.  
choices | The list of choices to display in the dropdown.  
defaultValue | The default value selected from the dropdown.  
formatSelectedValueCallback | Callback to format the selected value.  
formatListItemCallback | Callback to format the list items displayed in the dropdown.  
### Description
Construct a DropdownField. 
* * *
## Declaration
public DropdownField(List<string> choices, int defaultIndex, Func<string,string> formatSelectedValueCallback, Func<string,string> formatListItemCallback); 
### Parameters
Parameter | Description  
---|---  
choices | The list of choices to display in the dropdown.  
defaultIndex | The index of the choice selected by default.  
formatSelectedValueCallback | Callback to format the selected value.  
formatListItemCallback | Callback to format the list items displayed in the dropdown.  
### Description
Construct a DropdownField. 
* * *
## Declaration
public DropdownField(string label, List<string> choices, int defaultIndex, Func<string,string> formatSelectedValueCallback, Func<string,string> formatListItemCallback); 
### Parameters
Parameter | Description  
---|---  
label | The label to display in front of the field.  
choices | The list of choices to display in the dropdown.  
defaultIndex | The index of the choice selected by default.  
formatSelectedValueCallback | Callback to format the selected value.  
formatListItemCallback | Callback to format the list items displayed in the dropdown.  
### Description
Construct a DropdownField. 
* * *
