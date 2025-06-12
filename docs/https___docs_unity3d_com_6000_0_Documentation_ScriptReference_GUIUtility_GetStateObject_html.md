* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility.GetStateObject.html

#  [GUIUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility.html).GetStateObject
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
public static object GetStateObject(Type t, int controlID); 
### Description
Get a state object from a controlID.
This will return a recycled state object that is unique for `controlID`. If there is no state object then a new one will be created and hooked up to the `controlID`.  
  
On the first call into [GetStateObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility.GetStateObject.html) a new state object will be created. The `controlID` uniquely refers to this object. On subsequent calls the stored object will be returned.  
  
Additional resources: [GUIUtility.QueryStateObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility.QueryStateObject.html). 
* * *
