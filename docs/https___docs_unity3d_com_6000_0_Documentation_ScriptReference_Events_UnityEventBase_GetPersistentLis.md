* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Events.UnityEventBase.GetPersistentListenerState.html

#  [UnityEventBase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Events.UnityEventBase.html).GetPersistentListenerState
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
public [Events.UnityEventCallState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Events.UnityEventCallState.html) GetPersistentListenerState(int index); 
### Parameters
Parameter | Description  
---|---  
index | Index of the listener to query.  
### Returns
**UnityEventCallState** Execution state of the persistent listener. 
### Description
Returns the execution state of a persistent listener.
```
using UnityEngine;
using UnityEngine.Events;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public UnityEvent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Events.UnityEvent.html) onAction;  
  
    void Start()
    {
        // Prints out the details of all persistent events
        for (int i = 0; i < onAction.GetPersistentEventCount(); ++i)
        {
            var target = onAction.GetPersistentTarget(i);
            var method = onAction.GetPersistentMethodName(i);
            var state = onAction.GetPersistentListenerState(i);  
  
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"{target}:{method}({state})");
        }
    }
}

```

* * *
