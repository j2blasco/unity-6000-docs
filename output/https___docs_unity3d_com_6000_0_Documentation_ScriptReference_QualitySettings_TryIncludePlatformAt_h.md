* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings.TryIncludePlatformAt.html

#  [QualitySettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings.html).TryIncludePlatformAt
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
public static bool TryIncludePlatformAt(string buildTargetGroupName, int index, out Exception error); 
### Parameters
Parameter | Description  
---|---  
buildTargetGroupName | The platform name.  
index | The index of the Quality Level, must be positive and lower than the count of Quality Levels.  
error | The error found by the API.  
### Returns
**bool** If errors were found. 
### Description
[Editor Only] Includes a platform to be supported by the Quality Level.
```
public void IncludeQualityLevelForPlatform(int qualityLevelToExclude, BuildTarget[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTarget.html) platformToExclude)
{
    var activeBuildTargetGroup = BuildPipeline.GetBuildTargetGroup(platformToExclude);
    var namedBuildTarget = NamedBuildTarget.FromBuildTargetGroup[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.NamedBuildTarget.FromBuildTargetGroup.html)(activeBuildTargetGroup);
    bool result = QualitySettings.TryIncludePlatformAt[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings.TryIncludePlatformAt.html)(namedBuildTarget.TargetName, qualityLevelToExclude, out var ex);
    Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(result
        ? "Successfully included the platform at the specified quality level."
        : $"Failed to include the platform. {ex.Message}");
}
```

Includes a platform in a given Quality Level.
* * *
