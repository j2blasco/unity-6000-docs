* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUserBuildSettings-overrideTextureCompression.html

#  [EditorUserBuildSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUserBuildSettings.html).overrideTextureCompression
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
[Build.OverrideTextureCompression](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.OverrideTextureCompression.html) overrideTextureCompression; 
### Description
The asset importing override of texture compression.
This setting lets you override the texture compression settings that Unity uses when it imports assets. This is mostly useful for local development, to speed up texture importing or build target switching.  
  
This setting affects all textures in your project, and overrides the import settings for individual textures. For example, if a texture's import settings indicate that a "Normal" compressor quality should be used, but `overrideTextureCompression` is set to [OverrideTextureCompression.ForceFastCompressor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.OverrideTextureCompression.ForceFastCompressor.html), the texture will be compressed with "Fast" compressor quality setting.  
  
Overriding the texture compression format can increase the speed of the import process considerably, but it is important to understand the implications. For information on the effects of the different values, see the documentation for the [OverrideTextureCompression](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.OverrideTextureCompression.html) enum.  
  
The Unity editor command line argument `-overrideTextureCompression` can also be used to set this.  
  
Additional resources: [OverrideTextureCompression](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.OverrideTextureCompression.html), [EditorUserBuildSettings.overrideMaxTextureSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUserBuildSettings-overrideMaxTextureSize.html), [Texture Importer](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html), [command line arguments](https://docs.unity3d.com/6000.0/Documentation/Manual/CommandLineArguments.html).
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Build;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/Switch[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Switch.html) textures to import with Fast compressor")]
    public static void OverrideToFastCompressor()
    {
        EditorUserBuildSettings.overrideTextureCompression[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUserBuildSettings-overrideTextureCompression.html) = OverrideTextureCompression.ForceFastCompressor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.OverrideTextureCompression.ForceFastCompressor.html);
        AssetDatabase.Refresh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.Refresh.html)();
    }
}

```

* * *
