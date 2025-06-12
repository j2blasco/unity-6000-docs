* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.SetPlatformIcons.html

#  [PlayerSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.html).SetPlatformIcons
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
public static void SetPlatformIcons([Build.NamedBuildTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.NamedBuildTarget.html) buildTarget, [PlatformIconKind](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlatformIconKind.html) kind, PlatformIcon[] icons); 
**Obsolete** Use SetPlatformIcons(NamedBuildTarget , PlatformIconKind) instead.
## Declaration
public static void SetPlatformIcons([BuildTargetGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTargetGroup.html) platform, [PlatformIconKind](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlatformIconKind.html) kind, PlatformIcon[] icons); 
### Parameters
Parameter | Description  
---|---  
platform | The full list of platforms that support this API the supported kinds can be found in [icon kinds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlatformIconKind.html).  
icons | All available [PlatformIcon](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlatformIcon.html) slots must be retrieved with GetPlatformIcons.  
buildTarget | The [NamedBuildTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.NamedBuildTarget.html).  
### Description
Assign a list of icons for the specified platform and icon kind.
Most platforms support icons with several different sizes. This methods allows you to set [Icons](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlatformIcon.html) for each platform that supports them. GetPlatformIcons has to be used to retrieve all the supported icons for specified [PlatformIconKind](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlatformIconKind.html) and platform. Texture files must be stored in the project and instances obtained using [AssetDatabase.LoadAssetAtPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadAssetAtPath.html).  
  
BuildTargetGroup is marked for deprecation in the future. Use [NamedBuildTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.NamedBuildTarget.html) instead.  
  
The following code sample shows how to set up adaptive icons for an Android application. This is an editor script which means it must be within an Editor folder to compile.
```
using UnityEditor.Android;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;
using UnityEditor.Build;  
  
public static class AndroidPlayerSettingsUtility
{
    // `Adaptive` icons for Android[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android.html) require a background and foreground layer for each icon
    public static void SetIcons(Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html)[][] textures)
    {
        NamedBuildTarget[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.NamedBuildTarget.html) platform = NamedBuildTarget.Android[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.NamedBuildTarget.Android.html);
        PlatformIconKind[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlatformIconKind.html) kind = AndroidPlatformIconKind.Adaptive[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidPlatformIconKind.Adaptive.html);  
  
        PlatformIcon[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlatformIcon.html)[] icons = PlayerSettings.GetPlatformIcons[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.GetPlatformIcons.html)(platform, kind);  
  
        //Assign textures to each available icon slot.
        for (int i = 0; i < icons.Length; i++)
        {
            icons[i].SetTextures(textures[i]);
        }
        PlayerSettings.SetPlatformIcons[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.SetPlatformIcons.html)(platform, kind, icons);
    }
}

```

The following code sample shows how to set all App icons for an iOS application. This is an editor script which means it must be within an Editor folder to compile.
```
using UnityEditor.iOS;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;
using UnityEditor.Build;  
  
public static class iOSPlayerSettingsUtility
{
    // Setting all `App` icons for iOS[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.iOS.html)
    public static void SetAppIcons(Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html)[] textures)
    {
        NamedBuildTarget[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.NamedBuildTarget.html) platform = NamedBuildTarget.iOS[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.NamedBuildTarget.iOS.html);
        PlatformIconKind[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlatformIconKind.html) kind = iOSPlatformIconKind.Application[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.iOSPlatformIconKind.Application.html);  
  
        PlatformIcon[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlatformIcon.html)[] icons = PlayerSettings.GetPlatformIcons[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.GetPlatformIcons.html)(platform, kind);  
  
        //Assign textures to each available icon slot.
        for (int i = 0; i < icons.Length; i++)
        {
            icons[i].SetTextures(textures[i]);
        }
        PlayerSettings.SetPlatformIcons[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.SetPlatformIcons.html)(platform, kind, icons);
    }
}

```

* * *
