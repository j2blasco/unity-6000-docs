* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.PropertyScope-ctor.html

# EditorGUI.PropertyScope Constructor
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
public EditorGUI.PropertyScope([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) totalPosition, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) property); 
### Parameters
Parameter | Description  
---|---  
totalPosition | Rectangle on the screen to use for the control, including label if applicable.  
label | Label in front of the slider. Use null to use the name from the SerializedProperty. Use GUIContent.none to not display a label.  
property | The SerializedProperty to use for the control.  
### Description
Create a new PropertyScope and begin the corresponding property.
* * *
