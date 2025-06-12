* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Events.UnityEvent.html

# UnityEvent
class in UnityEngine.Events
/
Inherits from:[Events.UnityEventBase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Events.UnityEventBase.html)
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
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
### Description
A zero argument persistent callback that can be saved with the Scene.
```
using UnityEngine;
using UnityEngine.Events;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    UnityEvent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Events.UnityEvent.html) m_MyEvent;  
  
    void Start()
    {
        if (m_MyEvent == null)
            m_MyEvent = new UnityEvent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Events.UnityEvent.html)();  
  
        m_MyEvent.AddListener(DoSomething);
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        if (Input.anyKeyDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input-anyKeyDown.html) && m_MyEvent != null)
        {
            m_MyEvent.Invoke();
        }
    }  
  
    void DoSomething()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Callback called");
    }
}

```

Note: UnityEvent can also be awaited in any async method.
### Constructors
Constructor | Description  
---|---  
[UnityEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Events.UnityEvent-ctor.html) | Constructor.  
### Public Methods
Method | Description  
---|---  
[AddListener](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Events.UnityEvent.AddListener.html) | Adds a non-persistent listener to the UnityEvent.  
[Invoke](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Events.UnityEvent.Invoke.html) | Invoke all registered callbacks (runtime and persistent).  
[RemoveListener](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Events.UnityEvent.RemoveListener.html) | Remove a non persistent listener from the UnityEvent. If you have added the same listener multiple times, this method will remove all occurrences of it.  
### Inherited Members
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
