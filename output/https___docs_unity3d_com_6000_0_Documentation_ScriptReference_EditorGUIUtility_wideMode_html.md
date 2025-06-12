* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility-wideMode.html

#  [EditorGUIUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.html).wideMode
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
wideMode; 
### Description
Is the Editor GUI currently in wide mode?
Wide mode is a mode for Editor GUI where the controls for structs such as Vector3 and Rect are inlined so they take up less vertical space. For example, in wide mode a Vector3Field takes up one line height instead of two, and a RectField takes up two line heights instead of three.  
  
When creating your own multi-line controls, you can query wideMode and make the layout of your control follow the same logic.
* * *
