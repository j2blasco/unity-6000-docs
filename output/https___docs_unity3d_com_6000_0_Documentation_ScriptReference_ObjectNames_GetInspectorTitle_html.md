* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectNames.GetInspectorTitle.html

#  [ObjectNames](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectNames.html).GetInspectorTitle
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
public static string GetInspectorTitle([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) obj); 
## Declaration
public static string GetInspectorTitle([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) obj, bool multiObjectEditing); 
### Parameters
Parameter | Description  
---|---  
obj | Object to get a title from.  
multiObjectEditing | Tells if the inspector is running multi-edit.  
### Returns
**string** Returns the best title according to objects being inspected. 
### Description
Inspector title for an object.
If an object is a script, this will return "_scriptname_ (Script)", for example.  
  
Additional resources: [ObjectNames.GetClassName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectNames.GetClassName.html), [ObjectNames.NicifyVariableName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectNames.NicifyVariableName.html).
* * *
