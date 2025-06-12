* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug-unityLogger.html

#  [Debug](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.html).unityLogger
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Debug.html "Go to Debug Component in the Manual")
[ILogger](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ILogger.html) unityLogger; 
### Description
Get default debug logger.
Logs `message` to the Unity Console using default logger.  
  
Additional resources: [ILogger](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ILogger.html), [ILogHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ILogHandler.html).
```
using UnityEngine;
using System.Collections;  
  
public class MyGameClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private static ILogger[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ILogger.html) logger = Debug.unityLogger[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug-unityLogger.html);
    private static string kTAG = "MyGameTag";  
  
    void MyGameMethod()
    {
        logger.Log(kTAG, "Hello");  
  
        Debug.unityLogger.Log(kTAG, "World");
    }
}

```

* * *
