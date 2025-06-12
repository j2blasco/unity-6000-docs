* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SplashScreen.Draw.html

#  [SplashScreen](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SplashScreen.html).Draw
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
public static void Draw(); 
### Description
Immediately draws the splash screen. Ensure you have called [SplashScreen.Begin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SplashScreen.Begin.html) before you start calling this.
```
using System.Collections;
using UnityEngine;
using UnityEngine.Rendering;  
  
// This example shows how you could draw the splash screen at the start of a Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html). This is a good way to integrate the splash screen with your own or add extras such as Audio.
public class SplashScreenExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    IEnumerator Start()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Showing splash screen");
        SplashScreen.Begin[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SplashScreen.Begin.html)();
        while (!SplashScreen.isFinished[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SplashScreen-isFinished.html))
        {
            SplashScreen.Draw[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SplashScreen.Draw.html)();
            yield return null;
        }
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Finished showing splash screen");
    }
}

```

* * *
