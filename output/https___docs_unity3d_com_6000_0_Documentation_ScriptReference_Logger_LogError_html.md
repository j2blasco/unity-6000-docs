* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Logger.LogError.html

#  [Logger](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Logger.html).LogError
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
public void LogError(string tag, object message); 
## Declaration
public void LogError(string tag, object message, [Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) context); 
### Parameters
Parameter | Description  
---|---  
tag | Used to identify the source of a log message. It usually identifies the class where the log call occurs.  
message | String or object to be converted to string representation for display.  
context | Object to which the message applies.  
### Description
A variant of [Logger.Log](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Logger.Log.html) that logs an error message.
```
using UnityEngine;
using System.Collections;  
  
public class MyGameClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private static ILogger[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ILogger.html) logger = Debug.unityLogger[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug-unityLogger.html);
    private static string kTAG = "MyGameTag";
    private Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) tr;  
  
    void MyGameMethod()
    {
        if (tr == null)
        {
            logger.LogError(kTAG, "memberVariable must be set to point to a Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html).", tr);  
  
            Debug.unityLogger.LogError(kTAG, "Failed! to set Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html)",  tr);
        }
    }
}

```

Note that this pauses the editor when 'ErrorPause' is enabled.
* * *
