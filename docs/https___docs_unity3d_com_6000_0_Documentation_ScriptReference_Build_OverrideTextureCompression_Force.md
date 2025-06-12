* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.OverrideTextureCompression.ForceNoCrunchCompression.html

#  [OverrideTextureCompression](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.OverrideTextureCompression.html).ForceNoCrunchCompression
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
Import textures with crunch compression disabled.
You can set [EditorUserBuildSettings.overrideTextureCompression](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUserBuildSettings-overrideTextureCompression.html) to `ForceNoCrunchCompression` to import all textures with Crunch compression disabled. This is the same as if all the textures had their Crunch compression option disabled in their per-platform import settings.  
  
This setting is mostly useful for local development as Crunch compressing textures can take a long time, disabling it can speed up texture importing or a platform switch process significantly.  
  
Note: `ForceFastCompressor` also disables Crunch compression.   
  
Additional resources: [EditorUserBuildSettings.overrideTextureCompression](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUserBuildSettings-overrideTextureCompression.html), [Texture Importer](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html), [command line arguments](https://docs.unity3d.com/6000.0/Documentation/Manual/CommandLineArguments.html).
* * *
