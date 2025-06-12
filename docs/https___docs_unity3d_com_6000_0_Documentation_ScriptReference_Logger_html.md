* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Logger.html

# Logger
class in UnityEngine
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
Leave feedback
  

Implements interfaces:[ILogger](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ILogger.html), [ILogHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ILogHandler.html)
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
Initializes a new instance of the Logger.
Create a new instance or use default [Debug.unityLogger](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug-unityLogger.html). Additional resources: [ILogger](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ILogger.html), [ILogHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ILogHandler.html).
```
using UnityEngine;
using System.Collections;
using System.IO;
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);  
  
public class MyLogHandler : ILogHandler[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ILogHandler.html)
{
    public void LogFormat(LogType[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LogType.html) logType, UnityEngine.Object context, string format, params object[] args)
    {
        Debug.unityLogger.logHandler.LogFormat(logType, context, format, args);
    }  
  
    public void LogException(Exception exception, UnityEngine.Object context)
    {
        Debug.unityLogger.LogException(exception, context);
    }
}  
  
public class MyGameClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private static string kTAG = "MyGameTag";
    private Logger[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Logger.html) myLogger;  
  
    void Start()
    {
        myLogger = new Logger[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Logger.html)(new MyLogHandler());  
  
        myLogger.Log(kTAG, "MyGameClass Start.");
    }
}

```

### Properties
Property | Description  
---|---  
[filterLogType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Logger-filterLogType.html) | To selective enable debug log message.  
[logEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Logger-logEnabled.html) | To runtime toggle debug logging [ON/OFF].  
[logHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Logger-logHandler.html) | Set Logger.ILogHandler.  
### Constructors
Constructor | Description  
---|---  
[Logger](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Logger-ctor.html) | Create a custom Logger.  
### Public Methods
Method | Description  
---|---  
[IsLogTypeAllowed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Logger.IsLogTypeAllowed.html) | Check logging is enabled based on the LogType.  
[Log](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Logger.Log.html) | Logs message to the Unity Console using default logger.  
[LogError](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Logger.LogError.html) | A variant of Logger.Log that logs an error message.  
[LogException](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Logger.LogException.html) | A variant of Logger.Log that logs an exception message.  
[LogFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Logger.LogFormat.html) | Logs a formatted message.  
[LogWarning](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Logger.LogWarning.html) | A variant of Logger.Log that logs an warning message.  
* * *
