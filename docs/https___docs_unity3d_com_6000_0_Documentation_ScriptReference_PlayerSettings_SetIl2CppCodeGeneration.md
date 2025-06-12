* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.SetIl2CppCodeGeneration.html

#  [PlayerSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.html).SetIl2CppCodeGeneration
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettings.html "Go to PlayerSettings Component in the Manual")
## Declaration
public static void SetIl2CppCodeGeneration([Build.NamedBuildTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.NamedBuildTarget.html) buildTarget, [Build.Il2CppCodeGeneration](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Il2CppCodeGeneration.html) value); 
### Parameters
Parameter | Description  
---|---  
buildTarget | The [NamedBuildTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.NamedBuildTarget.html).  
value | Code generation option.  
### Description
Sets the code generation option for IL2CPP for the specified build target.
There are two options for IL2CPP code generation. [Il2CppCodeGeneration.OptimizeSpeed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Il2CppCodeGeneration.OptimizeSpeed.html) generates code that is optimized for runtime performance. This is the default and the behavior in previous versions of Unity. [Il2CppCodeGeneration.OptimizeSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Il2CppCodeGeneration.OptimizeSize.html) generates code that is optimized for build size and iteration. It generates less code and produces a smaller build but may have an impact on runtime performance, especially for generic code. You should consider this option when faster build times are important, such as when iterating on changes.  
  
Additionally, [Il2CppCodeGeneration.OptimizeSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Il2CppCodeGeneration.OptimizeSize.html) generates a universal version of each generic type and method. This avoids some restrictions [Il2CppCodeGeneration.OptimizeSpeed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Il2CppCodeGeneration.OptimizeSpeed.html) has when executing generic code.
* * *
