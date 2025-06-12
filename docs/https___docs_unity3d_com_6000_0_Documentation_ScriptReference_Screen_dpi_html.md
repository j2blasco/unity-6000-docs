* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-dpi.html

#  [Screen](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen.html).dpi
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
dpi; 
### Description
The current pixel density of the screen measured in dots-per-inch (DPI) (Read Only).
This is the actual DPI of the screen or physical device running the application. The property returns `0` if the current DPI cannot be determined.  
  
**Android:** On Android devices, this property uses [densityDpi](https://developer.android.com/reference/android/util/DisplayMetrics.html#densityDpi) which is a logical bucket containing a range of DPI values rather than providing an exact value. Alternatively, you can calculate the DPI value using an average of [xdpi](https://developer.android.com/reference/android/util/DisplayMetrics.html#xdpi) and [ydpi](https://developer.android.com/reference/android/util/DisplayMetrics.html#ydpi) as shown in the following code example.  
  
While this approach might provide more accurate DPI value, some Android devices might report incorrect `xdpi` and `ydpi` values. It is recommended to account for these inaccuracies when following this method.
```
using UnityEngine;
using UnityEngine.Android;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private void Start()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("SCREEN DPI: " + GetDPI());
    }
    
    float GetDPI()
    {
        using var version = new AndroidJavaClass[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJavaClass.html)("android.os.Build$VERSION");
        var apiLevel = version.GetStatic<int>("SDK_INT");
        using var metrics = new AndroidJavaObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJavaObject.html)("android.util.DisplayMetrics");
        if (apiLevel >= 30)
        {
            using var display = AndroidApplication.currentActivity.Call<AndroidJavaObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJavaObject.html)>("getDisplay");
            
            display.Call("getRealMetrics", metrics);
        }
        else
        {
            using var display = AndroidApplication.currentActivity.Call<AndroidJavaObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJavaObject.html)>("getWindowManager")
            .Call<AndroidJavaObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJavaObject.html)>("getDefaultDisplay");
            display.Call("getMetrics", metrics);
        }
        
        float xdpi = metrics.Get<float>("xdpi");
        float ydpi = metrics.Get<float>("ydpi");
        return (xdpi + ydpi) * 0.5f;
    }
}

```

* * *
