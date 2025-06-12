* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.Xcode.PBXProject.GetUnityFrameworkTargetGuid.html

#  [PBXProject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.Xcode.PBXProject.html).GetUnityFrameworkTargetGuid
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
public string GetUnityFrameworkTargetGuid(); 
### Returns
**string** The GUID for the framework target. 
### Description
Returns the GUID of the framework target in Unity project.
Returns the GUID of the framework target. This target includes source code, plugins, dependent frameworks, and source compile/link build options. You can retrieve the other targets using [GetUnityMainTargetGuid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.Xcode.PBXProject.GetUnityMainTargetGuid.html) and [TargetGuidByName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.Xcode.PBXProject.TargetGuidByName.html).
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Callbacks;
using UnityEditor.iOS.Xcode;  
  
public class Sample_GetUnityFrameworkTargetGuid  
{
    [PostProcessBuild]
    public static void OnPostprocessBuild(BuildTarget[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTarget.html) buildTarget, string pathToBuiltProject)
    {  
  
        // Stop processing if build target is not iOS[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.iOS.html)
        if (buildTarget != BuildTarget.iOS[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTarget.iOS.html))
            return;  
  
        // Initialize PBXProject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.Xcode.PBXProject.html)
        string projectPath = PBXProject.GetPBXProjectPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.Xcode.PBXProject.GetPBXProjectPath.html)(pathToBuiltProject);  
  
        PBXProject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.Xcode.PBXProject.html) pbxProject = new PBXProject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.Xcode.PBXProject.html)();
        pbxProject.ReadFromFile(projectPath);  
  
        // Get the GUID for the UnityFramework target
        string unityFrameworkGuid = pbxProject.GetUnityFrameworkTargetGuid();  
  
        // The unityFrameworkGuid can be later used to specify UnityFramework as the target when manipulating the pbxproj file
        pbxProject.AddFrameworkToProject(unityFrameworkGuid, "Security.framework", false);
        pbxProject.SetBuildProperty(unityFrameworkGuid, "ENABLE_BITCODE", "NO");  
  
        // Apply changes to the pbxproj file
        pbxProject.WriteToFile(projectPath);
    }
}

```

* * *
