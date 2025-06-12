* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderPickingArgs-pickingIndex.html

#  [RenderPickingArgs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderPickingArgs.html).pickingIndex
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
pickingIndex; 
### Description
Specifies the picking index value that the first pickable object uses to write to the picking render texture.
The picking index must be encoded to a [Vector4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html) `selectionId` value that uses [HandleUtility.EncodeSelectionId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.EncodeSelectionId.html), and output from the shader. If you are rendering more than one pickable object in the callback, increment the `pickingIndex` for every additional object.  
  
Additional resources: [HandleUtility.EncodeSelectionId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.EncodeSelectionId.html).
* * *
