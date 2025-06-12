* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.LoadAsync.html

#  [Resources](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.html).LoadAsync
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
public static [ResourceRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ResourceRequest.html) LoadAsync(string path); 
## Declaration
public static [ResourceRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ResourceRequest.html) LoadAsync(string path, Type type); 
### Parameters
Parameter | Description  
---|---  
path | Pathname of the target folder. When using the empty string (i.e., ""), the function will load the entire contents of the Resources folder.  
systemTypeInstance | Type filter for objects returned.  
### Description
Asynchronously loads an asset stored at `path` in a Resources folder.
Returns a ResourceRequest, from which the asset can be retrieved once the loading operation is completed. Only objects of type will be returned if this parameter is supplied. The path is relative to any Resources folder inside the Assets folder of your project, extensions must be omitted.  
  
**Note:** All asset names and paths in Unity use forward slashes. Paths using backslashes will **not** work.
* * *
## Declaration
public static [ResourceRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ResourceRequest.html) LoadAsync(string path); 
### Parameters
Parameter | Description  
---|---  
path | Pathname of the target folder. When using the empty string (i.e., ""), the function will load the entire contents of the Resources folder.  
### Description
Asynchronously loads an asset stored at `path` in a Resources folder.
Returns a ResourceRequest, from which the asset can be retrieved once the loading operation is completed. Only objects of type `T` will be returned. The `path` is relative to any Resources folder inside the Assets folder of your project, extensions must be omitted.  
  
**Note:** All asset names and paths in Unity use forward slashes. Paths using backslashes will **not** work.
* * *
