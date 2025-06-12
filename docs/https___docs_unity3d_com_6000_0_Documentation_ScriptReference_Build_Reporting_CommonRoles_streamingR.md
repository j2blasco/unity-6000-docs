* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.CommonRoles-streamingResourceFile.html

#  [CommonRoles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.CommonRoles.html).streamingResourceFile
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
streamingResourceFile; 
### Description
The [BuildFile.role](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.BuildFile-role.html) value of a file that contains streaming resource data.
For example, when a texture is packed into a build, only metadata about the texture is packed into the [CommonRoles.sharedAssets](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.CommonRoles-sharedAssets.html) file - the actual content of the texture is packed into a streamingResourceFile, where it can be streamed into memory asynchronously at runtime.
* * *
