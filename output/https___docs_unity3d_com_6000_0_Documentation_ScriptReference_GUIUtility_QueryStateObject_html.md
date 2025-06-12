* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility.QueryStateObject.html

#  [GUIUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility.html).QueryStateObject
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
public static object QueryStateObject(Type t, int controlID); 
### Description
Get an existing state object from a controlID.
This will return a recycled state object that is unique for `controlID`. If the state object has not been created by calling [GetStateObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility.GetStateObject.html) then it cannot be accessed using [QueryStateObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility.QueryStateObject.html). A call into [QueryStateObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility.QueryStateObject.html) with the state object not created is invalid. A null may be returned, but is not guaranteed. An exception may happen instead.  
  
Additional resources: [GUIUtility.GetStateObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility.GetStateObject.html). 
* * *
