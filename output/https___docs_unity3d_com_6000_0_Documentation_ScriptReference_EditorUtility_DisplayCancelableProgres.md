* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.DisplayCancelableProgressBar.html

#  [EditorUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.html).DisplayCancelableProgressBar
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
public static bool DisplayCancelableProgressBar(string title, string info, float progress); 
### Description
Displays or updates a progress bar that has a cancel button.
The window title sets to `title` and the info sets to `info`. Set progress should to a value between 0.0 and 1.0, where 0 indicates nothing is loaded and 1.0 indicates loading is complete.  
  
This is useful when you perform a long blocking operation in an Editor script, and want to notify the user of progress. Use this method for long operations that make the Editor non-responsive. For long operations that happen in the background, use the [Progress](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.html) class instead.  
  
A return value of true indicates that the user pressed the **Cancel** button. When the return value is true, you must stop the task that is in progress. After you display the progress bar, use [EditorUtility.ClearProgressBar](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.ClearProgressBar.html) to clear it.  
  
Additional resources: [EditorUtility.DisplayProgressBar](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.DisplayProgressBar.html), [EditorUtility.ClearProgressBar](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.ClearProgressBar.html), and [Progress](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.html).  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/EditorUtilityDisplayCancelableProgressBar.png)  
_Cancelable progress bar in the Editor._
```
using System.Threading;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
// Shows a cancellable progress bar for the specified number of seconds.
public class EditorUtilityDisplayCancelableProgressBar : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    public float secs = 5f;
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Progress[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.html) Bar Usage")]
    static void Init()
    {
        var window = GetWindow(typeof(EditorUtilityDisplayCancelableProgressBar));
        window.Show();
    }  
  
    void OnGUI()
    {
        secs = EditorGUILayout.Slider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.Slider.html)("Time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time.html) to wait:", secs, 1.0f, 20.0f);
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Display[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Display.html) bar"))
        {
            var step = 0.1f;
            for (float t = 0; t < secs; t += step)
            {
                if (EditorUtility.DisplayCancelableProgressBar[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.DisplayCancelableProgressBar.html)("Cancelable", "Doing some work...", t / secs))
                    break;
                // Normally, some computation happens here.
                // This example uses Sleep.
                Thread.Sleep((int)(step * 1000.0f));
            }
            EditorUtility.ClearProgressBar[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.ClearProgressBar.html)();
        }
    }
}

```

* * *
