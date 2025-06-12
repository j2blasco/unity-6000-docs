* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.RegisterRenderPickingCallback.html

#  [HandleUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.html).RegisterRenderPickingCallback
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
public static bool RegisterRenderPickingCallback([HandleUtility.RenderPickingCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.RenderPickingCallback.html) renderPickingCallback); 
### Parameters
Parameter | Description  
---|---  
renderPickingCallback | The delegate object to register to the callback.  
### Returns
**bool** True if the registration succeeds. False if the callback is already registered. 
### Description
Registers a callback to invoke when Unity renders for picking.
Use this callback to render custom geometries on top of the existing scene objects to the picking render texture, so that the GameObjects represented by custom geometries can be picked.  
  
Each rendering must write out a [Vector4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html)-typed `selectionId` to the picking render texture. The `selectionId` is encoded from the [pickingIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderPickingArgs-pickingIndex.html) passed into the callback through the [RenderPickingArgs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderPickingArgs.html) struct using the function [HandleUtility.EncodeSelectionId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.EncodeSelectionId.html). You can render multiple SelectionIds in one callback if they are encoded sequentially from incrementing the `pickingIndex`, and you return the total number of rendered picking indices when returning from the callback.  
  
Most Unity shaders have a "ScenePickingPass" pass that can be used for the rendering. Use [Material.FindPass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.FindPass.html) with the pass name "ScenePickingPass" to find the index of the shader pass from a [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html), and use this pass index when you call APIs such as [Material.SetPass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.SetPass.html). Note that you can only use render functions that are considered to take effect immediately, such as [Graphics.DrawMeshNow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.DrawMeshNow.html) and [Graphics.DrawProceduralNow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.DrawProceduralNow.html) (instead of their non-immediate counterparts [Graphics.DrawMesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.DrawMesh.html) and [Graphics.DrawProcedural](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.DrawProcedural.html)). The alternative is to record your rendering to a [CommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.html) object, and call [Graphics.ExecuteCommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.ExecuteCommandBuffer.html) after the recording.  
  
The picking render texture has already been bound as the active render texture when it entered the callback. You can change the active render texture during the callback, but you must restore the active render texture before exiting the callback.  
  
Your rendering must respect the ignore and filter GameObject sets passed to the callback through the [RenderPickingArgs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderPickingArgs.html) struct argument to determine under the current context what should be rendered. Refer to [RenderPickingArgs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderPickingArgs.html) for more information.  
  
After rendering, return a [RenderPickingResult](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderPickingResult.html) struct with the number of picking indices you used, and another callback function to invoke to resolve the picking index to a GameObject reference to be selected once the user ends up clicking on the rendered pixel under the mouse. If nothing needs to render, you can return the struct with [renderedPickingIndexCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderPickingResult-renderedPickingIndexCount.html) being 0, or simply [RenderPickingResult.NoOperation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderPickingResult.NoOperation.html). Refer to [RenderPickingResult](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderPickingResult.html) for more information.  
  
The method throws `InvalidOperationException` if you try to call it inside render picking callbacks.  
  
Additional resources: [UnregisterRenderPickingCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.UnregisterRenderPickingCallback.html).
* * *
