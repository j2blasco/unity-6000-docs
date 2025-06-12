* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.ExternalFileReference.html

# ExternalFileReference
struct in UnityEditor.Build.Content
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
Desribes an externally referenced file. This is returned as part of the [WriteResult](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.WriteResult.html) when writing a serialized file.
### Properties
Property | Description  
---|---  
[filePath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.ExternalFileReference-filePath.html) | The path of the file that is referenced.  
[guid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.ExternalFileReference-guid.html) | A GUID that represents the file being referenced. This GUID might be used to locate default editor resources, but generally pathName is used to identify externally referenced files.  
[type](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.ExternalFileReference-type.html) | The lookup resolution index for the GUID field in the editor. This is used in conjunction with the GUID internally and should not be modified.  
* * *
