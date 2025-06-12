* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogException.html

#  [Debug](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.html).LogException
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
public static void LogException(Exception exception); 
## Declaration
public static void LogException(Exception exception, [Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) context); 
### Parameters
Parameter | Description  
---|---  
context | Object to which the message applies.  
exception | Runtime Exception.  
### Description
A variant of Debug.Log that logs an error message to the console.
When you select the message in the console a connection to the context object will be drawn. This is very useful if you want know on which object an error occurs.  
  
Additional resources: [Debug.unityLogger](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug-unityLogger.html), [ILogger](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ILogger.html), [Logger.LogException](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Logger.LogException.html).
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using UnityEngine;
using System.Collections;  
  
public class MyGameClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void MyGameMethod()
    {
        try
        {
            // Do something that can throw an exception
        }
        catch (Exception e)
        {
            Debug.LogException[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogException.html)(e, this);
        }
    }
}

```

Note that this pauses the editor when 'ErrorPause' is enabled.
* * *
