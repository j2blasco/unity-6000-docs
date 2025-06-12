* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchUtils.GetObjectPath.html

#  [SearchUtils](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchUtils.html).GetObjectPath
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
public static string GetObjectPath([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) obj); 
### Parameters
Parameter | Description  
---|---  
obj | Object to obtain a path from.  
### Returns
**string** Returns the path of an object. 
### Description
Get the path of a Unity Object. If it is a GameObject or a Component it is the <see cref="SearchUtils.GetTransformPath(Transform)"/>. Else it is the asset name.
* * *
