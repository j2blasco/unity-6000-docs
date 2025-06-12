* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.TrIconContent.html

#  [EditorGUIUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.html).TrIconContent
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
public static [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) TrIconContent(string iconName, string tooltip); 
## Declaration
public static [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) TrIconContent([Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) icon, string tooltip); 
### Parameters
Parameter | Description  
---|---  
iconName | The name of the icon.  
tooltip | The tooltip to display when the cursor hovers over the icon.  
icon | The icon to associate with the [GUIContent.image](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent-image.html).  
### Description
Gets the [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) from Unity built-in resources with the given information or creates a [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) for a GUI element.  
  
The icon is loaded with a localized tooltip.   
  
Typically, the icon from `Assets/Editor Default Resources/Icons` is fetched using the icon name. Only the name of the icon, without the .png extension is needed.
* * *
