* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.TryGetValue.html

#  [SearchItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html).TryGetValue(string,Field)
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
### Parameters
Parameter | Description  
---|---  
name | Field name.  
field | Copy of the field found.  
context | Search context if available to resolve the search field.  
### Returns
**void** Returns true if a field value was found. 
### Description
Returns' a field's value if any. Compared to [SearchItem.TryGetField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.TryGetField.html) this method also resolved built-in field such as id, label, description, value, etc.
* * *
