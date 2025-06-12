* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Events.UnityEventBase.html

# UnityEventBase
class in UnityEngine.Events
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
Leave feedback
  

Implements interfaces:[ISerializationCallbackReceiver](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ISerializationCallbackReceiver.html)
Suggest a change
## Success!
Thank you for helping us improve the quality of Unity Documentation. Although we cannot accept all submissions, we do read each suggested change from our users and will make updates where applicable.
Close
## Submission failed
For some reason your suggested change could not be submitted. Please <a>try again</a> in a few minutes. And thank you for taking the time to help us improve the quality of Unity Documentation.
Close
Your name Your email Suggestion* Submit suggestion
Cancel
### Description
Abstract base class for UnityEvents.
This class provides the base functionality for the UnityEvents.
### Public Methods
Method | Description  
---|---  
[GetPersistentEventCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Events.UnityEventBase.GetPersistentEventCount.html) | Get the number of registered persistent listeners.  
[GetPersistentListenerState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Events.UnityEventBase.GetPersistentListenerState.html) | Returns the execution state of a persistent listener.  
[GetPersistentMethodName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Events.UnityEventBase.GetPersistentMethodName.html) | Get the target method name of the listener at index index.  
[GetPersistentTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Events.UnityEventBase.GetPersistentTarget.html) | Get the target component of the listener at index index.  
[RemoveAllListeners](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Events.UnityEventBase.RemoveAllListeners.html) | Remove all non-persistent (ie created from script) listeners from the event.  
[SetPersistentListenerState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Events.UnityEventBase.SetPersistentListenerState.html) | Modify the execution state of a persistent listener.  
### Static Methods
Method | Description  
---|---  
[GetValidMethodInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Events.UnityEventBase.GetValidMethodInfo.html) | Given an object, function name, and a list of argument types; find the method that matches.  
* * *
