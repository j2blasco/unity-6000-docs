* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings.GetActiveQualityLevelsForPlatform.html

#  [QualitySettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings.html).GetActiveQualityLevelsForPlatform
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
public static int[] GetActiveQualityLevelsForPlatform(string buildTargetGroupName); 
### Parameters
Parameter | Description  
---|---  
buildTargetGroupName | The platform target.  
### Returns
**int[]** The array with the Quality Level indexes that are selected for the given platform. 
### Description
[Editor Only] Obtains an array with the Quality Level indexes that are selected for the given platform.
```
public int[] GetActiveQualityLevelsForPlatform(BuildTarget[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTarget.html) platform)
{
    var activeBuildTargetGroup = BuildPipeline.GetBuildTargetGroup(platform);
    var namedBuildTarget = NamedBuildTarget.FromBuildTargetGroup[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.NamedBuildTarget.FromBuildTargetGroup.html)(activeBuildTargetGroup);
    return QualitySettings.GetActiveQualityLevelsForPlatform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings.GetActiveQualityLevelsForPlatform.html)(namedBuildTarget.TargetName);
}
```

Obtains the indexes that where a given platform is included.
* * *
