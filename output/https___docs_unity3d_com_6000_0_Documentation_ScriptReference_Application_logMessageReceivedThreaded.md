* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-logMessageReceivedThreaded.html

#  [Application](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.html).logMessageReceivedThreaded
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
Event that is fired if a log message is received.
This event will be triggered regardless of whether the message comes in on the main thread or not. This means that the handler code has to be thread-safe. It may be invoked from different threads and may be invoked in parallel. Make sure to only access Unity APIs from your handlers that are allowed to be called from threads other than the main thread.  
  
**Note:** It is not necessary to subscribe to both [Application.logMessageReceived](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-logMessageReceived.html) and `Application.logMessageReceivedThreaded`. The multi-threaded variant will also be called for messages on the main thread.  
  
Additional resources: [Application.logMessageReceived](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-logMessageReceived.html).
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public string output = "";
    public string stack = "";  
  
    void OnEnable()
    {
        Application.logMessageReceivedThreaded[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-logMessageReceivedThreaded.html) += HandleLog;
    }  
  
    void OnDisable()
    {
        Application.logMessageReceivedThreaded[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-logMessageReceivedThreaded.html) -= HandleLog;
    }  
  
    void HandleLog(string logString, string stackTrace, LogType[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LogType.html) type)
    {
        output = logString;
        stack = stackTrace;
    }
}

```

* * *
