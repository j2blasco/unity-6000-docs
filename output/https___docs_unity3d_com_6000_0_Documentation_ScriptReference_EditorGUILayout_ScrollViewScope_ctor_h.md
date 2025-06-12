* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.ScrollViewScope-ctor.html

# EditorGUILayout.ScrollViewScope Constructor
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
public EditorGUILayout.ScrollViewScope([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) scrollPosition, params GUILayoutOption[] options); 
## Declaration
public EditorGUILayout.ScrollViewScope([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) scrollPosition, bool alwaysShowHorizontal, bool alwaysShowVertical, params GUILayoutOption[] options); 
## Declaration
public EditorGUILayout.ScrollViewScope([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) scrollPosition, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) horizontalScrollbar, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) verticalScrollbar, params GUILayoutOption[] options); 
## Declaration
public EditorGUILayout.ScrollViewScope([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) scrollPosition, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style, params GUILayoutOption[] options); 
## Declaration
public EditorGUILayout.ScrollViewScope([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) scrollPosition, bool alwaysShowHorizontal, bool alwaysShowVertical, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) horizontalScrollbar, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) verticalScrollbar, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) background, params GUILayoutOption[] options); 
### Parameters
Parameter | Description  
---|---  
scrollPosition | The scroll position to use.  
alwaysShowHorizontal | Whether to always show the horizontal scrollbar. If false, it is only shown when the content inside the ScrollView is wider than the scrollview itself.  
alwaysShowVertical | Whether to always show the vertical scrollbar. If false, it is only shown when the content inside the ScrollView is higher than the scrollview itself.  
horizontalScrollbar | Optional [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) to use for the horizontal scrollbar. If left out, the `horizontalScrollbar` style from the current [GUISkin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUISkin.html) is used.  
verticalScrollbar | Optional [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) to use for the vertical scrollbar. If left out, the `verticalScrollbar` style from the current [GUISkin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUISkin.html) is used.  
### Description
Create a new ScrollViewScope and begin the corresponding ScrollView.
* * *
