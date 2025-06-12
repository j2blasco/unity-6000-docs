* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidBlitType.html

# AndroidBlitType
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
Describes the method for how content is displayed on the screen.
Options are as follows:  
  
Use **Always** to render offscreen and blit to the backbuffer. Use **Never** to render directly to the backbuffer. Use **Auto** or automatically choose the most appropriate option.  
  
Depending on the device, [AndroidBlitType.Never](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidBlitType.Never.html) may not support switching MSAA settings at runtime or rendering at non-native resolution. [AndroidBlitType.Never](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidBlitType.Never.html) does not provide a sRGB backbuffer. Linear rendering requires a framebuffer that does sRGB read/write conversions (see [RenderTexture.sRGB](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-sRGB.html)), otherwise the generated image typically appears too dark. Therefore [AndroidBlitType.Never](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidBlitType.Never.html) is not recommended when linear rendering is used. If you want to use linear rendering with [AndroidBlitType.Never](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidBlitType.Never.html) despite this information, you have to setup your own sRGB render target and handle the blit to the backbuffer.  
  
AndroidBlitType is ignored when the Vulkan Graphics API is used.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Build;
using UnityEngine;  
  
public class AndroidBlitTypeExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Build/Android[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android.html) Blit Type Auto Example")]
    public static void AndroidBlitTypes()
    {
        PlayerSettings.SetScriptingBackend[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.SetScriptingBackend.html)(NamedBuildTarget.Android[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.NamedBuildTarget.Android.html), ScriptingImplementation.IL2CPP[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptingImplementation.IL2CPP.html));
        PlayerSettings.Android.targetArchitectures[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-targetArchitectures.html) = AndroidArchitecture.ARM64[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidArchitecture.ARM64.html);  
  
        //Set AndroidBlitType[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidBlitType.html) to Auto which automatically determines
        //the most appropriate method for drawing to the screen.
        PlayerSettings.Android.blitType[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-blitType.html) = AndroidBlitType.Auto[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidBlitType.Auto.html);  
  
        BuildPlayerOptions[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPlayerOptions.html) options = new BuildPlayerOptions[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPlayerOptions.html)();
        options.scenes = new[] { "Assets/Scenes/SampleScene.unity" };
        options.locationPathName = "Builds/AndroidBuild.apk";
        options.target = BuildTarget.Android[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTarget.Android.html);
        options.targetGroup = BuildTargetGroup.Android[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTargetGroup.Android.html);  
  
        BuildPipeline.BuildPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPipeline.BuildPlayer.html)(options);
    }
}
```

### Properties
Property | Description  
---|---  
[Always](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidBlitType.Always.html) | Always render offscreen and blit to the backbuffer.  
[Never](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidBlitType.Never.html) | Never render offscreen and blit to the backbuffer. Always render directly to the backbuffer.  
[Auto](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidBlitType.Auto.html) | Automatically determine the most appropriate method for drawing to the screen.  
* * *
