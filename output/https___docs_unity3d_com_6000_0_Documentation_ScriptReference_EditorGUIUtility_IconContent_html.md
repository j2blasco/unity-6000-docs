* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.IconContent.html

#  [EditorGUIUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.html).IconContent
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
public static [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) IconContent(string name, string text = null); 
### Parameters
Parameter | Description  
---|---  
name | Name of the desired icon.  
text | Tooltip for hovering over the icon.  
### Description
Fetch the [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) from the Unity builtin resources with the given name.
[EditorGUIUtility.IconContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.IconContent.html) is used to create a [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) for a GUI element. Only icons are loaded. Typically the icon from `Assets/Editor Default Resources/Icons` is fetched using the first argument. Only the name of the icon, without the png extension is needed.  
  
The second argument provides the text for a hovering tooltip. This string needs to start with a vertical bar "**|** " character to flag it as a tooltip.  
  
**Note:** The hovering over the tooltip cannot currently be positioned. 
* * *
