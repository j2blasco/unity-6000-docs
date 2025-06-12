* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings.IsPlatformIncluded.html

#  [QualitySettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings.html).IsPlatformIncluded
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
public static bool IsPlatformIncluded(string buildTargetGroupName, int index); 
### Parameters
Parameter | Description  
---|---  
buildTargetGroupName | The platform name.  
index | The index of the Quality Level, must be positive and lower than the count of Quality Levels.  
### Returns
**bool** If the platform is included. 
### Description
[Editor Only] Returns if the given platform is included by the Quality Level.
```
    public bool IsPlatformIcluded(BuildTarget[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTarget.html) platform, int index)
    {
        var activeBuildTargetGroup = BuildPipeline.GetBuildTargetGroup(platform);
        var namedBuildTarget = NamedBuildTarget.FromBuildTargetGroup[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.NamedBuildTarget.FromBuildTargetGroup.html)(activeBuildTargetGroup);
        return QualitySettings.IsPlatformIncluded[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings.IsPlatformIncluded.html)(namedBuildTarget.TargetName, index);
    }
```

* * *
