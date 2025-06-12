* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Events.UnityEventTools.AddObjectPersistentListener.html

#  [UnityEventTools](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Events.UnityEventTools.html).AddObjectPersistentListener
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
public static void AddObjectPersistentListener([Events.UnityEventBase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Events.UnityEventBase.html) unityEvent, UnityAction<T> call, T argument); 
### Parameters
Parameter | Description  
---|---  
unityEvent | Event to modify.  
call | Function to call.  
argument | Argument to use when invoking.  
### Description
Adds a persistent, preset call to the listener.
* * *
