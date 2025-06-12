* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.TrTextContent.html

#  [EditorGUIUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.html).TrTextContent
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
public static [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) TrTextContent(string key, string text, string tooltip, [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) icon); 
## Declaration
public static [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) TrTextContent(string text, string tooltip, [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) icon); 
## Declaration
public static [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) TrTextContent(string text, string tooltip, string iconName); 
## Declaration
public static [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) TrTextContent(string text, [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) icon); 
### Parameters
Parameter | Description  
---|---  
key | The key of the existing [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html).  
text | The text associated with the [GUIContent.text](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent-text.html).  
tooltip | The tooltip to display when the cursor hovers over the icon.  
icon | The icon to associate with the [GUIContent.image](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent-image.html).  
iconName | The name of the icon.  
### Description
Gets the [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) from the Unity built-in resources with the given key or creates a [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) for a GUI element.  
  
The text and the tooltip are localized and loaded with an icon.  
  
Typically, the icon from `Assets/Editor Default Resources/Icons` is fetched using the icon name. Only the name of the icon, without the .png extension is needed.
* * *
