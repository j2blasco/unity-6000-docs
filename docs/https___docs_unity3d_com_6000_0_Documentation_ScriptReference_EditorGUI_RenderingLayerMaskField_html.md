* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.RenderingLayerMaskField.html

#  [EditorGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.html).RenderingLayerMaskField
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
public static void RenderingLayerMaskField([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, string label, [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) property); 
## Declaration
public static void RenderingLayerMaskField([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) property); 
### Parameters
Parameter | Description  
---|---  
position | Rectangle on the screen to use for field.  
label | Optional label in front of the field.  
property | Serialized property which contains [RenderingLayerMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderingLayerMask.html) struct.  
### Description
Makes a rendering layer selection field.
* * *
## Declaration
public static [RenderingLayerMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderingLayerMask.html) RenderingLayerMaskField([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, string label, [RenderingLayerMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderingLayerMask.html) layers); 
## Declaration
public static [RenderingLayerMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderingLayerMask.html) RenderingLayerMaskField([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, string label, [RenderingLayerMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderingLayerMask.html) layers, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style); 
## Declaration
public static [RenderingLayerMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderingLayerMask.html) RenderingLayerMaskField([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, [RenderingLayerMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderingLayerMask.html) layers); 
## Declaration
public static [RenderingLayerMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderingLayerMask.html) RenderingLayerMaskField([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, [RenderingLayerMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderingLayerMask.html) layers, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style); 
### Parameters
Parameter | Description  
---|---  
position | Rectangle on the screen to use for field.  
label | Optional label in front of the field.  
layers | Value which represents [RenderingLayerMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderingLayerMask.html).  
style | Optional [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html).  
### Returns
**RenderingLayerMask** The Rendering Layer selected by the User. 
### Description
Makes a rendering layer selection field.
* * *
