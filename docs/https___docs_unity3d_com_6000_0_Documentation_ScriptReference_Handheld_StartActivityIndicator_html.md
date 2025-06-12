* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handheld.StartActivityIndicator.html

#  [Handheld](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handheld.html).StartActivityIndicator
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
public static void StartActivityIndicator(); 
### Description
Starts os activity indicator.
Please be warned that this informs os ui system to start. For actual animation to take effect you usually need to wait till the end of this frame. So if you want activity indicator to be animated during synced operation, please use coroutines. Note: You can't move the activity indicator invoked by this method.
```
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;  
  
public class Example2 : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    IEnumerator Load()
    {
        #if UNITY_IPHONE
        Handheld.SetActivityIndicatorStyle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handheld.SetActivityIndicatorStyle.html)(iOS.ActivityIndicatorStyle.Gray);
        #elif UNITY_ANDROID
        Handheld.SetActivityIndicatorStyle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handheld.SetActivityIndicatorStyle.html)(AndroidActivityIndicatorStyle.Small[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidActivityIndicatorStyle.Small.html));
        #endif  
  
        Handheld.StartActivityIndicator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handheld.StartActivityIndicator.html)();
        yield return new WaitForSeconds[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitForSeconds.html)(0);
        SceneManager.LoadScene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.LoadScene.html)("My Next Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html)");
    }  
  
    void OnGUI()
    {
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 10, 200, 200), "Load!"))
            StartCoroutine(Load());
    }
}

```

* * *
