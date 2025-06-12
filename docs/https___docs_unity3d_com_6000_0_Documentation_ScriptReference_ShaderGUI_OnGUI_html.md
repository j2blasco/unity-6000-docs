* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderGUI.OnGUI.html

#  [ShaderGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderGUI.html).OnGUI
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
public void OnGUI([MaterialEditor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.html) materialEditor, MaterialProperty[] properties); 
### Parameters
Parameter | Description  
---|---  
materialEditor | The MaterialEditor that are calling this OnGUI (the 'owner').  
properties | Material properties of the current selected shader.  
### Description
To define a custom shader GUI use the methods of **materialEditor** to render controls for the **properties** array.
* * *
