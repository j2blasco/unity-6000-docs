* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ResourcesAPI.LoadAsync.html

#  [ResourcesAPI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ResourcesAPI.html).LoadAsync
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
protected [ResourceRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ResourceRequest.html) LoadAsync(string path, Type systemTypeInstance); 
### Parameters
Parameter | Description  
---|---  
path | Path to the target resource to load.  
systemTypeInstance | Type filter for objects returned.  
### Description
Override for customizing the behavior of the [Resources.LoadAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.LoadAsync.html) function.
Note: [AssetBundleRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundleRequest.html) inherits from [ResourceRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ResourceRequest.html) and can also be returned here.
* * *
