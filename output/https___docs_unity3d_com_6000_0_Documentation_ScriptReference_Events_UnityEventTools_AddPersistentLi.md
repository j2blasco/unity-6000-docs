* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Events.UnityEventTools.AddPersistentListener.html

#  [UnityEventTools](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Events.UnityEventTools.html).AddPersistentListener
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
public static void AddPersistentListener([Events.UnityEventBase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Events.UnityEventBase.html) unityEvent); 
## Declaration
public static void AddPersistentListener([Events.UnityEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Events.UnityEvent.html) unityEvent, [Events.UnityAction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Events.UnityAction.html) call); 
## Declaration
public static void AddPersistentListener([Events.UnityEvent_1](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Events.UnityEvent_1.html) unityEvent, [Events.UnityAction_1](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Events.UnityAction_1.html) call); 
## Declaration
public static void AddPersistentListener([Events.UnityEvent_2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Events.UnityEvent_2.html) unityEvent, [Events.UnityAction_2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Events.UnityAction_2.html) call); 
## Declaration
public static void AddPersistentListener([Events.UnityEvent_3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Events.UnityEvent_3.html) unityEvent, [Events.UnityAction_3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Events.UnityAction_3.html) call); 
## Declaration
public static void AddPersistentListener([Events.UnityEvent_4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Events.UnityEvent_4.html) unityEvent, [Events.UnityAction_4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Events.UnityAction_4.html) call); 
### Parameters
Parameter | Description  
---|---  
unityEvent | Event to modify.  
call | Function to call.  
### Description
Adds a persistent call to the listener. Will be invoked with the arguments as defined by the Event and sent from the call location.
* * *
