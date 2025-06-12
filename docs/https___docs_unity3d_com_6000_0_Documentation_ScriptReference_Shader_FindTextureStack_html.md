* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.FindTextureStack.html

#  [Shader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html).FindTextureStack
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Shader.html "Go to Shader Component in the Manual")
## Declaration
public bool FindTextureStack(int propertyIndex, out string stackName, out int layerIndex); 
### Parameters
Parameter | Description  
---|---  
propertyIndex | Index of the property.  
stackName | On exit, contanis the name of the stack if one was found.  
layerIndex | On exit, contains the stack layer index of the texture property.  
### Returns
**bool** True, if a stack was found for the given texture property, false if not. 
### Description
Find the name of a texture stack a texture belongs too.
* * *
