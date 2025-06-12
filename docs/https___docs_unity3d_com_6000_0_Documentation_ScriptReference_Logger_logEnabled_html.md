* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Logger-logEnabled.html

#  [Logger](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Logger.html).logEnabled
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
logEnabled; 
### Description
To runtime toggle debug logging [ON/OFF].
```
using UnityEngine;
using System.Collections;  
  
public class MyGameClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private static ILogger[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ILogger.html) logger = Debug.unityLogger[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug-unityLogger.html);
    private static string kTAG = "MyGameTag";  
  
    void Start()
    {
        logger.logEnabled = Debug.isDebugBuild[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug-isDebugBuild.html);  
  
        logger.Log(kTAG, "This log will be displayed only in debug build");
    }
}

```

* * *
