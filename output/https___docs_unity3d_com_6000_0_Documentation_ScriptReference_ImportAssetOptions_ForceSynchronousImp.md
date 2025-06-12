* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ImportAssetOptions.ForceSynchronousImport.html

#  [ImportAssetOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ImportAssetOptions.html).ForceSynchronousImport
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
Import all assets synchronously.
By default some assets can be imported asynchronously (e.g. scripts can be compiled in the background). In some cases all importing needs to be synchronous; use this flag then. For example, when importing a scripts + prefabs, scripts have to be fully compiled before Prefab is serialized, otherwise it might get old variables.  
  
Additional resources: [AssetDatabase.ImportAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.ImportAsset.html), [AssetDatabase.Refresh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.Refresh.html).
* * *
