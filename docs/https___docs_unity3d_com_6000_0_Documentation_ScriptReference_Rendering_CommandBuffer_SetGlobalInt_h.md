* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.SetGlobalInt.html

#  [CommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.html).SetGlobalInt
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
public void SetGlobalInt(string name, int value); 
## Declaration
public void SetGlobalInt(int nameID, int value); 
### Description
Adds a command to set the value of a given property for all Shaders, where the property has a type of `Int` in ShaderLab code.
When Unity executes the CommandBuffer, it sets the value of the given property for all Shaders. Internally, the shader property types `Float` and `Int` are treated exactly the same; therefore, this function is an alias to [SetGlobalFloat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.SetGlobalFloat.html).  
  
For properties that use the ShaderLab type `Integer`, which are internally represented as integers, use [SetGlobalInteger](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.SetGlobalInteger.html).
* * *
