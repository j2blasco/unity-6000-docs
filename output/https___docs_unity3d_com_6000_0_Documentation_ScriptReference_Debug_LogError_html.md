* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogError.html

#  [Debug](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.html).LogError
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
## Declaration
public static void LogError(object message); 
## Declaration
public static void LogError(object message, [Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) context); 
### Parameters
Parameter | Description  
---|---  
message | String or object to be converted to string representation for display.  
context | Object to which the message applies.  
### Description
A variant of Debug.Log that logs an error message to the console.
When you select the message in the console a connection to the context object will be drawn. This is very useful if you want know on which object an error occurs.  
  
When the message is a string, rich text markup can be used to add emphasis. See the manual page about [rich text](https://docs.unity3d.com/6000.0/Documentation/Manual/StyledText.html) for details of the different markup tags available.  
  
Additional resources: [Debug.unityLogger](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug-unityLogger.html), [ILogger](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ILogger.html), [Logger.LogError](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Logger.LogError.html).
```
using UnityEngine;
using System.Collections;  
  
public class MyGameClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) transform;  
  
    void MyGameMethod()
    {
        if (transform == null)
            Debug.LogError[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogError.html)("memberVariable must be set to point to a Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html).", transform);
    }
}

```

Note that this pauses the editor when 'ErrorPause' is enabled.
* * *
