* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings.SetLODSettings.html

#  [QualitySettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings.html).SetLODSettings
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
## Declaration
public static void SetLODSettings(float lodBias, int maximumLODLevel, bool setDirty); 
### Parameters
Parameter | Description  
---|---  
lodBias | Global multiplier for the LOD's switching distance.  
maximumLODLevel | A maximum LOD level. All LOD groups.  
setDirty | If true, marks all views as dirty.  
### Description
Sets the [lodBias](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-lodBias.html) and [maximumLODLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-maximumLODLevel.html) at the same time.
If you pass in `true` for the `setDirty` parameter, Unity refreshes all views.  
  
Additional resources: [lodBias](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-lodBias.html), [maximumLODLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-maximumLODLevel.html).
* * *
