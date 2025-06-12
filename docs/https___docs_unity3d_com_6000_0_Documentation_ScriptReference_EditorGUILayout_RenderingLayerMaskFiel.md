* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.RenderingLayerMaskField.html

#  [EditorGUILayout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.html).RenderingLayerMaskField
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
public static [RenderingLayerMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderingLayerMask.html) RenderingLayerMaskField(string label, [RenderingLayerMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderingLayerMask.html) layers, params GUILayoutOption[] options); 
## Declaration
public static [RenderingLayerMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderingLayerMask.html) RenderingLayerMaskField(string label, [RenderingLayerMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderingLayerMask.html) layers, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style, params GUILayoutOption[] options); 
## Declaration
public static [RenderingLayerMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderingLayerMask.html) RenderingLayerMaskField([GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, [RenderingLayerMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderingLayerMask.html) layers, params GUILayoutOption[] options); 
## Declaration
public static [RenderingLayerMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderingLayerMask.html) RenderingLayerMaskField([GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, [RenderingLayerMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderingLayerMask.html) layers, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style, params GUILayoutOption[] options); 
### Parameters
Parameter | Description  
---|---  
label | Optional label in front of the field.  
layers | The layer shown in the field.  
style | Optional [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html).  
options | An optional list of layout options that specify extra layout properties. Any values passed in here will override settings defined by the `style`.  
Additional resources: [GUILayout.Width](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Width.html), [GUILayout.Height](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Height.html), [GUILayout.MinWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MinWidth.html), [GUILayout.MaxWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MaxWidth.html), [GUILayout.MinHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MinHeight.html), [GUILayout.MaxHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MaxHeight.html), [GUILayout.ExpandWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.ExpandWidth.html), [GUILayout.ExpandHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.ExpandHeight.html).  
### Returns
**RenderingLayerMask** The Rendering Layer selected by the User. 
### Description
Makes a layer selection field.
* * *
## Declaration
public static uint RenderingLayerMaskField(string label, uint layers, params GUILayoutOption[] options); 
## Declaration
public static uint RenderingLayerMaskField(string label, uint layers, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style, params GUILayoutOption[] options); 
## Declaration
public static uint RenderingLayerMaskField([GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, uint layers, params GUILayoutOption[] options); 
## Declaration
public static uint RenderingLayerMaskField([GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, uint layers, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style, params GUILayoutOption[] options); 
### Parameters
Parameter | Description  
---|---  
label | Optional label in front of the field.  
layers | Value which represents [RenderingLayerMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderingLayerMask.html).  
style | Optional [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html).  
options | An optional list of layout options that specify extra layout properties. Any values passed in here will override settings defined by the `style`.  
Additional resources: [GUILayout.Width](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Width.html), [GUILayout.Height](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Height.html), [GUILayout.MinWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MinWidth.html), [GUILayout.MaxWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MaxWidth.html), [GUILayout.MinHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MinHeight.html), [GUILayout.MaxHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MaxHeight.html), [GUILayout.ExpandWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.ExpandWidth.html), [GUILayout.ExpandHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.ExpandHeight.html).  
### Returns
**uint** The Rendering Layer selected by the User and returned as uint. 
### Description
Makes a layer selection field.
* * *
## Declaration
public static void RenderingLayerMaskField([GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) property, params GUILayoutOption[] options); 
### Parameters
Parameter | Description  
---|---  
label | Optional label in front of the field.  
property | Serialized property which contains [RenderingLayerMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderingLayerMask.html) struct.  
options | An optional list of layout options that specify extra layout properties. Any values passed in here will override settings defined by the `style`.  
Additional resources: [GUILayout.Width](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Width.html), [GUILayout.Height](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Height.html), [GUILayout.MinWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MinWidth.html), [GUILayout.MaxWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MaxWidth.html), [GUILayout.MinHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MinHeight.html), [GUILayout.MaxHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MaxHeight.html), [GUILayout.ExpandWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.ExpandWidth.html), [GUILayout.ExpandHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.ExpandHeight.html).  
### Description
Makes a layer selection field.
* * *
