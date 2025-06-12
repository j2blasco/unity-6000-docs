* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Logger-filterLogType.html

#  [Logger](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Logger.html).filterLogType
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
[LogType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LogType.html) filterLogType; 
### Description
To selective enable debug log message.
By settings filterLogType to  
  
[LogType.Log](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LogType.Log.html) (default setting) will display all log messages.  
  
[LogType.Warning](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LogType.Warning.html) will display Warning, Assert, Error and Exception log messages.  
  
[LogType.Assert](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LogType.Assert.html) will display Assert, Error and Exception log messages.  
  
[LogType.Error](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LogType.Error.html) will display Error and Exception log messages.  
  
[LogType.Exception](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LogType.Exception.html) will display Exception log messages.
```
using UnityEngine;
using System.Collections;  
  
public class MyGameClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private static ILogger[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ILogger.html) logger = Debug.unityLogger[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug-unityLogger.html);
    private static string kTAG = "MyGameTag";  
  
    void Start()
    {
        if (Debug.isDebugBuild[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug-isDebugBuild.html))
            logger.filterLogType = LogType.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LogType.Log.html);
        else
            logger.filterLogType = LogType.Warning[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LogType.Warning.html);  
  
        logger.Log(kTAG, "This log will be displayed only in debug build");
        logger.LogError(kTAG, "This log will be displayed in debug and release build");
    }
}

```

* * *
