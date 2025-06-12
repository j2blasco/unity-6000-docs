* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.AssignType.html

# AssignType
enumeration
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
An assign type for property elements.
Properties in gradle files use different ways to assign a value. Use the `AssignType` parameter to choose which way to assign the property value.
```
using Unity.Android.Gradle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.html);
using UnityEditor.Android;  
  
public class ModifyProject : AndroidProjectFilesModifier[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidProjectFilesModifier.html)
{
    public override void OnModifyAndroidProjectFiles(AndroidProjectFiles[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidProjectFiles.html) projectFiles)
    {
        // This will produce "buildToolsVersion = '30.0.0'"
        projectFiles.UnityLibraryBuildGradle.Android.BuildToolsVersion.Set("30.0.0", AssignType.Equals[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.AssignType.Equals.html));
        // This will produce "compileSdk(30)"
        projectFiles.UnityLibraryBuildGradle.Android.CompileSdk.Set(30, AssignType.Parentheses[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.AssignType.Parentheses.html));
    }
}

```

### Properties
Property | Description  
---|---  
[None](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.AssignType.None.html) | Places value after a space: property value.  
[Equals](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.AssignType.Equals.html) | Places value after an equals: property = value.  
[PlusEquals](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.AssignType.PlusEquals.html) | Places value after plus-equals: property += value.  
[Column](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.AssignType.Column.html) | Places value after a column: property : value.  
[Parentheses](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.AssignType.Parentheses.html) | Places value in parentheses: property(value).  
[Brackets](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.AssignType.Brackets.html) | Places value in brackets: property [value].  
[EqualsBrackets](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.AssignType.EqualsBrackets.html) | Places value in brackets after an equals: property = [value].  
[SetFunction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.AssignType.SetFunction.html) | Places value in a set function: property.set(value).  
* * *
