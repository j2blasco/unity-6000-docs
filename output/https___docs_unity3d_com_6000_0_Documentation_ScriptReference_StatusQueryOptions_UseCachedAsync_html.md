* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StatusQueryOptions.UseCachedAsync.html

#  [StatusQueryOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StatusQueryOptions.html).UseCachedAsync
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
This option sets the status query to first use the latest valid version control system status of the file and query for a valid status asynchronously if otherwise.
Note that [AssetDatabase.IsOpenForEdit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.IsOpenForEdit.html) and [AssetDatabase.IsMetaFileOpenForEdit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.IsMetaFileOpenForEdit.html) returns false while a query is in progress as the VCS status is still unknown.  
  
Additional resources: [AssetDatabase.IsOpenForEdit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.IsOpenForEdit.html), [AssetDatabase.IsMetaFileOpenForEdit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.IsMetaFileOpenForEdit.html).
* * *
