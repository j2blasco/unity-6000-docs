* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderGUI.ValidateMaterial.html

#  [ShaderGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderGUI.html).ValidateMaterial
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
public void ValidateMaterial([Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) material); 
### Parameters
Parameter | Description  
---|---  
material | The material to validate.  
### Description
When the user loads a Material using this ShaderGUI into memory or changes a value in the Inspector, the Editor calls this method.
Use this method to ensure that when you import a Material or modify material properties in an Inspector, keywords and passes are enabled or disabled accordingly.
* * *
