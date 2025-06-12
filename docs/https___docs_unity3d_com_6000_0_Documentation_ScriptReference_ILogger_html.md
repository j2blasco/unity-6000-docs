* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ILogger.html

# ILogger
interface in UnityEngine
Leave feedback
  

Implements interfaces:[ILogHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ILogHandler.html)
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
Interface for custom logger implementation.
Additional resources: [Logger](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Logger.html), [Debug.unityLogger](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug-unityLogger.html) [ILogHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ILogHandler.html).
### Properties
Property | Description  
---|---  
[filterLogType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ILogger-filterLogType.html) | To selective enable debug log message.  
[logEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ILogger-logEnabled.html) | To runtime toggle debug logging [ON/OFF].  
[logHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ILogger-logHandler.html) | Set Logger.ILogHandler.  
### Public Methods
Method | Description  
---|---  
[IsLogTypeAllowed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ILogger.IsLogTypeAllowed.html) | Check logging is enabled based on the LogType.  
[Log](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ILogger.Log.html) | Logs message to the Unity Console using default logger.  
[LogError](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ILogger.LogError.html) | A variant of ILogger.Log that logs an error message.  
[LogException](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ILogger.LogException.html) | A variant of ILogger.Log that logs an exception message.  
[LogFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ILogger.LogFormat.html) | Logs a formatted message.  
[LogWarning](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ILogger.LogWarning.html) | A variant of Logger.Log that logs an warning message.  
* * *
