* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StatusQueryOptions.html

# StatusQueryOptions
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
Options for querying the version control system status of a file.
Additional resources: [AssetDatabase.IsOpenForEdit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.IsOpenForEdit.html), [AssetDatabase.IsMetaFileOpenForEdit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.IsMetaFileOpenForEdit.html).
### Properties
Property | Description  
---|---  
[ForceUpdate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StatusQueryOptions.ForceUpdate.html) | Force a refresh of the version control system status of the file. This is slow but accurate.  
[UseCachedIfPossible](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StatusQueryOptions.UseCachedIfPossible.html) | This option sets the status query to first use the latest valid version control system status of the file and query for a valid status synchronously if otherwise.  
[UseCachedAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StatusQueryOptions.UseCachedAsync.html) | This option sets the status query to first use the latest valid version control system status of the file and query for a valid status asynchronously if otherwise.  
* * *
