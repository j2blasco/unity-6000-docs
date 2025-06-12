* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility-singleLineHeight.html

#  [EditorGUIUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.html).singleLineHeight
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
singleLineHeight; 
### Description
Get the height used for a single Editor control such as a one-line EditorGUI.TextField or EditorGUI.Popup.
When creating your own multi-line controls, such as controls for custom classes with multiple fields, you can use [EditorGUILayout.GetControlRect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.GetControlRect.html) and pass in a height value that is a multiple of [EditorGUIUtility.singleLineHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility-singleLineHeight.html). This is advisable over hardcoding specific pixel values. Additional resources: [EditorGUILayout.GetControlRect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.GetControlRect.html).
* * *
