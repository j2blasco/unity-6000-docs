* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Logger.Log.html

#  [Logger](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Logger.html).Log
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
public void Log([LogType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LogType.html) logType, object message); 
## Declaration
public void Log([LogType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LogType.html) logType, object message, [Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) context); 
## Declaration
public void Log([LogType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LogType.html) logType, string tag, object message); 
## Declaration
public void Log([LogType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LogType.html) logType, string tag, object message, [Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) context); 
## Declaration
public void Log(object message); 
## Declaration
public void Log(string tag, object message); 
## Declaration
public void Log(string tag, object message, [Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) context); 
### Parameters
Parameter | Description  
---|---  
logType | The type of the log message.  
tag | Used to identify the source of a log message. It usually identifies the class where the log call occurs.  
message | String or object to be converted to string representation for display.  
context | Object to which the message applies.  
### Description
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
  
        logger.Log("Hello Logger[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Logger.html)");
    }
}

```

* * *
