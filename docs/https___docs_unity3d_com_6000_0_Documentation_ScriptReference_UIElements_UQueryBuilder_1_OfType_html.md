* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UQueryBuilder_1.OfType.html

#  [UQueryBuilder<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UQueryBuilder_1.html).OfType
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
public UQueryBuilder<T2> OfType(string name, params string[] classes); 
### Parameters
Parameter | Description  
---|---  
name | If specified, will select elements with this name.  
classes | If specified, will select elements with the given class (not to be confused with Type).  
### Returns
**UQueryBuilder <T2>** QueryBuilder configured with the associated selection rules. 
### Description
Selects all elements of the specified Type (eg: Label, Button, ScrollView, etc). 
* * *
## Declaration
public UQueryBuilder<T2> OfType(string name, string className); 
### Parameters
Parameter | Description  
---|---  
name | If specified, will select elements with this name.  
className | If specified, will select elements with the given class (not to be confused with Type).  
### Returns
**UQueryBuilder <T2>** QueryBuilder configured with the associated selection rules. 
### Description
Selects all elements of the specified Type (eg: Label, Button, ScrollView, etc). 
* * *
