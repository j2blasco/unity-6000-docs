* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.TextureCompatibilityWarning.html

#  [MaterialEditor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.html).TextureCompatibilityWarning
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
public void TextureCompatibilityWarning([MaterialProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialProperty.html) prop); 
### Parameters
Parameter | Description  
---|---  
prop | The texture property to check and display warning for, if necessary.  
### Description
Checks if particular property has incorrect type of texture specified by the material, displays appropriate warning and suggests the user to automatically fix the problem.
The warning box is shown using GUILayout so it is recommended to call this method right after the property.
* * *
