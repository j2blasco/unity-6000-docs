* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImportContext-selectedBuildTarget.html

#  [AssetImportContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImportContext.html).selectedBuildTarget
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
[BuildTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTarget.html) selectedBuildTarget; 
### Description
Returns the current build target and creates a dependency on the target platform within a scripted importer.
This property returns the current build target platform (similar to EditorUserBuildSettings.activeBuildTarget), however this property is provided specifically as a way for you to create a dependency on the build target within a scripted importer.  
  
You should use this property if you are writing a scripted importer and you want your importer to generate different results based on the target platform. Using this property within a scripted importer creates a platform dependency in your importer. This means when you change the Editor's active build target, all assets imported by this importer will be automatically re-imported to reflect any changes caused by the dependency you set up.  
  
_Note: If you are not writing an importer, and just want to read the currently selected build target, you should use_ [EditorUserBuildSettings.activeBuildTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUserBuildSettings-activeBuildTarget.html).
* * *
