* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchRendererGroup.html

# BatchRendererGroup
class in UnityEngine.Rendering
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
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
A `BatchRendererGroup` is an object that lets you perform customizable high performance rendering.
You can set up batches in advance to set up groups of instances with shared metadata values that describe how to load Material properties. Whenever Unity renders a `BatchRendererGroup`, it invokes the `OnPerformCulling` callback to perform visibility culling and to generate a variable sized list of draw commands that describe how to render the visible parts of the `BatchRendererGroup`. Each draw command instructs Unity to render a group of instances from a given batch with a specific Mesh and Material.
### Static Properties
Property | Description  
---|---  
[BufferTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchRendererGroup.BufferTarget.html) | The buffer target BatchRendererGroup.AddBatch accepts for the active graphics API.  
### Constructors
Constructor | Description  
---|---  
[BatchRendererGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchRendererGroup-ctor.html) | Constructor for a BatchRendererGroup object.  
### Public Methods
Method | Description  
---|---  
[AddBatch](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchRendererGroup.AddBatch.html) | Create a draw command batch that shares a single set of metadata values and a single GraphicsBuffer.  
[Dispose](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchRendererGroup.Dispose.html) | Deletes a group.  
[GetRegisteredMaterial](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchRendererGroup.GetRegisteredMaterial.html) | Returns the previously registered Material associated with this MaterialID.  
[GetRegisteredMesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchRendererGroup.GetRegisteredMesh.html) | Returns the previously registered Mesh associated with this MeshID.  
[GetThreadedBatchContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchRendererGroup.GetThreadedBatchContext.html) | Get the thread-safe API for interacting with a BatchRendererGroup from Burst jobs.  
[RegisterMaterial](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchRendererGroup.RegisterMaterial.html) | Registers a Material in BatchRendererGroup and returns its BatchMaterialID. Each registration of a specific Material increases its number of owners by 1.  
[RegisterMesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchRendererGroup.RegisterMesh.html) | Registers a mesh in BatchRendererGroup and returns its BatchMeshID. Each registration of a specific mesh increases its number of owners by 1.  
[RemoveBatch](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchRendererGroup.RemoveBatch.html) | Delete a batch that was previously created with AddBatch.  
[SetBatchBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchRendererGroup.SetBatchBuffer.html) | Change the GraphicsBuffer associated with the given batch.  
[SetEnabledViewTypes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchRendererGroup.SetEnabledViewTypes.html) | Set the combination of BatchCullingViewType for which this BatchRendererGroup should receive an OnPerformCulling callback.  
[SetErrorMaterial](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchRendererGroup.SetErrorMaterial.html) | Set the error material for the BatchRendererGroup. This material will be used internally by Unity to render the draw commands referring to erroneous shaders. You can also pass 'null' to this method to unset the material.  
[SetGlobalBounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchRendererGroup.SetGlobalBounds.html) | Set the bounds of the BatchRendererGroup. The bounds should encapsulate the render bounds of every object rendered with this BatchRendererGroup. Unity uses these bounds internally for culling.  
[SetLoadingMaterial](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchRendererGroup.SetLoadingMaterial.html) | Set the loading material for the BatchRendererGroup.  
[SetPickingMaterial](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchRendererGroup.SetPickingMaterial.html) | Set the material that Unity uses to render object picking data using the draw commands in the Scene view.  
[UnregisterMaterial](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchRendererGroup.UnregisterMaterial.html) | Unregister the Material ID associated with BatchRendererGroup. Each deregistration of a specific Material reduces its number of owners by 1.  
[UnregisterMesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchRendererGroup.UnregisterMesh.html) | Unregister the mesh ID associated with BatchRendererGroup. Each deregistration of a specific mesh reduces its number of owners by 1.  
### Static Methods
Method | Description  
---|---  
[GetConstantBufferMaxWindowSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchRendererGroup.GetConstantBufferMaxWindowSize.html) | Defines the maxiumum amount (in bytes) the BatchRendererGroup constant buffer window size is visible from the shader.  
[GetConstantBufferOffsetAlignment](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchRendererGroup.GetConstantBufferOffsetAlignment.html) |   
### Delegates
Delegate | Description  
---|---  
[OnFinishedCulling](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchRendererGroup.OnFinishedCulling.html) | Finished culling callback function.  
[OnPerformCulling](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchRendererGroup.OnPerformCulling.html) | Culling callback function.  
* * *
