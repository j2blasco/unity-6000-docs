* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SplashScreen.Stop.html

#  [SplashScreen](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SplashScreen.html).Stop
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
public static void Stop([Rendering.SplashScreen.StopBehavior](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SplashScreen.StopBehavior.html) stopBehavior); 
### Description
Stop the SplashScreen rendering.
```
using System.Collections;
using UnityEngine;
using UnityEngine.Rendering;  
  
// This example shows how the SplashScreen[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SplashScreen.html) can be canceled early via the user pressing any key.
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public SplashScreen.StopBehavior stopBehavior;  
  
    void Start()
    {
        StartCoroutine(SplashScreenController());
    }  
  
    IEnumerator SplashScreenController()
    {
        SplashScreen.Begin[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SplashScreen.Begin.html)();
        while (!SplashScreen.isFinished[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SplashScreen-isFinished.html))
        {
            // Fade to the background if the user presses any key during the splash screen rendering.
            if (Input.anyKeyDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input-anyKeyDown.html))
            {
                SplashScreen.Stop[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SplashScreen.Stop.html)(stopBehavior);
                break;
            }
            yield return null;
        }
    }
}

```

* * *
