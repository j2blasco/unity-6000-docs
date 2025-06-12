* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-activeQualityLevelChanged.html

#  [QualitySettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings.html).activeQualityLevelChanged
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-QualitySettings.html "Go to QualitySettings Component in the Manual")
### Parameters
Parameter | Description  
---|---  
value | If the current Quality level is being changed this callback will be raised.  
### Description
Delegate that you can use to invoke custom code when Unity changes the current Quality Level.
Parameters are the previous Quality Level and the new Quality Level.
```
using UnityEngine;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        QualitySettings.activeQualityLevelChanged[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-activeQualityLevelChanged.html) += QualitySettings_activeQualityLevelChanged;
    }  
  
    private void QualitySettings_activeQualityLevelChanged(int previousQuality, int currentQuality)
    {
        // Put the code that you want to execute everytime the Quality used is changed
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"Quality Level has been changed from {QualitySettings.names[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-names.html)[previousQuality]} to {QualitySettings.names[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-names.html)[currentQuality]}");
    }  
  
    void OnDestroy()
    {
        QualitySettings.activeQualityLevelChanged[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-activeQualityLevelChanged.html) -= QualitySettings_activeQualityLevelChanged;
    }
}

```

* * *
