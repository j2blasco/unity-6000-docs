* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidApplication-onConfigurationChanged.html

#  [AndroidApplication](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidApplication.html).onConfigurationChanged
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
### Description
A callback to detect the device configuration changes when the application is running.
Unity invokes this callback for the configuration changes related to the following aspects. 
  * Orientation
  * Keyboard visibility
  * Dark theme
  * Screen layout
  * Screen size


For more information on the configuration changes, refer to the [Android developer documentation](https://developer.android.com/guide/topics/resources/runtime-changes).
```
using UnityEngine;
using UnityEngine.Android;  
  
public class MyApplication : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    AndroidConfiguration[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidConfiguration.html) m_PrevConfig;  
  
    public void Start()
    {
        m_PrevConfig = new AndroidConfiguration[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidConfiguration.html)(AndroidApplication.currentConfiguration[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidApplication-currentConfiguration.html));
        AndroidApplication.onConfigurationChanged[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidApplication-onConfigurationChanged.html) += OnConfigurationChanged;
    }  
  
    public void OnDisable()
    {
        AndroidApplication.onConfigurationChanged[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidApplication-onConfigurationChanged.html) -= OnConfigurationChanged;
    }  
  
    private void OnConfigurationChanged(AndroidConfiguration[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidConfiguration.html) newConfig)
    {
        if (m_PrevConfig.orientation != newConfig.orientation ||
            m_PrevConfig.screenLayoutSize != newConfig.screenLayoutSize)
        {
            ApplyUIChanges(newConfig.orientation, newConfig.screenLayoutSize);
        }  
  
        if (m_PrevConfig.uiModeNight != newConfig.uiModeNight)
        {
            ApplyUINightMode(newConfig.uiModeNight);
        }  
  
        if (m_PrevConfig.screenHeightDp != newConfig.screenHeightDp ||
            m_PrevConfig.screenWidthDp != newConfig.screenWidthDp)
        {
            ApplyScreenSizeChanges();
        }  
  
        m_PrevConfig.CopyFrom(newConfig);
    }  
  
    private void ApplyUIChanges(AndroidOrientation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidOrientation.html) orientation, AndroidScreenLayoutSize[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidScreenLayoutSize.html) layoutSize)
    {  
  
    }  
  
    private void ApplyUINightMode(AndroidUIModeNight[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidUIModeNight.html) nightMode)
    {  
  
    }  
  
    private void ApplyScreenSizeChanges()
    {  
  
    }
}
```

* * *
