* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Events.UnityEventTools.RemovePersistentListener.html

#  [UnityEventTools](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Events.UnityEventTools.html).RemovePersistentListener
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
public static void RemovePersistentListener([Events.UnityEventBase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Events.UnityEventBase.html) unityEvent, int index); 
## Declaration
public static void RemovePersistentListener([Events.UnityEventBase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Events.UnityEventBase.html) unityEvent, [Events.UnityAction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Events.UnityAction.html) call); 
## Declaration
public static void RemovePersistentListener([Events.UnityEventBase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Events.UnityEventBase.html) unityEvent, [Events.UnityAction_1](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Events.UnityAction_1.html) call); 
## Declaration
public static void RemovePersistentListener([Events.UnityEventBase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Events.UnityEventBase.html) unityEvent, [Events.UnityAction_2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Events.UnityAction_2.html) call); 
## Declaration
public static void RemovePersistentListener([Events.UnityEventBase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Events.UnityEventBase.html) unityEvent, [Events.UnityAction_3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Events.UnityAction_3.html) call); 
## Declaration
public static void RemovePersistentListener([Events.UnityEventBase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Events.UnityEventBase.html) unityEvent, [Events.UnityAction_4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Events.UnityAction_4.html) call); 
### Parameters
Parameter | Description  
---|---  
unityEvent | Event to modify.  
index | Index to remove (if specified).  
call | Function to remove (if specified).  
### Description
Removes the given function from the event.
You can specify either the index of the listener function to remove, or the delegate type of the listener function to remove. If you specify the delegate type, this method removes all occurrences of that listener function from the event. If you specify the the index, this method only removes the listener function at the index specified.
* * *
