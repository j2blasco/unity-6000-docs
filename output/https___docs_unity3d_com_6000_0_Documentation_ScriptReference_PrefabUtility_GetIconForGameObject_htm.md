* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.GetIconForGameObject.html

#  [PrefabUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.html).GetIconForGameObject
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
public static [Texture2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) GetIconForGameObject([GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) gameObject); 
### Parameters
Parameter | Description  
---|---  
gameObject | The GameObject to get an icon for.  
### Returns
**Texture2D** The icon for the GameObject. 
### Description
Retrieves the icon for the given GameObject.
This method returns the icon for the GameObject, as it appears in the Hierarchy or Project Browser. Prefab instance or Asset roots have a Prefab, Prefab Mode, or Prefab Variant icon, while other GameObjects have a regular GameObject icon.
* * *
