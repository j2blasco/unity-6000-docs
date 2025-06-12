* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchUtils.CreateSceneResult.html

#  [SearchUtils](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchUtils.html).CreateSceneResult
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
public static [Search.SearchItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html) CreateSceneResult([Search.SearchContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html) context, [Search.SearchProvider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider.html) sceneProvider, [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) go); 
### Parameters
Parameter | Description  
---|---  
context | Search context used to yield this item.  
sceneProvider | Source search provider. Can be the scene provider obtained with [SearchService.GetProvider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.GetProvider.html) using the id "scene".  
go | Scene game object instance to create the new search item.  
### Returns
**SearchItem** Scene search item that can be yielded by your custom provider. 
### Description
Creates a search item compatible with the scene provider.
* * *
