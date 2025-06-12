* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer.html

# ParticleSystemRenderer
class in UnityEngine
/
Inherits from:[Renderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html)
/
Implemented in:[UnityEngine.ParticleSystemModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.ParticleSystemModule.html)
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
Use this class to render particles on to the screen.
### Properties
Property | Description  
---|---  
[activeTrailVertexStreamsCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer-activeTrailVertexStreamsCount.html) | The number of currently active custom trail vertex streams.  
[activeVertexStreamsCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer-activeVertexStreamsCount.html) | The number of currently active custom vertex streams.  
[alignment](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer-alignment.html) | Control the direction that particles face.  
[allowRoll](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer-allowRoll.html) | Allow billboard particles to roll around their z-axis.  
[cameraVelocityScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer-cameraVelocityScale.html) | How much do the particles stretch depending on the Camera's speed.  
[enableGPUInstancing](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer-enableGPUInstancing.html) | Enables GPU Instancing on platforms that support it.  
[flip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer-flip.html) | Flip a percentage of the particles, along each axis.  
[freeformStretching](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer-freeformStretching.html) | Enables freeform stretching behavior.  
[lengthScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer-lengthScale.html) | How much are the particles stretched in their direction of motion, defined as the length of the particle compared to its width.  
[maskInteraction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer-maskInteraction.html) | Specifies how the Particle System Renderer interacts with SpriteMask.  
[maxParticleSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer-maxParticleSize.html) | Clamp the maximum particle size.  
[mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer-mesh.html) | The Mesh that the particle uses instead of a billboarded Texture.  
[meshCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer-meshCount.html) | The number of Meshes the system uses for particle rendering.  
[meshDistribution](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer-meshDistribution.html) | Specifies how the system randomly assigns meshes to particles.  
[minParticleSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer-minParticleSize.html) | Clamp the minimum particle size.  
[normalDirection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer-normalDirection.html) | Specifies how to calculate lighting for the billboard.  
[pivot](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer-pivot.html) | Modify the pivot point used for rotating particles.  
[renderMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer-renderMode.html) | Specifies how the system draws particles.  
[rotateWithStretchDirection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer-rotateWithStretchDirection.html) | Rotate the particles based on the direction they are stretched in. This is added on top of other particle rotation.  
[shadowBias](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer-shadowBias.html) | Apply a shadow bias to prevent self-shadowing artifacts. The specified value is the proportion of the particle size.  
[sortingFudge](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer-sortingFudge.html) | Biases Particle System sorting amongst other transparencies.  
[sortMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer-sortMode.html) | Specifies how to sort particles within a system.  
[supportsMeshInstancing](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer-supportsMeshInstancing.html) | Determines whether the Particle System can be rendered using GPU Instancing.  
[trailMaterial](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer-trailMaterial.html) | Set the Material that the TrailModule uses to attach trails to particles.  
[velocityScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer-velocityScale.html) | Specifies how much particles stretch depending on their velocity.  
### Public Methods
Method | Description  
---|---  
[BakeMesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer.BakeMesh.html) | Creates a snapshot of ParticleSystemRenderer and stores it in a mesh.  
[BakeTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer.BakeTexture.html) | Creates a snapshot of ParticleSystemRenderer and stores it in a Texture2D.  
[BakeTrailsMesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer.BakeTrailsMesh.html) | Creates a snapshot of ParticleSystem Trails and stores them in a mesh.  
[BakeTrailsTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer.BakeTrailsTexture.html) | Creates a snapshot of ParticleSystem Trails and stores them in a Texture2D.  
[GetActiveTrailVertexStreams](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer.GetActiveTrailVertexStreams.html) | Queries which trail Vertex Shader streams are enabled on the ParticleSystemRenderer.  
[GetActiveVertexStreams](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer.GetActiveVertexStreams.html) | Queries which Vertex Shader streams are enabled on the ParticleSystemRenderer.  
[GetMeshes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer.GetMeshes.html) | Gets the array of Meshes to use when selecting particle meshes.  
[GetMeshWeightings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer.GetMeshWeightings.html) | Gets the array of Mesh weightings to use when randomly selecting particle meshes.  
[SetActiveTrailVertexStreams](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer.SetActiveTrailVertexStreams.html) | Enables a set of Vertex Shader streams on the ParticleSystemRenderer for particle trails.  
[SetActiveVertexStreams](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer.SetActiveVertexStreams.html) | Enables a set of Vertex Shader streams on the ParticleSystemRenderer.  
[SetMeshes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer.SetMeshes.html) | Sets the Meshes that the ParticleSystemRenderer uses to display particles when the ParticleSystemRenderer.renderMode is set to ParticleSystemRenderMode.Mesh.  
[SetMeshWeightings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer.SetMeshWeightings.html) | Sets the weights that the ParticleSystemRenderer uses to assign Meshes to particles.  
### Inherited Members
### Properties
Property | Description  
---|---  
[gameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component-gameObject.html) | The game object this component is attached to. A component is always attached to a game object.  
[tag](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component-tag.html) | The tag of this game object.  
[transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component-transform.html) | The Transform attached to this GameObject.  
[hideFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-hideFlags.html) | Should the object be hidden, saved with the Scene or modifiable by the user?  
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-name.html) | The name of the object.  
[allowOcclusionWhenDynamic](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-allowOcclusionWhenDynamic.html) | Controls if dynamic occlusion culling should be performed for this renderer.  
[bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-bounds.html) | The bounding box of the renderer in world space.  
[enabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-enabled.html) | Makes the rendered 3D object visible if enabled.  
[forceRenderingOff](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-forceRenderingOff.html) | Allows turning off rendering for a specific component.  
[isLOD0](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-isLOD0.html) | Is the renderer the first LOD level in its group.  
[isPartOfStaticBatch](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-isPartOfStaticBatch.html) | Indicates whether the renderer is part of a static batch with other renderers.  
[isVisible](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-isVisible.html) | Is this renderer visible in any camera? (Read Only)  
[lightmapIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-lightmapIndex.html) | The index of the baked lightmap applied to this renderer.  
[lightmapScaleOffset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-lightmapScaleOffset.html) | The UV scale & offset used for a lightmap.  
[lightProbeProxyVolumeOverride](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-lightProbeProxyVolumeOverride.html) | If set, the Renderer will use the Light Probe Proxy Volume component attached to the source GameObject.  
[lightProbeUsage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-lightProbeUsage.html) | The light probe interpolation type.  
[localBounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-localBounds.html) | The bounding box of the renderer in local space.  
[localToWorldMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-localToWorldMatrix.html) | Matrix that transforms a point from local space into world space (Read Only).  
[LODGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.LODGroup.html) | The LODGroup for this Renderer.  
[material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-material.html) | Returns the first instantiated Material assigned to the renderer.  
[materials](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-materials.html) | Returns all the instantiated materials of this object.  
[motionVectorGenerationMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-motionVectorGenerationMode.html) | Specifies the mode for motion vector rendering.  
[probeAnchor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-probeAnchor.html) | If set, Renderer will use this Transform's position to find the light or reflection probe.  
[rayTracingAccelerationStructureBuildFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-rayTracingAccelerationStructureBuildFlags.html) | The flags Unity uses when it builds acceleration structures associated with geometry used by renderers.  
[rayTracingAccelerationStructureBuildFlagsOverride](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-rayTracingAccelerationStructureBuildFlagsOverride.html) | Whether to override the default build flags specified when creating a RayTracingAccelerationStructure.  
[rayTracingMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-rayTracingMode.html) | Describes how this renderer is updated for ray tracing.  
[realtimeLightmapIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-realtimeLightmapIndex.html) | The index of the real-time lightmap applied to this renderer.  
[realtimeLightmapScaleOffset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-realtimeLightmapScaleOffset.html) | The UV scale & offset used for a real-time lightmap.  
[receiveShadows](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-receiveShadows.html) | Does this object receive shadows?  
[reflectionProbeUsage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-reflectionProbeUsage.html) | Should reflection probes be used for this Renderer?  
[rendererPriority](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-rendererPriority.html) | This value sorts renderers by priority. Lower values are rendered first and higher values are rendered last.  
[renderingLayerMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-renderingLayerMask.html) | Determines which rendering layer this renderer lives on, if you use a scriptable render pipeline.  
[shadowCastingMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-shadowCastingMode.html) | Does this object cast shadows?  
[sharedMaterial](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-sharedMaterial.html) | The shared material of this object.  
[sharedMaterials](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-sharedMaterials.html) | All the shared materials of this object.  
[sortingLayerID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-sortingLayerID.html) | Unique ID of the Renderer's sorting layer.  
[sortingLayerName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-sortingLayerName.html) | Name of the Renderer's sorting layer.  
[sortingOrder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-sortingOrder.html) | Renderer's order within a sorting layer.  
[staticShadowCaster](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-staticShadowCaster.html) | Is this renderer a static shadow caster?  
[worldToLocalMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-worldToLocalMatrix.html) | Matrix that transforms a point from world space into local space (Read Only).  
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
[GetClosestReflectionProbes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.GetClosestReflectionProbes.html) | Returns an array of closest reflection probes with weights, weight shows how much influence the probe has on the renderer, this value is also used when blending between reflection probes occur.  
[GetMaterials](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.GetMaterials.html) | Returns all the instantiated materials of this object.  
[GetPropertyBlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.GetPropertyBlock.html) | Get per-Renderer or per-Material property block.  
[GetSharedMaterials](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.GetSharedMaterials.html) | Returns all the shared materials of this object.  
[HasPropertyBlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.HasPropertyBlock.html) | Returns true if the Renderer has a material property block attached via SetPropertyBlock.  
[ResetBounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.ResetBounds.html) | Reset custom world space bounds.  
[ResetLocalBounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.ResetLocalBounds.html) | Reset custom local space bounds.  
[SetMaterials](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.SetMaterials.html) | Assigns the shared materials of this object using the list of materials provided.  
[SetPropertyBlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.SetPropertyBlock.html) | Lets you set or clear per-renderer or per-material parameter overrides.  
[SetSharedMaterials](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.SetSharedMaterials.html) | Assigns the shared materials of this object using the list of materials provided.  
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
### Messages
Message | Description  
---|---  
[OnBecameInvisible](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.OnBecameInvisible.html) |  OnBecameInvisible is called when the object is no longer visible by any camera.  
[OnBecameVisible](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.OnBecameVisible.html) |  OnBecameVisible is called when the object became visible by any camera.  
* * *
