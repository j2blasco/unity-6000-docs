* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CanvasRenderer.html

# CanvasRenderer
class in UnityEngine
/
Inherits from:[Component](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.html)
/
Implemented in:[UnityEngine.UIModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.UIModule.html)
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
A component that will render to the screen after all normal rendering has completed when attached to a [Canvas](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Canvas.html). Designed for GUI application.
Additional resources:[Canvas](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Canvas.html).
### Properties
Property | Description  
---|---  
[absoluteDepth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CanvasRenderer-absoluteDepth.html) | Depth of the renderer relative to the root canvas.  
[clippingSoftness](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CanvasRenderer-clippingSoftness.html) | The clipping softness to apply to the renderer.  
[cull](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CanvasRenderer-cull.html) | Indicates whether geometry emitted by this renderer is ignored.  
[cullTransparentMesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CanvasRenderer-cullTransparentMesh.html) | Indicates whether geometry emitted by this renderer can be ignored when the vertex color alpha is close to zero for every vertex of the mesh.  
[hasMoved](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CanvasRenderer-hasMoved.html) | True if any change has occured that would invalidate the positions of generated geometry.  
[hasPopInstruction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CanvasRenderer-hasPopInstruction.html) | Enable 'render stack' pop draw call.  
[hasRectClipping](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CanvasRenderer-hasRectClipping.html) | True if rect clipping has been enabled on this renderer. Additional resources: CanvasRenderer.EnableRectClipping, CanvasRenderer.DisableRectClipping.  
[materialCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CanvasRenderer-materialCount.html) | The number of materials usable by this renderer.  
[popMaterialCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CanvasRenderer-popMaterialCount.html) | The number of materials usable by this renderer. Used internally for masking.  
[relativeDepth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CanvasRenderer-relativeDepth.html) | Depth of the renderer realative to the parent canvas.  
### Public Methods
Method | Description  
---|---  
[Clear](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CanvasRenderer.Clear.html) | Remove all cached vertices.  
[DisableRectClipping](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CanvasRenderer.DisableRectClipping.html) | Disables rectangle clipping for this CanvasRenderer.  
[EnableRectClipping](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CanvasRenderer.EnableRectClipping.html) | Enables rect clipping on the CanvasRendered. Geometry outside of the specified rect will be clipped (not rendered).  
[GetAlpha](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CanvasRenderer.GetAlpha.html) | Get the current alpha of the renderer.  
[GetColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CanvasRenderer.GetColor.html) | Get the current color of the renderer.  
[GetInheritedAlpha](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CanvasRenderer.GetInheritedAlpha.html) | Get the final inherited alpha calculated by including all the parent alphas from included parent CanvasGroups.  
[GetMaterial](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CanvasRenderer.GetMaterial.html) | Gets the current Material assigned to the CanvasRenderer.  
[GetMesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CanvasRenderer.GetMesh.html) | Returns the current mesh used to render the canvas content into.  
[GetPopMaterial](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CanvasRenderer.GetPopMaterial.html) | Gets the current Material assigned to the CanvasRenderer. Used internally for masking.  
[SetAlpha](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CanvasRenderer.SetAlpha.html) | Set the alpha of the renderer. Will be multiplied with the UIVertex alpha and the Canvas alpha.  
[SetAlphaTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CanvasRenderer.SetAlphaTexture.html) | The Alpha Texture that will be passed to the Shader under the _AlphaTex property.  
[SetColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CanvasRenderer.SetColor.html) | Set the color of the renderer. Will be multiplied with the UIVertex color and the Canvas color.  
[SetMaterial](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CanvasRenderer.SetMaterial.html) | Set the material for the canvas renderer. If a texture is specified then it will be used as the 'MainTex' instead of the material's 'MainTex'. Additional resources: CanvasRenderer.materialCount, CanvasRenderer.SetTexture.  
[SetMesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CanvasRenderer.SetMesh.html) | Sets the Mesh used by this renderer. Note the Mesh must be read/write enabled.  
[SetPopMaterial](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CanvasRenderer.SetPopMaterial.html) | Set the material for the canvas renderer. Used internally for masking.  
[SetTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CanvasRenderer.SetTexture.html) | Sets the texture used by this renderer's material.  
### Static Methods
Method | Description  
---|---  
[AddUIVertexStream](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CanvasRenderer.AddUIVertexStream.html) | Take the Vertex stream and split it corrisponding arrays (positions, colors, uv0s, uv1s, normals and tangents).  
[CreateUIVertexStream](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CanvasRenderer.CreateUIVertexStream.html) | Convert a set of vertex components into a stream of UIVertex.  
[SplitUIVertexStreams](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CanvasRenderer.SplitUIVertexStreams.html) | Given a list of UIVertex, split the stream into it's component types.  
### Events
Event | Description  
---|---  
[onRequestRebuild](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CanvasRenderer-onRequestRebuild.html) | (Editor Only) Event that gets fired whenever the data in the CanvasRenderer gets invalidated and needs to be rebuilt.  
### Inherited Members
### Properties
Property | Description  
---|---  
[gameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component-gameObject.html) | The game object this component is attached to. A component is always attached to a game object.  
[tag](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component-tag.html) | The tag of this game object.  
[transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component-transform.html) | The Transform attached to this GameObject.  
[hideFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-hideFlags.html) | Should the object be hidden, saved with the Scene or modifiable by the user?  
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-name.html) | The name of the object.  
### Public Methods
Method | Description  
---|---  
[BroadcastMessage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.BroadcastMessage.html) | Calls the method named methodName on every MonoBehaviour in this game object or any of its children.  
[CompareTag](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.CompareTag.html) | Checks the GameObject's tag against the defined tag.  
[GetComponent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponent.html) | Gets a reference to a component of type T on the same GameObject as the component specified.  
[GetComponentInChildren](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponentInChildren.html) | Gets a reference to a component of type T on the same GameObject as the component specified, or any child of the GameObject.  
[GetComponentIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponentIndex.html) | Gets the index of the component on its parent GameObject.  
[GetComponentInParent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponentInParent.html) | Gets a reference to a component of type T on the same GameObject as the component specified, or any parent of the GameObject.  
[GetComponents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponents.html) | Gets references to all components of type T on the same GameObject as the component specified.  
[GetComponentsInChildren](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponentsInChildren.html) | Gets references to all components of type T on the same GameObject as the component specified, and any child of the GameObject.  
[GetComponentsInParent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponentsInParent.html) | Gets references to all components of type T on the same GameObject as the component specified, and any parent of the GameObject.  
[SendMessage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.SendMessage.html) | Calls the method named methodName on every MonoBehaviour in this game object.  
[SendMessageUpwards](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.SendMessageUpwards.html) | Calls the method named methodName on every MonoBehaviour in this game object and on every ancestor of the behaviour.  
[TryGetComponent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.TryGetComponent.html) | Gets the component of the specified type, if it exists.  
[GetInstanceID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.GetInstanceID.html) | Gets the instance ID of the object.  
[ToString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.ToString.html) | Returns the name of the object.  
### Static Methods
Method | Description  
---|---  
[Destroy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.Destroy.html) | Removes a GameObject, component or asset.  
[DestroyImmediate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.DestroyImmediate.html) | Destroys the object obj immediately. You are strongly recommended to use Destroy instead.  
[DontDestroyOnLoad](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.DontDestroyOnLoad.html) | Do not destroy the target Object when loading a new Scene.  
[FindAnyObjectByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindAnyObjectByType.html) | Retrieves any active loaded object of Type type.  
[FindFirstObjectByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindFirstObjectByType.html) | Retrieves the first active loaded object of Type type.  
[FindObjectsByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindObjectsByType.html) | Retrieves a list of all loaded objects of Type type.  
[Instantiate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.Instantiate.html) | Clones the object original and returns the clone.  
[InstantiateAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.InstantiateAsync.html) | Captures a snapshot of the original object (that must be related to some GameObject) and returns the AsyncInstantiateOperation.  
### Operators
Operator | Description  
---|---  
[bool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_Object.html) | Does the object exist?  
[operator !=](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_ne.html) | Compares if two objects refer to a different object.  
[operator ==](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_eq.html) | Compares two object references to see if they refer to the same object.  
* * *
