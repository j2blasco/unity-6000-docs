* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.CanCacheInspectorGUI.html

**Method group is Obsolete**   

#  [EditorGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.html).CanCacheInspectorGUI
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
**Obsolete** CanCacheInspectorGUI has been deprecated and is no longer used.
## Declaration
public static bool CanCacheInspectorGUI([SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) property); 
### Parameters
Parameter | Description  
---|---  
property | The [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) in question.  
### Returns
**bool** Whether the property's inspector GUI can be cached. 
### Description
Get whether a [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html)'s inspector GUI can be cached.
For builtin EditorGUI controls, this is always true. If the property has a custom PropertyDrawer, the function will return the cacheability value returned by that drawer.
* * *
