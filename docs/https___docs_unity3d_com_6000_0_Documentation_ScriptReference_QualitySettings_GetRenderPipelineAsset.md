* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings.GetRenderPipelineAssetsForPlatform.html

#  [QualitySettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings.html).GetRenderPipelineAssetsForPlatform
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
public static void GetRenderPipelineAssetsForPlatform(string buildTargetGroupName, out HashSet<T> uniqueRenderPipelineAssets); 
### Parameters
Parameter | Description  
---|---  
buildTargetGroupName | The platform to obtain the Render Pipeline Assets.  
uniqueRenderPipelineAssets | A collection with the non null selected Render Pipeline Assets for the platform.  
### Description
[Editor Only] Obtains a set with the non null Render Pipeline Assets selected on all the Quality Levels for the given platform.
* * *
## Declaration
public static void GetRenderPipelineAssetsForPlatform(string buildTargetGroupName, out HashSet<T> uniqueRenderPipelineAssets, out bool allLevelsAreOverridden); 
### Parameters
Parameter | Description  
---|---  
buildTargetGroupName | The platform to obtain the Render Pipeline Assets.  
uniqueRenderPipelineAssets | A collection with the non null selected Render Pipeline Assets for the platform.  
allLevelsAreOverridden | An additional information that state if all quality settings were overridden in the project.  
### Description
[Editor Only] Obtains a set with the non null Render Pipeline Assets selected on all the Quality Levels for the given platform.
```
public T[] GetAllRenderPipelineAssets<T>(BuildTarget[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTarget.html) platform)
    where T : RenderPipelineAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineAsset.html)
{
    var activeBuildTargetGroup = BuildPipeline.GetBuildTargetGroup(platform);
    var namedBuildTarget = NamedBuildTarget.FromBuildTargetGroup[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.NamedBuildTarget.FromBuildTargetGroup.html)(activeBuildTargetGroup);
    QualitySettings.GetRenderPipelineAssetsForPlatform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings.GetRenderPipelineAssetsForPlatform.html)<T>(namedBuildTarget.TargetName, out var uniqueAssets, out bool allLevelsAreOverridden);
    if(allLevelsAreOverridden)
        return uniqueAssets.ToArray();  
  
    return Array.Empty<T>();
}
```

* * *
