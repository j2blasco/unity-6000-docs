* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.ToObject.html

#  [SearchItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html).ToObject
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
public Object ToObject(); 
## Declaration
public Object ToObject(Type type); 
### Parameters
Parameter | Description  
---|---  
type | Used to validate if the object is assignable to Type.  
### Returns
**Object** Returns a Unity Object or null if there is none. 
### Description
Returns any valid Unity Object held by the search item.
See [SearchProvider.toObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider-toObject.html) more information on what it means to convert a SearchItem to a UnityEngine.Object.
* * *
## Declaration
public T ToObject(); 
### Returns
**T** Used to validate if the object is assignable to T. 
### Description
Returns any valid Unity Object held by the search item.
* * *
