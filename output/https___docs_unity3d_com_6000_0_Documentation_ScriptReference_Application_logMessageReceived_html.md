* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-logMessageReceived.html

#  [Application](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.html).logMessageReceived
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
This event only ever triggers on the main thread. Use it if your handler requires accessing parts of the Unity API that are restricted to the main thread or if for other reasons your handler isn't thread-safe.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public string output = "";
    public string stack = "";  
  
    void OnEnable()
    {
        Application.logMessageReceived[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-logMessageReceived.html) += HandleLog;
    }  
  
    void OnDisable()
    {
        Application.logMessageReceived[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-logMessageReceived.html) -= HandleLog;
    }  
  
    void HandleLog(string logString, string stackTrace, LogType[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LogType.html) type)
    {
        output = logString;
        stack = stackTrace;
    }
}

```

Additional resources: [Application.logMessageReceived](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-logMessageReceived.html), [LogType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LogType.html), [Application.logMessageReceivedThreaded](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-logMessageReceivedThreaded.html).
* * *
