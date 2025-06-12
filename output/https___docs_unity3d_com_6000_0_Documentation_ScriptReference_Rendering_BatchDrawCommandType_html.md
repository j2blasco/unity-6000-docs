* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchDrawCommandType.html

# BatchDrawCommandType
enumeration
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
### Description
Enumerates the different draw command types a [BatchRendererGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchRendererGroup.html) can draw.
This is used in [BatchDrawRange](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchDrawRange.html) to say from what draw command stream the batch will read the commands.
### Properties
Property | Description  
---|---  
[Direct](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchDrawCommandType.Direct.html) | A direct draw command with a mesh and material.  
[Indirect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchDrawCommandType.Indirect.html) | An indirect draw command with a mesh and material.  
[Procedural](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchDrawCommandType.Procedural.html) | A procedural draw command. Has a material but vertex data is procedurally fetched by the shader.  
[ProceduralIndirect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchDrawCommandType.ProceduralIndirect.html) | A procedural indirect draw command. Has a material but vertex data is procedurally fetched by the shader.  
* * *
