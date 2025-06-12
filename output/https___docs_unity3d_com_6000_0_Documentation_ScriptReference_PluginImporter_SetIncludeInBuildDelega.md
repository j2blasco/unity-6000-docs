* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PluginImporter.SetIncludeInBuildDelegate.html

#  [PluginImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PluginImporter.html).SetIncludeInBuildDelegate
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
public void SetIncludeInBuildDelegate([PluginImporter.IncludeInBuildDelegate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PluginImporter.IncludeInBuildDelegate.html) includeInBuildDelegate); 
### Description
Setting the delegate function to be called by ShouldIncludeInBuild.
The delegate will be called by ShouldIncludeInBuild and will return true if the plugin is to be included in the build, false otherwise.
* * *
